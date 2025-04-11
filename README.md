# 🔊 PropertyLoop Agent

## :pushpin: Project Overview

**PropertyLoop Agent** is a Streamlit-based multi-agent chatbot designed to resolve Real Estate–related queries using multimodal inputs. Users can upload property images and enter text queries (e.g., questions about property issues or tenancy FAQs), and the system intelligently routes the request to the correct agent. The project leverages LangChain for agent orchestration with a Groq-backed Llama 3.2 vision model and an external SerpAPI tool (integrated via LangChain) for Web Search to enrich its responses.

Key components of the project include:
- **Image Upload & Caching:** Uploaded images are encoded and stored in Streamlit's session state, preventing redundant Base64 re-encoding across multiple queries.
- **Agent Switching:** A routing logic determines which agent to use based on image presence and text keywords.
- **Multimodal Analysis:** The property issue troubleshooting agent uses image analysis (via a placeholder vision function) combined with text context to diagnose issues like water damage, cracks, or mold.
- **Tenancy FAQ Agent:** This agent handles tenancy-related questions by leveraging external context sourced from SerpAPI.
  
---

## :rocket: Features

- **Dynamic Image Caching:** Utilizes Streamlit session state to cache the Base64-encoded version of the uploaded image, so that it need not be re-processed on subsequent queries.
- **Intelligent Agent Routing:** Automatically selects the property troubleshooting or tenancy FAQ agent based on input analysis.
- **Multimodal Input Handling:** Supports both image and text input, dynamically updating when the image is changed or removed.
- **External Context Integration:** Incorporates external search results from SerpAPI (via LangChain) to enrich responses.
- **Deployment Ready:** Designed for easy deployment on platforms like Railway hosting.

---

## :hammer_and_wrench: Installation & Setup

### :one: Clone the Repository
```bash
git clone https://github.com/YourUsername/PropertyLoopAgent.git
cd PropertyLoopAgent
```
:two: Create a Virtual Environment &
bash
Copy
Edit
python -m venv venv
source venv/bin/activate   # On macOS/Linux
venv\Scripts\activate      # On Windows
:three: Install Dependencies
Ensure you are in the project directory where requirements.txt is located:

bash
Copy
Edit
pip install -r requirements.txt
:four: Set Up Environment Variables
Create a .env file in the project directory with the following keys (or set them in your Railway hosting panel):

bash
Copy
Edit
GROQ_API_KEY=your_groq_api_key_here
SERPAPI_API_KEY=your_serpapi_api_key_here
BASE_URL=https://api.groq.com/openai/v1
:five: Run the App Locally
bash
Copy
Edit
streamlit run demo.py
Then access the app in your browser at http://localhost:8501.

:scroll: How It Works
User Upload & Caching:

The user uploads an image using the Streamlit file uploader.

The app encodes the image to Base64 once and stores it in st.session_state.uploaded_image.

If the image is changed or removed, the session state updates accordingly.

Agent Routing:

A helper function (classify_input) examines the presence of an image and keywords in the text query.

If an image is present, the query is routed to the Property Issue Troubleshooting Agent (Agent1).

If the text query contains tenancy-specific keywords, it is routed to the Tenancy FAQ Agent (Agent2).

Response Generation:

The property agent integrates a simulated image analysis (replaceable with an actual vision model) and text query to generate a detailed diagnosis.

The tenancy agent leverages external context via the SerpAPI tool to provide expert tenancy law guidance.

Dynamic UI Feedback:

The app uses dynamic spinner placeholders to update status messages sequentially (e.g., "Getting your solution..." → "Routing to {agent}...").

:hammer_and_wrench: Technologies Used
Python – Primary programming language.

Streamlit – Web framework for building the interactive UI.

LangChain – For agent orchestration and tool integration.

Groq Llama 3.2 Vision Model – Multimodal LLM for processing property-related image and text queries.

SerpAPI – Provides external search context (integrated via LangChain).

Session State – Efficient caching of image uploads to avoid repeated processing.

Railway Hosting – (Planned) Deployment platform for the application.

:question: FAQ
Which tools/tech were used?

The project uses LangChain for agent management and tool binding, the Groq-backed Llama 3.2 vision model for multimodal processing, and SerpAPI (via DuckDuckGo or SerpAPI as configured) for external context.

What is the logic behind agent switching?

The logic checks if an image is provided or if the text query contains tenancy-related keywords. Based on that, it routes the query to either the property troubleshooting agent (when an image exists) or the tenancy FAQ agent.

How does image-based issue detection work?

The image is encoded and stored in session state; a placeholder image analysis function (which can be replaced with a real model like CLIP/BLIP) extracts information about potential issues (e.g., water damage, cracks).

Use case examples covered:

Diagnosing property issues from uploaded images.

Answering tenancy law questions enriched by external web search results.

THE TOOL USED:

LangChain’s ChatGroq integration coupled with the Groq Llama 3.2 vision model, alongside an external search tool (SerpAPI).

Deployment:

The plan is to deploy this project on Railway Hosting.


