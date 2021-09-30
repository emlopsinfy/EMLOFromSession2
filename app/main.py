from app.src.utils import get_encoded_img, get_image
import app.src.config as config
from flask import Flask, render_template, request, redirect, url_for,jsonify
from app.src.predict import get_prediction

app = Flask(__name__)

def allowed_file(filename):
    return (
        "." in filename
        and filename.rsplit(".", 1)[1].lower() in config.ALLOWED_EXTENSIONS
    )

@app.route('/')
def home():
    return render_template('home.html')


@app.route("/predict", methods=["GET", "POST"])
def predict():
    if request.method == 'POST':
        file = request.files.get('file')
        if file is None or file.filename == "":
            return jsonify({'error': 'no file'})
        if not allowed_file(file.filename):
            return jsonify({'error': 'format not supported'})
        
        img_byte = file.read()
        img = get_image(img_byte)
        encoded_img = get_encoded_img(img_byte)
        img_data = f"data:image/jpeg;base64,{encoded_img.decode('utf-8')}"
        pred = get_prediction(img)
        print(pred)
        data = {'prediction': pred, 'class_name': pred}
        return render_template('home.html',prediction=pred,img=img_data)
        
if __name__ == '__main__':
    #host='127.0.0.1'
    app.run(debug=True)
    #app.run(debug=True,host=host)
