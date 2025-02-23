#!/usr/bin/env python
from random import randint

from pydantic import BaseModel

from crewai.flow import Flow, listen, start

from knowledge_and_rag.crews.user_crew.user_crew import UserCrew

class KnowledgeAndRagFlow(Flow):

    @start()
    def answer_question(self):
        print("Answering question")
        result = (
            UserCrew()
            .crew()
            .kickoff(inputs={"question": "What is user Name?"})
        )
        print("Question answered", result.raw)
        self.state["answer"] = result.raw

def kickoff():
    knowledge_and_rag_flow = KnowledgeAndRagFlow()
    knowledge_and_rag_flow.kickoff()


def plot():
    knowledge_and_rag_flow = KnowledgeAndRagFlow()
    knowledge_and_rag_flow.plot()