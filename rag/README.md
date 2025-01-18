# Retrieval-Augmented Generation (RAG) Project

---

This repository contains a comprehensive exploration of Retrieval-Augmented Generation (RAG) for various applications.
Each notebook provides a detailed, hands-on guide to setting up and experimenting with RAG from an introductory level to advanced implementations, including multi-querying and custom RAG builds.

![rag_detail_v2](assets/img/rag-architecture.png)

### [1]\_rag_setup_overview.ipynb

This introductory notebook provides an overview of RAG architecture and its foundational setup.
The notebook walks through:

- **Environment Setup**: Configuring the environment, installing necessary libraries, and API setups.
- **Initial Data Loading**: Basic document loaders and data preprocessing methods.
- **Embedding Generation**: Generating embeddings using various models, including OpenAI's embeddings.
- **Vector Store**: Setting up a vector store (ChromaDB/Pinecone) for efficient similarity search.
- **Basic RAG Pipeline**: Creating a simple retrieval and generation pipeline to serve as a baseline.

## Getting Started

Pre-requisites: Python 3.11.7 (preferred)

1.  **Clone the repository**:

    ```{bash}
    git clone https://github.com/JahanzaibTayyab/AI-201

    cd A1-201/rag
    ```

2.  **Create a virtual environment**

    ```{bash}
    python -m venv venv

    source venv/bin/activate
    ```

3.  **Install dependencies**: Make sure to install the required packages listed in `requirements.txt`.

    `pip install -r requirements.txt`

4.  **Run the Notebooks**:
    Begin with `[1]_rag_setup_overview.ipynb` to get familiar with the setup process. Proceed sequentially through the other notebooks to build and experiment with more advanced RAG concepts.

5.  **Set Up Environment Variables**:

    - Duplicate the `.env._example` file in the root directory and name it `.env` and include the following keys (replace with your actual keys):

      ```
      #LLM Modal
      OPENAI_API_KEY="your-api-key"

      #LangSmith
      LANGCHAIN_TRACING_V2=true
      LANGCHAIN_ENDPOINT="https://api.smith.langchain.com"
      LANGCHAIN_API_KEY="your-api-key"
      LANGCHAIN_PROJECT="your-project-name"

      #Pinecone Vector Database
      PINECONE_INDEX_NAME="your-project-index"
      PINECONE_API_HOST="your-host-url"
      PINECONE_API_KEY="your-api-key"
      ```

## Usage

After setting up the environment and running the notebooks in sequence, you can:

1.  **Experiment with Retrieval-Augmented Generation**:
    Use the foundational setup in `[1]_rag_setup_overview.ipynb` to understand the basics of RAG.
