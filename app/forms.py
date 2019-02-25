from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import validators, ValidationError

class UploadForm(FlaskForm):
    photo = FileField('Upload Photo', validators=[FileRequired(), FileAllowed(['jpg', 'png', 'Images only!'])])

