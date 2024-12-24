# FastAPI Chat Application with Google Generative AI

This is a web application built with **FastAPI** that integrates **Google Generative AI** for generating responses based on user input. The app is deployed on **Vercel** and uses environment variables for secure API key management.

---

## Features

- Accepts user input via a web form.
- Integrates with Google Generative AI (Gemini 1.5 flash model) to generate responses.
- Dynamically renders results on an HTML interface using Jinja2 templates.
- Deployed on Vercel for seamless scalability and accessibility.

---

## Token Limit and Rate Restrictions

- The application uses the **Google Generative AI API**, which enforces a **rate limit of 15 requests per minute**.
- Exceeding this limit will result in an **Internal Server Error (HTTP 500)**.
- To avoid this:
  - Minimize rapid, consecutive submissions.
  - Handle errors gracefully in the application by displaying a user-friendly message when the limit is reached.

--- 

## Acknowledgements 

Built with 💖 using **Vercel** and **FastAPI**
