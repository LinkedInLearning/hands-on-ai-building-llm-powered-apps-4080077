from typing import List, Dict, Any

from dotenv import load_dotenv
from langchain.schema import Document
from langchain_openai import ChatOpenAI
from langchain.vectorstores.base import VectorStore
from langchain.chains import RetrievalQAWithSourcesChain
from langchain.prompts import PromptTemplate
import streamlit as st

# NOTE: we moved create_search_engine to utils.py for better organization
from utils import create_search_engine

# Load environment variables
load_dotenv()


# Page configuration
st.set_page_config(
    page_title="PDF Q&A Assistant - RAG Challenge",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = []
if "chain" not in st.session_state:
    st.session_state.chain = None
if "docs" not in st.session_state:
    st.session_state.docs = None
if "processed_file" not in st.session_state:
    st.session_state.processed_file = None
if "vector_store" not in st.session_state:
    st.session_state.vector_store = None


def create_qa_chain(vector_store: VectorStore) -> RetrievalQAWithSourcesChain:
    """Create the QA chain with the vector store."""
    # Create the ChatOpenAI model
    llm = ChatOpenAI(
        model='gpt-4.1-mini',
        temperature=0,      # For consistent outputs
        streaming=True,     # Enable streaming
        max_tokens=8192     # Set max_tokens
    )

    PROMPT = PromptTemplate(template=template, input_variables=[
                            "summaries", "question"])

    EXAMPLE_PROMPT = PromptTemplate(
        template="Content: {page_content}\nSource: {source}",
        input_variables=["page_content", "source"],
    )

    # Create the RetrievalQAWithSourcesChain
    chain = RetrievalQAWithSourcesChain.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=vector_store.as_retriever(search_kwargs={"k": 5}),
        chain_type_kwargs={
            "prompt": PROMPT,
            "document_prompt": EXAMPLE_PROMPT
        },
        return_source_documents=True
    )

    return chain


def format_answer_with_sources(response: Dict[str, Any], docs: List[Document]) -> tuple[str, List[str]]:
    """Format the answer with source information."""
    answer = response["answer"]
    sources = response.get("sources", "").strip()
    source_contents = []

    if sources and docs:
        metadatas = [doc.metadata for doc in docs]
        all_sources = [m["source"] for m in metadatas]
        found_sources = []

        for source in sources.split(","):
            source_name = source.strip().replace(".", "")
            try:
                index = all_sources.index(source_name)
                text = docs[index].page_content
                found_sources.append(source_name)
                source_contents.append({
                    "name": source_name,
                    "content": text
                })
            except ValueError:
                continue

        if found_sources:
            answer += f"\n\n**Sources:** {', '.join(found_sources)}"

    return answer, source_contents


# Main app
def main():
    st.title("📚 PDF Q&A Assistant")
    st.markdown("""
    Welcome to the PDF Q&A Assistant!
    This version uses vector embeddings for better search accuracy.
    To get started:
    1. Upload a PDF file
    2. Ask any question about the file!
    """)

    # Sidebar for file upload
    with st.sidebar:
        st.header("📤 Upload PDF")
        uploaded_file = st.file_uploader(
            "Choose a PDF file",
            type=["pdf"],
            help="Upload a PDF file to ask questions about its content"
        )

        if uploaded_file is not None:
            if st.session_state.processed_file != uploaded_file.name:
                with st.status("Processing PDF...", expanded=True) as status:
                    st.write("📄 Reading PDF content...")

                    try:
                        # Create vector store and process the PDF
                        st.write("🔍 Creating vector store...")
                        vector_store, docs = create_search_engine(
                            uploaded_file.getvalue(), "application/pdf")

                        st.write(f"✅ Indexed {len(docs)} text chunks")

                        st.session_state.docs = docs
                        st.session_state.processed_file = uploaded_file.name
                        st.session_state.vector_store = vector_store

                        status.update(
                            label="✅ PDF processed successfully!", state="complete")

                    except Exception as e:
                        status.update(
                            label="❌ Error processing PDF", state="error")
                        st.error(f"Error: {str(e)}")
                        return

            st.success(f"📄 **{uploaded_file.name}** is ready for questions!")

            if st.button("🔄 Process New File"):
                # Reset session state
                st.session_state.chain = None
                st.session_state.docs = None
                st.session_state.processed_file = None
                st.session_state.messages = []
                st.rerun()

    ##########################################################################
    # Exercise 1:
    # Now we have search engine setup, our Chat with PDF application can do
    # RAG architecture pattern. Please use the appropriate RetrievalQA Chain
    # from Langchain.
    #
    # Remember, we would want to set the model temperature to
    # 0 to ensure model outputs do not vary across runs, and we would want to
    # also return sources to our answers.
    ##########################################################################
    if st.session_state.vector_store is not None:
        st.write("🧠 Setting up Q&A chain...")

        model = ChatOpenAI(
            ...
        )
        chain = RetrievalQAWithSourcesChain.from_chain_type(
            ...
        )

        # Store in session state
        st.session_state.chain = chain
    ##########################################################################

    # Chat interface
    if st.session_state.chain is not None:
        st.markdown("### 💬 Chat with your PDF")

        # Display chat messages
        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])

                # Display sources if available
                if "sources" in message and message["sources"]:
                    for source in message["sources"]:
                        with st.expander(f"📄 Source: {source['name']}"):
                            st.text(source["content"])

        # Chat input
        if prompt := st.chat_input("Ask a question about the PDF..."):
            # Add user message to chat history
            st.session_state.messages.append(
                {"role": "user", "content": prompt})

            # Display user message
            with st.chat_message("user"):
                st.markdown(prompt)

            # Generate response
            with st.chat_message("assistant"):
                with st.spinner("Thinking..."):
                    try:
                        response = st.session_state.chain.invoke(
                            {"question": prompt})
                        answer, source_contents = format_answer_with_sources(
                            response, st.session_state.docs
                        )

                        st.markdown(answer)

                        # Display sources
                        if source_contents:
                            for source in source_contents:
                                with st.expander(f"📄 Source: {source['name']}"):
                                    st.text(source["content"])

                        # Add assistant response to chat history
                        st.session_state.messages.append({
                            "role": "assistant",
                            "content": answer,
                            "sources": source_contents
                        })

                    except Exception as e:
                        error_msg = f"Error generating response: {str(e)}"
                        st.error(error_msg)
                        st.session_state.messages.append({
                            "role": "assistant",
                            "content": error_msg
                        })

    else:
        st.info("👆 Please upload a PDF file to get started!")

        # Show example questions
        st.markdown("### 📝 Example Questions Once You Upload a PDF:")
        st.markdown("""
        - What is the main topic of this document?
        - Can you summarize the key points?
        - What are the important findings mentioned?
        - Tell me about [specific topic in the PDF]
        - What evidence supports [claim from the document]?
        """)

        # Show technology stack
        st.markdown("### 🛠️ Technology Stack:")
        st.markdown("""
        - **Frontend**: Streamlit
        - **LLM**: OpenAI gpt-4.1-mini
        - **Embeddings**: OpenAI text-embedding-3-small
        - **Vector Store**: Chroma
        - **Document Processing**: LangChain + PDFPlumber
        - **RAG Framework**: LangChain RetrievalQAWithSourcesChain
        """)


if __name__ == "__main__":
    main()
