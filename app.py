# importing all the required libraries and methods
from flask import Flask, render_template, request, redirect, url_for 
from flask_sqlalchemy import SQLAlchemy

# initializing the Flask App
app = Flask(__name__)
# configuring the database named 'db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# creating the user class
class user(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(200))
    name = db.Column(db.String(200))
    age = db.Column(db.Integer)
    phone = db.Column(db.Integer)
    batch = db.Column(db.Integer)
    enrollment_date = db.Column(db.Date)

# creating the payment class
class payment(db.Model):
    payment_id = db.Column(db.Integer, primary_key=True)
    paid_user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))
    amt = db.Column(db.Integer)
    payment_status = db.Column(db.Boolean)


'''
Routes for all the operations
'''

# initial page - enrollment form
@app.route('/')
def form():
    # get the details filled by the user from the enrollment form
    name = request.form.get('user_name')
    email = request.form.get('email_id')
    age = request.form.get('user_age')
    phone = request.form.get('phone')
    batch = request.form.get('batch')
    date = request.form.get('enrollment_date')
    # add the new user's details in the database
    new_user = user(email=email, name=name, age=age, phone=phone,
     batch=batch, enrollment_date=date)
    db.session.add(new_user)
    db.session.commit()

    return render_template('enrollment_form.html')


# payment form page
@app.route('/payment', methods=['GET', 'POST'])
def make_payment():
    # get the details filled by the user in the payment form
    paid_user_id = request.form.get('user_id')
    amt = request.form.get('fee')
    # add the details as a new entry in the database
    new_payment = payment(paid_user_id=paid_user_id, amt=amt, payment_status=True)
    db.session.add(new_payment)
    db.session.commit()

    return render_template('payment.html')


# payment confirmation page
@app.route('/payment_done', methods=['GET', 'POST'])
def complete_payment():
    return render_template('confirmation.html')


# for back to home (enrollment form) button
@app.route('/home')
def back_to_home():
    return redirect(url_for('form'))


if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)