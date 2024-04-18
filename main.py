from flask import Flask, render_template, url_for
from datetime import datetime
import requests

app = Flask(__name__)

url= "https://api.npoint.io/91568c88b75c92501198"
posts = requests.get(url).json()

year = datetime.today().year

@app.route('/')
def all_posts():
    return render_template('index.html', all_posts=posts, year=year)

@app.route('/about')
def about():
    return render_template('about.html', year=year)

@app.route('/contact')
def contact():
    return render_template('contact.html', year=year)

@app.route('/post/<int:index>')
def show_post(index):
    send_post = None
    for blog_post in posts:
        if int(blog_post["id"]) == index:
            send_post = blog_post
    return render_template('post.html', post=send_post, year=year)


if __name__ == '__main__':
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(debug=True, use_reloader=True)
   