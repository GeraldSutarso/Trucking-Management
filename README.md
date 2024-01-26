# Trucking-Management
Capstone Project
## Title
How to Install?

1. Assuming Python and pip are already installed, open the cmd of this folder
2. type "py -m venv env" to create virtual environment
3. Activate it by navigating to the >env/Scripts and opening the activate.bat, can be done by continuing the command prompt from before.
<br>>cd env/Scripts
<br>>activate.bat

<br>You can also do this instead: .\env\Scripts\activate
5. After that, go back to the project folder and install the required dependencies, can be done by continuing the command prompt from before.
<br>>cd..
<br>>cd..
<br>>pip install -r requirements.txt

6. To setting the database, create a MySql Database named tm (you may change the setting in tm\settings.py), then run this.
<br>>py manage.py migrate

7. To run the project, simply go to the tm folder 
<br>>-Trucking-Management
<br>>--.git
<br>>--env
<br>>--tm  <--- This folder
<br>>--.gitignore
<br>>--readme.md
<br>>--requirements
8. open cmd, then:
<br>>py manage.py runserver

### To save the dependencies:> pip freeze > requirements.txt
