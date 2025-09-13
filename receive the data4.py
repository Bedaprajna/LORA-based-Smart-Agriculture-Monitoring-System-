import mysql.connector

# Example incoming message (simulate receiving from sensor or sender script)
message = "node1,soil=523.2,temp=23.01"

# Parse the data
parts = message.split(',')
node_id = parts[0]
soil = float(parts[1].split('=')[1])
temp = float(parts[2].split('=')[1])

# Define the function to insert data
def insert_sensor_data(node_id, soil, temp):
    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password='Mysql@2005',
        database='lora'
    )
    c = conn.cursor()
    c.execute(
        "INSERT INTO readings (node_id, soil_moisture, temperature) VALUES (%s, %s, %s)",
        (node_id, soil, temp)
    )
    conn.commit()
    conn.close()
    print(f"Inserted: node_id={node_id}, soil={soil}, temp={temp}")

# Call the insert function with the parsed values
insert_sensor_data(node_id, soil, temp)