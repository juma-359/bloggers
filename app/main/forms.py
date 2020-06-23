from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField, SubmitField,PasswordField, ValidationError, TextAreaField
from wtforms.validators import Email, EqualTo, Required
from app.models import Pitch

class BlogForm(FlaskForm):
    title = StringField('title', validators=[Required()])
    pitch = TextAreaField('Pitch', validators=[Required()])
    submit = SubmitField('Post Pitch')

class CommentsForm(FlaskForm):
    comments = TextAreaField('Comment', validators=[Required()])
    submit = SubmitField('Post Pitch')