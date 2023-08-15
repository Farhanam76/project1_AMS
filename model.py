from app import app, db, Books



book1 = Books(ISBN = 9781509858637, name = 'This Is Going To Hurt', author = 'Adam Kay', price = 8.99, quantity = 4  )
book2 = Books(ISBN = 9780143415862, name = 'The Kite Runner', author = 'Khaled Hosseini', price = 7.99, quantity = 2  )
book3 = Books(ISBN = 9780393356502, name = 'Astrophysics for People in a Hurry', author = 'Neil deGrasse Tyson', price = 8.99, quantity = 3  )
book4 = Books(ISBN = 9780192832634, name = 'Beyond Good and Evil: Prelude to a Philosophy of the Future', author = ' Friedrich Nietzsche', price = 9.99, quantity = 5  )
book5 = Books(ISBN = 9780743226721, name = '1776', author = 'David McCullough', price = 6.99, quantity = 2 )
book6 = Books(ISBN = 9780140569322, name = 'The Very Hungry Caterpillar', author = 'Eric Carle', price = 5.00, quantity = 7  )
book7 = Books(ISBN = 9780007548699, name = 'All the Light We Cannot See', author = 'Anthony Doerr', price = 9.99, quantity = 1  )
book8 = Books(ISBN = 9781529094961, name = 'The Murders at Fleat House', author = ' Lucinda Riley', price = 15.99, quantity = 4  )
book9 = Books(ISBN = 9781788402170, name = 'The Dark Side of the Mind', author = 'Kerry Daynes', price = 7.99, quantity = 2  )
book10 = Books(ISBN = 9780060194994, name = 'To Kill a Mockingbird', author = 'Harper Lee', price = 9.99, quantity = 8  )

with app.app_context():
    db.session.add(book1)
    db.session.add(book2)
    db.session.add(book3)
    db.session.add(book4)
    db.session.add(book5)
    db.session.add(book6)
    db.session.add(book7)
    db.session.add(book8)
    db.session.add(book9)
    db.session.add(book10)



    db.session.commit()

