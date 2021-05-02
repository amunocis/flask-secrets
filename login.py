from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length


class LoginForm(FlaskForm):
    email = StringField(
        label='email',
        validators=[
            DataRequired("You have to provide an email"),
            Email(),
            Length(max=120)
        ]
    )
    password = PasswordField(
        'password',
        validators=[
            DataRequired("You have to provide a password"),
            Length(min=8, message="Password should be at least %(min)d characters long")
        ]
    )
    submit = SubmitField("Log In")
