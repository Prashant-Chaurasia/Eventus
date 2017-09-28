## Eventus - A Platform To Book Events Around You
Simple app to display the college events in different colleges around you that is in your city and also the events going on in your college.
We will be providing a perfect gateaway to book the tickets or participate in a particular event . Also we will be providing coupons and 
cashback to you which you can use to buy or book tickets further.

### Development Setup

##### Database Setup
* Install postgresql (``` >=9.2 ```)
* Install pycharm 
* Go to terminal and run following -
  ``` 
  sudo su - postgres
  psql
  ```
* Create database and user 
  ```
  Create database eventus ;
  Create user eventus with password 'eventus';
  Grant all on database eventus to eventus;
  Alter role eventus with login;
  ```
* Exit to root console

##### Cloning Project

* Fork this project and clone to local system.Now through terminal go to the directory where you have downloaded.
  ```
  cd Eventus
  ```
* Install all the requirements 
  ```
  sudo -H pip install -r requirements.txt or sudo pip install -r requirements.txt
  ```
  If pip command not found install it and then run above command.
  
* Migrate Database and Run to Check Everything is upto up
  ```
  python manage.py migrate
  python manage.py runserver
  ```
### Contributing Guidelines
* Adhere to universal coding standard and practices .
* Don't commit or push directly to this branch always use Pull Request.
* Only one commit is allowed per pull request .
* Your PR should reference the issue pertaining to which you have made changes .
* Use good commit messages to clearly state what has been done .
* No one would merge the pull requests except me . In time to come I may ask someone to do this work.
  
  

 
  
