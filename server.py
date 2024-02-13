from app import app
from app.controllers import tasks
from app.controllers import users

if __name__ == "__main__":
    app.run(debug=True)
