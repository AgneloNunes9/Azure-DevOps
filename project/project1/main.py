from flask import Flask, request, jsonify, send_file,after_this_request
import subprocess
import numpy as np
import os

app = Flask(__name__)

# Enable CORS (Cross-Origin Resource Sharing) for all routes
@app.after_request
def add_headers(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type'
    return response

@app.route('/api/load', methods=['GET'])
def load(matrix_size=1000):
    # Generate two random matrices
    matrix_a = np.random.rand(matrix_size, matrix_size)
    matrix_b = np.random.rand(matrix_size, matrix_size)

    result_matrix = np.dot(matrix_a, matrix_b)
    
    return "<h1>Processed Matrix</h1>"

@app.route('/api/test', methods=['GET'])
def test():
    return "<h1>The API is running DEVOPS FINAL</h1>"

@app.route('/api/convert', methods=['POST'])
def convertX():
    print(request.files)
    if 'file' not in request.files:
        return jsonify({"error": "No File Provided"}), 400

    file = request.files['file']

    if file.filename == '':
        return jsonify({"error":"Empty File Name"}), 400

    word_file = file.filename.replace('/project1/','')
    file.save(word_file)
    pdf_file = file.filename.replace('.docx','.pdf').replace('/project1/','')

    subprocess.run(["libreoffice", "--headless", "--invisible", "--convert-to", "pdf", word_file,"--outdir" , "./"], bufsize=0)

    @after_this_request
    def delete_files(response):
        try:
            os.remove(word_file)
            os.remove(pdf_file)
            print(f"Deleted files: {word_file}, {pdf_file}")
        except Exception as e:
            print(f"Error deleting files: {e}")
        return response

    return send_file(pdf_file, as_attachment=True)


def send_pdf(pdf_content, filename):
    return send_file(
        pdf_content,
        as_attachment=True,
        download_name=filename,
        mimetype='application/pdf'
    )



if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')