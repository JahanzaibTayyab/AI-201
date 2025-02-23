from crewai.flow.flow import Flow, start, listen
from litellm import completion  # Replace with your LLM API client


class OrchestratorWorkersFlow(Flow):
    # Set the model to use (adjust according to your deployment)
    model = "gpt-4o-mini"

    @start()
    def initial_task(self):
        """
        The orchestrator's starting point:
        - Receives a complex problem description.
        - Dynamically breaks it down into subtasks.
        """
        problem_description = (
            "Analyze the code for potential vulnerabilities and suggest improvements."
        )
        print("Orchestrator received problem:", problem_description)
        # Dynamically define subtasks (in practice, these could be generated via an LLM)
        subtasks = [
            "Identify potential security vulnerabilities in the code.",
            "Recommend improvements for code efficiency.",
            "Suggest best practices for error handling.",
        ]
        # Store the subtasks in the flow's state for later reference
        self.state.subtasks = subtasks
        return problem_description

    @listen(initial_task)
    def delegate_subtasks(self, problem_description):
        """
        The orchestrator delegates each subtask to a worker function.
        In this simple example, we iterate through the subtasks,
        call a worker for each, and collect the results.
        """
        subtasks = self.state.get("subtasks", [])
        results = []
        for task in subtasks:
            # Delegate the subtask to the worker function and collect its result
            result = self.worker_task(task)
            results.append(result)
        # Save the worker outputs in state for synthesis
        self.state.worker_results = results
        return results

    def worker_task(self, subtask):
        """
        Worker function simulating the processing of a subtask.
        Each worker could be an independent LLM call or a specialized agent.
        """
        print("Worker processing subtask:", subtask)
        # Create a prompt for the worker to address the subtask
        prompt = f"Please address the following task: {subtask}"
        # Call the LLM (or another agent) to generate an answer for this subtask
        response = completion(
            model=self.model, messages=[{"role": "user", "content": prompt}]
        )
        # Extract the worker's output from the response
        worker_output = response["choices"][0]["message"]["content"].strip()
        print("Worker output:", worker_output)
        return worker_output

    @listen(delegate_subtasks)
    def synthesize_results(self, worker_results):
        """
        The orchestrator synthesizes the outputs from all workers into one final report.
        """
        synthesized = "Synthesized Report:\n"
        for idx, output in enumerate(worker_results, start=1):
            synthesized += f"Subtask {idx}: {output}\n"
        print(synthesized)
        return synthesized


if __name__ == "__main__":
    # Create and kick off the flow
    flow = OrchestratorWorkersFlow()
    final_report = flow.kickoff()
    print("Final Report:")
    print(final_report)
