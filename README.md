# Hands-On AI: Building and Deploying LLM-Powered Apps
This is the repository for the LinkedIn Learning course `Hands-On AI: Building and Deploying LLM-Powered Apps`. The full course is available from [LinkedIn Learning][lil-course-url].

_See the readme file in the main branch for updated instructions and information._
## Lab3: Enabling Load PDF to Streamlit App
Building on top of the current simplified version of ChatGPT using Streamlit, we now going to add loading PDF capabilities into the application.

In this lab, we will utilize the build in PDF loading and parsing connectors inside Langchain, load the PDF, and chunk the PDFs into individual pieces with their associated metadata.


## Exercises

We will build on top of our existing Streamlit app code in `app/app.py` in the `app` folder. As in our previous app, we added some template code and instructions in `app/app.py`

1. Please go through the exercises in `app/app.py`. 

2. Please lanuch the application by running the following command on the Terminal:

```bash
streamlit run app/app.py
```

## Solution

Please see `app/app.py`.

Alternatively, to launch the application, please run the following command on the Terminal:

```bash
streamlit run app/app.py
```


## References

- [Langchain PDF Loaders](https://python.langchain.com/docs/modules/data_connection/document_loaders/pdf)
- [Langchain Text Splitters](https://python.langchain.com/docs/modules/data_connection/document_transformers/#text-splitters)
- [streamlit](https://docs.streamlit.io/)
