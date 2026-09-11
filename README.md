# 💊 MedTrack — Medicine Reminder & Health Record Manager

A Python and Streamlit-based healthcare management application designed to help users manage medicines, dosage schedules, reminders, health records, and medical appointments through a simple and interactive web interface.

---

## 📌 Project Overview

**MedTrack — Medicine Reminder & Health Record Manager** is a healthcare management application developed using **Python and Streamlit**.

The application provides a centralized platform for organizing medicine information, monitoring dosage schedules, checking reminders, maintaining health records, and managing medical appointments.

The project uses **JSON files for data storage**, making it lightweight and easy to understand for an academic and portfolio project.

---

## 🎯 Objectives

The main objectives of MedTrack are:

- To manage medicine information efficiently.
- To maintain medicine dosage and schedule details.
- To provide medicine reminders based on stored schedules.
- To maintain health records in an organized format.
- To manage medical appointments.
- To provide quick medicine summaries.
- To provide a simple and user-friendly healthcare management interface.
- To demonstrate practical Python programming and file-handling concepts.

---

# ✨ Features

## 💊 1. Add Medicine

Users can add medicine details such as:

- Medicine ID
- Medicine name
- Dosage
- Frequency
- Start date
- End date
- Status

---

## 📋 2. View Medicines

Users can view all medicines stored in the application.

The medicine information can include:

- Medicine name
- Dosage
- Frequency
- Start date
- End date
- Status

---

## 🔍 3. Search Medicine

Users can search for a specific medicine from the available medicine records.

This makes it easier to find information when multiple medicines are stored.

---

## ✏️ 4. Update Medicine

Users can update existing medicine information whenever required.

Medicine details such as dosage, frequency, dates, and status can be modified.

---

## 🗑️ 5. Delete Medicine

Users can delete medicine records that are no longer required.

---

## 🔄 6. Update Medicine Status

Users can update the current status of a medicine.

Example statuses include:

- Active
- Completed
- Inactive

---

## 📊 7. Medicine Summary

The application provides a summary of medicine information, allowing users to quickly understand their stored medication records.

---

## 🕐 8. Medicine Schedule

Users can view medicine schedules and check the expected timings for taking medicines.

---

## 🔔 9. Current Medicine Reminders

MedTrack checks the stored medicine schedule and displays relevant reminders.

This feature helps users stay aware of their medication schedule.

> **Note:** MedTrack is an educational management and reminder application. It does not provide medical diagnosis or replace professional medical advice.

---

## 🩺 10. Health Records

Users can add and view health-related records.

Health records can contain information such as:

- Record ID
- Date
- Health condition
- Symptoms
- Notes

This helps organize health information in one place.

---

## 📅 11. Appointment Management

Users can manage medical appointments.

Appointment information can include:

- Appointment ID
- Doctor name
- Appointment date
- Appointment time
- Purpose
- Notes

Users can:

- Add appointments
- View appointments
- Delete appointments

---

# 🛠️ Technologies Used

| Technology | Purpose |
|------------|---------|
| **Python** | Application development and business logic |
| **Streamlit** | Web-based interactive user interface |
| **JSON** | Data storage |
| **Git** | Version control |
| **GitHub** | Source code hosting and project management |

---

# 🐍 Python Concepts Used

This project demonstrates the practical use of several Python concepts.

### Variables and Data Types

Used to store medicine, health record, appointment, and application information.

### Conditional Statements

Used to control application behavior based on user selections and conditions.

### Loops

Used to process and display multiple records.

### Functions

Used to organize the application into reusable and manageable sections.

### Lists and Dictionaries

Used to store and process structured healthcare information.

### File Handling

Used to read and write JSON files for persistent data storage.

### Exception Handling

Used to handle invalid inputs and unexpected situations.

### Date and Time Handling

Used for medicine schedules, reminders, and appointment dates and times.

### CRUD Operations

The application implements the basic CRUD operations:

- **Create** — Add new records
- **Read** — View existing records
- **Update** — Modify records
- **Delete** — Remove records

---

# 📂 Project Structure

