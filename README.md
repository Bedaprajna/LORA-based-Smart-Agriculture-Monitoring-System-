# LORA based Smart Agriculture Monitoring System

A web-based IoT system using LoRa wireless technology, Python, MySQL, and Flask to monitor and visualize soil and environmental data in real time for smart agriculture applications.

---

## Features

- Wireless sensor data collection using LoRa modules
- Automated storage of soil moisture and temperature data in MySQL database
- Real-time dashboard using Flask and HTML/CSS
- Data parsing, database interaction, and web display with Python scripts

---

## Technologies Used

- *LoRa* for long-range data transmission  
- *Raspberry Pi* (or similar) for data collection
- *Python 3* for backend scripts and Flask server
- *Flask* for the web application
- *MySQL* for data storage
- *HTML/CSS & JavaScript* for the dashboard UI

---

## Project Structure

- app.py - The main Flask web application
- python code for sendig sensor data1.py - Script for sending sensor data via LoRa
- receive the data4.py - Script for receiving and parsing LoRa messages
- table creation3.py - Script to create the database table in MySQL
- data store in database5.py - Script for inserting simulated data into MySQL
- templet.html - Web template for data display
- sensor_data.db - (if using SQLite in testing)

---

## Quick Start

1. *Clone the repo:*
2. *Install dependencies:*
3. *Set up the MySQL database:*  
- Create a database called lora
- Run table creation3.py to create the readings table
4. *Run the data sender and data receiver scripts* as described above
5. *Start the Flask web dashboard:*
  Open in your browser

---

## Demo


![dashboard-screenshot](<img width="1366" height="768" alt="Screenshot (31)" src="https://github.com/user-attachments/assets/3a1c5480-bb24-447f-89ff-60770fe83ff3" />
)

---

## Author

- [Bedaprajna](https://github.com/Bedaprajna)

---

## License

MIT License (optional)
