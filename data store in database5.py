import mysql.connector

def insert_sensor_data(node_id, soil, temp):
    conn = mysql.connector.connect(
        host='localhost',
        user='root',           # <-- your username
        password='Mysql@2005',   # <-- your password
        database='lora'
    )
    c = conn.cursor()
    c.execute(
        "INSERT INTO readings (node_id, soil_moisture, temperature) VALUES (%s, %s, %s)",
        (node_id, soil, temp)
    )
    conn.commit()
    conn.close()

# Simulate receiving a sensor data string
message = "node1,soil=523.2,temp=23.01"
parts = message.split(',')
node_id = parts[0]
soil = float(parts[1].split('=')[1])
temp = float(parts[2].split('=')[1])

# Insert into database
insert_sensor_data(node_id, soil, temp)
print("Data inserted successfully!")
