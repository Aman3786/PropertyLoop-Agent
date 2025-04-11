import streamlit as st
from utils import encode_image_base64, get_response_property_issue_agent, get_response_tenancy_agent


# Router to route to correct Agent
def classify_input(image,text):
    """
    Decide which agent to route input to, based on image presence and keywords in text.
    """
    if image:
        return "Agent1"  # Property issue troubleshooting agent.
    elif any(keyword in text.lower() for keyword in ["agreement", "rent", "tenant", "landlord", "deposit", "notice", "evict", "buy", "sell"]):
        return "Agent2"  # Tenancy FAQ agent.
    else:
        return "Clarify"


# UI starts from here
st.set_page_config(
    page_title="PropertyLoop Agent",
    page_icon="👷",
)

st.title('👷 PropertyLoop Agent')
st.caption('Get your Property/Tenancy laws related query resolved here!') 

with st.sidebar.expander("⚙️ Bot Settings"):
    
    model = st.selectbox(
        "Vision + Chat Model 🤖",
        [
            "llama-3.2-90b-vision-preview",
            "llama-3.2-11b-vision-preview"
        ]
    )
    
    
image = st.file_uploader(label="Choose Image (optional):", type=["jpg", "jpeg", "png"])
query = st.text_area("Enter your query:", height=68)

if st.button("Submit"):
    if not query and not image:
        st.warning("Please provide a message or upload an image.")
    else:
        if image and not query:
            st.warning("Please provide a query along with image")
        else:
            try:
                with st.spinner('Getting your solution..'):
                    agent = classify_input(image, query)
                    
                    with st.spinner(f"Routing to {agent}..."):
                        if agent == "Agent1":
                            response = get_response_property_issue_agent(model, image, query)
                        elif agent == "Agent2":
                            response = get_response_tenancy_agent(model, query)
                        else:
                            response = ("Could you please clarify whether your question relates to a property issue or tenancy information?")
                
                if image:
                    st.image(image, caption=image.name, use_container_width=False)
                st.write(response)

            except Exception as e:
                st.error(e)