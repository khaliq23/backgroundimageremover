from flask import Flask, request, render_template, send_file
from rembg import remove
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/remove-bg', methods=['POST'])
def remove_bg():
    image_file = request.files['image']
    if image_file:
        input_data = image_file.read()
        output_data = remove(input_data)
        output_path = os.path.join(UPLOAD_FOLDER, 'output.png')
        with open(output_path, 'wb') as f:
            f.write(output_data)
        return send_file(output_path, mimetype='image/png')
    return 'No image uploaded', 400

if __name__ == '__main__':
    app.run(debug=True)
