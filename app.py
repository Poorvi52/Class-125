import json
from flask import Flask, jsonify, request
from clf import get_prediction

app= Flask(__name__)

@app.route("/pred-digit", methods=["POST"])
def pred_data():
    image=request.files.get("digit")
    prediction=get_prediction(image)
    return jsonify ({
        "prediction":prediction
    }),200
    
if __name__=="__main__":
    
    app.run(debug=True)    
          




















