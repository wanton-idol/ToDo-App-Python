# TODO APP with Flask
It's a TO-DO App developed using Python Flask and MySQL Database.

## :computer: Tech used 

1. Python Flask
2. SQLAlchemy
3. MySQL
4. Semantic UI for Styling

## Application Requirement

1. Create a directory.
```console
$ mkdir ToDo
$ cd ToDo
```
2. Clone this repository
```console
$ git clone https://github.com/wanton-idol/ToDo-App-Python.git
```
3. Create a Virtual Environment and Activate it.
```console
$ py -3 -m venv venv
$ venv\Scripts\activate
```
4. Install Flask , Flask SQLAlchemy and pymysql
```console
$ pip install Flask
$ pip install Flask-SQLAlchemy
$ pip install pymysql
```
5. Set Environment variables
```console
$ set FLASK_APP=app.py
$ set FLASK_ENV=development
```
6. Create a MySQL Database in local and provide the credentials in the 'SQLALCHEMY_DATABASE_URI' in app.py.
7. Run the ToDo App.
```console
$ flask run
```
OR
```console
$ python app.py
```
## Image
### Home
![](https://github.com/wanton-idol/ToDo-App-Python/blob/main/images/home.png)

### After Updating
![](https://github.com/wanton-idol/ToDo-App-Python/blob/main/images/update.png)

### After Deleting updated tasks
![](https://github.com/wanton-idol/ToDo-App-Python/blob/main/images/delete.png)

## Author   

#### :wave: [Nishchal Gupta](https://www.linkedin.com/in/itsnishchal/)


## License

[MIT License](LICENSE).
