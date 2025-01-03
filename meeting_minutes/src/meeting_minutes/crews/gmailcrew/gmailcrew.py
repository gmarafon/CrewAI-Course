from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from .tools.gmail_tool import GmailTool


@CrewBase
class GmailCrew:
    """Gmailcrew crew"""

    tasks_config = "config/tasks.yaml"

    @agent
    def gmail_draft_agent(self) -> Agent:
        return Agent(config=self.agents_config["gmail_draft_agent"], verbose=True)

    @task
    def gmail_draft_task(self) -> Task:
        return Task(config=self.tasks_config["gmail_draft_task"], tools=[GmailTool()])

    @crew
    def crew(self) -> Crew:
        """Creates the Gmailcrew crew"""

        return Crew(
            agents=self.agents,  # Automatically created by the @agent decorator
            tasks=self.tasks,  # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
        )
