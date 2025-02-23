from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import (
    DirectoryReadTool,
    FileReadTool,
    SerperDevTool,
    WebsiteSearchTool
)

# Instantiate tools
docs_tool = DirectoryReadTool(directory='./blog-posts')
file_tool = FileReadTool()
search_tool = SerperDevTool()
web_rag_tool = WebsiteSearchTool()

@CrewBase
class ResearchWriterCrew:
    """Research Writer Crew"""

    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    @agent
    def researcher(self) -> Agent:
        return Agent(
            config=self.agents_config["researcher"],
            tools=[search_tool, web_rag_tool],
            verbose=True
        )
        
    @agent
    def writer(self) -> Agent:
        return Agent(
            config=self.agents_config["writer"],
            tools=[docs_tool, file_tool],
            verbose=True
        )
        
        
    @task
    def research(self) -> Task:
        return Task(
            config=self.tasks_config["research"],
        )


    @task
    def write(self) -> Task:
        return Task(
            config=self.tasks_config["write"],
        )

    @crew
    def crew(self) -> Crew:
        """Creates the Research Writer Crew"""

        return Crew(
            agents=self.agents,  # Automatically created by the @agent decorator
            tasks=self.tasks,  # Automatically created by the @task decorator
            verbose=True,
            planning=True,
            process=Process.sequential,
        )