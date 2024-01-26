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
4. After that, go back to the project folder and install the required dependencies, can be done by continuing the command prompt from before.
<br>>cd..
<br>>cd..
<br>>pip install -r requirements.txt

5. To setting the database, create a MySql Database named tm (you may change the setting in tm\settings.py), then run this.
<br>>py manage.py migrate

6. To run the project, simply go to the tm folder
```
|___ Trucking-Management
      |___ .git
      |___ env
      |___ tm  <--- This folder
            |___ tm
                  |___ __pycache__
                  |___ static
                  |___ __init__.py
                  |___ asgi.py
                  |___ settings.py
                  |___ urls.py
                  |___ wsgi.py
            |___ "Application folders"
            |___ db.sqlite3
            |___ manage.py
      |___ .gitignore
      |___ readme.md
      |___ requirements
```
7. open cmd, then:
<br>>py manage.py runserver

### To save the dependencies:> pip freeze > requirements.txt
