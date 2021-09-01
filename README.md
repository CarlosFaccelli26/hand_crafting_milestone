# The Art House
You can see live project on the following link [The Art Kingdom](https://carlos-the-kingdom-art.herokuapp.com/)
The Art Kingdom project consist in a website with the lots of functionality, among them are purchase items, add remove items on wihslist, see orders made by the user etc...
The main concept of the website is sell hand crafting items, most of the pictures show are made by my girlfriend wich in his spare time do some hand crafting stuffs. Rest of the images are taken from a website called [PixaBay]().
It's simple in structure but with nice contrasts of colours, wich make the website more attractive to the user when surface through the website.
# User Stories
1. As a User
  - As a user would be nice to easy navigate through the website. Each link with its define purpose.
  - As a user would be nice to easy register and log in.
  - As a user would be nice to see record of purchases that the user has made.
  - As a user would be nice to add, remove and read items on user's wishlist.
  - As a user would be nice to add a comment to a certain product.
2. As a owner
  - As a owner would be nice to have the ablility to send messages when users register to confirm their registration.
  - As a owner would be nice to have the ability to delete any post wich contains malicious content wich is not appropiate to the store.
  - As a owner would be nice to add, edit and delete products which may be out of stock or sold out.

# Design
1. Color Scheme
  - Main colours used throught the webiste are, black, white and brown, to create a catching layout
2. Typography
  - Main font used for the website is, Poppins.
3. Wireframs
  - Desktop - [View]()
  - Mobile - [View]()

# Technologies Used
- Programming Lenguages
  2. [CSS]()
  3. [JavaScript]()
  4. [Python]()
  5. [Django]()
  6. [Heroku]()
  7. [GitHub]()
  8. [Git]()
  9. [Sqlite]()
  10. [Bootstrap]()
  11. [Font Awesome]()
  12. [Amazon Web Services]()
  13. [Balsamiq]()

# Features
- User
  1. Purchase Items on Store
  2. Add and Remove Items to Wish Lists.
  3. Add Reviews to a single Product.
- Owner
  1. Add, Edit or Delete Products.
  2. Delete Reviews.
  3. Send Email when users register, and when a purchase is made.
# Testing
1. Code Validation:
  - Html:
    - Products Page ![View](/screenshots/screenshots11.png)
    - Product Detail ![View](/screenshots/screenshots12.png)
    - Bag ![View](/screenshots/screenshots13.png)
    - Wish List ![View](/screenshots/screenshots14.png)
    - Order History ![View](/screenshots/screenshots16.png)
    - Add Product ![View](/screenshots/screenshots17.png)
    - Edit Product ![View](/sreenshots/screenshots18.png)
  - CSS:
    - Base css ![View](/screenshots/screenshots19.png)
    - Checkout css ![View](/screenshots/screenshots20.png)

  - JS: [View]()
  - Python: [View]()

- Screenshots
1.
![Home Page](/screenshots/screenshots1.png)
  - As we can see when the user open the browser the first page will be the home page wich contains all products of the store. At the top the user will have the navbar to navigate through the website, wich include log in, log out, register, wishlist if the user has any. If Admin is log in will have an additional link to add a product to the store wich will be explained later on.
  Below the navbar we can see a second navbar wich include categories for the products. Is based on four main categories, each link will display a sub-menu with all categories of that specific link.
  The previous two navbar will be visible throughout all the website wich will give the user the ablity tu surface faster with no need to go back to the previous page.
  Below the two navbars will be display all products of the store, each product will display its price, name, rate if it has, image and its categories wich product belongs.
  Before all products are display we can see an input wich will give the user the ability to sort products by its name, price, category and rate. Rate is not working properly and will be something to working on in the near future.
  If the user scroll down a button will appear on the bottom right corner wich will lead the user to the top of the page. This button only will appear on the home page.
2.
![Product Detail](/screenshots/screenshots2.png)
![Product Detail Review](/screenshots/screenshots3.png)
  * First Image:
    - Product Detail will display all the information available to a specific product. For example its name, price, description, rate, category wich products belong.
    Also we can see a small input to adjust quantity of items if the user wants it. It won't go below 1 and won't go more than 99. Once product is updated price will adjust automatically.
    Below that input will have two buttons one will be to go back to the products/home page and the other one will be add to the bag if the user wanst to buy that specific product.
  * Second Image:
    - The second image show us two things: First there is a form that user can fill up the give a feedback of the product. Can describe things about the product, and provide a rate to the product, wich will have five choices: Horrible, bad, good, very good, excellent.
    Second on the left side will display all the reviews that the products has if there is any. Will display a maximum of three reviews in case that there is more reviews will paginate the reviews by 3 per page.
    Reviews will provide the following data: User that reviewd the item, date that the review was made, content and rate.
    Once the review is made django will calculate the rate and display the rate by stars on the product detail and products/home page, wich will give the user an idea on how good or bad is the product the the user is planning to buy.
    If admin is currenly log in will have the ability to delete the review if admin considere that there is any reviewd that doesn't fit to the store or if there are malicious content.
3.
![Bag Page](/screenshots/screenshots4.png)
  - Bag page will display items that are currently on the bag of the user. Will display in a simple table all information about quantity of products, name, price, image if there is any and the subtotal.
  Users can adjust quantity of items that they want to purchase if the wish to do it, the price will adjust automatically.
  Below the table we can see a few lines wich will describe subtotal, delivery cost, grand total and a warning text providing information about user if it has free delivery or it needs to add more products to theirs bag to get a free delivery on the purchase.
  Finally we can see two buttons, one will be to go back to the main page and the last one will lead the user to the secure payment.
4.
![Secure Payment](/screenshots/screenshots5.png)
![Secure Payment Second](/screenshots/screenshots6.png)
  - Secure Payment
    * First image show us the template wich will prodive the user the ability to make the purchase of the item.
    Will have a form on the left and on the right a small preview of the items that user is going to buy.
    The form will ask for information about the user such as: email, phone number, country, county, street address and postal code.
    * Second Image, show the input to put the credit card and cvc number. The only card number that is working due stripe is used on test mode is **4242 4242 4242 4242** the user can improvised on those two inputs.
    If the user is not logged in, user won't be able to save deliveries information for future purchases.
    Finally we have buttons wich one of the will lead us to bag page in wich user can adjust its bag in case that user wish to adjust the bag, otherwise user can follow to the purchase and end the purchase procedure.
5.
![Checkout](/screenshots/screenshots7.png)
  - Once the user had finally made the purchase, the store will send a message to the user with all the information relative to the purchase. As well we can see on the page all the information about the purchase such as the order number, price, delivery information and billing info.
  Finally a button to go to the new arrivals section to keep the user on the store and not leave to early before user miss anything.
6.
![Wish List Empty](/screenshots/screenshots8.png)
![Wish List](/screenshots/screenshots9.png)
  * Wish List
    - First image we can see wish list page but without any items on it. To access this page user must be authenticated otherwise won't be able to access it. Once logged in user can navigate to that page to see if user has products on user's wishlist. In this image there is no items so its empty. a text will give us the ablility to go back to the products page and add products if user wish to do it.
    Products added on the wishlist will be appear on the left side and on the right side will display a small table to few links to make things easier to the user.
    - Second image, show wish list with items. Products will provide the same information provided on products page. Users will have the ability to remove the product from the wishlist if they wish to do it.
7.
  ![Product Review](/screenshots/screenshots10.png)
    - As we can see user can post a review of the product. And will appear on the left side of the screen. In this case admin is logged in so admin will be avialable to delete the review if admin wish to do it.


# Deployment
Project was deployed on heroku and its host on github.
- First of all locate our repository wich is [The ark Kingdom](https://github.com/CarlosFaccelli26/Bread-Butter-Milestone).
- Once we find the repository, we need to create an [Heroku]() app.

# Credits

[Review Avarage](https://stackoverflow.com/questions/68255990/how-to-show-average-of-star-rating-in-django) Used to calculate avarage rating and display on templates.


Products images:
All products images  are items that were created by my girlfriend Sofia.