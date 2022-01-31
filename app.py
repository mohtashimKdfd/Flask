from flask import Flask , render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///test.db'

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200),nullable=False) #We want the name to be not blank
    date_created = db.Column(db.DateTime, default=datetime.utcnow)


    def __repr__(self) -> str:
        return '<User %r>' % self.name

@app.route('/')
def index():
    # return 'Hello World'
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)