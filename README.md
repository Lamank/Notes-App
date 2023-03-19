# Notes-App
This project is a complete CRUD (Create, Read, Update, Delete) application that enables users to manage their notes efficiently. The application has been built using Python-Django Rest Framework on the backend and React on the frontend. The backend is responsible for serving RESTful APIs, while the frontend is responsible for handling the user interface. With this application, users can create, read, update, and delete their notes with ease.

## Endpoints

### Notes APIs

- ```GET /notes``` -- Returns an array of notes 
- ```POST /notes``` -- Creates new note with data sent in post request
- ```GET /notes/id``` -- Returns a single note object
- ```PUT /notes/id``` -- Updates an existing note with data sent in post request
- ```DELETE /notes/id``` -- Delete an existing note
 
## How to run
### Cloning the repository

1. Clone the repository by running the following command :
- `https://github.com/Lamank/Notes-App.git`

2. Move into the directory where the project files are located :
- `cd Notes-App`

### Create a Virtual Environment
1. Create a virtual environment :
```
# If you are on Windows
virtualenv env
# If you are on Linux or Mac
python -m venv env
```
2. Activate the virtual environment :
```
# If you are on Windows
.\env\Scripts\activate
# If you are on Linux or Mac
source env/bin/activate
```
### Install the Requirements
Install the necessary requirements by running the following command :
- `pip install -r requirements.txt`

### Set Up the Environment Variables
1. Create an environment file : 
- `mkdir .env`

2. Add the following variables to the environment file :
```
POSTGRES_USER=YOUR_USER
POSTGRES_PASSWORD=YOUR_PASSWORD
POSTGRES_DB=YOUR_DB
POSTGRES_HOST=YOUR_HOST
POSTGRES_PORT=YOUR_PORT
SECRET_KEY=YOUR_SECRET_KEY
```
### Activate Docker-Compose
Activate docker-compose by running the following command :
- `docker-compose up -d`

### Migrate the Migration
Run the migration using the following command :
- `python manage.py migrate`

### Run the Server
Start the server by running the following command:
`python manage.py runserver`

