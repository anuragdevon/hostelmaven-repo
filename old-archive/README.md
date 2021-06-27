# DBMS Second Session Project
## Title : Hostel Management System for IIITDM Kancheepuram
   - Under Dr. Jagdish kakarla
   - Team 'C' 

[![CI](https://github.com/primer/octicons/actions/workflows/ci.yml/badge.svg?branch=main&event=push)](https://github.com/DBMS-Web/hostel-management/actions/workflows/main.yml) 
[![Octicons Build](https://github.com/primer/octicons/workflows/Octicons%20Build/badge.svg)](https://github.com/DBMS-Web/hostel-management/deployments/activity_log?environment=hms-iiitdmk)

## Steps to run the web-application in local machine
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

## Demo
![HMS](./2021-04-23-00-51-21.png?raw=true "Hostel Management System")

## Tags
[![Python](https://img.shields.io/badge/-Python-black?style=flat&logo=python&link=https://github.com/Anuragkar234)](https://github.com/Anuragkar234)
[![Django](https://img.shields.io/badge/-Django-darkgreen?style=flat&logo=django&link=https://github.com/Anuragkar234)](https://github.com/Anuragkar234)
[![Bootstrap](https://img.shields.io/badge/-Bootstrap-563D7C?style=flat&logo=bootstrap&link=https://github.com/Anuragkar234)](https://github.com/Anuragkar234)
[![HTML5](https://img.shields.io/badge/-HTML5-E34F26?style=flat&logo=html5&logoColor=white&link=https://github.com/Anuragkar234)](https://github.com/Anuragkar234)
[![CSS3](https://img.shields.io/badge/-CSS3-1572B6?style=flat&logo=css3&link=https://github.com/Anuragkar234)](https://github.com/Anuragkar234)
[![JavaScript](https://img.shields.io/badge/-JavaScript-black?style=flat&logo=javascript&link=https://github.com/Anuragkar234)](https://github.com/Anuragkar234)
[![JQuery](https://img.shields.io/badge/-JQuery-blue?style=flat&logo=jquery&link=https://github.com/Anuragkar234)](https://github.com/Anuragkar234)
