```bash
This repository contains five Streamlit applications built with LangChain that demonstrate different ways to use OpenAI's language models for practical text processing and generation tasks.
Table of Contents

Overview

# Applications
    * Text Redaction Improver
    * Blog Post Generator
    * Split and Summarize
    * Text Summarization
    * Extract Data from Reviews


Installation
* Usage
* Requirements
* Project Structure
* Environment Variables
* Contributing
* License

Overview
This collection showcases how to build interactive web applications that leverage the power of OpenAI's language models through LangChain and Streamlit. Each application demonstrates different capabilities and use cases for LLMs in real-world scenarios.
Applications
Text Redaction Improver
An application that rewrites text in different tones and dialects.
Features:

    Supports formal and informal tones
    American and British English dialect options
    Maintains the core meaning while adapting style
    Character limit protection (maximum 700 words)
    Detailed examples of different tones and dialects

Use Case:
Useful for writers, marketers, and content creators who need to adapt their writing for different audiences or publications.
Blog Post Generator
A simple application that generates 400-word blog posts on any topic.
Features:

    - Clean, user-friendly interface
    - Topic input field
    - Word count tracking
    - Professional blog post generation with consistent length

Use Case:
Perfect for content creators, marketers, or anyone needing quick blog content ideas or drafts.
Split and Summarize
An application that summarizes large text files by splitting them into manageable chunks.
Features:

File upload functionality for text files
Handles long documents (up to 20,000 words)
Efficient text splitting with context preservation
Map-reduce summarization technique for better results

Use Case:
Ideal for researchers, students, and professionals who need to extract key information from large documents.
Text Summarization
A simpler text summarization tool that works with pasted text rather than uploaded files.
Features:

    - Text area for direct input
    - Form-based submission for better security
    - Character-based text splitting
    - Clean presentation of summary results

Use Case:
Perfect for quickly summarizing articles, reports, or any text that needs condensing.
Extract Data from Reviews
An application that extracts key information from product reviews.
Features:

    - Sentiment analysis (Positive, Negative, Neutral, Unknown)
    - Delivery time extraction
    - Price perception analysis (Expensive, Cheap, Neutral, Unknown)
    - Formatted bullet-point output
    - Character limit protection (maximum 700 words)

Use Case:
Ideal for e-commerce businesses, market researchers, and product managers who need to analyze customer feedback efficiently.
```

# Installation

1. Clone this repository:

```bash
git clone https://github.com/yourusername/langchain-streamlit-apps.git
cd langchain-streamlit-apps
```
2. Create a virtual environment and activate it:
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate
```
3. Install the required packages:

```bash
pip install -r requirements.txt
```

### Usage
##### Each application can be run individually using Streamlit:
```bash
#Run the Text Redaction Improver

cd 01-streamlit-redaction-improver
streamlit run main.py

# Run the Blog Post Generator
cd 02-streamlit-blog-post-generator
streamlit run main.py

# Run the Split and Summarize app
cd 03-streamlit-split-and-summarize
streamlit run main.py

# Run the Text Summarization app
cd 04-streamlit-text-summarization
streamlit run main.py

# Run the Extract Data from Reviews app
cd 05-streamlit-extract-json-from-review
streamlit run main.py
```
You will need to provide your OpenAI API key when using the applications, either through the interface or by setting it as an environment variable.

Requirements
This project requires the following packages:

    - streamlit>=1.36.0
    - langchain==0.3.25
    - langchain-core==0.3.61
    - langchain-openai==0.3.18
    - pydantic==2.11.5
    - langsmith==0.1.75
    - pandas
    - python-dotenv

See the full list in the requirements.txt file within each application folder.
## Project Structure
```bash
langchain-streamlit-apps/
├── 01-streamlit-redaction-improver/
│   ├── main.py          # Text redaction app
│   ├── requirements.txt # Dependencies
│   └── README.md        # App-specific documentation
├── 02-streamlit-blog-post-generator/
│   ├── main.py          # Blog post generation app
│   ├── requirements.txt # Dependencies
│   └── README.md        # App-specific documentation
├── 03-streamlit-split-and-summarize/
│   ├── main.py          # File-based text summarization app
│   ├── requirements.txt # Dependencies
│   └── README.md        # App-specific documentation
├── 04-streamlit-text-summarization/
│   ├── main.py          # Text area summarization app
│   ├── requirements.txt # Dependencies
│   └── README.md        # App-specific documentation
├── 05-streamlit-extract-json-from-review/
│   ├── main.py          # Review data extraction app
│   ├── requirements.txt # Dependencies
│   └── README.md        # App-specific documentation
└── README.md            # This file
```

Environment Variables
For security and convenience, you can store your OpenAI API key in a `.env` file in the root directory of each application:
```bASH
OPENAI_API_KEY=your_api_key_here
```
To load this environment variable, make sure to add the following code to your applications:
```bash
python

import os
from dotenv import load_dotenv

load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")
```
# Project Credits and Resources

## Inspiration and Tutorials
Subscribe to [**dswithbappy YouTube Channel**](https://www.youtube.com/@dswithbappy) for more tutorials and guidance on building LLM applications with LangChain and Streamlit.

## Key Technologies and Frameworks

### LangChain
- **Website:** [https://www.langchain.com/](https://www.langchain.com/)
- **Framework for developing LLM-powered applications**
- Provides powerful tools for working with language models
- **GitHub Repository:** [LangChain Official Repository](https://github.com/langchain-ai/langchain)

### Streamlit
- **Website:** [https://streamlit.io/](https://streamlit.io/)
- **Open-source app framework for Machine Learning and Data Science**
- Easily create web applications with Python
- **GitHub Repository:** [Streamlit Official Repository](https://github.com/streamlit/streamlit)

### OpenAI
- **Website:** [https://openai.com/](https://openai.com/)
- **Leading artificial intelligence research laboratory**
- Provides state-of-the-art language models
- **GitHub Repository:** [OpenAI API Library](https://github.com/openai/openai-python)

## Acknowledgements
- Special thanks to [dswithbappy YouTube Channel](https://www.youtube.com/@dswithbappy) for providing invaluable tutorials
- Inspiration and learning resources that made this project possible

## Learn More
- **Documentation Links:**
  - [LangChain Documentation](https://python.langchain.com/)
  - [Streamlit Documentation](https://docs.streamlit.io/)
  - [OpenAI API Documentation](https://platform.openai.com/docs/)
