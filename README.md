# The Art House
You can see live project on the following link [The Art Kingdom](https://carlos-the-kingdom-art.herokuapp.com/)
The Art Kingdom project consist in a website full of functionalities, some of them are purchase items, add and remove items on wihslist, see orders which have been made by the user etc...
The prupose of the website is to collect several handmade items, all together, to sell them as home decor, diy projects or gifts. The inspiration to set up this project it comes from  my partner's hobbies. She truely believes art and handmade items are therapy to avoid the pressure and the stress is around us in the society. At the same time she gives a big value to the pieces you can make by your own. She always says they are little treasures. Because of that I strongly believe It will be a nice idea to show a bit of her art and share with the others throught this project. All the products pictures have been taken by her, however there are some pictures along the project, which being taken from a website called [PixaBay]().
As you can see all the website has a super simple structure where we play with the contrasts of neutral colours, giving the website the perfect balance and attractive appearance to catch up the attention of the user.
# User Stories
1. As a User
  - As a user It will be nice to have an easy navigation experience.  Each link with its define purpose.
  - As a user I expect the process of registration and log in simple and easy.
  - As a user I would like to be able to see the record of my previous purchases.
  - As a user I want to have the possibility to add, remove or read items being in my wishlist.
  - As a user It will be a good option to be able to add a coment below the products.
2. As a owner
  - As a owner It will be mandatory to be able to send messages once the user finish the registration form to confirm the procedure.
  - As a owner I would like to have the posibility to delete any post contained of hate-speech, or inappropiate content. 
  - As a owner I need to be able to add, edit and delete products when they may be out of stock or sold out.
  - As a owner I really want to assure the user an amazing navigate experience. 

# Design
1. Color Scheme
  - As you can see in this project I wanted to move on from the black, orange and grey. Main colours used throught the webiste are more neutrals like beige, white or brown. However you can see some black colour to create a catching layout all together. 
2. Typography
  - Main font have been used along this project is, Poppins.
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
  - As we can see, once the user open the browser the first page to pop up It will be 'home page'. This page characterize because of the background image, contains all the products of the store. If the user move to the top, he will find the navbar which allow him to navigate through the website. Meanwhile the user is surfing the website, he will be able to register, log in, log out at the same time he can add products to his  wishlist in the case he owns one. However, If we talk about the Admin; once he is log in, an additional link to add a product to the store it will appear. This procedure will be explained on detail later on. 
  Below the navbar we can see how a second navbar appears on the game. Thanks to this navbar, the user will be able to see all the categories which classify the different products available on the store. The distribution of the products, have been made in four main categories (macrame, sales, new arrivals and BUSCAR CATEGORIAS); each link will display a sub-menu with more categories inside of that specific link.
  It is mandatory to explain, the previous two navbars will be visible throughout all the website with the prupose to assure the user an easy navigation experience. The user will have the ablity tu surface faster with no need to go back to the previous page.
  Moving on from the navbars, we can see how just below these two, there is a display of all the products available on the store at that moment. Each product display the price, name and description, image of the item, the categories the product belongs and of course, the rate If that item has one.
  To make the navigation eassier, the user will be able to sort the search of the products by name, price, category and rate. However, rate is not working properl; definitly will be an improvement to work out in the near future.
  If the user scroll down, a button will appear on the right corner just in the botton of the website. This control, will lead the user back to the top of the page. This button only will appear on the home page.
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