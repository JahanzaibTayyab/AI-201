from crewai.flow.flow import Flow, start, listen, or_
from litellm import completion


class ParallelFlow(Flow):
    model = "gemini/gemini-1.5-flash"

    @start()
    def generate_variant_1(self):
        print("01")
        response = completion(
            model=self.model,
            messages=[
                {
                    "role": "user",
                    "content": "Generate a single creative blog topic variant #1.",
                }
            ],
        )
        variant = response["choices"][0]["message"]["content"].strip()
        print(f"\n\n\nVariant 1: {variant}\n\n\n")
        return variant

    @start()
    def generate_variant_2(self):
        print("02")
        response = completion(
            model=self.model,
            messages=[
                {
                    "role": "user",
                    "content": "Generate a single creative blog topic variant #2.",
                }
            ],
        )
        variant = response["choices"][0]["message"]["content"].strip()
        print(f"\n\n\nVariant 2: {variant}\n\n\n")
        return variant

    @listen(or_(generate_variant_1, generate_variant_2))
    def aggregate_variants(self, variant):
        # For simplicity, print the first variant received.
        print(f"\n\n\nAggregated Variant:: {variant}\n\n\n")

        return variant


def kickoff():
    flow = ParallelFlow()
    final = flow.kickoff()
    print("\n\n\nFinal Aggregated Output:")
    print(final)
