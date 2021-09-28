from flask import Flask, request, jsonify, render_template
from torch_utils import transform_image, get_prediction
from PIL import Image
import base64
import io
app = Flask(__name__)

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
def allowed_file(filename):
    # xxx.png
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict',methods=['POST'])
def predict():
    if request.method == 'POST':
        file = request.files.get('file')
        if file is None or file.filename == "":
            return jsonify({'error': 'no file'})
        if not allowed_file(file.filename):
            return jsonify({'error': 'format not supported'})

        try:
            
            #im = Image.open('six.jpg')
            
            im = Image.open('six.jpg').convert('RGB')            
            data = io.BytesIO()
            im.save(data,"JPEG")
            encoded_img_data = base64.b64encode(data.getvalue())
            
            img_bytes = file.read()            
            tensor = transform_image(img_bytes)[0]
            img = transform_image(img_bytes)[1]
                                  
            prediction = get_prediction(tensor)
            data = {'prediction': prediction.item(), 'class_name': str(prediction.item())}
            #return jsonify(data)
            #return render_template("result.html",result = data)
            return render_template("result.html",result = data,img_data=encoded_img_data.decode('utf-8'))
            #return render_template('home.html',prediction=prediction.item(),img=img)
        except:
            return jsonify({'error': 'error during prediction'})

if __name__ == '__main__':
    #host='127.0.0.1'
    app.run(debug=True)
    #app.run(debug=True,host=host)