from . import db
from datetime import datetime

class Pitch(db.Model):
    __tablename__='blog'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    pitch = db.Column(db.String(255))
    date_posted = db.Column(db.DateTime, default=datetime.utcnow)
    comments = db.relationship('Comments', backref='blog',cascade="all,delete")
    
    @classmethod
    def get_single_blog(cls, blog_id):
        blog = blog.query.filter_by(id=blog_id).first()
        return blog
    
   
class Comments(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True)
    comment = db.Column(db.String(255))
    bloh_id = db.Column(db.Integer, db.ForeignKey('blog.id'))
    date_posted = db.Column(db.DateTime, default=datetime.utcnow)

    @classmethod
    def get_comments(cls,blog_id):
        comments=Comments.query.filter_by(blog_id=blog_id)
        return comments