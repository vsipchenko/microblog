from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import ValidationError, DataRequired, Length

from app.models import User


class EditProfileForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    about_me = TextAreaField('About me', validators=[Length(min=0, max=140)])
    submit = SubmitField('Submit')

    def __init__(self, user, *args, **kwargs):
        super(EditProfileForm, self).__init__(*args, **kwargs)
        self.user = user

    def validate_username(self, username):
        if username.data != self.user.username:
            if User.query.filter_by(username=self.username.data).first():
                raise ValidationError('Please use a different username.')


class PostForm(FlaskForm):
    post = TextAreaField('Say something', validators=[DataRequired(), Length(min=1, max=140)])
    submit = SubmitField('Submit')



