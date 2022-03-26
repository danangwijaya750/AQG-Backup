from flask import Flask, redirect, url_for, request, jsonify
import os
from os.path import dirname
import sys
from src.preprocess.prepare_free_input import prepare_featured_input

app = Flask(__name__)

@app.route('/',methods=['GET'])
def index():
    return '<h1>BE OF AQG </h1>'

@app.route('/generate', methods=['POST'])
def generate():
    materials = request.form['materi']
    doGenerate(materials)

@app.route('/generator',methods=['POST'])
def doGenerate():
    materials = request.form['materi']
    print(materials)
    print("preparing feature extraction .....")
    prepare_featured_input(materials, output_file_name="free_input.txt", manual_ne_postag=False, lower=False, seed=42)
    print("prepared data")
    os.system(
        f'onmt_translate -model models/checkpoints/onmt/gru_045_step_32100.pt \
            -src free_input.txt \
            -output free_input_pred.txt -replace_unk \
            -beam_size 2 \
            -max_length 22'
    )
    with open("free_input_pred.txt", 'r') as f_in:
        predictions = f_in.readlines()
        print(predictions)
        predicteds = []
        taxs=['C1','C2']
        taxs_name=['C1-Menginggat','C2-Memahami']
        ind=0
        for val in taxs :
            questions = []
            for i in predictions :
                deleted = i.replace('\n','')
                questions.append(deleted)
            predicteds.append({'c' : val, 'name' : taxs_name[i],'q' : questions})
            i+=1
        return jsonify(predicteds)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
