from flask import Flask, render_template, request
from pandas import read_csv
from hack.clean import cleanIt
from hack.transform import transformIt
from hack.model import predict


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('upload.html')


@app.route('/result', methods=['POST'])
def result():
    rawFile = request.files['file']
    originalDf = read_csv(rawFile)
    cleanedDf = cleanIt(originalDf)
    transformedDf = transformIt(cleanedDf)
    result = predict(transformedDf)

    return render_template(
        'result.html',
        originalDf=originalDf.shape,
        cleanedDf=cleanedDf.shape,
        transformedDf=transformedDf.shape,
        result=result
    )


if __name__ == '__main__':
   app.run(debug = True)