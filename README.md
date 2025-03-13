# Voice-Based Database Management System (VBDMS)

## 📌 Project Overview

VBDMS (Voice-Based Database Management System) is an interactive system that allows users to manage a MySQL database through voice commands. The system integrates FastAPI for backend processing, MySQL for data storage, and Streamlit for a user-friendly frontend interface.

## 📂 Project Structure

```
VBDMS/
│-- Backend/
│   │-- database_updater.py      # Updates sensor values in the database
│   │-- db_helper.py             # Functions for database queries
│   │-- server.py                # FastAPI server to process voice commands
│   │-- voice_assistant.py        # Voice processing and command execution
│
│-- DataBase/
│   │-- To_create_fresh_DB.sql   # SQL script to create a fresh database
│   │-- VBDMS_demo_database.sql  # Pre-filled demo database
│
│-- Frontend/
│   │-- streamlit_app.py         # Streamlit web application for voice interaction
│
│-- requirements.txt             # List of required dependencies
│-- README.md                    # Project documentation
```

---

## ⚙️ Prerequisites

Ensure you have the following installed on your system:

- Python (>=3.8)
- MySQL Server
- MySQL Connector (`pip install mysql-connector-python`)
- Required Python packages (`requirements.txt` is provided)

---

## 🛠 Installation & Setup

### 1️⃣ Clone the Repository

```sh
git clone https://github.com/ankit85810/VBDMS.git
cd VBDMS
```

### 2️⃣ Setup MySQL Database

Start your MySQL server and execute the SQL script to create a fresh database:

```sh
mysql -u root -p < DataBase/To_create_fresh_DB.sql
```

(Use `VBDMS_demo_database.sql` if you want a pre-filled database.)

### 3️⃣ Install Dependencies

```sh
pip install -r requirements.txt
```

---

## 🚀 Running the Project

### 1️⃣ Start the Database Updater

```sh
cd Backend
python database_updater.py
```

This script updates sensor data in the database every 5 seconds.

### 2️⃣ Start the FastAPI Server

```sh
python server.py
```

The server will start at `http://localhost:8000`.

### 3️⃣ Run the Streamlit Frontend

```sh
cd ../Frontend
streamlit run streamlit_app.py
```

This will launch the web interface where you can give voice commands.

---

## 🎤 Using the System

### Available Voice Commands:

- **"Maximum value of sensor X"** → Fetch max value of sensor X
- **"Minimum value of sensor X"** → Fetch min value of sensor X
- **"Last value of sensor X"** → Get last recorded value
- **"Status of sensor X"** → Get active/inactive status

Simply click the **Record Voice Command** button in the Streamlit interface and speak your command.

---

## 🔧 Troubleshooting

- **Database connection issues?**
  - Ensure MySQL is running and credentials in `db_helper.py` match your setup.
- **Microphone not working?**
  - Check your system microphone permissions.
- **FastAPI or Streamlit not starting?**
  - Make sure all dependencies are installed properly (`pip install -r requirements.txt`).

---

## 🏆 Credits

Developed by **Ankit Vishwakarma**. 🚀

---


