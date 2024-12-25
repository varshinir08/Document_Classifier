from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename
from app.ocr import extract_text_from_pdf
from app.classifier import classify_document
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = './uploads'
app.config['ALLOWED_EXTENSIONS'] = {'pdf'}

# Check allowed file types
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file provided'}), 400
    file = request.files['file']
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)

        # Extract text from PDF
        text = extract_text_from_pdf(filepath)
        
        # Classify document
        document_type = classify_document(text)

        return jsonify({
            'message': 'File processed successfully',
            'document_type': document_type,
            'extracted_text': text[:500]  # Show a snippet of the text
        })

    return jsonify({'error': 'Invalid file type'}), 400

if __name__ == '__main__':
    app.run(debug=True)


