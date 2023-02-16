from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


# URI for connecting MySQL = 'mysql://username:password@localhost/db_name'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost:3306/todo'

db = SQLAlchemy(app)

# Creating a database model
class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(255))
    status = db.Column(db.Boolean, default=False)


# Route for home page where all tasks are shown
@app.route("/")
def home():
    try:
        list = Todo.query.all()
        # rendering the HTML file using render_template
        return render_template("index.html", todo_list=list)
    except:
        print("Error rendering home page.")


# Route for add/create task.
@app.route("/add", methods=["POST"])
def add():
    try:
        # Getting task from index.html form tag.
        task = request.form.get("task")
        createTask = Todo(task=task, status=False)
        db.session.add(createTask)
        db.session.commit()
        # After creating the task we are again calling home page.
        return redirect(url_for("home"))
    except:
        print("Error in creating a new task")


# Route for updating a task, whether the task is done or pending.
@app.route("/update/<int:todo_id>")
def update(todo_id):
    try:
        todo = Todo.query.filter_by(id=todo_id).first()
        todo.status = not todo.status
        db.session.commit()
        return redirect(url_for("home"))
    except:
        print("Error in updating the status of task with id =", todo_id)


# Route for deleting a task.
@app.route("/delete/<int:todo_id>")
def delete(todo_id):
    try:
        todo = Todo.query.filter_by(id=todo_id).first()
        db.session.delete(todo)
        db.session.commit()
        return redirect(url_for("home"))
    except:
        print("Error in deleting a task with id =", todo_id)



if __name__ == "__main__":
    # pushing a context manually, everything that runs in the block will have access to current_app.
    with app.app_context():
        db.create_all()
        app.run(debug=True)
