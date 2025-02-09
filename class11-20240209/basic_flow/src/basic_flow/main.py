from crewai.flow.flow import Flow, start, listen
from litellm import completion  # Replace with your preferred LLM API client


class TopicOutlineFlow(Flow):
    model = "gemini/gemini-1.5-flash"

    @start()
    def generate_topic(self):
        # Prompt the LLM to generate a blog topic.
        response = completion(
            model=self.model,
            messages=[
                {
                    "role": "user",
                    "content": "Generate a creative blog topic for 2025 and write a paragraph about it",
                }
            ],
        )
        response = response["choices"][0]["message"]["content"].strip()
        return response


def kickoff():
    flow = TopicOutlineFlow()
    final_outline = flow.kickoff()
    print("Final Output:")
    print(final_outline)
