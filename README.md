# 
# project1_AMS/ONS
## Author - Farhana Motlib

 ## Objective
 * To create a simple online storefront, fully conforming to a provided client specification. This will involve the use of supporting tools, methodologies and technologies that encapsulate all modules covered during training.
This project has the following requirements:


## Jira board
I initially began this project by outlining my plans for an online store specializing in books. To effectively monitor my project's development, I established a Kanban board. Within this board, I created a backlog column containing user stories of the customer and the owner outlining their preferences and desires for the website's functionality.


## ERD/EER
I started by creating a basic entity relationship diagram to outline the expected connections between different entities. I expected that I would only need two tables where in the stored details of the customer, I expected information of customer book purchases as well through the db relationship. This is what it initially looked like:
![Screenshot (118)](https://github.com/Farhanam76/project1_AMS/assets/138291154/c572001e-cf5c-4860-a1d7-d2d804eed9ce)

As my project advanced, I came to understand that the initial approach was quite complex and wouldn't have been effective for storing customer information alongside the corresponding book IDs they bought. To address this, I introduced a third table named "Purchase," which includes the customer ID and the book ISBN. This new table establishes a relationship between the book and customer tables. Ultimately, the outcome shifted from associating customer IDs with book ISBNs to associating customer IDs with book names.
This is the final look:
![Screenshot (122)](https://github.com/Farhanam76/project1_AMS/assets/138291154/ed19e40c-bafc-494d-a38f-36ef51236532)

## Checkout/Payment page  
I first started making the app routes for the checkout and payment page, importing the necessary modules from Flask. In a separate file, I created a Flask form for both the Payment and the checkout page which includes validators to ensure the data entered by the user meet certain requirements. I then used html to display the form fields on the webpage:
![Screenshot (126)](https://github.com/Farhanam76/project1_AMS/assets/138291154/5baf9ecc-67fd-42fe-92eb-0fc20b6a66d8)
![Screenshot (127)](https://github.com/Farhanam76/project1_AMS/assets/138291154/041ae938-f0d7-42be-a576-7e5e630f3cff)
in the checkout page I ensured to do a form validate which means when the person submit, thier details will be in stored into the customer table. 
## Create SQL Database
using importation from SQALCHEMY , sqlalchemy.orm in flask , it has allowed me to create the database table of Books customer and Purchases Table. I have used app configuration to connect to my local mysql. I then in a separate file have input the database for the tale books and db session and commit.

## Product page 
Once the database for the books has been created, I retrieved the data of the available books into my product page and in the html I have used a loop it iterates the book list and displays in my product.

## cart page 
 In the cart new list called serialized_cart by iterating through each item in the cart. It creates a dictionary for each item containing its name, quantity, and price.

## home page
On my home page I added a nav bar which allows 


