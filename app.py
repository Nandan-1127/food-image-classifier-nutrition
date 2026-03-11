from flask import Flask, render_template, request, redirect
import os
from model_utils import get_prediction
from nutrition import nutrition_data

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads/'
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files: return redirect('/')
    file = request.files['file']
    if file.filename == '': return redirect('/')

    if file:
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(file_path)

        label, conf = get_prediction(file_path)

        # normalize label to match nutrition keys
        label_key = label.lower().replace(" ", "_").rstrip("_")
        
        data = nutrition_data.get(label_key)
        
        return render_template('result.html', 
                               label=label.replace("_", " ").title(),
                               conf=round(conf * 100, 2),
                               img=file_path,
                               data=data)

if __name__ == '__main__':
    app.run(debug=True)