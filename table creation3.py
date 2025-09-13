import mysql.connector

conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Mysql@2005',
    database='lora'
)
c = conn.cursor()

c.execute('''
CREATE TABLE IF NOT EXISTS readings (
    id INT AUTO_INCREMENT PRIMARY KEY,
    node_id VARCHAR(255),
    soil_moisture DOUBLE,
    temperature DOUBLE,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
)
''')

conn.commit()
conn.close()