# Import necessary libraries
import streamlit as st  # For building the web interface
from langchain_core.prompts import PromptTemplate  # For creating structured prompts
from langchain_openai import OpenAI  # OpenAI LLM integration

# Define the template for extracting key information from product reviews
# This template provides instructions for the AI to extract sentiment, delivery time, and price perception
template = """\
For the following text, extract the following \
information:

sentiment: Is the customer happy with the product? 
Answer Positive if yes, Negative if \
not, Neutral if either of them, or Unknown if unknown.

delivery_days: How many days did it take \
for the product to arrive? If this \
information is not found, output No information about this.

price_perception: How does it feel the customer about the price? 
Answer Expensive if the customer feels the product is expensive, 
Cheap if the customer feels the product is cheap,
not, Neutral if either of them, or Unknown if unknown.

Format the output as bullet-points text with the \
following keys:
- Sentiment
- How long took it to deliver?
- How was the price perceived?

Input example:
This dress is pretty amazing. It arrived in two days, just in time for my wife's anniversary present. It is cheaper than the other dresses out there, but I think it is worth it for the extra features.

Output example:
- Sentiment: Positive
- How long took it to deliver? 2 days
- How was the price perceived? Cheap

text: {review}
"""

# Create a PromptTemplate with a variable for the review text
prompt = PromptTemplate(
   input_variables=["review"],  # Variable to be inserted into the template
   template=template,  # The template string defined above
)

# Function to initialize the OpenAI LLM with the provided API key
def load_LLM(openai_api_key):
   """Logic for loading the chain you want to use should go here."""
   # Create an OpenAI LLM instance with temperature=0 (deterministic outputs)
   llm = OpenAI(temperature=0, openai_api_key=openai_api_key)
   return llm

# Configure the Streamlit page
st.set_page_config(page_title="Extract Key Information from Product Reviews")  # Set browser tab title
st.header("Extract Key Information from Product Reviews")  # Add main header to the page

# Create a two-column layout for introduction text
col1, col2 = st.columns(2)

# Left column: App description and information to be extracted
with col1:
   st.markdown("Extract key information from a product review.")
   st.markdown("""
       - Sentiment
       - How long took it to deliver?
       - How was its price perceived?
       """)

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

# Section for entering the product review
st.markdown("## Enter the product review")

# Function to create and get the review text input
def get_review():
   review_text = st.text_area(
       label="Product Review", 
       label_visibility='collapsed',  # Hide the label
       placeholder="Your Product Review...", 
       key="review_input"
   )
   return review_text

# Get the review text from the user
review_input = get_review()

# Check if the review is too long (more than 700 words)
if len(review_input.split(" ")) > 700:
   st.write("Please enter a shorter product review. The maximum length is 700 words.")
   st.stop()  # Stop execution if review is too long

# Section for displaying the extracted information
st.markdown("### Key Data Extracted:")

# Process the input if review text is provided
if review_input:
   # Check if API key is provided
   if not openai_api_key:
       # Show warning if API key is missing
       st.warning('Please insert OpenAI API Key. \
           Instructions [here](https://help.openai.com/en/articles/4936850-where-do-i-find-my-secret-api-key)', 
           icon="⚠️")
       st.stop()  # Stop execution if API key is missing

   # Initialize the LLM with the API key
   llm = load_LLM(openai_api_key=openai_api_key)

   # Format the prompt with the user's review
   prompt_with_review = prompt.format(
       review=review_input  # User's review text
   )

   # Generate the key data extraction using the LLM
   # Note: This should be updated to use llm.invoke() for newer versions of LangChain
   key_data_extraction = llm(prompt_with_review)

   # Display the extracted information
   st.write(key_data_extraction)