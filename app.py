from flask import Flask, render_template
from wtforms.fields.simple import SubmitField
import christina
from wtforms import StringField
from flask_wtf import FlaskForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'christina\'s butt is the worst /s'

class SearchForm(FlaskForm):
    search_field = StringField('Enter search word:')
    submit = SubmitField("Submit!")


# Home function @ localhost:5000/home
@app.route('/home')
def home():
    return render_template("home.html")


@app.route('/search', methods=['GET','POST'])
def search():
    search_form = SearchForm()
    output = None
    first_line = None
    if search_form.validate_on_submit():
        user_search_word = search_form.search_field.data
        first_line, output = christina.find_frequency(search_word=user_search_word)
    # if output:
    #     first_line = output[0]
    #     del output[0]
    return render_template('search.html', search_form=search_form, first_line=first_line, output=output)





