from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class userPrompt(FlaskForm):
    definition = StringField('Definition',
                           validators=[DataRequired(), Length(min=3)])
    
    submit = SubmitField('Submit')