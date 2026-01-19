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

    try:
        with sync_playwright() as p:
            # 더 많은 브라우저 옵션으로 실제 브라우저처럼 보이게 설정
            browser = p.chromium.launch(
                headless=True,
                args=[
                    "--disable-blink-features=AutomationControlled",
                    "--disable-dev-shm-usage",
                    "--no-sandbox",
                ],
            )

            # 컨텍스트 생성 시 User-Agent 설정
            context = browser.new_context(
                user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
                viewport={"width": 1920, "height": 1080},
            )

            page = context.new_page()

            # 추가 헤더 설정
            page.set_extra_http_headers(
                {
                    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
                    "Accept-Language": "en-US,en;q=0.9",
                    "Accept-Encoding": "gzip, deflate, br",
                    "Connection": "keep-alive",
                    "Upgrade-Insecure-Requests": "1",
                }
            )

            # 페이지 로드 - networkidle 대신 domcontentloaded 사용
            page.goto(url, timeout=30000, wait_until="domcontentloaded")

            # JavaScript 실행 대기
            time.sleep(2)

            html = page.content()
            browser.close()

            soup = BeautifulSoup(html, "html.parser")

            unwanted_tags = ["script", "style", "iframe", "svg"]
            for tag in soup.find_all(unwanted_tags):
                tag.decompose()

            content = soup.get_text(separator=" ")
            return content if content != "" else "No content"

    except Exception as e:
        print(f"Error scraping {url}: {str(e)}")
        return "No content"
