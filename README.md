# UMBA
### A Flask tool to show git hub users

## Getting started

This is a project on Flask over python 9. 

## Local machine
After clonning the project you need folow the next steps to run it on your local machine

- Create a virtual environment on the root of the proyect 
  - ```python3 -m virtualenv ENV_UMBA```

- Start your virtual env
  - ```source ENV_UMBA/bin/activate``` 

- Istall dependencies 
  - ```pip install -r requirements.txt ```

- Set the flask application environment value 
  - ```export FLASK-APP=main.py```

- Initialize the database content
  - ```flask db init```
  - ```flask db makemigrations```
  - ```flask db migrate```
  - ```flask-script <num_users> <since_id>```

- Run the app 
  - ```flask runserver ```

## Run it using docker 
(Require Docker and docker-compose installed)

- Run composer
  - ```docker-compose build```
  - ```docker-compose up ```

### Starting database connecting to container
- Look for the image name asigned to flask web
  - ```docker container ls```
      - example: ``` umba_web            "flask run"  ```
- Initialize the database
  - ```docker exec -it <container_id_or_name> echo flask flask-script <num_users> <since_id>```
    - example: ``` docker exec -it umba_web echo flask flask-script 150 1 ```
