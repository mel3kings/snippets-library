from flask import Flask, request, jsonify
import base64
import PyPDF2
from flask_cors import CORS

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 32 * 1024 * 1024  # Set maximum content length to 32MB (change the value as per your requirement)
CORS(app)

@app.route('/upload', methods=['POST'])
def upload_pdf():
    if 'file' not in request.files:
        return 'No file found', 400

    pdf_file = request.files['file']
    pdf_data = pdf_file.read()

    # # Decode PDF file from base64
    # decoded_pdf = base64.b64decode(pdf_data)

    # Create a PDF reader object
    pdf_reader = PyPDF2.PdfReader(pdf_file)

    # Extract text from each page
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()
    
    text = sanitize_string(text)

    # Return the extracted text as the response
    return jsonify({'text': text}), 200



def sanitize_string(s):
    lines = s.split('\n')
    new_lines = []
    for line in lines:
        if len(line.split(' ')) <= 3:
            continue
        if line in new_lines:
            continue
        if line == '':
            continue
        if line.startswith('Title:'):
            continue
        new_lines.append(line)
    return '\n'.join(new_lines)

@app.route('/health', methods=['GET'])
def health():
    return "hello", 200

if __name__ == '__main__':
    app.run()
