from flask import Flask, request, jsonify, render_template
from Fuzzy_cepat import model_fuzzy
import os

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/soal')
def question():
    return render_template('soal.html')

@app.route('/hasil')
def result():
    return render_template('hasil.html')

@app.route('/api/data', methods=['POST'])
def receive_data():
    data = request.json

    if 'data1' in data and 'data2' in data and 'data3' in data and 'data4' in data and 'data5' in data:
        data_BPM = data['data1']
        data_SPO2 = data['data2']
        data_suhu = data['data3']
        data_Tekanan = data['data4']
        data_Konduktivitas = data['data5']
    # Lakukan sesuatu dengan data yang diterima di sini
    
    # Lakukan sesuatu dengan data yang diterima di sini
        if data['data6'] == 1:    
            # Kirim balik respons ke JavaScript
            hasil = round(model_fuzzy(float(data_suhu), int(data_Konduktivitas), int(data_BPM), int(data_Tekanan), float(data_SPO2)), 2)
            if hasil >= 50:
                hasil2 = True
            else:
                hasil2 = False 
            
            return jsonify({
                'hasil1': hasil,
                'hasil2': hasil2
            })
        else:
            # Kirim balik respons ke JavaScript
            hasil = round(model_fuzzy_akurat(float(data_suhu), int(data_Konduktivitas), int(data_BPM), int(data_Tekanan), float(data_SPO2)), 2)
            if hasil >= 50:
                hasil2 = True
            else:
                hasil2 = False 
            
            return jsonify({
                'hasil1': hasil,
                'hasil2': hasil2
            })


if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
