import random
import time
import mysql.connector
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Mysql@2005',
    database='lora'
)
c = conn.cursor()

for i in range(10):  # Simulate 10 sensor readings
    node_id = "node1"
    soil = random.uniform(300, 700)      # Soil moisture value between 300 and 700
    temp = random.uniform(20, 35)        # Temperature value between 20 and 35 °C

    # Insert simulated data into the database
    c.execute(
    "INSERT INTO readings (node_id, soil_moisture, temperature) VALUES (%s, %s, %s)",
    (node_id, soil, temp)
)
    print(f"Inserted: node_id={node_id}, soil={soil:.2f}, temp={temp:.2f}")
    time.sleep(1)  # Wait 1 second between readings

conn.commit()
conn.close()