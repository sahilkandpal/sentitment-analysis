from flask import Flask,request
app = Flask(__name__)
from transformers import pipeline
sentiment_pipeline = pipeline("sentiment-analysis")

@app.route("/predict", methods=["POST", "GET"])
def result():
    output = request.get_json()

    if not "review" in output.keys():
        return {"message": "review as undefined is not allowed"}
    data =  [output["review"]]
    return sentiment_pipeline(data)

if __name__ == '__main__':
    app.run(debug=True,port=8000)