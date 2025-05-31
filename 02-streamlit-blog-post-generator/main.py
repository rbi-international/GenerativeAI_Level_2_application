# Import necessary libraries
import streamlit as st  # For creating the web application interface
from langchain_openai import OpenAI  # OpenAI LLM integration for LangChain
from langchain_core.prompts import PromptTemplate  # For structured prompt creation

# Configure the Streamlit page with a title that appears in the browser tab
st.set_page_config(
   page_title="Blog Post Generator"  # Sets the browser tab title
)

# Add a main title to the application page
st.title("Blog Post Generator")  # Displays the app title at the top of the page

# Create a text input field in the sidebar for the API key
# The "password" type ensures the key is masked for security
openai_api_key = st.sidebar.text_input(
   "OpenAI API Key",  # Label for the input field
   type="password"  # Makes the input appear as dots for security
)

# Define the function that will generate the blog post
def generate_response(topic):
   # Initialize the OpenAI language model with the provided API key
   llm = OpenAI(openai_api_key=openai_api_key)
   
   # Create a template for the prompt with instructions for the AI
   # This template defines what we want the AI to generate
   template = """
   As experienced startup and venture capital writer, 
   generate a 400-word blog post about {topic}
   
   Your response should be in this format:
   First, print the blog post.
   Then, sum the total number of words on it and print the result like this: This post has X words.
   """
   
   # Create a PromptTemplate object that allows inserting the topic into the template
   prompt = PromptTemplate(
       input_variables=["topic"],  # Variables that can be inserted into the template
       template=template  # The template string defined above
   )
   
   # Format the prompt by inserting the actual topic
   query = prompt.format(topic=topic)
   
   # Call the language model with the formatted prompt
   # Using invoke() method (current recommended approach) instead of the deprecated __call__
   # max_tokens limits the response length to 2048 tokens
   response = llm.invoke(query, max_tokens=2048)
   
   # Display the response in the Streamlit app
   return st.write(response)

# Create a text input field for the user to enter the blog topic
topic_text = st.text_input("Enter topic: ")

# Check if the API key is valid (should start with "sk-")
if not openai_api_key.startswith("sk-"):
   # Show a warning if the API key is missing or invalid
   st.warning("Enter OpenAI API Key")
elif topic_text:  # Only proceed if the user has entered a topic
   # Call the generate_response function with the user's topic
   generate_response(topic_text)