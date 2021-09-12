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
  1. [Html]()
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
    - As we can see in the attached picture, once you click on a product, all details (description, name, price, category...) will be displayed.
    Beside the image, we can see a small input to adjust quantity of items if the user decides to make a purchase. The user will be able to buy from one product to a maximum of 99 pieces. However, once the quantity of items is update, the price will adjust automatically.
    Below that input will have two different buttons. On one hand we have a button to go back to the products/home page. On the other hand we have a button to add any product to the basket once the user take the decision to make that purchase.  
  * Second Image:
    - In this case, along the image we can see two different topics to talk about. First, we can see a form to create a review. The user will be able to fill up the form to provide a feedback about the product. Along the review, the user not only will be able to describe the product,but also he will have the posibility to value the purchase with a rate. The rate will display different options: Horrible, bad, good, very good, excellent.
    To continue describing what we can see on the above image, we are able to appreciate how on the left side we find all the reviews if there are any. It will display a maximum of three reviews of the item per page. That means if that piece has more than three reviews, the user will need to go to the next page. 
    Reviews will provide the following data: User that reviewd the item, date when the item was reviewd, the opinion of the user and as we mentioned before, the rate.
    Once the review is done, Django will calculate the rate and display the result through a maximum of 5 stars. It is mandatory to say, these stars will apear beside all the products and also along the home page. The main goal of using stars instead of a number, it is to give the user an idea about the quality of the product through a visual display. 
    Last but not least, when the admin is log in, he will be able to delete any review with the finality to avoid hate or any unrespectful review. 
    
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


# Testing Users Stories

1. As a User
  - As a user It will be nice to have an easy navigation experience.  Each link with its define purpose.
    * Users will experience a nice and easy navigation due the display of both navbar wich will give a descreptive action with its respective link, making it easier for intuition for users.
  - As a user I expect the process of registration and log in simple and easy.
    * Proccess for registration and login is as simple to fill a form with basic details that users must provide, in the following screenshots will be explained in deep.
      1. ![Registration](/screenshots/screenshots21.png)
        - As we can see in the screenshot, regsitration process it will be easy for the user due simplicity and description on each field such as: username, e-mail, password. If the user fill up the fields without respecting the minimal requirements, user won't be able to register, instead will receive an error explaining what the user did wrong.
      2. ![Registration Email](/screenshots/screenshots22.png)
        - Once the user complete the proccess of registration, a message will be sent to the email provided. If project is running locally the email sent will be in the console however if the project is running in production email will be sent to the email provided by the user. This ensure that the user is real, because users needs to confirm the email sent to them, otherwise users won't be able to login.
      3. ![Login](/screenshots/screenshots23.png)
        - Similar process will be required by users to login. Users must fill up the fileds required on the page with the information previous given; in this case username and password. If user wants to save the credentials to login they can thanks to the small box below the two inputs with the label of **Remember me** wich will save the info provided by the user making it easier to users in this process.
  - As a user I would like to be able to see the record of my previous purchases.
    * Users once they made a purchase will be able to see the details of that orders, or in case that users made previous orders they will be able to see previous orders and its details.
      1. ![Previous Orders](/screenshots/screenshots24.png)
        - As we can see in the screenshot users are able to see details of the purchase such as name of the product, quantity, delivery cost if any, subtotal, total, etc...
        Tihs invoice will give the user all the details about the purchase that they just made. 
  - As a user I want to have the possibility to add, remove or read items being in my wishlist.
    * Add items to wishlist is a must have in any e-commerce, because allows the user to add items that they're insterested in, wich allows user to not be wasting time looking an item each time that users open the browser. Something to keep in mind is that only authenticated users are able to add or remove items from the wishlist
  - As a user It will be a good option to be able to add a coment below the products.
    * Process of adding a review is simple as a filling a simple form wich will take less than a minute. Though is missing some functionallity wich in the future will be improve such the ability that only authenticated usuers who made a pruchase of that specific product can post a review. At the moment any authenticated user are able to post a review, wich is not quite right, but as I wrote before this will be a feature to add in the coming future.
2. As a owner
  - As a owner It will be mandatory to be able to send messages once the user finish the registration form to confirm the procedure.
    * ![Email Registration Website](/screenshots/screenshots25.png)
      - As we can see using the project in production wich will send an email to the email provided by the user, in this case I use a temporarily email. Once a finished the process of registration that message will be received by the user. To confirm that the user registered in the website will appear a link to confirm the registration proccess. Wich will allow the user to login.
      - However if project is running locally confrimation e-mail will be sent to the console like in the following screenshots:
      - ![Email Registration Console](/screenshots/screenshots28.png)
  - As a owner I would like to have the posibility to delete any post contained of hate-speech, or inappropiate content.
    * ![Delete Post](/screenshots/screenshots26.png)
    - Owners will be able to delete post wich with their judgement considered that post are malicious or contains some sort of bad language.
    - Once owners tries to delete a post, a pop up will appear to ensure owners wants to delete that specific post and not make a mistake, in the following screenshots will be shown.
    - ![Delete Post Popup](/screenshots/screenshots27.png)
  - As a owner I need to be able to add, edit and delete products when they may be out of stock or sold out.
    * Owners will be able to add delete or edit any product that they want to. To add a product admins has to fill a form providing some specific details such as name, description, price, image if admin has one to provide. Attached will be a picture showing the form.
    ![Add Product](/screenshots/screenshots29.png)
    ![Add Product](/screenshots/screenshots30.png)


# Deployment
Project was deployed on heroku and its host on github. First of all create a repo on github wich will be our host to store our code, and heroku will store the full website, due heroku is capable of store backend code wich github does not.
- ![Create a Repo](/screenshots/screenshots31.png)
  ![Create a Repo 1](/screenshots/screenshots32.png)
- After the repo is created we head to heroku to create an app to store our project.
![Create App](/screenshots/screenshots33.png)
After app is created we choose our closest region
![Choose Region](/screenshots/screenshots34.png)
Once the app is created we add all the necessary variables wich the project will need to run.
![Setting Variables](/screenshots/screenshots38.png)
Once our closest region is selected we connect our github repo with our app on heroku.
![Connect Github](/screenshots/screenshots35.png)
![Connect Github 1](/screenshots/screenshots36.png)
![Connect Github 2](/screenshots/screenshots37.png)
A note to mention, to this project we used AWS(Amazon Web Services) wich allows to host our images and static files like our css and javascript.
Before we push our code to heroku we need to run a command on the terminal to disable collectstatic wich basically will disable all static files due Heroku does not store static files. The following command has to be run on the terminal **heroku config:set DISABLE_COLLECTSTATIC=1**.
Once AWS is set up we can collect static running the following command: **heroku config:set DEBUG_COLLECTSTATIC=1** or just removing the variable from the heroku panel on the heroku website.

**Clone Repository**
- First of all locate our repository wich is [The ark Kingdom](https://github.com/CarlosFaccelli26/Bread-Butter-Milestone).
  * ![Repo](/screenshots/screenshots31.png)
- Once we Find the repo we can copy the link and head back to our code editor
![Copy Repo](/screenshots/screenshots39.png)
Once Link is copied we head back to our code editor and open it. Once we are located on the terminal we can run a command to clone the repository to store in our own machine.
![Clone Repo](/screenshots/screenshots40.png)
![Clone Repo 1](/screenshots/screenshots41.png)

# Credits

[Review Avarage](https://stackoverflow.com/questions/68255990/how-to-show-average-of-star-rating-in-django) Used to calculate avarage rating and display on templates.


Products images:
All products images  are items that were created by my girlfriend Sofia.