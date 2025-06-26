from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

WELCOME_MESSAGE = """\
Welcome to Introduction to LLM App Development Sample PDF QA Application!
To get started:
1. Upload a PDF or text file
2. Ask any question about the file!
"""

##############################################################################
# Exercise 1:
# Please create a ChatPromptTemplate with message history.
#
# This documentation will help you
# https://python.langchain.com/api_reference/core/prompts/langchain_core.prompts.chat.ChatPromptTemplate.html
##############################################################################
PROMPT = ChatPromptTemplate.from_messages(
    ...
)
##############################################################################
