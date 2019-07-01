from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, PasswordField, BooleanField
from wtforms.validators import Required, Length, Email, EqualTo

class RegistrationForm(FlaskForm):
    username = StringField('Username',validators=[Required(), Length(min=2,max=30)])
    email = StringField('Email', validators=[Required(), Email()])
    password = PasswordField('Password',validators=[Required()]) 
    confirm_password = PasswordField('Confirm Password',validators=[Required(), EqualTo('password')])
    submit = SubmitField('Sign Up') 

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[Required(), Email()])
    password = PasswordField('Password',validators=[Required()]) 
    remember = BooleanField('Remember Me')
    submit = SubmitField('Sign Up')
