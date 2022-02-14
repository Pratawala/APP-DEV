from flask import render_template,flash,redirect,url_for,flash,redirect,request
from wtforms.validators import Email
from website.models import User
from website.forms import RegistrationForm, LoginForm, UpdateAccountForm , RequestResetForm, ResetForm
from website import app,db,bcrypt
from flask_login import current_user, login_required, login_user, logout_user
from flask_mail import Message
#from os import 
import os
import secrets
from PIL import Image
 




@app.route("/")
def home():
    return render_template('home.html', title='Home')
#do  not remove this apprently it crashes the entire server when removed


@app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)
    #register.html is the file name for the register form


@app.route("/child",methods=['GET','POST'])
def register_sub(): #sub creating user
    form=RegistrationForm()  #creates a form object from Registraion form
    if form.validate_on_submit():
        hashed_password=bcrypt.generate_password_hash(form.password).decode('utf-8') #hash value will be in string instead of bytes
        user=User(username=form.username.data,email=form.email.data,password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You are now able to log in','success')
        flash(f'Account successfully created for {form.username.data}!') #flash displays a popup message
        return redirect(url_for("login"))
    return render_template("register.html",title="Register",form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', title='Login', form=form)


@app.route('/movie')
def movie():
    loginform = True



@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))



# @app.route("/account", methods=['GET','POST'])
# @login_required
# def update():
#     form =UpdateAccountForm()  #create a form variable from form class imported 
#     if form.validate_on_submit():
#         current_user.username=form.username.data #what user will enter into the usernmame field
#         current_user.email=form.email.data #change the current data to what is inputted
#         db.session.commit()
#         flash("Information successfully updated!","success")
#         return redirect(url_for("account"))
#     elif request.method == 'GET':
#         form.username.data
#     image_file=url_for('templates',filename='pictures/'+current_user.image_file)
#     return render_template('accountpage.html',title="Account",
#      image_file=image_file,form=form)

def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(app.root_path, 'static/profile_pics', picture_fn)

    output_size = (125, 125)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)

    return picture_fn


@app.route("/account", methods=['GET', 'POST'])
@login_required
def account():
    form = UpdateAccountForm()
    if form.validate_on_submit():
        if form.picture.data:
            picture_file = save_picture(form.picture.data)
            current_user.image_file = picture_file
        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash('Your account has been updated!', 'success')
        return redirect(url_for('account'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
    image_file = url_for('static', filename='profile_pics/' + current_user.image_file)
    return render_template('account.html', title='Account',
                           image_file=image_file, form=form)

@app.route("/upload")
def upload_file():
    return render_template('upload.html')


@app.route("/uploaded", methods = ['GET','POST'])
def uploaded_file():#upload_file():
    if request.method == 'POST':
        f = request.files['file']
        f.save(secure_filename(f.filename))
        return 'file uploaded successfully'
    
    if __name__ == '__main__':
        app.run(debug = True)
    
    
    # @app.route("/delete")

@app.route("/retrieve")
def send_reset_email(user):
    token= user.get_reset_token()
    msg= Message('Password Reset Request',sender='210511G@mymail.nyp.edu.sg',recipients=[user.email]) 
    msg.body=f'''To reset your password,visit the following link:'
{url_for('reset_token',token=token,_external=True) } 

If you did not make this request, simply ignore this email and no changes will be made'''


@app.route("/reset_password", methods=['GET', 'POST'])
def reset_request():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RequestResetForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        send_reset_email(user)
        flash('An email has been sent with instructions to reset your password.', 'info')#bootstrap alert button
        return redirect(url_for('login'))
    return render_template('reset_request.html', title='Reset Password', form=form)


@app.route("/reset_password/<token>", methods=['GET', 'POST'])
def reset_token(token):
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    user = User.verify_reset_token(token)
    if user is None:
        flash('That is an invalid or expired token', 'warning') #bootstrap warning class
        return redirect(url_for('reset_request'))
    form = RequestResetForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user.password = hashed_password
        db.session.commit()
        flash('Your password has been updated! You are now able to log in', 'success')
        return redirect(url_for('login'))
    form = ResetForm()
    if form.validate_on_submit(): 
            hashed_password=bcrypt.generate_password_hash(form.password).decode('utf-8') #hash value will be in string instead of bytes
            user.password=hashed_password #hashing the new user password
            db.session.commit()#adding the new password to database
            flash('Password Successfully changed','success')
            flash(f'Account successfully created for {form.username.data}!') #flash displays a popup message
            return redirect(url_for("login"))
    return render_template('reset_token.html', title='Reset Password', form=form)


@app.route('/database', methods=['GET', 'POST'])
def database():
    query = []
    for i in session.query(website.models):
        query.append((i.title, i.post, i.date))
    return render_template('database.html', query = query)


@app.route("/forgot_password/", methods=['GET', 'POST'])
def forgotpw():
    return render_template('forgotpw.html',)

@app.route('/payment')
def test():
    return render_template('payment.html')