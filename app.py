from flask import Flask, render_template
import mysql.connector

app = Flask(__name__)

# Replace these with your MySQL credentials
DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'password': 'Mysql@2005',
    'database': 'lora'
}

@app.route('/')
def dashboard():
    conn = mysql.connector.connect(**DB_CONFIG)
    c = conn.cursor(dictionary=True)
    c.execute('SELECT * FROM readings ORDER BY timestamp DESC LIMIT 10')
    data = c.fetchall()
    conn.close()
    # Renders a web page with recent sensor data
    return render_template('dashboard.html', data=data)

if __name__ == '_main_':
    app.run(debug=True)