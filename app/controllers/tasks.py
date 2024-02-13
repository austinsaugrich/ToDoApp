from app import app
from flask import Flask, session, render_template, request, redirect
from app.models.task import Task

Tasks = [
    {
        'id': 3423,
        'name': 'Shopping',
        'urgency': 1,
        'date': 'today'
    }
]


def pull_task_by_id(id):
    found_task = None
    for task in session['tasks']:
        if task['id'] == id:
            found_task = task
    return found_task


# new task form


@app.route('/add/task')
def add_task_form():
    # if 'tasks' not in session:
    # session['tasks'] = Tasks

    return render_template('add.html')

# requesting data from the form


@app.route('/add/task', methods=['POST'])
def add_task():
    # form = request.form
    data = {
        'name': request.form['name'],
        'urgency': request.form['urgency'],
        'date': request.form['date'],
        'users_id': session['user_id']
    }
    Task.add(data)


# used for session, switched to db

    # tasks = session['tasks']
    # tasks.append({
    # 'id': len(tasks) + 1,
    # 'name': form['name'],
    # 'urgency': form['urgency'],
    # 'date': form['date'],
    # })
    # session['tasks'] = tasks
    return redirect('/dashboard')


# update a task

@app.route('/task/edit/<int:id>')
def update_task_form(id):
    # if 'tasks' not in session:
    # session['tasks'] = Tasks

    return render_template('update.html', task=Task.get_by_id(id))


@app.route('/task/edit', methods=['POST'])
def update_task():
    # form = request.form
    Task.edit(request.form)
# no longer using session, using db
    # task_to_update = pull_task_by_id(int(form['id']))
    # updated_tasks = []
    # for task in session['tasks']:
    # if int(task['id']) == int(task_to_update['id']):
    # updated_tasks.append({
    # 'id': task['id'],
    # 'name': form['name'],
    # 'urgency': form['urgency'],
    # 'date': form['date'],
    # })
    # else:
    # updated_tasks.append(task)

    # session['tasks'] = updated_tasks
    return redirect('/dashboard')
# view indiviual task


@app.route('/task/<int:id>')
def get_task(id):
    # if 'tasks' not in session:
    # session['tasks'] = Tasks

    return render_template('view.html', task=Task.get_by_id(id))


# delete a task

@app.route('/task/delete/<int:id>')
def delete_task(id):
    # if 'tasks' not in session:
    # session['tasks'] = Tasks
    Task.delete(id)
    # list comprehension
    # session['tasks'] = [task for task in session['tasks'] if task['id'] != id]
    return redirect('/dashboard')


# shows the todo list

@app.route('/dashboard')
def dashboard():
    # if 'tasks' not in session:
    # session['tasks'] = Tasks

    return render_template('dashboard.html', tasks=Task.get_task_by_user_id(session['user_id']))
