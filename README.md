# Document Classifier

A simple Flask-based web application for classifying documents (such as pay stubs, passports, applications, invoices, and more) by extracting text from PDF files using PyMuPDF (fitz).

## Features

- Upload PDF files through a web interface.
- Extract key text from PDF files.
- Classify the document type based on its content (Pay Stub, Passport, Application, etc.).
- Display the extracted text (first 500 characters) and document classification.

## Requirements

- Python 3.7+
- Flask
- PyMuPDF (fitz)
- Werkzeug
