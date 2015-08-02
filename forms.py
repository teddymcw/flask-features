from flask_wtf import Form
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired

class PlayerSignUpForm(Form):
    name = StringField('name', validators=[DataRequired()])
    age = IntegerField('age', validators=[DataRequired()])
    chips = IntegerField('chips', validators=[DataRequired()])
    
