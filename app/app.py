import streamlit as st


st.set_page_config(
    page_title="Chat Echo Bot",
    page_icon="🤖",
    layout="wide"
)
st.title("🤖 Chat Echo Bot")

##############################################################################
# Exercise 1a:
# Please setup a messages session state in Streamlit to keep message
# history
##############################################################################
if "messages" not in ...:
    ...

# Displaying chat messages from sessino state
for message in ...:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

##############################################################################
# Exercise 1b:
# Please create a simple chat interface that:
# 1. Accepts user input using st.chat_input()
# 2. Displays the user's message using st.chat_message("user")
# 3. Echoes back the same message using st.chat_message("assistant")
##############################################################################
if prompt := st.chat_input("Type your message here..."):
    # Add user message to chat history
    ...

    # Display user message
    with st.chat_message("user"):
        ...

    # Echo the message back as assistant
    with st.chat_message("assistant"):
        ...

    # Add assistant response to chat history
    ...
