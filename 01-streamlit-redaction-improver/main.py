# Import necessary libraries
import streamlit as st  # For building the web interface
from langchain_core.prompts import PromptTemplate  # For creating structured prompts
from langchain_openai import OpenAI  # OpenAI LLM integration

# Define the template for text rewriting
# This template contains instructions for the AI to rewrite text based on tone and dialect
template = """
    Below is a draft text that may be poorly worded.
    Your goal is to:
    - Properly redact the draft text
    - Convert the draft text to a specified tone
    - Convert the draft text to a specified dialect

    Here are some examples different Tones:
    - Formal: Greetings! OpenAI has announced that Sam Altman is rejoining the company as its Chief Executive Officer. After a period of five days of conversations, discussions, and deliberations, the decision to bring back Altman, who had been previously dismissed, has been made. We are delighted to welcome Sam back to OpenAI.
    - Informal: Hey everyone, it's been a wild week! We've got some exciting news to share - Sam Altman is back at OpenAI, taking up the role of chief executive. After a bunch of intense talks, debates, and convincing, Altman is making his triumphant return to the AI startup he co-founded.  

    Here are some examples of words in different dialects:
    - American: French Fries, cotton candy, apartment, garbage, \
        cookie, green thumb, parking lot, pants, windshield
    - British: chips, candyfloss, flag, rubbish, biscuit, green fingers, \
        car park, trousers, windscreen

    Example Sentences from each dialect:
    - American: Greetings! OpenAI has announced that Sam Altman is rejoining the company as its Chief Executive Officer. After a period of five days of conversations, discussions, and deliberations, the decision to bring back Altman, who had been previously dismissed, has been made. We are delighted to welcome Sam back to OpenAI.
    - British: On Wednesday, OpenAI, the esteemed artificial intelligence start-up, announced that Sam Altman would be returning as its Chief Executive Officer. This decisive move follows five days of deliberation, discourse and persuasion, after Altman's abrupt departure from the company which he had co-established.

    Please start the redaction with a warm introduction. Add the introduction \
        if you need to.
    
    Below is the draft text, tone, and dialect:
    DRAFT: {draft}
    TONE: {tone}
    DIALECT: {dialect}

    YOUR {dialect} RESPONSE:
"""

# Create a PromptTemplate with variables for tone, dialect, and draft text
prompt = PromptTemplate(
    input_variables=["tone", "dialect", "draft"],
    template=template,
)

# Function to initialize the OpenAI LLM with the provided API key
def load_LLM(openai_api_key):
    """Logic for loading the chain you want to use should go here."""
    # Create an OpenAI LLM instance with temperature=0.7 (more creative outputs)
    llm = OpenAI(temperature=.7, openai_api_key=openai_api_key)
    return llm

# Configure the Streamlit page
st.set_page_config(page_title="Re-write your text")  # Set browser tab title
st.header("Re-write your text")  # Add main header to the page

# Create a two-column layout for introduction text
col1, col2 = st.columns(2)

# Left column: App description
with col1:
    st.markdown("Re-write your text in different styles.")

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

# Section for entering the text to rewrite
st.markdown("## Enter the text you want to re-write")

# Function to create and get the draft text input
def get_draft():
    draft_text = st.text_area(
        label="Text", 
        label_visibility='collapsed',  # Hide the label
        placeholder="Your Text...", 
        key="draft_input"
    )
    return draft_text

# Get the draft text from the user
draft_input = get_draft()

# Check if the text is too long (more than 700 words)
if len(draft_input.split(" ")) > 700:
    st.write("Please enter a shorter text. The maximum length is 700 words.")
    st.stop()  # Stop execution if text is too long

# Create a two-column layout for tone and dialect options
col1, col2 = st.columns(2)

# Left column: Tone selection dropdown
with col1:
    option_tone = st.selectbox(
        'Which tone would you like your redaction to have?',
        ('Formal', 'Informal')  # Options for tone
    )
    
# Right column: Dialect selection dropdown
with col2:
    option_dialect = st.selectbox(
        'Which English Dialect would you like?',
        ('American', 'British')  # Options for dialect
    )
    
# Section for displaying the rewritten text
st.markdown("### Your Re-written text:")

# Process the input if draft text is provided
if draft_input:
    # Check if API key is provided
    if not openai_api_key:
        # Show warning if API key is missing
        st.warning('Please insert OpenAI API Key. \
            Instructions [here](https://help.openai.com/en/articles/4936850-where-do-i-find-my-secret-api-key)', 
            icon="⚠️")
        st.stop()  # Stop execution if API key is missing

    # Initialize the LLM with the API key
    llm = load_LLM(openai_api_key=openai_api_key)

    # Format the prompt with the user's selections and draft text
    prompt_with_draft = prompt.format(
        tone=option_tone,  # Selected tone
        dialect=option_dialect,  # Selected dialect
        draft=draft_input  # User's text
    )

    # Generate the improved redaction using the LLM
    # Note: This should be updated to use llm.invoke() for newer versions of LangChain
    improved_redaction = llm(prompt_with_draft)

    # Display the rewritten text
    st.write(improved_redaction)