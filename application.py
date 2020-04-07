from flask import Flask, request, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return '<h1>The Flask API is working!</h1>'

@app.route('/predict')
def predict():
    from sklearn.externals import joblib
    model = joblib.load('marriage_age_pred_model.ml')
    pred_age = model.predict([[int(request.args['gender']),
                            int(request.args['height']),
                            int(request.args['religion']),
                            int(request.args['caste']),
                            int(request.args['mother_tongue']),
                            int(request.args['profession']),
                            int(request.args['country'])
                            ]])
    return str(round(pred_age[0],2))


if __name__ == "__main__":
    app.run()