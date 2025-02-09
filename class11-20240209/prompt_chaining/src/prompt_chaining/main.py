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
                {"role": "user", "content": "Generate a creative blog topic for 2025."}
            ],
        )
        topic = response["choices"][0]["message"]["content"].strip()
        print(f"=====> Generated Topic: {topic}")
        return topic

    @listen(generate_topic)
    def generate_outline(self, topic):
        # Now chain the output by using the topic in a follow-up prompt.
        response = completion(
            model=self.model,
            messages=[
                {
                    "role": "user",
                    "content": f"Based on the topic '{topic}', create a detailed outline for a blog post.",
                }
            ],
        )
        outline = response["choices"][0]["message"]["content"].strip()
        print("+++++> Generated Outline:")
        print(outline)
        return outline

    @listen(generate_outline)
    def generate_blog(self, topic, outline):
        # Now chain the output by using the topic in a follow-up prompt.
        response = completion(
            model=self.model,
            messages=[
                {
                    "role": "user",
                    "content": f"Write a blog post on the topic '{topic}', based on the outline '{outline}'.",
                }
            ],
        )
        blog = response["choices"][0]["message"]["content"].strip()
        print("*****> Generated Blog:")
        print(blog)
        return blog


def kickoff():
    flow = TopicOutlineFlow()
    final_blog = flow.kickoff()
    print("&&&&&> Final Output:")
    print(final_blog)
