from flask_wtf import FlaskForm
from wtforms import IntegerField, PasswordField, StringField, SubmitField
from wtforms.validators import InputRequired


class ConnectionForm(FlaskForm):
    username = StringField("Username", validators=[InputRequired()])
    password = PasswordField("Password", validators=[InputRequired()])
    port = IntegerField("Port", validators=[InputRequired()])
    host = StringField("Host", validators=[InputRequired()])
    database = StringField("Database Name", validators=[InputRequired()])
    submit = SubmitField("Connect")


class DisconnectionForm(FlaskForm):
    submit = SubmitField("Disconnect")
