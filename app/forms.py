from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField, TextAreaField, SelectField, DateField, TimeField
from wtforms.validators import DataRequired, Length, Email, EqualTo, NumberRange

### Authentification ###

class RegisterForm(FlaskForm):
    username = StringField('Nom d\'utilisateur', validators=[DataRequired(), Length(min=3, max=50)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Mot de passe', validators=[DataRequired(), Length(min=6)])
    confirm_password = PasswordField('Confirmer le mot de passe', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('S\'inscrire')

class LoginForm(FlaskForm):
    username = StringField('Nom d\'utilisateur', validators=[DataRequired()])
    password = PasswordField('Mot de passe', validators=[DataRequired()])
    submit = SubmitField('Se connecter')

### Utilisateur (Admin) ###

class CreateUserForm(FlaskForm):
    username = StringField('Nom d\'utilisateur', validators=[DataRequired(), Length(min=3, max=50)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Mot de passe', validators=[DataRequired()])
    role = SelectField('Rôle', choices=[('user', 'Utilisateur'), ('driver', 'Conducteur'), ('admin', 'Administrateur')])
    submit = SubmitField('Créer utilisateur')

### Trajet ###

class CreateRideForm(FlaskForm):
    departure_city = StringField('Ville de départ', validators=[DataRequired()])
    arrival_city = StringField('Ville d\'arrivée', validators=[DataRequired()])
    date = DateField('Date', validators=[DataRequired()])
    time = TimeField('Heure', validators=[DataRequired()])
    seats_available = IntegerField('Places disponibles', validators=[DataRequired(), NumberRange(min=1)])
    price = IntegerField('Prix (€)', validators=[DataRequired(), NumberRange(min=1)])
    description = TextAreaField('Description')
    submit = SubmitField('Créer trajet')

### Réservation ###

class ReservationForm(FlaskForm):
    ride_id = IntegerField('ID du trajet', validators=[DataRequired()])
    user_id = IntegerField('ID de l\'utilisateur', validators=[DataRequired()])
    seats_reserved = IntegerField('Places réservées', validators=[DataRequired(), NumberRange(min=1)])
    submit = SubmitField('Réserver')
