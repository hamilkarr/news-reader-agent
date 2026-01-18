import dotenv
from crewai import LLM, Agent, Crew, Task
from crewai.project import CrewBase, agent, crew, task

from tools import scrape_tool, search_tool

dotenv.load_dotenv()


@CrewBase
class NewsReaderAgent:
    @agent
    def news_hunter_agent(self) -> Agent:
        return Agent(
            config=self.agents_config["news_hunter_agent"],
            llm=LLM(model="google/gemini-3-flash-preview"),
            tools=[search_tool, scrape_tool],
        )

    @agent
    def summarizer_agent(self) -> Agent:
        return Agent(
            config=self.agents_config["summarizer_agent"],
            llm=LLM(model=self.agents_config["summarizer_agent"]["llm"]),
            tools=[scrape_tool],
        )

    @agent
    def curator_agent(self) -> Agent:
        return Agent(
            config=self.agents_config["curator_agent"],
            llm=LLM(model="google/gemini-3-flash-preview"),
        )

    @task
    def content_harvesting_task(self) -> Task:
        return Task(config=self.tasks_config["content_harvesting_task"])

    @task
    def summarization_task(self) -> Task:
        return Task(config=self.tasks_config["summarization_task"])

    @task
    def final_report_assembly_task(self) -> Task:
        return Task(config=self.tasks_config["final_report_assembly_task"])

    @crew
    def crew(self) -> Crew:
        return Crew(
            tasks=self.tasks,
            agents=self.agents,
            verbose=True,
        )


result = NewsReaderAgent().crew().kickoff(inputs={"topic": "AI Stock"})

print(result.tasks_output)
