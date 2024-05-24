import os
import nltk
from nltk import ne_chunk, pos_tag, word_tokenize
from nltk.tree import Tree
from PyPDF2 import PdfFileReader
from docx import Document

# Descargar los recursos necesarios para NLTK si aún no están descargados
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')
nltk.download('words')

def extract_text_from_pdf(pdf_path):
    text = ""
    with open(pdf_path, "rb") as f:
        pdf_reader = PdfFileReader(f)
        for page_num in range(pdf_reader.numPages):
            page = pdf_reader.getPage(page_num)
            text += page.extractText()
    return text

def extract_text_from_docx(docx_path):
    doc = Document(docx_path)
    text = ""
    for paragraph in doc.paragraphs:
        text += paragraph.text + "\n"
    return text

def identify_named_entities(text):
    tokens = word_tokenize(text)
    pos_tags = pos_tag(tokens)
    ner_chunks = ne_chunk(pos_tags)
    named_entities = []
    for chunk in ner_chunks:
        if isinstance(chunk, Tree):
            entity = " ".join([token for token, tag in chunk.leaves()])
            named_entities.append((entity, chunk.label()))
    return named_entities

def analyze_document(file_path):
    _, file_extension = os.path.splitext(file_path)
    if file_extension.lower() == ".txt":
        with open(file_path, "r", encoding="utf-8") as file:
            text = file.read()
    elif file_extension.lower() == ".pdf":
        text = extract_text_from_pdf(file_path)
    elif file_extension.lower() == ".docx":
        text = extract_text_from_docx(file_path)
    else:
        raise ValueError("Unsupported file format")
    
    named_entities = identify_named_entities(text)
    return named_entities

if __name__ == "__main__":
    file_path = input("Enter the path to the text, PDF, or Word document: ")
    named_entities = analyze_document(file_path)
    print("Named Entities:")
    for entity, entity_type in named_entities:
        print(f"{entity} - {entity_type}")
