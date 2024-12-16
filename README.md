# Chat with PDF using Gemini

This project leverages **Google Generative AI (Gemini)** and **LangChain** to create a Streamlit-based web application that allows users to:

1. Upload PDF files.
2. Process the PDF content into manageable chunks.
3. Ask questions based on the content of the uploaded PDFs, with answers powered by Google Generative AI and FAISS.

This app demonstrates the seamless integration of document processing and conversational AI for knowledge extraction from PDFs.

---

## Features

- **PDF Upload & Processing**: Extract text from multiple PDF files and split it into meaningful chunks for analysis.
- **FAISS Vector Store**: Index the processed text for efficient similarity search.
- **Conversational Q&A**: Ask detailed questions about the PDF content with context-aware responses.
- **Streamlit UI**: User-friendly interface for uploading, processing, and interacting with PDFs.

---

## Tools & Technologies

### Core Tools:
- **[Google Generative AI (Gemini)](https://developers.generativeai.google/)**: Generates contextually accurate and detailed answers.
- **LangChain**: Framework for building language model applications.
- **FAISS**: Efficient similarity search for vectorized text.

### Python Libraries:
- `streamlit`: For building the interactive web application.
- `PyPDF2`: Extracts text from PDFs.
- `langchain`: Orchestrates prompts and chains for AI workflows.
- `langchain_google_genai`: Integration with Google Generative AI.
- `dotenv`: Securely loads environment variables from a `.env` file.

---

## Installation & Setup

### Prerequisites
- Python 3.8+
- A valid Google Generative AI API key

### Steps

1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```

2. **Set Up Virtual Environment (Optional)**:
   ```bash
   python -m venv env
   source env/bin/activate   # For Linux/Mac
   env\Scripts\activate     # For Windows
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Add Your Google API Key**:
   - Create a `.env` file in the project root directory.
   - Add your Google Generative AI API key to the file:
     ```env
     GOOGLE_API_KEY=your_google_api_key_here
     ```

5. **Run the Application**:
   ```bash
   streamlit run app.py
   ```

---

## Usage

1. Open the Streamlit application in your browser.
2. Upload PDF files via the sidebar.
3. Click **Submit & Process** to extract and index the content.
4. Type your question about the PDF content in the input box and receive context-aware answers.

Example Interaction:

- **User Question**: "What is the summary of Chapter 1?"
- **AI Response**: "The summary of Chapter 1 is as follows: ..."

---

## Project Structure

```
.
├── app.py                  # Streamlit app script
├── generator.py            # Core functions for text processing and QA
├── .env                    # Environment file (contains API key)
├── requirements.txt        # Python dependencies
├── README.md               # Project documentation
└── ... (additional files as needed)
```

---

## How It Works

1. **Text Extraction**:
   - Upload and read PDF files using `PyPDF2`.
   - Extract raw text from the PDF pages.

2. **Text Chunking**:
   - Split the extracted text into manageable chunks with the `RecursiveCharacterTextSplitter`.

3. **Vector Store**:
   - Embed the text chunks using Google Generative AI embeddings.
   - Store and index the embeddings in FAISS for similarity search.

4. **Conversational QA**:
   - Use LangChain's `ChatGoogleGenerativeAI` with a custom prompt template to generate detailed and accurate answers based on the PDF content.

---

## Requirements

- Python 3.8+
- Google Generative AI API key
- Streamlit (for running the web app)

---

## Contributing

Contributions are welcome! Feel free to submit issues or pull requests to improve the app. Follow the [contribution guidelines](CONTRIBUTING.md) for details.

---

## Acknowledgments

Special thanks to:
- **Google Generative AI Team** for their advanced AI tools.
- The developers of **LangChain** for simplifying complex AI workflows.
- The **Streamlit Community** for their excellent support and resources.

---

## Author

**Bisma Shafiq**

Connect with me on [LinkedIn](https://www.linkedin.com/in/bisma-shafiq-3a3b31242/)!
