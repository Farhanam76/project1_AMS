from flask import Flask, render_template, url_for, send_from_directory, redirect, request, jsonify, session
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import sessionmaker
import json
from form import Checkout, Payment

app = Flask(__name__)
# cart = []
app.config['SECRET_KEY'] ='547de724e07da73af3b7ec37cb0d0221'
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:Holiday5@localhost:3306/bookstore"

db = SQLAlchemy(app)
cart =[]
class Purchase(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'))
    book_isbn = db.Column(db.BIGINT, db.ForeignKey('books.ISBN'))
    book_name = db.Column(db.String(100))  # For display purposes
class Books(db.Model):
    ISBN = db.Column(db.BIGINT, primary_key=True, unique=True)
    name = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(30), nullable=False)
    price = db.Column(db.Float)
    quantity = db.Column(db.Integer)
# class Books(db.Model):
#     ISBN = db.Column(db.BIGINT, primary_key=True, unique=True)
#     name = db.Column(db.String(100), nullable = False, unique = True)
#     author = db.Column(db.String(30), nullable = False)
#     price = db.Column(db.Float)
#     quantity = db.Column(db.Integer)
    
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'))
    purchases = db.relationship('Purchase', backref='book')

    
class Customer(db.Model):
    id = db.Column(db.Integer, primary_key = True, autoincrement= True)
    firstname = db.Column(db.String(50), nullable = False)
    lastname = db.Column(db.String(50), nullable = False)
    email = db.Column(db.String(50))
    book = db.relationship('Books', backref='bookbr')


# class Purchase(db.Model):
#         id= db.Column(db.Integer, primary_key=True)
#         customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'))
#         book_name = db.Column(db.String(100), db.ForeignKey('books.name'))


# #class Purchase(db.Model):
#     id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     book_id = db.Column(db.BIGINT, db.ForeignKey('books.ISBN'))
#     customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'))



