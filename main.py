from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from store_data import DatabaseManager

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/api/temperature', methods=['GET'])
def get_temperature_data():
    # ดึงข้อมูล Temperature จาก SQLite และแปลงเป็น JSON
    db_obj = DatabaseManager()
    temperature_data = db_obj.get_temperature_data() 
    return jsonify(temperature_data)

@app.route('/api/humidity', methods=['GET'])
def get_humidity_data():
    db_obj = DatabaseManager()
    humidity_data = db_obj.get_humidity_data()  
    return jsonify(humidity_data)

if __name__ == '__main__':
    app.run(debug=True)

