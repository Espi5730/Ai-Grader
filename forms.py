from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, HiddenField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class userPrompt(FlaskForm):
    word = HiddenField('Word')

    definition = StringField('Definition',
                           validators=[DataRequired(), Length(min=3)])
    
    submit = SubmitField('Submit')

    def getDefintion(self):
        return self.definition.data
