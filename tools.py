import time

from bs4 import BeautifulSoup
from crewai.tools import tool
from crewai_tools import SerperDevTool
from playwright.sync_api import sync_playwright

search_tool = SerperDevTool()


@tool
def scrape_tool(url: str) -> str:
    """
    Use this when you need to read the content of a webpage.
    return the content of the url. in case the website is not accessible, return 'No content'.
    input should be a 'url' string. for example: 'https://abcnews.go.com/US/trump-announces-tariffs-nato-allies-opposing-us-control/story?id=129310383'
    """
    print(f"Scraping URL: {url}")

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(url)
        time.sleep(5)
        html = page.content()
        browser.close()

        soup = BeautifulSoup(html, "html.parser")

        unwanted_tags = ["script", "style", "iframe", "svg"]
        for tag in soup.find_all(unwanted_tags):
            tag.decompose()

        content = soup.get_text(separator=" ")
        return content if content != "" else "No content"
