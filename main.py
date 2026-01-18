import dotenv
from crewai import LLM, Agent, Crew, Task
from crewai.project import CrewBase, agent, crew, task

from tools import count_letters

dotenv.load_dotenv()


@CrewBase
class TranslatorCrew:
    @agent
    def translator_agent(self) -> Agent:
        return Agent(
            config=self.agents_config["translator_agent"],
            llm=LLM(model="google/gemini-3-flash-preview", temperature=0.7),
        )

    @agent
    def count_letters_agent(self) -> Agent:
        return Agent(
            config=self.agents_config["count_letters_agent"],
            llm=LLM(model="google/gemini-3-flash-preview", temperature=0.7),
            tools=[count_letters],
        )

    @task
    def translation_task(self) -> Task:
        return Task(config=self.tasks_config["translation_task"])

    @task
    def retranslation_task(self) -> Task:
        return Task(config=self.tasks_config["retranslation_task"])

    @task
    def count_letters_task(self) -> Task:
        return Task(config=self.tasks_config["count_letters_task"])

    @crew
    def assemble_crew(self) -> Crew:
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            verbose=True,
        )


translator_crew = TranslatorCrew()
result = translator_crew.assemble_crew().kickoff(
    inputs={"sentence": "Hello, how are you?"}
)
print(result)
