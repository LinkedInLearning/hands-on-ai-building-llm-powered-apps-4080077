from typing import List, Dict, Any

from dotenv import load_dotenv
from langchain.callbacks.base import BaseCallbackHandler
from langchain_openai import ChatOpenAI
from langchain_core.messages.utils import convert_to_messages

import streamlit as st


# Load environment variables
load_dotenv()


# Page configuration
st.set_page_config(
    page_title="PDF Q&A Assistant",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Initialize session states
if "messages" not in st.session_state:
    st.session_state.messages = []
if "chain" not in st.session_state:
    st.session_state.chain = None


class StreamlitCallbackHandler(BaseCallbackHandler):
    """Custom callback handler for streaming responses in Streamlit."""

    def __init__(self, container):
        self.container = container
        self.text = ""

    def on_llm_new_token(self, token: str, **kwargs) -> None:
        """Called when LLM generates a new token."""
        self.text += token
        self.container.markdown(self.text)


def main():
    st.title("📚 PDF Q&A Assistant")
    ##########################################################################
    # Exercise 1a:
    # First, we need to choose an LLM from OpenAI's list of models. Remember
    # to set streaming=True for streaming tokens
    ##########################################################################
    chain = ChatOpenAI(
        ...
    )
    # Store the chain in session state
    st.session_state.chain = chain

    # Display chat messages
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Chat input
    if prompt := st.chat_input("Ask a question..."):
        ##########################################################################
        # Exercise 1b:
        # Now we get a new user prompt in `prompt` variable, we we will need to add it into the chat history.
        #
        # Refer to the documentation listed in the README.md file for reference.
        ##########################################################################
        # Add user message to chat history
        st.session_state.messages.append(
            ...
        )

        # Display user message
        with st.chat_message("user"):
            st.markdown(prompt)

        # Generate response
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                try:
                    ##########################################################################
                    # Exercise 1c:
                    # Now we have the model, chat history, and the new user prompt, let's invoke our Chain. A Chain is one or a series of LLM calls.
                    # Reminder
                    # After invoking, please remember adding the # response to chat history.
                    ##########################################################################
                    chat_history = convert_to_messages(
                        ...
                    )

                    response = ...
                    answer = response.content

                    st.markdown(answer)

                    # Add assistant response to chat history
                    st.session_state.messages.append(
                        ...
                    )

                except Exception as e:
                    error_msg = f"Error generating response: {str(e)}"
                    st.error(error_msg)
                    st.session_state.messages.append({
                        "role": "assistant",
                        "content": error_msg
                    })


if __name__ == "__main__":
    main()
