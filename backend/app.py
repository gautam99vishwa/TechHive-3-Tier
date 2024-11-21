from flask import Flask, request, jsonify
from flask_cors import CORS
import mysql.connector

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Connect to the database
db_config = {
    'host': 'db',
    'user': 'root',
    'password': 'rootpassword',
    'database': 'mydb'
}

@app.route('/add', methods=['POST'])
def add_user():
    data = request.json
    name = data.get('name')

    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (name) VALUES (%s)", (name,))
        conn.commit()
        cursor.close()
        conn.close()
        return jsonify({"message": f"User '{name}' added successfully!"}), 201
    except Exception as e:
        return jsonify({"message": "Error connecting to the database", "error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

