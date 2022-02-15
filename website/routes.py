from flask import render_template,flash,redirect,url_for,flash,redirect,request,jsonify
from flask import render_template,flash,redirect,url_for,flash,redirect,request,session
from flask import render_template,flash,redirect,url_for,flash,redirect,request,session,jsonify,request
from sqlalchemy import true
from wtforms.validators import Email
from website.models import User
from website.forms import PaymentForm, RegistrationForm, LoginForm, UpdateAccountForm, RequestResetForm, ResetPasswordForm
from website.forms import RegistrationForm, LoginForm, UpdateAccountForm , RequestResetForm, ResetForm
from website import app,db,bcrypt,stripe_keys
from flask_login import current_user, login_required, login_user, logout_user
from flask_mail import Message
#from os import 
import os
import secrets
import stripe
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
        return render_template("confirm.html") #url for name of function for redirect route
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
        return redirect(url_for('moviepage'))
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


@app.route('/moviepage')
def moviepage():
    return render_template('moviepage.html', title='Movies')



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
    secure_filename = true
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
    msg= Message('Password Reset Request',sender='kingsleylow2013@gmail.com',recipients=[user.email]) 
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
    return render_template('newpassword.html', title='Reset Password', form=form)


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


@app.route("/loginsuccess", methods=['GET', 'POST'])
def loginsuccess():
    if current_user.is_authenticated:
        return redirect(url_for('moviepage'))
    

    

@app.route('/payment')
def test0():
    return render_template('payment.html')

@app.route('/reqotp')
def test1():
    return render_template('reqotp.html')

@app.route('/otp')
def test2():
    return render_template('otp.html')

@app.route('/newpassword')
def test3():
    return render_template('newpassword.html')


@app.route("/config")
def get_publishable_key():
    stripe_config = {"publicKey": stripe_keys["publishable_key"]}
    return jsonify(stripe_config)

@app.route("/create-checkout-session")
def create_checkout_session():
    domain_url = "http://127.0.0.1:5000/"
    stripe.api_key = stripe_keys["secret_key"]

    try:
        # Create new Checkout Session for the order
        # Other optional params include:
        # [billing_address_collection] - to display billing address details on the page
        # [customer] - if you have an existing Stripe Customer ID
        # [payment_intent_data] - capture the payment later
        # [customer_email] - prefill the email input in the form
        # For full details see https://stripe.com/docs/api/checkout/sessions/create

        # ?session_id={CHECKOUT_SESSION_ID} means the redirect will have the session ID set as a query param
        checkout_session = stripe.checkout.Session.create(
            success_url=domain_url + "success?session_id={CHECKOUT_SESSION_ID}",
            cancel_url=domain_url + "cancelled",
            payment_method_types=["card"],
            mode="payment",
            line_items=[
                {
                    "name": "H-movie Premium Plan (Monthly)",
                    "quantity": 1,
                    "currency": "sgd",
                    "amount": "1000",
                }
            ]
        )
        return jsonify({"sessionId": checkout_session["id"]})
    except Exception as e:
        return jsonify(error=str(e)), 403


@app.route("/success")
def success():
    return render_template("success.html")


@app.route("/cancelled")
def cancelled():
    return render_template("cancelled.html")


@app.route("/webhook", methods=["POST"]) #prints a message everytime payment goes through successfully
def stripe_webhook():
    payload = request.get_data(as_text=True)
    sig_header = request.headers.get("Stripe-Signature")

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, stripe_keys["endpoint_secret"]
        )

    except ValueError as e:
        # Invalid payload
        return "Invalid payload", 400
    except stripe.error.SignatureVerificationError as e:
        # Invalid signature
        return "Invalid signature", 400

    # Handle the checkout.session.completed event
    if event["type"] == "checkout.session.completed":
        print("Payment was successful.")
        # TODO: run some custom code here

    return "Success", 200


