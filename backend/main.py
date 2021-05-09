from flask import Flask, render_template, request, redirect, jsonify, url_for
import logging

from backend.models.base import Todo

app = Flask(__name__, static_folder='../dist/static', template_folder='../dist')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/doing', methods=['GET'])
def get_todo_doing():
    todos = Todo.get_todos_doing()
    return jsonify(todos)


@app.route('/done', methods=['GET'])
def get_todo_done():
    todos = Todo.get_todos_done()
    return jsonify(todos)


@app.route('/create', methods=['POST'])
def create():
    import datetime
    req = request.json
    title = req['title']
    Todo.create(title=title, due_date=datetime.datetime.now(), status=0)
    return jsonify({'status': 201})


@app.route('/delete', methods=['POST'])
def delete():
    id = int(request.json['id'])
    Todo.delete(id)
    return jsonify({'status': 201})


@app.route('/complete', methods=['POST'])
def complete():
    id = int(request.json['id'])
    Todo.complete(id)
    return jsonify({'status': 201})


@app.route('/update', methods=['POST'])
def update():
    req = request.json
    print(req)
    id = req['id']
    title = req['title']
    due = req['due']
    status = req['status']
    Todo.update(id, title, due, status)
    return jsonify({'status': 201})


if __name__ == '__main__':
    import datetime
    now = datetime.datetime(2020, 1, 2, 3, 4, 5)
    # develop
    Todo.to_all_doing()
    app.run()





