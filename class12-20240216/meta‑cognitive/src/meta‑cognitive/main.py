
from crewai.flow.flow import Flow, start, listen
from litellm import completion

class MetaCognitiveFlow(Flow):
    model = "gpt-4o-mini"

    @start()
    def generate_initial_draft(self):
        # The agent generates an initial draft on a given topic.
        response = completion(
            model=self.model,
            messages=[{"role": "user", "content": "Draft a brief summary on the benefits of renewable energy."}]
        )
        draft = response["choices"][0]["message"]["content"].strip()
        print("Initial Draft:")
        print(draft)
        return draft

    @listen(generate_initial_draft)
    def reflect_on_draft(self, draft):
        # The agent reflects on the draft and provides constructive feedback.
        reflection_prompt = (
            f"Review the following summary and point out any logical gaps, unclear points, or areas for improvement:\n\n{draft}"
        )
        response = completion(
            model=self.model,
            messages=[{"role": "user", "content": reflection_prompt}]
        )
        feedback = response["choices"][0]["message"]["content"].strip()
        print("Reflection Feedback:")
        print(feedback)
        # Save the feedback for the next step.
        self.state["feedback"] = feedback
        return feedback

    @listen(reflect_on_draft)
    def refine_draft(self, draft):
        # The agent uses its own feedback to refine the initial draft.
        feedback = self.state.get("feedback", "")
        refine_prompt = (
            f"Here is the initial summary:\n{draft}\n\nAnd here is some feedback:\n{feedback}\n\n"
            "Revise the summary to address the feedback and improve clarity and accuracy."
        )
        response = completion(
            model=self.model,
            messages=[{"role": "user", "content": refine_prompt}]
        )
        final_draft = response["choices"][0]["message"]["content"].strip()
        print("Refined Draft:")
        print(final_draft)
        return final_draft

if __name__ == "__main__":
    flow = MetaCognitiveFlow()
    final_output = flow.kickoff()
    print("Final Output:")
    print(final_output)
