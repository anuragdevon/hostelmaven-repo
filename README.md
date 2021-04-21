# DBMS 2nd Session Project
## Title : Hostel Management System for IIITDM
   - Under Dr. Jagdish kakarla
   - Team 'C'  
## Demo ScreenShots
![HMS](./2021-04-22-00-54-06.png?raw=true "Hostel Management System")
# Steps to run the web-application on local machine
   - Pre-requisites:
      - Python version 3.8.5
      - Pip package Manger 20.0.2
   - Installation:
      - Create a folder where you want to save the cloned project
      - Using python virtual environment create env.(Not neccessary but recommended)
         ` python3 -m venv venv`(Name as you want)
      - Clone this project using cli
         ` git clone https://github.com/DBMS-Web/hostel-management.git `
      - Open hostel-mangement directory and install all requirements:
         ` pip3 install -r requirements.txt `
      - Run the following commands and your local development server will be hosted:
         ` python3 manage.py makemigrations `
         ` python3 manage.py migrate`
         ` python3 manage.py runserver `
      - Our authentication system is built django in-built authentication system, to create a new super User:
         ` python3 manage.py createsuperuser `
      - Once created using the credentials you can login into system as Dean/Wadon and add working staffs, students who can login with the credentials supplied to them.
