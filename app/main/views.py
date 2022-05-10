from flask import render_template,redirect,url_for,abort,request
from . import main
from .forms import PitchForm,CommentForm,UpdateProfile
from flask_login import login_required,current_user
from ..models import User,Pitch,Comment,Upvote,Downvote
from .. import db,photos


# Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    pitches=Pitch.query.all()
    Elevatorpitch=Pitch.query.filter_by(category ='Elevatorpitch').all()
    Pickuplines=Pitch.query.filter_by(category ='Pickuplines').all()
    Puns=Pitch.query.filter_by(category ='Puns').all()
    title = 'MINUTE PITCH'
    # message ='welcome to minute pitches'
    return render_template('index.html',title= title,pitches=pitches,Elevatorpitch=Elevatorpitch,Pickuplines=Pickuplines,Puns=Puns)

@main.route('/user/<name>')
def profile(name):
    user = User.query.filter_by(username = name).first()
    user_id = current_user._get_current_object().id
    posts = Pitch.query.filter_by(user_id = user_id).all()
    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user,posts=posts)

@main.route('/new_pitch', methods = ['POST','GET'])
@login_required
def new_pitch():
    form = PitchForm()
    if form.validate_on_submit():
        title = form.title.data
        post = form.post.data
        category = form.category.data
        user_id= current_user._get_current_object().id
        new_pitch_object = Pitch(post=post,category=category,title=title,user_id=user_id)
        new_pitch_object.save_pitch()
        return redirect(url_for('main.index'))
        
    return render_template('pitches.html', form = form)

@main.route('/comment/<int:pitch_id>', methods = ['POST','GET'])
@login_required
def comment(pitch_id):
    form = CommentForm()
    pitch = Pitch.query.get(pitch_id)
    all_comments = Comment.query.filter_by(pitch_id = pitch_id).all()
    if form.validate_on_submit():
        comment = form.comment.data 
        pitch_id = pitch_id
        user_id = current_user._get_current_object().id
        new_comment = Comment(comment = comment,user_id = user_id,pitch_id = pitch_id)
        new_comment.save_comment()
        return redirect(url_for('.comment', pitch_id = pitch_id))
    return render_template('comment.html', form =form, pitch = pitch,all_comments=all_comments)

@main.route('/upvote/<int:id>',methods = ['POST','GET'])
@login_required
def upvote(id):
    get_pitches = Upvote.get_upvotes(id)
    valid_string = f'{current_user.id}:{id}'
    for pitch in get_pitches:
        to_str = f'{pitch}'
        print(valid_string+" "+to_str)
        if valid_string == to_str:
            return redirect(url_for('main.index',id=id))
        else:
            continue
    new_vote = Upvote(user = current_user, pitch_id=id)
    new_vote.save()
    return redirect(url_for('main.index',id=id))

@main.route('/downvote/<int:id>',methods = ['POST','GET'])
@login_required
def downvote(id):
    pitch = Downvote.get_downvotes(id)
    valid_string = f'{current_user.id}:{id}'
    for pie in pitch:
        to_str = f'{pie}'
        print(valid_string+" "+to_str)
        if valid_string == to_str:
            return redirect(url_for('main.index',id=id))
        else:
            continue
    new_downvote = Downvote(user = current_user, pitch_id=id)
    new_downvote.save()
    return redirect(url_for('main.index',id = id))

@main.route('/user/<name>/update_profile', methods = ['POST','GET'])
@login_required
def update_profile(name):
    form = UpdateProfile()
    user = User.query.filter_by(username = name).first()
    if user == None:
        abort(404)
    if form.validate_on_submit():
        user.bio = form.bio.data
        user.save_user()
        
        # db.session.add(user)
        # db.session.commit()

        return redirect(url_for('.profile',name=name))

    return render_template('profile/update.html',form =form)

@main.route('/user/<name>/update/pic',methods= ['POST'])
@login_required
def update_pic(name):
    user = User.query.filter_by(username = name).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.avatar = path
        db.session.commit()
    return redirect(url_for('main.profile',username=name))