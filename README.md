---
license: other
title: Test
sdk: streamlit
sdk_version: 1.46.0
emoji: 🚀
colorFrom: green
colorTo: green
pinned: false
app_file: app/app.py
---
# Hands-On AI: Building and Deploying LLM-Powered Apps
This is the repository for the LinkedIn Learning course `Hands-On AI: Building and Deploying LLM-Powered Apps`. The full course is available from [LinkedIn Learning][lil-course-url].

_See the readme file in the main branch for updated instructions and information._

## Lab 7: Deploying the application to Huggingface and trace the application outputs on Langsmith

Now we have the application up and running, lets deploy it to Huggingface Spaces and trace the applicatio outputs on Langsmith. This way we can proudly show our work and keep record of what our users are doing with our application!

Before that happens, please register your account on Huggingface and Langsmith.

> NOTE: [Huggingface Spaces](https://huggingface.co/pricing) provides free tier access starting at $0.
> NOTE: [Langsmith](https://www.langchain.com/pricing-langsmith) is a paid application with a Developer tier license that gives access to 1 user and 5k traces per month.

## Exercises

After registering accounts on Huggingface and Langsmith, please grab the API keys and lets get to work.

Oh, and currently we have OpenAI API key baked into our application. Lets make sure that users of our application need to input their own key to use the application!

And then we will setup CI/CD for automated deployment.

Complete the exercises in `app/app.py` and `.env` (see `.env.sample`). Make sure you follow the instruction here: [https://huggingface.co/docs/hub/en/spaces-github-actions](https://huggingface.co/docs/hub/en/spaces-github-actions) and here [Hugging Face Hub: Important Git Authentication Changes](https://huggingface.co/blog/password-git-deprecation).

After deployment, please remember to into Huggingface Space settings to setup the environment variables such as `LANGSMITH_API_KEY`.

> NOTE: To reduce the scope, we will manually deploy to Huggingface Only. We prepared `.github/workflows/deploy-to-hf.yml` workflow as an extracurricular exercise for the learner.

## References

- [Huggingface Spaces](https://huggingface.co/pricing)
- [Langsmith](https://www.langchain.com/pricing-langsmith)
- [Huggingface Spaces Github Actions](https://huggingface.co/docs/hub/en/spaces-github-actions)
- [Hugging Face Hub: Important Git Authentication Changes](https://huggingface.co/blog/password-git-deprecation)