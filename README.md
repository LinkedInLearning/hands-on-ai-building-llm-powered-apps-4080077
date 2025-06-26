# Hands-On AI: Building and Deploying LLM-Powered Apps
This is the repository for the LinkedIn Learning course `Hands-On AI: Building and Deploying LLM-Powered Apps`. The full course is available from [LinkedIn Learning][lil-course-url].

_See the readme file in the main branch for updated instructions and information._
## Lab6: Setup Prompting
Now our Chat with PDF application is up and running, but we run into a very slight problem: one of the key questions is not working despite that there's ample information in the PDF documents!!!

We can "fix" this is via prompt engineering. Prompt Engineering refers to methods for how to communicate with LLM to steer its behavior for desired outcomes without updating the model weights.

Before we can do that, we need to setup our LLM app to use prompt templates.

## Exercises

Please refactor our current code to utilize Langchain's LCEL and put the prompts into independent prompt.py in the app directory. Control (or Command for Mac) click will help you navigate this very quickly!

## References

- [Prompt Engineering vs Blind Prompting](https://mitchellh.com/writing/prompt-engineering-vs-blind-prompting)
- [LCEL RetrievalQA](https://python.langchain.com/docs/versions/migrating_chains/retrieval_qa/)
