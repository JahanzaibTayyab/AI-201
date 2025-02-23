from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.knowledge.source.string_knowledge_source import StringKnowledgeSource
from crewai.knowledge.source.crew_docling_source import CrewDoclingSource
from crewai.knowledge.source.text_file_knowledge_source import TextFileKnowledgeSource

import os

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Create a knowledge source
# content = "Users name is Hassan. He is 18 years old and lives in Lahore."
# content_source = StringKnowledgeSource(
#     content=content,
# )

#  MD, PDF, DOCX, HTML,
content_source = CrewDoclingSource(
    file_paths=[
        "https://github.com/JahanzaibTayyab/JahanzaibTayyab/blob/main/README.md",
    ],
)

# Create a text file knowledge source
# content_source = TextFileKnowledgeSource(
#     file_paths=["user_preference.txt"]
# )

# Text
# PDF
# CSV
# EXCEL
# JSON
# APi Source
# Agent Specif Source

@CrewBase
class UserCrew:
    """User Crew"""

    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    @agent
    def about_user(self) -> Agent:
        return Agent(
            config=self.agents_config["about_user"],
            # knowledge_sources=[content_source],
            embedder={
                "provider": "google",
                "config": {
                    "model": "models/text-embedding-004",
                    "api_key": GEMINI_API_KEY,
                },
            },
        )

    @task
    def answer_question(self) -> Task:
        return Task(
            config=self.tasks_config["answer_question"],
        )

    @crew
    def crew(self) -> Crew:
        """Creates the User Crew"""

        return Crew(
            agents=self.agents,  # Automatically created by the @agent decorator
            tasks=self.tasks,  # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
            knowledge_sources=[content_source],
            embedder={
                "provider": "google",
                "config": {
                    "model": "models/text-embedding-004",
                    "api_key": GEMINI_API_KEY,
                },
            },
        )
