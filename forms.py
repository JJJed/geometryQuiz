from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import InputRequired


class QuizForm(FlaskForm):
    name = StringField("First Name:", validators=[InputRequired()])
    asa = StringField("You can prove a triangle congruent using ASA (T/F):", validators=[InputRequired()])
    sas = StringField("You can prove a triangle congruent using SAS (T/F):", validators=[InputRequired()])
    aaa = StringField("You can prove a triangle congruent using AAA (T/F):", validators=[InputRequired()])
    sss = StringField("You can prove a triangle congruent using SSS (T/F):", validators=[InputRequired()])
    aas = StringField("You can prove a triangle congruent using AAS (T/F):", validators=[InputRequired()])
    ssa = StringField("You can prove a triangle congruent using SSA (T/F):", validators=[InputRequired()])
    submit = SubmitField("Submit!")
