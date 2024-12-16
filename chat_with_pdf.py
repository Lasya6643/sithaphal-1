import PyPDF2
import os
import openai
from sentence_transformers import SentenceTransformer
import torch
import time
from transformers import pipeline

# Load environment variables
from dotenv import load_dotenv

# Load the .env file if you are using one
load_dotenv()

# Get the API key from environment variables
openai.api_key = os.getenv("OPENAI_API_KEY")

# Check if the key is loaded
if openai.api_key is None:
    print("API key is not set. Please set the OPENAI_API_KEY environment variable.")
else:
    print("API key loaded successfully.")

# Load a pre-trained sentence transformer model for embedding
model = SentenceTransformer('all-MiniLM-L6-v2')

# Load Hugging Face model for local question-answering
qa_pipeline = pipeline("question-answering", model="deepset/roberta-base-squad2")

# Path to your PDF file
pdf_path = "D:/chat_with_pdf/sample.pdf"  # Update this path if necessary

# Function to extract text from PDF using PyPDF2
def extract_text_from_pdf(pdf_path):
    with open(pdf_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        text = ""
        for page in reader.pages:
            text += page.extract_text()
    return text

# Function to split the text into manageable chunks
def split_text(text, max_chunk_size=2000):
    words = text.split()
    chunks = []
    current_chunk = []
    
    for word in words:
        current_chunk.append(word)
        if len(' '.join(current_chunk)) > max_chunk_size:
            chunks.append(' '.join(current_chunk[:-1]))
            current_chunk = [word]
    if current_chunk:
        chunks.append(' '.join(current_chunk))
    return chunks

# Function to get embeddings for a given text
def get_embeddings(text):
    return model.encode(text)

# Retry logic for OpenAI API with exponential backoff
def query_openai_with_backoff(prompt, max_retries=5, delay=5):
    for attempt in range(max_retries):
        try:
            # Correct OpenAI API call for gpt-3.5-turbo
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": prompt}],
                max_tokens=100,  # Adjust as needed
                temperature=0.7
            )
            return response['choices'][0]['message']['content'].strip()
        except openai.error.RateLimitError:
            print(f"Rate limit exceeded. Retrying... (Attempt {attempt + 1}/{max_retries})")
            time.sleep(delay)
        except openai.error.OpenAIError as e:
            print(f"OpenAI error occurred: {e}")
            break  # Exit if any other OpenAI error occurs
    return None  # Return None if retries fail

# Use Hugging Face model for question answering if OpenAI is not available
def local_query(text, question):
    result = qa_pipeline(question=question, context=text)
    print("Local Model Answer:", result)  # Print local model output for debugging
    return result['answer']

# Function to get answers to your queries based on the PDF
def get_answer_from_pdf(pdf_path, query):
    # Extract text from PDF
    text = extract_text_from_pdf(pdf_path)
    text_chunks = split_text(text)

    # Get embeddings for the query
    query_embedding = get_embeddings(query)

    # Find the chunk most relevant to the query
    best_chunk = None
    best_score = -1
    for chunk in text_chunks:
        chunk_embedding = get_embeddings(chunk)
        score = torch.cosine_similarity(torch.tensor(query_embedding).unsqueeze(0), torch.tensor(chunk_embedding).unsqueeze(0))
        if score > best_score:
            best_score = score
            best_chunk = chunk

    # Use OpenAI API to generate an answer based on the best chunk or fallback to local model
    prompt = f"Given the following text from a PDF, answer the question:\n\nText: {best_chunk}\n\nQuestion: {query}\nAnswer:"
    answer = query_openai_with_backoff(prompt)
    if not answer:  # If OpenAI API is unavailable or rate-limited, fall back to local model
        print("OpenAI API rate-limited or failed. Trying local model...")
        answer = local_query(best_chunk, query)
    
    return answer

# Main function to run the script
def main():
    # Query to ask about the PDF
    query = "What is the main topic of this PDF?"  # Replace with your actual question
    answer = get_answer_from_pdf(pdf_path, query)
    print("Answer:", answer)

if __name__ == "__main__":
    main()