display = [{ 'title':' The bookish nook',
            'bio':" ' A book can make you visit the same world twice but now with a different perspective'",
            'content' : "Step into a world of literary wonders at 'The Bookish Nook.' Where every page holds a new adventure, and every corner is filled with the magic of words. Discover your next favorite story in the warmth of our cozy nook, where books come to life and readers find their sanctuary."

}]
@app.route('/add_to_cart', methods=['POST'])
def add_to_cart():
    try:
        data = request.json
        if data and 'name' in data and 'price' in data and 'quantity' in data:
            item = {
                'name': data['name'],
                'price': data['price'],
                'quantity': data['quantity']
            }
            cart.append(item)
            return jsonify({'message': 'Item added to cart successfully'})
        else:
            return jsonify({'error': 'Invalid request data'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500
@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', display=display)

@app.route("/about")
def about():
    return render_template('about.html', title = 'About')

@app.route("/contact")
def contact():
    return render_template('contact.html', title = 'Contact us')

@app.route("/products", methods= ['GET'])
def products():
    books = Books.query.all()
    return render_template('products.html', title ='Products listing', books = books) 
    # serialized_books = [{"name": book.name, "author": book.author} for book in books]
    # return serialized_books
    
@app.route("/category")
def category():
    return render_template('category.html', title= 'Category')
import json
from flask import render_template


@app.route("/show_cart")
def show_cart():
    serialized_cart = [{"name": item["name"], "quantity": item["quantity"], "price": item["price"]} for item in cart]
    session["cart_items"] = serialized_cart
    for item in serialized_cart:
        book_name = item["name"]
        purchase = Purchase(book_name=book_name)
        db.session.add(purchase)
        db.session.commit()


    cart_length = len(serialized_cart)

    return render_template('cart.html', title='Cart', cart=serialized_cart, cart_length=cart_length)


# @app.route("/show_cart")
# def show_cart():
    

#     serialized_cart = [{"name": item["name"],  "quantity": item["quantity"], "price": item["price"]} for item in cart]
#     cart_length = len(serialized_cart)
#     book_names = [item["name"] for item in serialized_cart]
#     book_names_str = ', '.join(book_names)
#     purchase = Purchase( book_name=book_names_str)
#     db.session.add(purchase)
#     db.session.commit()
    
#     cart_length = len(serialized_cart)
#     book_names = [item["name"] for item in serialized_cart]


#     return render_template('cart.html', title='Cart', cart=serialized_cart, cart_length=cart_length)




@app.route("/checkout", methods=['GET', 'POST'])
def checkout():
    form = Checkout()
    
    if form.validate_on_submit():  
        new_customer = Customer(
            firstname=form.firstname.data,
            lastname=form.lastname.data,
            email=form.email.data
        )
        
        db.session.add(new_customer)
        db.session.commit()
        customer_id = new_customer.id

        cart_items = session.get("cart_items")
        
        for item in cart_items:
            book_name = item["name"]
            purchase = Purchase(customer_id=customer_id, book_name=book_name)
            db.session.add(purchase)
            db.session.commit()
        
        return redirect(url_for('payment'))  # Redirect to a success page after checkout

    return render_template('checkout.html', title='Checking out', form=form)
    #     purchase = Purchase(customer_id=customer_id)
    #     db.session.add(purchase)
    #     db.session.commit()

        
    
    # return render_template('checkout.html', title='Checking out', form=form, )




    #     if request.method == 'POST':
    #     # Retrieve cart items from the session
    #         cart_items = session.get('cart', [])

    #     # Now you have the cart_items list which contains the items added to the cart

    #     # Process the cart items, create Purchase records, etc.
    #     # ...

    #     return redirect(url_for('payment'))  # Redirect to the payment page
    # else:
    #     form = Checkout()
    #     return render_template('checkout.html', title='Checkout', form=form)
    # #     return redirect(url_for('payment'))

    # # return render_template('checkout.html', title='Checking out', form=form)







        
        
       
       


# @app.route("/payment") 
# def payment():
#     form = Payment()
#     return render_template('payment.html', title = 'Payment method', form=form)
 



# ... (rest of the code)

# Payment Page
from flask import session

@app.route('/payment', methods=['GET', 'POST'])
def payment():
    form = Payment()

    
    return render_template('payment.html', title='Payment method', form=form)
    
    





@app.route('/images/<filename>')
def serve_image(filename):
    return send_from_directory('images', filename)

@app.route("/products/book1")
def book1():
    books = Books.query.all()
    book1 = next((book for book in books if book.name == "All the Light We Cannot See"), None)
    return render_template('book1.html', title = 'book1', book=book1)
@app.route("/products/book2")
def book2():
    
    books = Books.query.all()
    book2 = next((book for book in books if book.name == "To Kill a Mockingbird"), None)
    return render_template('book2.html', title='book2', book2=book2)

@app.route("/products/book3")
def book3():
    books = Books.query.all()
    book3 = next((book for book in books if book.name == "The Very Hungry Caterpillar"), None)
    return render_template('book3.html', title='book3', book3=book3)

@app.route("/products/book4")
def book4():
    
    books = Books.query.all()
    book4 = next((book for book in books if book.name == "The Kite Runner"), None)
    return render_template('book4.html', title='book4', book4=book4)

    


@app.route("/products/book5")
def book5():
    books = Books.query.all()
    book5 = next((book for book in books if book.name == "Beyond Good and Evil: Prelude to a Philosophy of the Future"), None)
    return render_template('book5.html', title='book5', book5=book5)
@app.route("/products/book6")
def book6():
    books = Books.query.all()
    book6 = next((book for book in books if book.name == "Astrophysics for People in a Hurry"), None)
    return render_template('book6.html', title='book6', book6=book6)
@app.route("/products/book7")
def book7():
    books = Books.query.all()
    book7 = next((book for book in books if book.name == "1776"), None)
    return render_template('book7.html', title='book7', book7=book7)
@app.route("/products/book8")
def book8():
    books = Books.query.all()
    book8 = next((book for book in books if book.name == "This Is Going To Hurt"), None)
    return render_template('book8.html', title='book8', book8=book8)
@app.route("/products/book9")
def book9():
    books = Books.query.all()
    book9 = next((book for book in books if book.name == "The Murders at Fleat House"), None)
    return render_template('book9.html', title='book9', book9=book9)
@app.route("/products/book10")
def book10():
    books = Books.query.all()
    book10 = next((book for book in books if book.name == "The Dark Side of the Mind"), None)
    return render_template('book10.html', title='book10', book10=book10)

if __name__ == '__main__':
    with app.app_context():
       
        db.create_all()
    
    
    app.run(debug=True)
