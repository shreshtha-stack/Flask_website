from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField

class AddForm(FlaskForm):

    addname = StringField("Enter the name of the puppy")
    submit = SubmitField("ADD")

class DelForm(FlaskForm):

    id = IntegerField("Enter the id of a puppy to Remove:")
    submit = SubmitField("Remove")


class AddOwnerForm(FlaskForm):

    name = StringField("Enter the name of the owner: ")
    id = IntegerField("Enter the id of the Puppy")
    submit = SubmitField("Add Owner")
    