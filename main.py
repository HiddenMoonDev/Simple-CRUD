from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Post(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  text = db.Column(db.String(100), nullable=False)


@app.route('/', methods=['GET', 'POST'])
def home():
  if request.method == 'POST':
    text_form = request.form['text_form']
    new_post = Post(text=text_form)
    db.session.add(new_post)
    db.session.commit()
    return redirect(url_for('home'))

  posts = Post.query.all()
  return render_template('home.html', posts=posts)


@app.route("/delete/<int:id>")
def delete(id):
  post = Post.query.get_or_404(id)
  db.session.delete(post)
  db.session.commit()
  return redirect(url_for('home'))


@app.route("/update/<int:id>", methods=['GET', 'POST'])
def update(id):
  post = Post.query.get_or_404(id)
  if request.method == 'POST':
    post.text = request.form['updated_text']
    db.session.commit()
    return redirect(url_for('home'))
  
  return render_template('update.html', post=post)


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=81, debug=True)
