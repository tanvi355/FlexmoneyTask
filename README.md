# FlexmoneyTask

# Yoga Class Admission form

I have built a web app using the below tech stack:

- Frontend: HTML, CSS, Bootstrap (Zephyr template on Boostwatch)

- Backend: Python, Flask


The enrollment form accepts user's details viz.:

- Name

- Age

- Email

- Phone

- Batch preference

- Date of registration

and performs validation checks accordingly. This data is stored into the user table in the database. 

Next, the user is asked to make the fee payment using a simple payment form asking for details like:

- Name

- Bank Name

- Payment method (Credit/Debit card)

- Expiry date

- Card number

- CVV

Amount of Rs. 500 is already displayed and cannot be changed.

<b> Assuming none of the above payment related information is relevant to the context of this task, it is not stored in the database as of yet. </b>

The payment table stores only attributes like: 

- payment_id (primary key)

- paid_user_id

- amount (amt)

- payment_status

Upon completing the payment, an enrollment confirmation message is displayed and also a dummy schedule for the batches is presented to the user.


### The ER diagram is also added in the repository.
It consists of twp entities namely, 'User' and 'Payment' which are related by a relation named 'CompletePayment'. The `user_id` attribute of the User entity acts the primary key for the 'User' and `payment_id` attribute acts as a promary key for the 'Payment' entity.

The `paid_user_id` attribute denotes the id of the user who has completed the payment and it references the `user_id` attribute of the user, hence resulting in a foreign key relation. 

## Screenshots

![image](https://user-images.githubusercontent.com/56465105/207318410-ca272ae0-f7e5-484c-81e0-947ee9f4285f.png)


![image](https://user-images.githubusercontent.com/56465105/207318136-4b8b461c-5545-4064-ac2b-9d499f0cb771.png)


![image](https://user-images.githubusercontent.com/56465105/207318289-12459964-f943-4529-babd-aa971b7465da.png)


## To run the project on local system

1. Fork and clone this repository or download the code.

2. In your command prompt, navigate to `FlexmoneyTask`.

3. Run this app using the command `python app.py`.

4. Now, navigate to http://127.0.0.1:5000/ in your web browser to use the app.

