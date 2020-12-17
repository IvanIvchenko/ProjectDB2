from flask_wtf import Form
from wtforms import TextField, TextAreaField, SubmitField, PasswordField, BooleanField
from wtforms.fields.html5 import EmailField
from wtforms.validators import Optional, DataRequired, Length, Email

def password_length_check(form,field):
    if len(field.data) < 6 or len(field.data)==0:
        raise ValidationError('Password should be longer than 6 characters')

def name_length_check(form,field):
    if len(field.data) < 2 or len(field.data)==0:
        raise ValidationError('Should be longer than 2 characters')

def email_length_check(form,field):
    if len(field.data) > 6 or len(field.data)==0:
        raise ValidationError('Non valid email')

class AddPostForm(Form):
    title = TextField('Title', validators=[ DataRequired()])
    description = TextAreaField('Description', validators = [DataRequired()])

class SignUpForm(Form):
    firstname= TextField('First Name', validators= [DataRequired(), Length(min=2)])
    lastname = TextField('Last Name', validators= [DataRequired()])
    username = TextField('User Name', validators= [ DataRequired(), Length(min=4)])
    password = PasswordField('Password',validators=[ DataRequired(), Length(min=6)])
    email = EmailField('Email', validators= [DataRequired(), Email()])
    submit = SubmitField('Sign Up')

class UserEditForm(Form):
    firstname= TextField('First Name', validators= [Optional(strip_whitespace=True), name_length_check])
    lastname = TextField('Last Name', validators= [Optional(strip_whitespace=True), name_length_check])
    password = TextField('Password',validators=[Optional(strip_whitespace=True), password_length_check])
    email = TextField('Email', validators= [Optional(strip_whitespace=True), Email()])
    submit = SubmitField('Commit changes')

class SignInForm(Form):
    email = EmailField('Email', validators = [DataRequired(), Email()])
    password = PasswordField('Password', validators = [DataRequired(), Length(min=6, max=30)])
    remember_me = BooleanField('Keep me logged in')
    submit = SubmitField('Sign In')

class AboutUserForm(Form):
    firstname= TextField('First Name', validators= [DataRequired(), name_length_check])
    lastname = TextField('Last Name', validators= [DataRequired()])
    password = PasswordField('Password',validators=[ DataRequired(), Length(min=6)])
    submit = SubmitField('Edit Profile')

