from flask.ext.wtf import Form
from wtforms import TextField, TextAreaField, SubmitField


class PrereqForm(Form):
  prereq = TextField("Prerequisite")
  
  submit = SubmitField("Send")
