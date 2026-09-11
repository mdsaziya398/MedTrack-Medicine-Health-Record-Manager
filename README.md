💊 MedTrack — Medicine Reminder & Health Record Manager

A Python and Streamlit-based healthcare management application for managing medicines, dosage schedules, reminders, health records, and medical appointments through a simple and user-friendly interface.

📌 Project Overview

MedTrack — Medicine Reminder & Health Record Manager is a healthcare management application developed using Python and Streamlit.

The application is designed to help users organize important healthcare information in one place. Users can manage their medicines, monitor dosage schedules, check reminders, maintain health records, and manage upcoming medical appointments.

MedTrack provides a simple interactive interface that makes it easier to maintain and access personal healthcare information.

🎯 Objectives

The main objectives of MedTrack are:

To provide a simple system for managing medicines.
To store medicine dosage and schedule information.
To help users keep track of medicine reminders.
To maintain health records in an organized format.
To manage medical appointments.
To provide medicine summaries and schedules.
To reduce the chances of forgetting scheduled medicines or appointments.
To provide a user-friendly healthcare management interface.
✨ Features
💊 1. Add Medicine

Users can add medicine information such as:

Medicine ID
Medicine name
Dosage
Frequency
Start date
End date
Medicine status
📋 2. View Medicines

Users can view all medicines stored in the system.

The medicine list provides important information such as:

Medicine name
Dosage
Frequency
Dates
Status
🔍 3. Search Medicine

Users can search for a specific medicine using its available information.

This makes it easier to find medicines when the list contains multiple records.

✏️ 4. Update Medicine

Existing medicine information can be updated whenever required.

Users can modify details such as dosage, frequency, dates, and other stored information.

🗑️ 5. Delete Medicine

Users can remove medicines that are no longer required from the system.

🔄 6. Update Medicine Status

Users can update the status of a medicine, such as:

Active
Completed
Inactive

This helps users understand which medicines are currently being used.

📊 7. Medicine Summary

The application provides a summary of medicine information to give users a quick overview of their medication records.

🕐 8. Medicine Schedule

Users can view their medicine schedules and check when medicines are supposed to be taken.

🔔 9. Current Reminders

MedTrack checks medicine schedules and displays relevant reminders to help users stay aware of their medication timings.

Note: MedTrack is a management and reminder application and does not replace professional medical advice.

🩺 10. Health Records

Users can add and maintain health-related records.

Health records can contain information such as:

Record ID
Date
Health condition
Symptoms
Notes

This provides an organized way to maintain health information.

📅 11. Appointment Management

Users can manage medical appointments, including:

Appointment ID
Doctor name
Appointment date
Appointment time
Purpose
Notes

Users can:

Add appointments
View appointments
Delete appointments
🛠️ Technologies Used
Technology	Purpose
Python	Application development and logic
Streamlit	Interactive web application interface
JSON	Data storage
Git	Version control
GitHub	Source code management and project hosting
🐍 Python Concepts Used

This project demonstrates several important Python concepts:

Variables and Data Types

Used for storing medicine, health record, and appointment information.

Conditional Statements

Used to handle different menu options and application conditions.

Loops

Used for displaying and processing multiple records.

Functions

Used to divide the application into reusable components.

Lists and Dictionaries

Used to manage structured healthcare data.

File Handling

Used to read and write JSON data files.

Exception Handling

Used to handle invalid inputs and prevent application crashes.

Date and Time Handling

Used for medicine schedules, reminders, and appointments.

CRUD Operations

The application supports:

Create — Add records
Read — View records
Update — Modify records
Delete — Remove records
📂 Project Structure
MedTrack-Medicine-Health-Record-Manager/
│
├── 📁 Data/
│   ├── appointments.json
│   ├── health_records.json
│   └── medicines.json
│
├── 📁 Screenshots/
│   
│
├── 📄 app.py
├── 📄 requirements.txt
└── 📄 README.md
Data Folder

The Data folder contains JSON files used to store application data:

appointments.json
health_records.json
medicines.json
Screenshots Folder

The Screenshots folder contains screenshots demonstrating the application's interface and features.

⚙️ Installation and Setup
1. Clone the Repository

Clone the project using Git:

git clone https://github.com/mdsaziya398/MedTrack-Medicine-Health-Record-Manager.git

Navigate to the project directory:

cd MedTrack-Medicine-Health-Record-Manager
2. Create a Virtual Environment

Create a Python virtual environment:

python -m venv .venv
Windows

Activate the environment:

.\.venv\Scripts\Activate.ps1

If PowerShell blocks activation, you can run the project using the Python executable inside .venv directly.

3. Install Dependencies

Install the required Python packages:

pip install -r requirements.txt
▶️ How to Run the Application

Run the Streamlit application using:

streamlit run app.py

If Streamlit is installed inside your virtual environment, you can use:

.\.venv\Scripts\python.exe -m streamlit run app.py

After running the command, Streamlit will provide a local URL, usually similar to:

http://localhost:8501

Open the URL in your browser to use MedTrack.

🖥️ Application Modules

The application provides the following main operations:

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
15. Exit
📸 Screenshots



🔄 Application Workflow
              ┌─────────────────────┐
              │      Start App      │
              └──────────┬──────────┘
                         │
                         ▼
              ┌─────────────────────┐
              │   Streamlit UI      │
              └──────────┬──────────┘
                         │
          ┌──────────────┼──────────────┐
          ▼              ▼              ▼
     Medicines      Health Records   Appointments
          │              │              │
          ▼              ▼              ▼
       Add/View       Add/View        Add/View
       Search         Records         Appointments
       Update                         Delete
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

MedTrack uses JSON files for storing application data.

The data is organized into:

Data/
│
├── medicines.json
├── health_records.json
└── appointments.json

JSON provides a simple and lightweight method for storing structured data without requiring a separate database server.

🔐 Data Privacy

This project is intended as an educational and portfolio project.

Do not upload real patient information, medical records, passwords, API keys, or other private information to a public GitHub repository.


🚀 Future Improvements

The project can be enhanced in the future with:

🔔 Automated notification reminders
📱 Mobile-friendly interface
👤 User authentication and login
🗄️ Database integration using SQLite or MySQL
☁️ Cloud-based data storage
📊 Advanced health analytics
📈 Health history charts
📧 Email reminders
📱 SMS notifications
🔄 Automatic backup and restore
🔒 Improved data security
🤖 AI-based medication assistance
🌟 Advantages
Simple and easy-to-use interface
Centralized healthcare information management
Easy medicine tracking
Medicine schedule monitoring
Appointment management
JSON-based lightweight storage
Built using Python
Interactive Streamlit interface
Demonstrates practical CRUD operations
Suitable for academic and portfolio use
🎓 Project Type

Academic & Portfolio Project

Domain: Healthcare / Health Management

Application Type: Web Application

Framework: Streamlit

Programming Language: Python

👩‍💻 Author

Mohammad Saziya

GitHub: mdsaziya398

📄 License

This project is developed for educational and portfolio purposes.

You may modify and extend the project for learning and development purposes.

⭐ GitHub Repository

MedTrack — Medicine Reminder & Health Record Manager

Repository:

https://github.com/mdsaziya398/MedTrack-Medicine-Health-Record-Manager

Repository:

📁 MedTrack-Medicine-Health-Record-Manager
│
├── 📁 Data
│   ├── appointments.json
│   ├── health_records.json
│   └── medicines.json
│
├── 📁 Screenshots
│   
│
├── 📄 app.py
├── 📄 requirements.txt
└── 📄 README.md
