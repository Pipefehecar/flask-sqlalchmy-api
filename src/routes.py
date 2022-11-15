from flask import Blueprint, request
from src.db import Task, tasks_schema, task_schema
from src.db import db

tasks = Blueprint('tasks', __name__)

@tasks.route('/')
def index():
    return '<h1>Task Api</h1>'

@tasks.route('/tasks', methods=['POST'])
def create_task():
    """Create a new task"""
    title = request.json['title']
    desc = request.json['desc']
    new_task = Task(title, desc)
    db.session.add(new_task)
    db.session.commit()
    return task_schema.jsonify(new_task)

@tasks.route('/tasks', methods=['GET'])
def list_tasks():
    """List all tasks"""
    tasks = Task.query.all()
    result = tasks_schema.dump(tasks)
    return tasks_schema.jsonify(result)

@tasks.route('/tasks/<int:id>', methods=['GET'])
def retrive_task(id):
    """Retrieve a task"""
    task = Task.query.get(id)
    if task is None:
        return 'Task not found'
    return task_schema.jsonify(task)

@tasks.route('/tasks/<int:id>', methods=['PUT'])
def update_task(id):
    """Update a task"""
    task = Task.query.get(id)
    if task:
        title = request.json['title']
        desc = request.json['desc']
        task.title = title
        task.description = desc
        db.session.commit()
        return task_schema.jsonify(task)
    return 'Task not found'

@tasks.route('/tasks/<int:id>', methods=['DELETE'])
def delete_task(id):
    """Deletes a task"""
    task = Task.query.get(id)
    if task:
        db.session.delete(task)
        db.session.commit()
        return task_schema.jsonify(task)
    return 'Task not found'