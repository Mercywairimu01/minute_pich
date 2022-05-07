from flask import render_template
from app import app
from app.forms import LoginUserForm,RegisterUserForm

app.config['SECRET_KEY'] = '12345678'
pitches1 = [
    {'author':'Mercy',
     'title':'blog 1',
     'content':'jfsdfnfjFKW', 
     'date':'2022'
     },
    {
        'author':'Mercy wvdvdvfd',
        'title':'blog 2',
        'content':'jfsdfnfjFKW',
        'date':'2021'
    }
]

# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    title = 'MINUTE PITCH'
    message ='welcome to minute pitches'
    return render_template('index.html',message =message,title= title,pitches1 =pitches1)
@app.route('/login')
def login():
	login_form = LoginUserForm()
	return render_template('login.html', login_form = login_form)

@app.route('/registration')
def registration():
    registration_form = RegisterUserForm()
    return render_template('reg.html', registration_form = registration_form)
    
    