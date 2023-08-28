import os
from flask import Flask, request, jsonify

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
  return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET'])
def index():
  return jsonify({"message": "Hello World!"})

@app.route('/upload', methods=['POST'])
def upload_file():

  file = request.files['file']

  if file and allowed_file(file.filename):
      filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
      file.save(filepath)
      return jsonify({"message": "File uploaded successfully"}), 200

  return jsonify({"error": "File type not allowed"}), 400

if __name__ == '__main__':
    app.run(debug=True)
