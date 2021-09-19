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
  - Desktop - [View]()
  - Mobile - [View]()

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
    - Edit Product ![View](/sreenshots/screenshots18.png)
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
 
2. As a owner
  - As a owner It will be mandatory to be able to send messages once the user finish the registration form to confirm the procedure.
  - As a owner I would like to have the posibility to delete any post contained of hate-speech, or inappropiate content. 
  - As a owner I need to be able to add, edit and delete products when they may be out of stock or sold out.
  - As a owner I really want to assure the user an amazing navigate experience. 


  - As a user It will be nice to have an easy navigation experience. 
    * Users will experience a nice and easy navigation due the display of the website. The project it is very intuitve as both navbars give different options allowing the user navigate throught several links being able to surf the website after some clicks.
  - As a user I expect the process of registration and log in simple and easy.
    *The procedures that the user needs to follow to registrate and login are quite easy as it will be just necesary to fill a form with basic details of the user (username, email, pasword...). You can find some screenshots attached below, where we explained the procedures deeply. 
      1. ![Registration](/screenshots/screenshots21.png)
        - As we can see in the screenshot, regsitration process it will be easy for the user due simplicity and the brief descriptions on each field. If the user fill up the fields without respecting the minimal requirements, user won't be able to register, instead will receive an error explaining what the user did wrong.
      2. ![Registration Email](/screenshots/screenshots22.png)
        - Once the user complete the proccess of registration, a message will be sent to the email provided. If project is running locally the email sent will be in the console however if the project is running in production email will be sent to the email provided by the user. This ensure that the user is real, because users needs to confirm the email sent to them, otherwise users won't be able to login.
      3. ![Login](/screenshots/screenshots23.png)
        - Similar process will be required by users to login. Users must fill up the fileds required on the page with the information previous given; in this case username and password. If user wants to save the credentials to login they can thanks to the small box below the two inputs with the label of **Remember me** wich will save the info provided by the user making it easier to users in this process.
  - As a user I would like to be able to see the record of my previous purchases.
    * Users once they made a purchase will be able to see the details of that orders, or in case that users made previous orders they will be able to see previous orders and its details.
      1. ![Previous Orders](/screenshots/screenshots24.png)
        - As we can see in the screenshot users are able to see details of the purchase such as name of the product, quantity, delivery cost if any, subtotal, total, etc...
        Tihs invoice will give the user all the details about the purchase that they just made. 
  - As a user I want to have the possibility to add, remove or read items being in my wish list.
    * Add items to wish list is a must have in any e-commerce, because allows the user to add items that they're insterested in, wich allows user to not be wasting time looking an item each time that users open the browser. Something to keep in mind is that only authenticated users are able to add or remove items from the wish list
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