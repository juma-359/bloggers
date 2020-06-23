from . import main
from flask import render_template, request, redirect, url_for
from ..models import Pitch, Comments
from .forms import PitchForm, CommentsForm
from .. import db
import requests

@main.route('/')
def index():

    blogs = Blog.query.all()

    title = 'Blog'
    url = 'http://quotes.stormconsultancy.co.uk/random.json'
    r = requests.get(url).json()
    print(r)
    data = {
        'author': r['author'],
        'quote': r['quote']
    }
    return render_template('index.html', title=title, data=data, pitches=pitches)

@main.route('/create_pitch', methods=['GET', 'POST'])
def blog():
    form = blogForm()
    if form.is_submitted():
        title = form.title.data
        pitch = form.pitch.data

        pitch = Pitch(title = title, pitch=pitch)

        db.session.add(blog)
        db.session.commit()

        return redirect(url_for('main.index'))
    
    title = 'New blog'
    return render_template('blog.html', title=title, form=form)

@main.route('/blog/<int:blog_id>', methods=['GET', 'POST'])
def single_blog(blog_id):
    blog = Blog.get_single_blog(blog_id)
    comments=Comments.query.all()
    print(comments)
    form = CommentsForm()
    if form.is_submitted():
        comment = form.comments.data
        blog_id =blog_id
        save_comment = Comments(comment=comment, blog_id = blog_id)
        db.session.add(save_comment)
        db.session.commit()
        return redirect(url_for('main.single_blog',blog_id=blog_id))
    
    title = 'single_blog'
    return render_template('single_blog.html', blog=blog, title=title, comments = comments, form = form)

@main.route('/update_blog/<int:blog_id>', methods=['GET', 'POST'])
def update_blog(blog_id):
   blog = Blog.get_single_blog(blog_id)
    if request.method == 'POST':
        blog.title = request.form['title']
        blog.blog = request.form['blog']
        db.session.commit()
        return redirect(url_for('main.index'))
    else:
        title = 'update'
        return render_template('update_blog.html', title=title, blog=blog)

@main.route('/delete/<int:blog_id>', methods=['GET', 'POST'])
def delete(blog_id):
    blog = Blog.get_single_blog(blog_id)
    db.session.delete(blog)
    db.session.commit()
    return redirect(url_for('main.index'))