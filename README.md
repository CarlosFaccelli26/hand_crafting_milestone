# The Art House
You can see live project on the following link [The Art Kingdom](https://carlos-the-kingdom-art.herokuapp.com/)
The Art Kingdom project consist in a website full of functionalities, some of them are purchase items, add and remove items on wihslist, see orders which have been made by the user etc...
The prupose of the website is to collect several handmade items, all together, to sell them as home decor, diy projects or gifts. The inspiration to set up this project it comes from  my partner's hobbies. She truely believes art and handmade items are therapy to avoid the pressure and the stress is around us in the society. At the same time she gives a big value to the pieces you can make by your own. She always says they are little treasures. Because of that I strongly believe It will be a nice idea to show a bit of her art and share with the others throught this project. All the products pictures have been taken by her, however there are some pictures along the project, which being taken from a website called [PixaBay]().
As you can see all the website has a super simple structure where we play with the contrasts of neutral colours, giving the website the perfect balance and attractive appearance to catch up the attention of the user.
# User Stories
1. As a User
  - As a user It will be nice to have an easy navigation experience.
  - As a user I expect the process of registration and log in simple and easy.
  - As a user I would like to be able to see the record of my previous purchases.
  - As a user I want to have the possibility to add, remove or read items being in my wish list.
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
  - Wishlist Desktop - ![View](/screenshots/wishlist-desktop.png)
  - Order History Desktop - ![View](/screenshots/order-history-desktop.png)
  - Products Detail Desktop - ![View](/screenshots/products-detail-desktop.png)
  - Bag Desktop - ![View](/screenshots/bag-desktop.png)
  - Checkout Desktop - ![View](/screenshots/checkout-desktop.png)
  - Products Desktop - ![View](/screenshots/products-desktop.png)
  - Profile Desktop - ![View](/screenshots/profile-desktop.png)
  - Secure Checkout Mobile - ![View](/screenshots/secure-checkout.png)
  - Wishlist Mobile - ![View](/screenshots/wishlist.png)
  - Products Mobile - ![View](/screenshots/products.png)
  - Products Detail Mobile - ![View](/screenshots/products-detail.png)
  - Checkout success Mobile - ![View](/screenshots/checkout-success.png)
  - Bag Mobile - ![View](/screenshots/bag.png)

# Technologies Used
- Programming Lenguages and Frameworks
  1. [Html](https://en.wikipedia.org/wiki/HTML)
  2. [CSS](https://en.wikipedia.org/wiki/CSS)
  3. [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
  4. [Python](https://en.wikipedia.org/wiki/Python_(programming_language))
  5. [Django](https://www.djangoproject.com/)
  6. [Heroku](https://id.heroku.com/login)
  7. [GitHub](https://github.com/)
  8. [Git](https://git-scm.com/)
  9. [Sqlite](https://en.wikipedia.org/wiki/SQLite)
  10. [Bootstrap](https://en.wikipedia.org/wiki/Bootstrap_(front-end_framework))
  11. [Font Awesome](https://fontawesome.com/)
  12. [Amazon Web Services](https://aws.amazon.com/)
  13. [Balsamiq](https://balsamiq.com/)
  14. [Django Countries](https://pypi.org/project/django-countries/)
  15. [AWS](https://aws.amazon.com/)

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
    - Edit Product ![View](/screenshots/screenshots18.png)
  - CSS:
    - Base css ![View](/screenshots/screenshots19.png)
    - Checkout css ![View](/screenshots/screenshots20.png)

  - JS: 
    - ![Add Product](/screenshots/screenshots42.png)
    - ![Products](/screenshots/screenshots43.png)
    - ![Bag](/screenshots/screenshots44.png)
    - ![Country Field](/screenshots/screenshots45.png)
    - ![Stripe](/screenshots/screenshots46.png)

  - Python:
    - ![Checkout](/screenshots/screenshots47.png)
    - ![Profile](/screenshots/screenshots48.png)
    - ![Products](/screenshots/screenshots49.png)
    - ![Bag Context](/screenshots/screenshots50.png)
    - ![Webhook Handler](/screenshots/screenshots51.png)
    - ![Webhook](/screenshots/screenshots52.png)
    - ![Bag](/screenshots/screenshots53.png)

- Screenshots
1.
![Home Page](/screenshots/screenshots1.png)
  - As we can see, once the user open the browser the first page to pop up It will be 'home page'. This page characterize because of the background image, contains all the products of the store. If the user move to the top, he will find the navbar which allow him to navigate through the website. Meanwhile the user is surfing the website, he will be able to register, log in, log out at the same time he can add products to his  wish list in the case he owns one. However, If we talk about the Admin; once he is log in, an additional link to add a product to the store it will appear. This procedure will be explained on detail later on. 
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
  - Bag page, as we can see in the picture, will display all the items that the user move into his purchase basket. All the details and information about the purchase have been collected in a simple table Where we can see quantity of products, name of the items, price of each piece, image if there is any and of course the subtotal of the purchase. 
 As we mentioned before, If the users change the amount of items they are buying, the final price will adjust automatically. 
 However,just below the table we can see a few lines with the detailed description of the subtotal, delivery cost, grand total and a warning text to provide some information to the user; for example: the user is suitable to get free delivery, or the user will be able to avoid delivery feed if he add more products to his basket. 
  As in the previous pages, at the end of the page we will find two buttons, one to go back to the main page; meanwhile the other one will lead the user to a secure payment procedure. 
4.
![Secure Payment](/screenshots/screenshots5.png)
![Secure Payment Second](/screenshots/screenshots6.png)
  - Secure Payment
    Along this first image, we can see the template the user will need to follow if he wants to confirm and complete the purchase.
   Not only we have a form on the left, but also we can find a small preview of the items being purchased on the right. 
    The form will be asking for user's contact details as email adress, phone number, country, and of course name of the road, county and the postal code. 
    * Last but not least, in the second image, we can see the input showed to the user, where he needs to introduce his payment method (credit card number, cvc, and expiration date). As this is a project, the only card number working at the moment, due stripe  used on test mode is **4242 4242 4242 4242** however, when the project will be tested, expiration date and cvc will be up to the user testing the website. 
    Needless to say, If the user is not logged in, the deliveries detailes will not be save for the future purchases.
    To sum up, we can see as well two different buttons. The first button will lead the user to the bag page where there is the posibbility to adjust the purchase details (amount of products) The second button will bring the purchase to the end; the user will accept the purchase and finally pay the products. 
5.
![Checkout](/screenshots/screenshots7.png)
  - Once the user had finally made the purchase, the store will send a message to the user with all the information relative to the purchase. As well we can see on the page all the information about the purchase such as the order number, price, delivery information and billing info.
  Finally, we have a button to go to new arrivals section to keep the user on the store being able to see the latest updates and do not miss anything.
6.
![Wish List Empty](/screenshots/screenshots8.png)
![Wish List](/screenshots/screenshots9.png)
  * Wish List
    - As we can see in the first image, we will be talking about the wish list page. In this case we have our wish list empty. The user needs to authenticated itself, otherwise it won't be able to access to the page and create the wish list. However,once the user is logged in, it will be able to navigate through the wish list. The user has the posibility to go back to the products page and add some items to the wish list. 
    Products added on the wish list will be appearing on the left side, meanwhile on the right side the user will be able to see different options (orders, products and change paswrord)) to make the navigation much easier and intuitve.
    - Along the second image, we can see this time the wish list filled with some items. As we mentioned before, all the products will show the same information provided on products page (name of the piece, category, description, rate...) Users will have the ability to remove the product from their wish list if they want to do it.
7.
  ![Product Review](/screenshots/screenshots10.png)
    - As we can see in the image, the user can add a review to any of the products. The reviews will appear on the left side of the screen. As we mentioned before if the admin is logged in, it will have the possibility of removing any comments or inappropriate reviews. 
# Testing Users Stories

1. As a User
  - As a user It will be nice to have an easy navigation experience. 
    * Users will experience a nice and easy navigation due the display of the website. The project it is very intuitve as both navbars give different options allowing the user navigate throught several links being able to surf the website after some clicks.
    
  - As a user I expect the process of registration and log in simple and easy.
    *The procedures that the user needs to follow to registrate and login are quite easy as it will be just necesary to fill a form with basic details of the user (username, email, pasword...). You can find some screenshots attached below, where we explained the procedures deeply. 
      1. ![Registration](/screenshots/screenshots21.png)
        - As we can see in the screenshot, regsitration process it will be easy for the user due simplicity and the brief descriptions on each field. If the user fill up the fields without respecting the minimal requirements, user won't be able to register, instead will receive an error explaining what the user did wrong.
      2. ![Registration Email](/screenshots/screenshots22.png)
        - Once the user complete the proccess of registration, a message will be sent to the email provided. However, if the  project is running locally, the email sent will be in the console. Meanwhile, If the project is running in production, the mentioned email will be sent to the email adress provided by the user. Thanks to this procedures, we will be able to verify if the user is real, at the same time, the user will need to confirm the email, otherwise users won't be able to login.
      3. ![Login](/screenshots/screenshots23.png)
        - As we explained before, a very similar process will be required by users to login. Users must fill up the fields with the information required, which was given before when the user registered himself (username and password). If the user wants to save the credentials to login they can click on the small box below the two inputs, the name of the box is **Remember me**. Once the user select that option, all the information provided by the user will be save straigh away making easier the procedures. 

  - As a user I would like to be able to see the record of my previous purchases.
    * If the user made a purchase, it will have the option to see the details of that order. However, the user will have access to all the information from previous orders.
      1. ![Previous Orders](/screenshots/screenshots24.png)
        - As we mentioned before, all the users are able to see purchase details. As you can see in the screenshot, some of the details are: name of the product, quantity, delivery cost if any, subtotal, total, etc...
        The main goal of this invoice is to give the maximun amount of information at once to the user. 

  - As a user I want to have the possibility to add, remove or read items being in my wish list.
    * Needless to say, add items to a wish list is a must have in any e-commerce. Because of that we take this in consideration along the project. The user will be able to add his fauvourites items that he might buy in the future. Thanks to the wish list the user can have a record of the products and it will not have the need to research them again when that user open the browser. However, something to keep in mind is that only authenticated users are able to add or remove items from the wish list as we mentioned before.

  - As a user It will be a good option to be able to add a coment below the products.
    *Following the main goal of creating a website with an easy navigation, add a review is not any different. The user will need to fill a simple form.  However, there is a missing functionallity: just authenticated users after made a purchase will be able to add a review, at the moment, everybody can do it. In future projects it will be something to improve as it is not following any logic that  aleatory people have the posibility to add a review. After sharing the project with some friends I realized some of them presented difficultities to figure it out how to add the review. Their were expecting to add the review straight away after finishing the purchase. Because of that I will keep on mind to improve the display of the review to make it more intuitive for the user.
    
2. As a owner
  - As a owner It will be mandatory to be able to send messages once the user finish the registration form to confirm the procedure.
  * ![Email Registration Website](/screenshots/screenshots25.png)
    As we explained before, when the project is being used in production the user will recieve the confirmation email straigh away into the email adress provided. As this project is a demo It will work with any temporarily email. Once the user got the confirmation email after registered, it will be mandatory to click on the link to finish the regustration process. From no on the user will be able to log in. 
    However, as we can see in the screenshot; if the project is running locally, the confrimation e-mail will be sent to the console instead of the email adress provided.
      - ![Email Registration Console](/screenshots/screenshots28.png)

  - As a owner I would like to have the posibility to delete any post contained of hate-speech, or inappropiate content.
    * ![Delete Post](/screenshots/screenshots26.png)
    - Owners will be able to delete any review if they consider there are some hate, innapropiate language or irrelevant information about the product and website. 
    - As wen can see in the below picture, when the owner of the website delete a review, a pop up will appear to confirm this action. Thanks to this control the owner will avoid any possible mistakes.
    - ![Delete Post Popup](/screenshots/screenshots27.png)

  - As a owner I need to be able to add, edit and delete products when they may be out of stock or sold out.
    * Owners need to have the control of their own website, because of that we want to give them the posibility to add delete or edit any product. To add a product admins has to fill a form providing a proper description of the item. Not only it wiill be essential to describe the product, but also the owner will need to give a name and a price to the product at the same time he add a picture of it. Pictures attached below.
    ![Add Product](/screenshots/screenshots29.png)
    ![Add Product](/screenshots/screenshots30.png)
    
-  As a owner I really want to assure the user an amazing navigate experience. 
 As we explained before, the owner wants to give the perfect service to the user, because of that an easy navigation is elemental. The display of the website makes the navigation experience pretty intuitive and simple for the user. In every moment the user will be able to surf the website just with some clicks moving from one link to another one. 

# Deployment
Project have been deployed on heroku and it is host on github. First of all, you will need to create a repo on github wich will be our host to store our code, meanwhile heroku will store the full website as heroku is capable of store backend code wich github does not.
- ![Create a Repo](/screenshots/screenshots31.png)
  ![Create a Repo 1](/screenshots/screenshots32.png)
- After the repo has been created, we head to heroku to create an app to store our project.
![Create App](/screenshots/screenshots33.png)
Once the app has been created we choose our closest region.
![Choose Region](/screenshots/screenshots34.png)
We will need to add all the necessary variables in the created app. Thanks to this variables, the project will run properly. 
![Setting Variables](/screenshots/screenshots38.png)
Once our closest region is selected we connect our github repo with our app on heroku.
![Connect Github](/screenshots/screenshots35.png)
![Connect Github 1](/screenshots/screenshots36.png)
![Connect Github 2](/screenshots/screenshots37.png)
A note to mention: Along this project we used AWS(Amazon Web Services) wich allow us to host our own images and static files like css and javascript.
Before we push our code to heroku we need to run a command on the terminal to disable collectstatic. This comand will disable all static files due Heroku does not store static files. The following command has to be run on the terminal **heroku config:set DISABLE_COLLECTSTATIC=1**.
Once AWS is set up, we can collect static running the following command: **heroku config:set DEBUG_COLLECTSTATIC=1** or just removing the variable from the heroku panel on the heroku website.

- In this case we add pictures made by my partner wich means I did not use a fixture folders to add images and all the data to the project. To load data to the project we use the following command which will dump data in a single json file, and then load that data into the project again in order to add all the data to the site.
*Dump data in a json file*
```python3 manage.py dumpdata --exclude auth.permission --exclude contenttypes > db.json```
*Upload data from the json file*
```python3 manage.py loaddata db.json```

---
- On our code we write this code to tell django if we are running on our local machine we want to use sqlite database, otherwise we use postgress database wich will be use by Heroku.
  ```if 'DATABASE_URL' in os.environ:
      DATABASES = {
          'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
      }
  else:
      DATABASES = {
          'default': {
              'ENGINE': 'django.db.backends.sqlite3',
              'NAME': BASE_DIR / 'db.sqlite3',
          }
      }
  ```

- The following code was use to set up AWS to store static files, wich includes a bucket name, closest region, secret key, custom domain. All this variables will be hidden in our enviroment variables, could be on heroku or in our local machine.
```
  if 'USE_AWS' in os.environ:
    # Cache control
    AWS_S3_OBJECT_PARAMETERS = {
        'Expires': 'thu, 31 Dec 2099 20:00:00 GMT',
        'CacheControl': 'max-age=94608000',
    }

    # Bucket Config
    AWS_STORAGE_BUCKET_NAME = '<bucket name></bucket>'
    AWS_S3_REGION_NAME = '<closest region>'
    AWS_ACCESS_KEY_ID = <aws access key>
    AWS_SECRET_ACCESS_KEY = <aws secret access key>
    AWS_S3_CUSTOM_DOMAIN = <aws custom domain>

    # Static and media files
    STATICFILES_STORAGE = 'custom_storages.StaticStorage'
    STATICFILES_LOCATION = 'static'
    DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'
    MEDIAFILES_LOCATION = 'media'

    # Override static and media URLs in production
    STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{STATICFILES_LOCATION}/'
    MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{MEDIAFILES_LOCATION}/'
```

**Clone Repository**
- First of all locate our repository wich is [The ark Kingdom](https://github.com/CarlosFaccelli26/Bread-Butter-Milestone).
  * ![Repo](/screenshots/screenshots31.png)
- Once we Find the repo we can copy the link and head back to our code editor
![Copy Repo](/screenshots/screenshots39.png)
Once Link is copied we head back to our code editor and open it. After it has been located on the terminal, we can run a command to clone the repository to store in our  machine.
![Clone Repo](/screenshots/screenshots40.png)
![Clone Repo 1](/screenshots/screenshots41.png)

# Credits

[Review Avarage](https://stackoverflow.com/questions/68255990/how-to-show-average-of-star-rating-in-django) Used to calculate avarage rating and display on templates.


Products images:
All products images have been taking by my grilfriend Sophie as all the pieces have been made by her. 

Base project was build with the walkthrough project provided by [Code Institute](https://codeinstitute.net/)

I need to thank my mentor [Rahul Lakhanpal](https://codeinstitute.net/)