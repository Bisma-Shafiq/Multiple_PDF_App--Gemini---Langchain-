import streamlit as st
from google.generativeai import genai
from PyPDF2 import PdfReader
import os
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbedding
from langchain.vectorstores import FAISS  # vector db
from langchain_google_genai import ChatGooglegenerativeAI   
from langchain.chains.question_answering import load_qa_chain  # for q-a
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv   # laod all envvironment

load_dotenv()  # see environmrnt variable

envir = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=envir)

models = genai.GenerativeaiModel("gemini-1.5-flash")

def get_pdf_text(pdf_document):
    text=""
    for pdf in pdf_document:
        pdf_reader = PdfReader(pdf)
    for pages in pdf_reader.pages:
        text = pages.extract_text()
    return text

def get_text_chunk(text):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=10000,chunk_overlap=1000)
    chunks = text_splitter.split_text(text)
    return chunks

def get_vector_embed(text_chunks):
    embeddings = GoogleGenerativeAIEmbedding(model="models/embedding-001")
    vector_store = FAISS.from_texts(text_chunks,embedding=embeddings)
    vector_store.save_local("Faiss_index")

def get_conversation():
    Prompt_Template = """
    Answer the question as detailed as possible from the provided context, make sure to provide context from given context, 
    make sure to provide context just say, "answer is available in the context", didn't provide the context
    Context: \n{context}?\n
    Question: \n{question}\n

    Answer:

    """
    model = ChatGooglegenerativeAI(models,temperature=0.2)
    prompt = PromptTemplate(template=Prompt_Template,input_variable=['context','question'])
    chain = load_qa_chain(model,chain_type = "stuff",prompt=prompt)
    return chain

def user_input(user_question):
    embeddings = GoogleGenerativeAIEmbedding(model = "models/embedding-001")
    new_doc = FAISS.load_local("faiss_index",embeddings)
    docs = new_doc.similarity_search(user_question)
    chain = get_conversation()

    response = chain(
        {'input_doc':docs,'question':user_question},return_only_outputs=True)

    print(response)
    st.write('Replay': response["output_text"])

def main():
    st.set_page_config("Multiple Chat PDF")
    st.header("Chat with PDF using Gemini💁")

    user_question = st.text_input("Ask a Question from  PDF Files")

    if user_question:
        user_input(user_question)

    with st.sidebar:
        st.title("Menu:")
        pdf_docs = st.file_uploader("Upload your PDF Files and Click on the Submit & Process Button", accept_multiple_files=True)
        if st.button("Submit & Process"):
            with st.spinner("Processing..."):
                raw_text = get_pdf_text(pdf_docs)
                text_chunks = get_text_chunks(raw_text)
                get_vector_store(text_chunks)
                st.success("Done")



if __name__ == "__main__":
    main()
