from crewai.flow.flow import Flow, start, listen, router
from litellm import completion


class RoutedFlow(Flow):
    model = "gemini/gemini-1.5-flash"

    @start()
    def generate_topic(self):
        response = completion(
            model=self.model,
            messages=[
                {"role": "user", "content": "Generate a single blog topic for 2025."}
            ],
        )
        topic = response["choices"][0]["message"]["content"].strip()
        self.state["is_tech"] = "tech" in topic.lower()
        print(f"\n\n\nTopic: {topic}\n\n\n")
        return topic

    @router(generate_topic)
    def route_topic(self, topic):
        response = completion(
            model=self.model,
            messages=[
                {
                    "role": "user",
                    "content": f"Identify the topic {topic} type: tech or lifestyle? Respond with the type.",
                }
            ],
        )
        topic_type = response["choices"][0]["message"]["content"].strip().lower()
        print(f"\n\n\nTopic Type: {topic_type}\n\n\n")
        self.state["is_tech"] = "tech" in topic_type
        if self.state.get("tech"):
            return "tech_route"
        else:
            return "lifestyle_route"

    @listen("tech_route")
    def generate_tech_outline(self, topic):
        response = completion(
            model=self.model,
            messages=[
                {
                    "role": "user",
                    "content": f"Create a detailed tech blog outline for: {topic}",
                }
            ],
        )
        outline = response["choices"][0]["message"]["content"].strip()
        print(f"\n\n\nTech Outline: {outline}\n\n\n")
        return outline

    @listen("lifestyle_route")
    def generate_lifestyle_outline(self, topic):
        response = completion(
            model=self.model,
            messages=[
                {
                    "role": "user",
                    "content": f"Create a detailed lifestyle blog outline for: {topic}",
                }
            ],
        )
        outline = response["choices"][0]["message"]["content"].strip()
        print(f"\n\n\nLifestyle Outline: {outline}\n\n\n")
        return outline


def kickoff():
    flow = RoutedFlow()
    final_output = flow.kickoff()
    print("\n\n\nFinal Output:")
    print(final_output)
    print("\n\n\n")
