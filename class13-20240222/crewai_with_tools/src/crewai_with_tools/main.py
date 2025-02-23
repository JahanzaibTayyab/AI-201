#!/usr/bin/env python
from random import randint

from crewai.flow import Flow, start

from crewai_with_tools.crews.research_writer_crew.research_writer_crew import (
    ResearchWriterCrew,
)

from dotenv import load_dotenv, find_dotenv

_ = load_dotenv(find_dotenv())


class ResearchWriterFlow(Flow):

    @start()
    def generate_research(self):
        print("Generating research")
        result = ResearchWriterCrew().crew().kickoff()
        print("Research generated", result.raw)


def kickoff():
    research_writer_flow = ResearchWriterFlow()
    research_writer_flow.kickoff()


def plot():
    research_writer_flow = ResearchWriterFlow()
    research_writer_flow.plot()


if __name__ == "__main__":
    kickoff()
