from flask import Flask, redirect , render_template, url_for, request
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

@app.route('/',methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        username = request.form['name']
        newUser = User(name=username)
        try:
            db.session.add(newUser)
            db.session.commit()
            return redirect('/')
        except:
            return "There was an issue creating the user"
    else:
        allUsers = User.query.order_by('date_created').all()
        return render_template('index.html',users=allUsers)

@app.route('/delete/<int:id>')
def delete(id):
    user_to_delete = User.query.get_or_404(id)
    try:
        db.session.delete(user_to_delete)
        db.session.commit()
        return redirect('/')
    except Exception as e:
        print(e)
        return "Invalid request"


if __name__ == '__main__':
    app.run(debug=True)