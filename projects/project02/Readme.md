# **Project 02: LangChain RAG Project**  

### **Objective**
This assignment focuses on creating a simple **Retrieval-Augmented Generation (RAG)** system using **LangChain**, **Google Gemini Flash**, and **Pinecone**. You will develop a Google Colab Notebook that retrieves relevant information from a vector database and uses that context to generate informed responses from the Gemini model.

### **Task**
**Create a Google Colab Notebook** that integrates a RAG workflow, leveraging the Google Gemini Flash API and Pinecone for vector storage and retrieval. Your system should:
1. **Load and Chunk Documents**: Demonstrate how to load a document (e.g., `documents.txt`), split it into smaller chunks, and embed these chunks using Gemini embeddings.
2. **Store and Retrieve from Pinecone**: Set up Pinecone, create an index, and store embeddings. Show how your system retrieves context for user queries.
3. **Integrate Gemini Flash LLM**: Use the Gemini Flash model in a RetrievalQA chain to answer user questions based on the retrieved context.
4. **Experiment with Parameters**: Fine-tune your RAG system by adjusting chunk size, overlap, temperature, or other relevant parameters.

### **Guidelines**
1. Use the provided prerequisites and step-by-step instructions as a starting point. https://github.com/panaversity/learn-agentic-ai/blob/main/02_generative_ai_for_beginners/PROJECTS/02_rag/readme.md
2. **Prerequisites**:  
   - Python 3.8+  
   - Valid API keys for Google Gemini Flash and Pinecone  
   - Python libraries: `langchain`, `pinecone-client`, `google-generativeai`, `openai`, `tqdm`  
3. **Environment**:  
   - Use **Google Colab** to develop and demonstrate your RAG project.  
   - Store your secrets (API keys) securely (e.g., `.env` file loaded with `dotenv`).  
4. **Document Your Process**:  
   - Clearly comment on your code.  
   - Use Markdown cells to explain each step of your workflow.  
5. **Enhanced Features (Optional)**:  
   - Hybrid search (metadata + vector search)  
   - Custom chunking or retrieval logic  
   - A simple UI for interactive querying  

### **Submission Requirements**
1. **Colab Notebook**:  
   - Ensure the file is publicly accessible. Any restricted or private submissions will not be evaluated.  
2. **Submission Form**:  
   - Complete the [Project Submission Form](https://forms.gle/b5Npy6eg4wKWro6m6).  
3. **Deadline**:  
   - **Jan 6, 2025, 11:59 PM**. No extensions will be granted.   

### **Output Expectations**
- **Demonstrate RAG Workflow**: Show the questions asked, the context retrieved, and the final responses from Gemini Flash.  
- **Clarity & Documentation**: Provide clear explanations of each step.  
- **One or More Enhancements**: At least one optional feature or parameter experiment.

**Enjoy exploring LangChain RAG with Google Gemini Flash and Pinecone! If you have any questions, feel free to ask before the deadline.**
