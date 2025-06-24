import streamlit as st


##############################################################################
# Exercise 1a: 
# Please configure the Streamlit page with:
# - A title "Chat Echo Bot"
# - A page icon "🤖"
# - Use the wide layout
##############################################################################
st.set_page_config(
    page_title="Chat Echo Bot",
    page_icon="🤖",
    layout="wide"
)

# Add title to the app
st.title("🤖 Chat Echo Bot")

# Initialize chat history in session state
if "messages" not in st.session_state:
    st.session_state.messages = []

##############################################################################
# Exercise 1b:
# Please create a simple chat interface that:
# 1. Accepts user input using st.chat_input()
# 2. Displays the user's message using st.chat_message("user")
# 3. Echoes back the same message using st.chat_message("assistant")
##############################################################################

# Display existing chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("Type your message here..."):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # Display user message
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Echo the message back as assistant
    with st.chat_message("assistant"):
        st.markdown(prompt)
    
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": prompt})