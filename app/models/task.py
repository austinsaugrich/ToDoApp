from app.config.mysqlconnection import MySQLConnection


class Task:
    def __init__(self, data):  # all data is a dic
        self.id = data['id']
        self.name = data['name']
        self.urgency = data['urgency']
        self.date = data['date']

    @classmethod
    def add(cls, data):
        query = """
        INSERT INTO tasks(name, urgency, date, users_id)
VALUES(%(name)s, %(urgency)s, %(date)s, %(users_id)s);
        """

        return MySQLConnection('tasks').query_db(query, data)

    @classmethod
    def edit(cls, data):
        query = """
        UPDATE tasks SET name = %(name)s, urgency = %(urgency)s, date = %(date)s
WHERE tasks.id = %(id)s
        """
        return MySQLConnection('tasks').query_db(query, data)

    @classmethod
    def delete(cls, id):
        query = """
        DELETE FROM tasks WHERE tasks.id = %(id)s
        """
        return MySQLConnection('tasks').query_db(query, {'id': id})

    @classmethod
    def get_all(cls):
        query = 'SELECT * FROM tasks;'

        results = MySQLConnection('tasks').query_db(query)

        all_tasks = []
        for row in results:
            all_tasks.append(Task(row))
        return all_tasks

    @classmethod
    def get_by_id(cls, id):
        query = 'SELECT * from tasks WHERE tasks.id = %(id)s;'

        results = MySQLConnection('tasks').query_db(query, {'id': id})

        return Task(results[0])

    @classmethod
    def get_task_by_user_id(cls, id):
        query = 'SELECT * FROM tasks WHERE users_id = %(id)s;'

        results = MySQLConnection('tasks').query_db(query, {'id': id})

        all_tasks = []
        for row in results:
            all_tasks.append(Task(row))
        return all_tasks
