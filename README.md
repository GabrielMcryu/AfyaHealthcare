# AFYA HEALTHCARE 
Afya healthcare is a web application that allows users to easily access the services of a doctor without going to the hospital. A user can book an appointment with any doctor available according to the region specified by the user. 
***
## TABLE OF CONTENTS
- [Technologies Used](#technologies-used)
- [Project Design Diagrams](#project-design-diagrams)
- [Features](#features)
- [Requirements](#requirements)
- [Installation Guide](#installation-guide)
***
## Technologies Used
- [Python 3.10](https://www.python.org/downloads/release/python-3108/)
- [Django 4](https://www.djangoproject.com/download/)
- [Sqlite Database](https://www.sqlite.org/index.html)
- [Html/Css](https://www.w3.org/standards/webdesign/htmlcss)
- [Jquery UI](https://releases.jquery.com/ui/)
- [Gmail](https://www.google.com/gmail/about/)
***
## Project Design Diagrams
You can view the Project Design diagrams [Here](https://www.figma.com/file/HR5dxMRhJfpxjJYJBqov5t/Project-Design-Diagrams?node-id=0%3A1&t=oBbDa8SfebmCx45N-1)
***
## Features
The web application has multiple features. It can allow a user to create an account and login to the system. A registered user can book an appointment with a doctor, where they can also update or cancel the appointment they booked. After the user books an appointment, the doctor can choose whether to approve or reject the appointment. The doctor also has the choice to update or cancel the appointment after they have approved it. The doctor has the ability to create his own schedule and it can be displayed when the appointment is being booked or updated.
\
The application has an admin panel to which the admin has the authority to perform crud operations according to the models available. A user can apply to become a doctor to which the admin can choose whether to approve or reject the application.
\ 
There is also an email sending feature to alert the user whether his appointment has been approved or rejected by the doctor, and also when the user’s doctor application has been approved or rejected by the admin.
***
## Requirements
To run this application, the user needs to have python3 installed in their system. They can download it [here](https://www.python.org/downloads/release/python-3108/).\
You will also need an email account to send emails to the users.
***
## Installation Guide
To run this application, you first need to create a directory:
```bash
mkdir 'your directory'
```
Enter your directory and create a virtual environment:
```bash
pip install virtualenv
python3.10 -m venv env
```
Activate the virtual environment:
```bash
source env/bin/activate
```
clone the repository
```bash
git clone https://github.com/GabrielMcryu/AfyaHealthcare.git
```
Install the requirements
```bash
pip install -r requirements.txt
```
Enter the directory
```bash
cd afya
```
Inside settings.py scroll down to the bottom and install the Email settings with yours.
Make migrations with this command in the terminal
```bash
python manage.py makemigrations
python manage.py migrate
```
Create a superuser running this command in the terminal
```bash
python manage.py createsuperuser
```
Run the app
```bash
python manage.py runserver
```
