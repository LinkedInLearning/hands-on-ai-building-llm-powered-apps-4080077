# Hands-On AI: Building and Deploying LLM-Powered Apps
This is the repository for the LinkedIn Learning course `Hands-On AI: Building and Deploying LLM-Powered Apps`. The full course is available from [LinkedIn Learning][lil-course-url].

_See the readme file in the main branch for updated instructions and information._
## Lab1: Introduction to Streamlit
We will be using [Streamlit](https://docs.streamlit.io/) as the frontend framework to develop our LLM Powered applications. Chainlit is an open-source Python package that makes it incredibly fast to build Chat GPT like applications with your own business logic and data.

In this lab, we will put up a very simple Chainlit application that echos a user's query.

For example, if user says

```
hello
```

Our Chainlit app will respond with 

```
Received: hello
```

The learning objective is to familiarize with Chainlit's framework and to launch the application.

## Exercises

We have created some template code in `app/app.py` in the `app folder`.

1. Please go through [Streamlit's documentation](https://docs.streamlit.io/) and answer the questions in `app/app.py`

2. Please lanuch the application by running the following command on the Terminal:

```bash
streamlit run app/app.py
```
