#Chat with PDF - README


Project Overview :

This project is a Python-based application designed to extract text from PDF files using various libraries, including PyPDF2, PDFMiner, and transformers. The main goal is to allow users to upload a PDF file and retrieve textual content, which can then be further processed for natural language understanding tasks such as text summarization, question answering, and more.

Key Features :
          PDF Text Extraction: Extracts readable text from various PDF formats.
Text Summarization:          
          Provides the option to summarize long text extracted from PDFs.
Question Answering: 
          Allows users to ask questions about the content of the uploaded PDF file.

Tech Stack :

Python: The core programming language for the project.
PyPDF2: A library for PDF parsing and text extraction.
PDFMiner: A more advanced PDF text extraction library.
transformers: A library from Hugging Face, providing pre-trained models for tasks like text summarization and question answering.
Torch: A deep learning library that powers models used for NLP tasks.
GitHub: For version control and code management.
Git Large File Storage (LFS): Used for handling large files that exceed GitHub’s size limits.

Installation and Setup :
1. Clone the Repository
Start by cloning the repository to your local machine. Open your terminal and run the following command:

bash
Copy code
git clone https://github.com/Lasya6643/Sithaphal-task-1.git
cd Sithaphal-task-1
2. Setting up the Python Environment
It is recommended to use a virtual environment to manage dependencies.

Using venv (Virtual Environment)
Create a virtual environment:

bash
Copy code
python -m venv env
Activate the virtual environment:

On Windows:

bash
Copy code
.\env\Scripts\activate
On macOS/Linux:

bash
Copy code
source env/bin/activate
3. Install Dependencies
With the virtual environment activated, install the required dependencies:

bash
Copy code
pip install -r requirements.txt
This will install the libraries needed for PDF text extraction and NLP tasks.

4. Additional Setup for Large Files
Some files, like torch_cpu.dll and dnnl.lib, are large and may require Git Large File Storage (LFS). If you haven't set up Git LFS yet, follow these steps:

Install Git LFS if it's not already installed:

bash
Copy code
git lfs install
Track the large files:

bash
Copy code
git lfs track "env/Lib/site-packages/torch/lib/torch_cpu.dll"
git lfs track "env/Lib/site-packages/torch/lib/dnnl.lib"
Add the .gitattributes to Git and commit the changes:

bash
Copy code
git add .gitattributes
git commit -m "Track large files with Git LFS"
git push origin master
5. Running the Application
To use the application for text extraction, summarization, or question answering, run the script with the following command:

bash
Copy code
python extract_text.py
Ensure that the required sample.pdf or any other PDF file is placed in the same directory or specify the full path to the file.

Folder Structure :
bash
Copy code
/Sithaphal-task-1
│
├── /env                # Virtual environment folder (do not upload to GitHub)
├── /test_file_access   # Tests for file access
├── /env/Lib/           # Libraries and dependencies
├── requirements.txt    # Project dependencies
├── extract_text.py     # Script to extract text from PDFs
├── sample.pdf          # Sample PDF file for text extraction
├── README.md           # This file
└── .gitignore          # Git ignore rules
Contributing
Contributions are welcome! If you find a bug or want to add new features, please fork the repository, create a new branch, and submit a pull request.

How to Contribute:
Fork the repository.
Clone your forked repository to your local machine.
Create a new branch for your changes:
bash
Copy code
git checkout -b feature/new-feature
Make your changes.
Commit your changes:
bash
Copy code
git commit -m "Description of changes"
Push your changes to your forked repository:
bash
Copy code
git push origin feature/new-feature
Create a pull request from your fork to the main repository.
License
This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgements :
PyPDF2: For PDF text extraction.
transformers: For pre-trained models from Hugging Face.
Torch: For deep learning capabilities.
Contact Information
For questions or support, feel free to reach out via GitHub Issues

Troubleshooting :
Large File Errors: If you encounter errors when pushing large files, ensure you are using Git Large File Storage (LFS).
Missing Libraries: Ensure all dependencies are installed via pip install -r requirements.txt.
