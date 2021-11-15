# crop2cash-jiji-clone-api Project Report

You can view the documentation [here](http://localhost:8000/swagger/#)

Technologies used:
- Django and Djangorestframework
- Djangorestframework-simplejwt for JWT authentication
- Postgres
- Redis and Django-redis for caching


## Running this project locally

- Clone the project
- run `pip install requirements.txt` to install all the required dependencies
- run `python manage.py runserver` in the project root folder
- on your browser, open up
  - `http://localhost:8000/swagger/#` to view the endpoints and their documentation
  
# What I have been able to acheive.

1.  I was able to build out the specification required for this assignment which include the following:
      - Seller App
  
    This app enables seller to create account and login into that account.
      - Buyer App
  
    This app enables buyers to indicate interest in an item by supplying their email address, name and location.
  
      - Item App

          This app enables an authenticated seller to create an item for sale. Item images are hosted on AWS S3       bucket to free up the server from serving images.

          Sellers can also see the list of items they have created according to the criteria described in the seller story
      
          This app also takes care of listing all the items in the database that has not been sold.

          Sellers can also view an individual item to see more details about the item.

          It also has an endpoint for choosing a buyer out of all the list of interested buyers.

          Sellers can also delete any item that they want.

          Buyers can also see the list of items they have shown interest in.
      
2. Cache the endpoint that lists all the unsold items in the database
3. The API is hosted on Heroku
