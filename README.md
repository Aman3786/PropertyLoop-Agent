# 👷 PropertyLoop Agent

## :pushpin: Project Overview

**PropertyLoop-Agent** is a Streamlit-based multi-agent chatbot designed to resolve Real Estate–related queries using multimodal inputs. Users can upload property images and enter text queries (e.g., questions about property issues or tenancy FAQs), and the system intelligently routes the request to the correct agent. The project leverages LangChain for agent orchestration with a Groq-backed Llama 3.2 vision model and an external SerpAPI tool (integrated via LangChain) for Web Search to enrich its responses.

Check Now: https://propertyloop-agent.up.railway.app/

---
Key components of the project include:
- **Image Upload & Caching:** Uploaded images are encoded and stored in Streamlit's session state, preventing redundant Base64 re-encoding across multiple queries.
- **Agent Switching:** A routing logic determines which agent to use based on image presence and text keywords.
- **Multimodal Analysis:** The property issue troubleshooting agent uses image analysis (via a placeholder vision function) combined with text context to diagnose issues like water damage, cracks, or mold.
- **Tenancy FAQ Agent:** This agent handles tenancy-related questions by leveraging external context sourced from SerpAPI.
  
---

## :rocket: Features
:white_check_mark: **Vision + Chat Model** – Analyze Image based on Query using **llama-3.2-90b-vision-preview** or **llama-3.2-11b-vision-preview**.

:white_check_mark: **External Context Integration:** Incorporates external search results from SerpAPI(via LangChain) web search to enrich responses.

:white_check_mark: **Agent Routing:** Automatically selects the property troubleshooting or tenancy FAQ agent based on input analysis.

:white_check_mark: **Interactive Web Interface** – Built with **Streamlit** for an easy-to-use experience.

:white_check_mark: **Real-Time Processing** – Instant Image Analysis, response generation with Web Search Functionality.

:white_check_mark: **Deployment Ready:** Designed for easy deployment on platforms like Railway hosting.

---

## :hammer_and_wrench: Tech Stack
| **Technology**    | **Purpose** |
|--------------|---------|
| **Python**   | Core language for the application |
| **Langchain**   | For LLM, agent orchestration and tool integration. |
| **Streamlit** | Web framework for UI and interaction |
| **llama-3.2-90b-vision-preview / llama-3.2-11b-vision-preview** | Groq-powered Multimodal Image + Text Analysis and response generation |
| **SerpAPI** | Web Search Tool for Agent using Langchain |
| **Railway Hosting** | Deployment platform for the application |

---

## :hammer_and_wrench: Installation & Setup

### :one: Clone the Repository
```bash
git clone https://github.com/Aman3786/PropertyLoop-Agent.git
cd PropertyLoop-Agent
```

### :two: Install Dependencies
For Windows (CMD)
```bash
pip install -r requirements.txt
```
For Linux (Terminal)
```bash
pip3 install -r requirements.txt
```

### :three: Create .env file and add Variables
For Groq: https://console.groq.com/keys

For SerpAPI: https://serpapi.com/manage-api-key
```bash
GROQ_API_KEY="Your Groq API Key"
SERPAPI_API_KEY="Your Serpapi API Key"
BASE_URL="https://api.groq.com/openai/v1"
```

### :four: Run the Application (Inside CMD/Terminal)
```bash
streamlit run app.py
```

### :five: Access the App
* Access the app in your browser at http://localhost:8501

---

## :scroll: How It Works

### User Upload & Encoded:

- The user uploads an image using the Streamlit file uploader.
- The app encodes the image to Base64 and pass it to the Multimodal Vision + Text for Analysis.

### Agent Routing (Router Mechanism):

- A helper function (classify_input) examines the presence of an image and keywords in the text query.
- If an image is present, the query is routed to the Property Issue Troubleshooting Agent (Agent1).
- If the text query contains tenancy-specific keywords, it is routed to the Tenancy FAQ Agent (Agent2).

### Response Generation:

- The property agent integrates a simulated image analysis and text query to generate a detailed diagnosis and solution of it.
- The tenancy agent takes text query and provide expert tenancy law guidance.
- Both Agent uses Langchain implemented SerpAPI Web Search tool to get Information from Internet for additional context

---

## :question: FAQ

Q. Which tools/tech were used?

Ans. The project uses LangChain for agent management and tool binding, the Groq-backed Llama 3.2 vision model for multimodal processing, and SerpAPI (via Google Search as configured) for external context.

Q. What is the logic behind agent switching?

Ans. Here, Router Mechanism is used for Agent Selection. The logic checks if an image is provided or if the text query contains tenancy-related keywords. Based on that, it routes the query to either the property troubleshooting agent (when an image exists) or the tenancy FAQ agent.

Q. How does image-based issue detection work?

Ans. The image is encoded with Base64 Encoder and passed Image + Text to Groq Llama 3.2 Vision Model along with prompts and extracts information about potential issues (e.g., water damage, cracks etc..) and provide solution of it.

---

## ❄️ Usecase Examples Covered:

- ### Property Issue Agent Examples

1. Mould on Ceiling
   
![Mould Ceiling 1](https://github.com/user-attachments/assets/2277336a-768d-4ce7-99f6-00b545d3fc60)

![Mould Ceiling 2](https://github.com/user-attachments/assets/d06b9b7b-9947-4ba8-a7d7-cff753dc0ce7)

2. Paint Peeling

![Paint Peeling 1](https://github.com/user-attachments/assets/02a60974-8768-4a23-a2dc-80991d3dcc97)

![Paint Peeling 2](https://github.com/user-attachments/assets/7d88ad7b-0b82-4377-ba55-02c780147583)


- ### Tenancy law Agent Examples

 1. Eviction Notice
    
![Tenant law 1](https://github.com/user-attachments/assets/316e9503-beb8-4d03-bdc1-91254f7ea08b)

 2. Eviction Notice Based on location

![Tenant law 2](https://github.com/user-attachments/assets/810a97ff-2897-4125-8963-9a6a37ad5576)


---
## :e-mail: Contact
For queries, reach out to:

:envelope_with_arrow: Email: amaanshk3786@gmail.com

:link: GitHub: [Aman3786](https://github.com/Aman3786)

Happy Coding! :rocket::studio_microphone:
