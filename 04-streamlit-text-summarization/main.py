# Import necessary libraries
import streamlit as st  # For building the web interface
from langchain_openai import OpenAI  # OpenAI LLM integration
from langchain.docstore.document import Document  # Document representation for LangChain
from langchain.text_splitter import CharacterTextSplitter  # For splitting text into chunks
from langchain.chains.summarize import load_summarize_chain  # Summarization chain from LangChain

# Define function to generate summary response
def generate_response(txt):
   # Initialize OpenAI language model with the provided API key and temperature 0 (deterministic output)
   llm = OpenAI(
       temperature=0,
       openai_api_key=openai_api_key
   )
   
   # Initialize text splitter to break long text into manageable chunks
   text_splitter = CharacterTextSplitter()  # Using default parameters
   
   # Split the input text into multiple chunks
   texts = text_splitter.split_text(txt)
   
   # Convert each text chunk into a Document object that LangChain can process
   docs = [Document(page_content=t) for t in texts]
   
   # Initialize the summarization chain with the map_reduce approach
   # map_reduce first summarizes each chunk, then summarizes those summaries
   chain = load_summarize_chain(
       llm,
       chain_type="map_reduce"
   )
   
   # Run the summarization chain and return the result
   return chain.run(docs)

# Configure the Streamlit page
st.set_page_config(
   page_title = "Writing Text Summarization"  # Sets the browser tab title
)

# Add a main title to the application
st.title("Writing Text Summarization")

# Create a text area for user input
# This allows users to enter or paste larger amounts of text
txt_input = st.text_area(
   "Enter your text",  # Label for the text area
   "",  # Default empty value
   height=200  # Set the height of the text area
)

# Initialize an empty list to store the result
result = []

# Create a form to collect the API key and handle submission
with st.form("summarize_form", clear_on_submit=True):  # clear_on_submit resets form after submission
   # Create a password field for the API key
   # Disabled if no text has been entered
   openai_api_key = st.text_input(
       "OpenAI API Key",
       type="password",  # Mask the API key for security
       disabled=not txt_input  # Disable if no text input provided
   )
   
   # Create a submit button
   submitted = st.form_submit_button("Submit")
   
   # Process the submission if form is submitted and API key is valid
   if submitted and openai_api_key.startswith("sk-"):
       # Generate the summary
       response = generate_response(txt_input)
       
       # Add the response to the results list
       result.append(response)
       
       # Delete the API key from memory for security
       del openai_api_key

# Display the result if there is one
if len(result):
   # Show the summary in an info box
   st.info(response)