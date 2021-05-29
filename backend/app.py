from flask import Flask, request, render_template, jsonify
from models.todos import Todo
from flask_restful import Api, Resource
from flask_cors import CORS
import datetime

import settings

app = Flask(__name__,
            static_folder='../dist/static',
            template_folder='../dist')

cors = CORS(app)


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def index(path):
    return render_template('index.html')


api = Api(app)
todo = Todo()


class TodoApp(Resource):
    def get(self):
        todos = Todo.get()
        return jsonify(todos)

    def put(self):
        req = request.json
        todo_id = req['id']
        title = req['title']
        due = datetime.datetime.strptime(req['due'], '%Y-%m-%d')
        description = req['description']
        status = req['status']
        Todo.update(
            todo_id=todo_id,
            title=title,
            due_date=due,
            description=description,
            status=status
        )
        return jsonify({'message': 'Update Succeeded'})

    def delete(self):
        todo_id = int(request.json['id'])
        Todo.delete(todo_id=todo_id)
        return jsonify({'message': 'Deleted Succeeded'})

    def post(self):
        req = request.json
        title = req['title']
        due_date = req['due']
        if not due_date:
            due_date = datetime.datetime.now().strftime('%Y-%m-%d')
        new_todo = Todo.create(
            title=title,
            due_date=datetime.datetime.strptime(due_date, '%Y-%m-%d'))
        return jsonify(new_todo)


api.add_resource(TodoApp, '/api/')

if __name__ == '__main__':
    app.run(port=settings.web_port)
