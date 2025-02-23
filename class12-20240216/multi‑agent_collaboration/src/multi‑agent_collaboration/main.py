
from crewai.flow.flow import Flow, start, listen, or_
from litellm import completion

class MultiAgentCollaborationFlow(Flow):
    model = "gpt-4o-mini"

    @start()
    def generate_introduction(self):
        # Agent A generates the introduction section.
        response = completion(
            model=self.model,
            messages=[{"role": "user", "content": "Write a concise introduction for an article on AI ethics."}]
        )
        introduction = response["choices"][0]["message"]["content"].strip()
        print("Introduction Generated:")
        print(introduction)
        return introduction

    @start()
    def generate_conclusion(self):
        # Agent B generates the conclusion section.
        response = completion(
            model=self.model,
            messages=[{"role": "user", "content": "Write a compelling conclusion for an article on AI ethics."}]
        )
        conclusion = response["choices"][0]["message"]["content"].strip()
        print("Conclusion Generated:")
        print(conclusion)
        return conclusion

    @listen(or_(generate_introduction, generate_conclusion))
    def synthesize_article(self, content):
        # The aggregator waits for both sections to be ready.
        # Here, for simplicity, we assume the first finished call triggers synthesis.
        # In practice, you might wait for both using more advanced state management.
        synthesis_prompt = (
            f"Given the following content from different sections of an article:\n{content}\n"
            "Combine and refine them into a coherent article section."
        )
        response = completion(
            model=self.model,
            messages=[{"role": "user", "content": synthesis_prompt}]
        )
        final_article = response["choices"][0]["message"]["content"].strip()
        print("Synthesized Article Section:")
        print(final_article)
        return final_article

if __name__ == "__main__":
    flow = MultiAgentCollaborationFlow()
    final_article = flow.kickoff()
    print("Final Article Section:")
    print(final_article)
