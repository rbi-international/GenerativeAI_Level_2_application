# Import necessary libraries
import streamlit as st  # For building the web interface
from langchain_core.prompts import PromptTemplate  # For creating structured prompts
from langchain_openai import OpenAI  # OpenAI LLM integration
from langchain.chains.summarize import load_summarize_chain  # Summarization chain
from langchain.text_splitter import RecursiveCharacterTextSplitter  # For splitting long texts
import pandas as pd  # For data manipulation (though not used directly in this app)
from io import StringIO  # For handling text file uploads

# Function to initialize the OpenAI LLM with API key
def load_LLM(openai_api_key):
   # Create an OpenAI LLM instance with temperature=0 (more deterministic outputs)
   llm = OpenAI(temperature=0, openai_api_key=openai_api_key)
   return llm

# Configure the Streamlit page
st.set_page_config(page_title="AI Long Text Summarizer")  # Set browser tab title
st.header("AI Long Text Summarizer")  # Add main header to the page

# Create a two-column layout for introduction text
col1, col2 = st.columns(2)

# Left column: App description
with col1:
   st.markdown("ChatGPT cannot summarize long texts. Now you can do it with this app.")

# Right column: Channel promotion
with col2:
   st.write("Subscribe to [dswithbappy](https://www.youtube.com/@dswithbappy)")

# Section for OpenAI API key input
st.markdown("## Enter Your OpenAI API Key")

# Function to create and get the API key input
def get_openai_api_key():
   input_text = st.text_input(
       label="OpenAI API Key ",  
       placeholder="Ex: sk-2twmA8tfCb8un4...", 
       key="openai_api_key_input", 
       type="password"  # Mask the API key for security
   )
   return input_text

# Get the API key from the user
openai_api_key = get_openai_api_key()

# Section for file upload
st.markdown("## Upload the text file you want to summarize")

# Create a file uploader that accepts .txt files
uploaded_file = st.file_uploader("Choose a file", type="txt")

# Section for displaying the summary output
st.markdown("### Here is your Summary:")

# Only process if a file has been uploaded
if uploaded_file is not None:
   # Read the uploaded file as bytes
   bytes_data = uploaded_file.getvalue()
   
   # Convert the bytes to a string using StringIO
   stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
   
   # Read the content as a string
   string_data = stringio.read()
   
   # Store the file content for processing
   file_input = string_data

   # Check if the file is too large (word count > 20000)
   if len(file_input.split(" ")) > 20000:
       st.write("Please enter a shorter file. The maximum length is 20000 words.")
       st.stop()  # Stop execution if file is too large

   # Check if we have both file content and API key
   if file_input:
       if not openai_api_key:
           # Show warning if API key is missing
           st.warning('Please insert OpenAI API Key. \
           Instructions [here](https://help.openai.com/en/articles/4936850-where-do-i-find-my-secret-api-key)', 
           icon="⚠️")
           st.stop()  # Stop execution if API key is missing

   # Initialize text splitter to break long text into manageable chunks
   text_splitter = RecursiveCharacterTextSplitter(
       separators=["\n\n", "\n"],  # Split on paragraph and line breaks
       chunk_size=5000,  # Each chunk will be approximately 5000 characters
       chunk_overlap=350  # Overlap between chunks to maintain context
   )

   # Split the input text into documents (chunks)
   splitted_documents = text_splitter.create_documents([file_input])

   # Initialize the LLM with the API key
   llm = load_LLM(openai_api_key=openai_api_key)

   # Create a summarization chain using the map_reduce approach
   # map_reduce first summarizes each chunk, then summarizes those summaries
   summarize_chain = load_summarize_chain(
       llm=llm, 
       chain_type="map_reduce"  # Use map_reduce for efficient handling of multiple chunks
   )

   # Run the summarization chain on the split documents
   summary_output = summarize_chain.run(splitted_documents)

   # Display the summary result
   st.write(summary_output)