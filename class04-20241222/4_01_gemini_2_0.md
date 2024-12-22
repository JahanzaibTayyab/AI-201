# Gemini 2.0

[Introducing Gemini 2.0: our new AI model for the agentic era](https://blog.google/technology/google-deepmind/google-gemini-ai-update-december-2024/#ceo-message)

**Evolution from Gemini 1.0 :** Gemini 2.0 evolves from Gemini 1.0 and 1.5 by adding "agentic" capabilities for improved real-world understanding, planning, and action-taking with user oversight.

**New Capabilities in 2.0 :** Gemini 2.0 introduces native image and audio output, along with native tool use, advancing towards a "universal assistant" with more sophisticated AI capabilities.

**Availability and Integration :** Gemini 2.0 is available to developers, testers, and Google products, with the "Gemini 2.0 Flash" model accessible to all users and "Deep Research" featured in Gemini Advanced for complex tasks.

**Impact on Search :** Gemini 2.0 enhances AI Overviews in Search with advanced reasoning for complex queries like math, multimodal questions, and coding, starting with limited testing and broader rollout next year.

**Underlying Technology :** Gemini 2.0's advancements are powered by Google's custom Trillium TPUs (6th-gen), which supported all its training and inference and are now available to customers.

**Shift in Focus :** Gemini 2.0 shifts from organizing information in Gemini 1.0 to enhancing its utility with agentic capabilities and deeper integration into Google products like Search.

Here is the table based on the content of the image:

| **Capability**   | **Benchmark**     | **Description**                                                                                                | **Gemini 1.5 Flash O02** | **Gemini 1.5 Pro O02** | **Gemini 2.0 Flash Experimental** |
| ---------------- | ----------------- | -------------------------------------------------------------------------------------------------------------- | ------------------------ | ---------------------- | --------------------------------- |
| **General**      | MMLU-Pro          | Enhanced version of popular MMLU dataset with questions across multiple subjects with higher difficulty tasks. | 67.3%                    | 75.8%                  | 76.4%                             |
| **Code**         | Natural2Code      | Code generation across Python, Java, C++, JS, Go. Held-out dataset HumanEval-like, not leaked on the web.      | 79.8%                    | 85.4%                  | 92.9%                             |
|                  | Bird-SQL (Dev)    | Benchmark evaluating converting natural language questions into executable SQL.                                | 45.6%                    | 54.4%                  | 56.9%                             |
|                  | LiveCodeBench     | Code generation in Python. Covers more recent examples (06/01/2024 - 10/05/2024).                              | 30.0%                    | 34.3%                  | 35.1%                             |
| **Factuality**   | FACTS Grounding   | Ability to provide factually correct responses given documents and diverse user requests.                      | 82.9%                    | 80.0%                  | 83.6%                             |
| **Math**         | MATH              | Challenging math problems (e.g., algebra, geometry, pre-calculus, etc.).                                       | 77.9%                    | 86.5%                  | 89.7%                             |
|                  | HiddenMath        | Competition-level math problems (AIME/AMC-like), held-out dataset crafted by experts.                          | 47.2%                    | 52.0%                  | 63.0%                             |
| **Reasoning**    | GPQA (Diamond)    | Challenging dataset of questions written by domain experts in biology, physics, and chemistry.                 | 51.0%                    | 59.1%                  | 62.1%                             |
| **Long Context** | MRCR (1M)         | Novel, diagnostic long-context understanding evaluation.                                                       | 71.9%                    | 82.6%                  | 69.2%                             |
| **Image**        | MMMU              | Multi-discipline college-level multimodal understanding and reasoning problems.                                | 62.3%                    | 65.9%                  | 70.7%                             |
|                  | Vibe-Eval (Reka)  | Visual understanding in chat models with challenging everyday examples.                                        | 48.9%                    | 53.9%                  | 56.3%                             |
| **Audio**        | CoVoST2 (21 lang) | Automatic speech translation (BLEU score).                                                                     | 37.4%                    | 40.1%                  | 39.2%                             |
| **Video**        | EgoSchema (Test)  | Video analysis across multiple domains.                                                                        | 66.8%                    | 71.2%                  | 71.5%                             |

- [Project Astra: agents using multimodal understanding in the real world](https://www.youtube.com/watch?v=hIIlJt8JERI&ab_channel=Google)
- [Project Mariner: agents that can help you accomplish complex tasks](https://www.youtube.com/watch?v=2XJqLPqHtyo&ab_channel=GoogleDeepMind)
- [Jules: agents for developers](https://developers.googleblog.com/en/the-next-chapter-of-the-gemini-era-for-developers/)
- [Gemini 2.0 for games](https://www.youtube.com/watch?v=IKuGNHJBGsc&t=2s&ab_channel=GoogleDeepMind)
- [Gemini 2.0 Docs](https://ai.google.dev/gemini-api/docs/models/gemini-v2)
- [Gemini 2.0 Coding Examples](https://github.com/google-gemini/cookbook/tree/main/gemini-2)
