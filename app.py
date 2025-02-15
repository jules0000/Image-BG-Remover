import os
from flask import Flask, request, render_template
from werkzeug.utils import secure_filename
from PIL import Image
from rembg import remove

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'webp'}

if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/remback', methods=['POST'])
def remback():
    if 'file' not in request.files:
        return 'No file part'
    file = request.files['file']
    if file.filename == '':
        return 'No selected file'
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        input_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(input_path)

        output_filename = f"no_bg_{filename}"
        output_path = os.path.join(app.config['UPLOAD_FOLDER'], output_filename)

        input_image = Image.open(input_path)
        output_image = remove(input_image)
        output_image.save(output_path)

        return render_template('home.html', original=filename, result=output_filename)
    else:
        return 'Invalid file type'

if __name__ == '__main__':
    app.run(debug=True)
