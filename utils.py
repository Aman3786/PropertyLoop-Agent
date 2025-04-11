import base64
from langchain_community.utilities import SerpAPIWrapper
from langchain_core.tools import Tool
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage
from prompts import get_property_issue_agent_prompt, get_tenancy_agent_prompt
import os

# Uncommment Below lines when in Development Phase
# from dotenv import load_dotenv        
# load_dotenv()


GROQ_API_KEY = os.getenv("GROQ_API_KEY")
SERPAPI_API_KEY = os.getenv("SERPAPI_API_KEY")
BASE_URL = os.getenv("BASE_URL")



# Function to encode the image
def encode_image_base64(image):
    try:
        return base64.b64encode(image.read()).decode("utf-8")
    except Exception as e:
        return e


# Function to get information from internet through SerpAPI
def get_serpapi_tool():
    try:
        search = SerpAPIWrapper(serpapi_api_key=SERPAPI_API_KEY,params={"engine": "google"})
        serpapi_search_tool = Tool(
            name="SerpAPI Search",
            func=search.run,
            description="Useful for providing external context on property issues and tenancy FAQs."
        )

        return serpapi_search_tool

    except Exception as e:
        return e




def get_llm(model):
    try:
        serpapi_search_tool = get_serpapi_tool()

        llm = ChatOpenAI(
            base_url=BASE_URL,
            api_key=GROQ_API_KEY,
            model=model,
            max_retries=2, 
        )

        llm.bind_tools([serpapi_search_tool])

        return llm

    except Exception as e:
        print(e)
        return e



def get_response_property_issue_agent(model, image, query):
    try:
        # Getting the Base64 string
        base64_image = encode_image_base64(image)

        # Getting the SerpAPI tool for Web Search
        serpapi_search_tool = get_serpapi_tool()

        # Getting Prompt for property Agent
        prompt = get_property_issue_agent_prompt(query=query)

        message = HumanMessage(
            content=[
                {   "type": "text",
                    "text": prompt,
                },
                {
                    "type": "image_url",
                    "image_url": {"url": f"data:image/jpeg;base64,{base64_image}"},
                },
            ]
        )

        llm = get_llm(model=model)    
        response = llm.invoke([message])

        return response.content

    except Exception as e:
        return e



def get_response_tenancy_agent(model, query):
    try:
        # Getting the SerpAPI tool for Web Search
        serpapi_search_tool = get_serpapi_tool()

        # Getting Prompt for property Agent
        prompt = get_tenancy_agent_prompt(query=query)

        message = HumanMessage(
            content=[
                {   "type": "text",
                    "text": prompt,
                },
            ]
        )
        

        llm = get_llm(model=model)
        response = llm.invoke([message])

        return response.content

    except Exception as e:
        return e