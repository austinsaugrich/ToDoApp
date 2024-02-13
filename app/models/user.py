from app.config.mysqlconnection import MySQLConnection


class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.email = data['email']
        self.password = data['password']

    @classmethod
    def add(cls, data):
        query = """
        INSERT INTO users(first_name, email, password)
VALUES(%(first_name)s, %(email)s, %(password)s);
        """

        return MySQLConnection('tasks').query_db(query, data)

    @classmethod
    def edit(cls, data):
        query = """
        UPDATE users SET first_name = %(first_name)s, email = %(email)s, password = %(password)s
WHERE users.id = %(id)s
        """
        return MySQLConnection('tasks').query_db(query, data)

    @classmethod
    def delete(cls, id):
        query = """
        DELETE FROM users WHERE users.id = %(id)s
        """
        return MySQLConnection('tasks').query_db(query, {'id': id})

    @classmethod
    def get_all(cls):
        query = 'SELECT * FROM users;'

        results = MySQLConnection('tasks').query_db(query)

        all_users = []
        for row in results:
            all_users.append(User(row))
        return all_users

    @classmethod
    def get_by_id(cls, id):
        query = 'SELECT * from users WHERE users.id = %(id)s;'

        results = MySQLConnection('tasks').query_db(query, {'id': id})

        return User(results[0])

    @classmethod
    def get_by_email(cls, data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        result = MySQLConnection("tasks").query_db(query, data)
        # Didn't find a matching user
        if len(result) < 1:
            return False
        return cls(result[0])