```text
MedTrack-Medicine-Health-Record-Manager/
│
├── 📁 Data/
│   ├── appointments.json
│   ├── health_records.json
│   └── medicines.json
│
├── 📁 Screenshots/
│
├── 📄 app.py
├── 📄 requirements.txt
└── 📄 README.md
requirements.txt

requirements.txt contains the Python packages required to run the application.

⚙️ Installation and Setup
1. Clone the Repository

Open a terminal or PowerShell and run:

git clone https://github.com/mdsaziya398/MedTrack-Medicine-Health-Record-Manager.git

Move into the project directory:

cd MedTrack-Medicine-Health-Record-Manager
2. Create a Virtual Environment

Create a Python virtual environment:

python -m venv .venv
3. Activate the Virtual Environment
Windows PowerShell
.\.venv\Scripts\Activate.ps1

If PowerShell prevents activation, you can still run the application using the Python executable inside the virtual environment.

4. Install Required Packages

Install the dependencies using:

pip install -r requirements.txt
▶️ How to Run

Start the Streamlit application using:

streamlit run app.py

Alternatively, if you are using the virtual environment directly:

.\.venv\Scripts\python.exe -m streamlit run app.py

After running the command, Streamlit will provide a local address such as:

http://localhost:8501

Open this address in your web browser to use the application.

🖥️ Application Modules

MedTrack provides the following main modules:

1. Add Medicine
2. View Medicines
3. Search Medicine
4. Update Medicine
5. Delete Medicine
6. Update Medicine Status
7. Medicine Summary
8. View Medicine Schedule
9. Check Current Reminders
10. Add/Update Health Record
11. View Health Record
12. Add Appointment
13. View Appointments
14. Delete Appointment
🔄 Application Workflow
                    ┌───────────────────┐
                    │    Start MedTrack  │
                    └─────────┬─────────┘
                              │
                              ▼
                    ┌───────────────────┐
                    │   Streamlit UI    │
                    └─────────┬─────────┘
                              │
             ┌────────────────┼────────────────┐
             │                │                │
             ▼                ▼                ▼
       ┌───────────┐   ┌──────────────┐  ┌──────────────┐
       │ Medicines │   │ Health       │  │ Appointments │
       │           │   │ Records      │  │              │
       └─────┬─────┘   └──────┬───────┘  └──────┬───────┘
             │                │                 │
             ▼                ▼                 ▼
       Add / View       Add / View        Add / View
       Search           Records           Delete
       Update
       Delete
             │
             ▼
      Medicine Schedule
             │
             ▼
         Reminders
             │
             ▼
        JSON Storage
💾 Data Storage

MedTrack uses JSON-based file storage.

The data is organized as:

Data/
│
├── medicines.json
├── health_records.json
└── appointments.json

JSON provides a simple and lightweight way to store structured data without requiring a separate database server.

🔐 Data Privacy

This project is developed for educational and portfolio purposes.

Do not upload real patient information or sensitive medical data to a public GitHub repository.

The JSON files included in this repository should contain sample or dummy data only.

🚀 Future Improvements

The following features can be added in future versions:

🔔 Automated medicine notifications
📱 Mobile-friendly interface
👤 User authentication and login
🔒 Improved data security
🗄️ SQLite or MySQL database integration
☁️ Cloud-based data storage
📊 Health analytics and statistics
📈 Health history charts
📧 Email medicine reminders
📱 SMS notifications
🔄 Automatic data backup and recovery
🤖 AI-based healthcare assistance

🌟 Advantages
Simple and user-friendly interface
Centralized medicine management
Medicine schedule tracking
Reminder management
Health record management
Appointment management
Lightweight JSON data storage
Interactive Streamlit interface
Demonstrates Python CRUD operations
Demonstrates file handling and exception handling
Suitable for academic and portfolio projects
🎓 Project Information

Project Name: MedTrack — Medicine Reminder & Health Record Manager

Domain: Healthcare / Health Management

Application Type: Web Application

Programming Language: Python

Framework: Streamlit

Data Storage: JSON

Project Type: Academic & Portfolio Project

👩‍💻 Author

Mohammad Saziya

GitHub: @mdsaziya398

📄 License

This project is developed for educational and portfolio purposes.

⭐ Repository

MedTrack — Medicine Reminder & Health Record Manager

GitHub Repository:

https://github.com/mdsaziya398/MedTrack-Medicine-Health-Record-Manager











