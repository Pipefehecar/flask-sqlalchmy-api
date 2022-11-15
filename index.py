from src.app import app
from src.db import db, ma

db.init_app(app)
ma.init_app(app)

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)