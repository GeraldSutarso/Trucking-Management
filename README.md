# Trucking-Management
Capstone Project
## Title
How to Install?

1. Assuming Python and pip are already installed, open the cmd of this folder
2. type "py -m venv env" to create virtual environment
3. Activate it by navigating to the >env/Scripts and opening the activate.bat, can be done by continuing the command prompt from before.
<br>>cd env/Scripts
<br>>activate.bat
4. After that, go back to the project folder and install the required dependencies, can be done by continuing the command prompt from before.
<br>>cd..
<br>>cd..
<br>>pip install -r requirements.txt

5. To setting the database, run this.
<br>>py manage.py makemigrations tm_app
<br>>py manage.py migrate tm_app

### To save the dependencies:> pip freeze > requirements.txt