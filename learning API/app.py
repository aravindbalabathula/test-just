from flask import Flask, render_template, request
from model.regression_model import predict

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict_value():
    try:
        x1 = float(request.form['x1'])
        x2 = float(request.form['x2'])
        prediction = predict(x1, x2)
        return render_template('index.html', prediction=prediction)
    except Exception as e:
        return str(e)

if __name__ == '__main__':
    app.run(debug=True)
