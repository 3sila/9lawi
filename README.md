## Data Centric Development Project - Code Institute
---
# Snoop
Tired of signing up just to place your toaster or TV in order to get few bobs? Tired of unwanted spam mail in your e-mail about adverts that don't interest you?
With **Snoop** you don't have to give your e-mail or phone number! No more long sign-up process and you have more time to snoop for a good deal on that car you like!

#### Click on the picture to see live demo!
[![Snoop Demo](https://raw.githubusercontent.com/romangrubic/database-project/master/static/images/readme/responsive/responsive.png "Snoop Demo")](https://adverts-project.herokuapp.com/home)

---
## Summary
* [Project Background](#project-background)
* [User Experience](#ux)
    * [User Stories](#user-stories)
    * [Five planes](#strategy)
* [Features](#features)
    * [Existing Features](#existing-features)
    * [Future Features](#future-features)
* [Information Architecture](#information-architecture)
* [Technology used](#technology-used)
* [Testing](#testing)
* [Deployment](#deployment)
* [Credits](#credits)

---
## Project Background

Welcome to my Data Centric Milestone Project for Code Institute. 

The goal of this project was to allow the user to make simple operations where it could create, retrieve, update and delete data. Database used is a noSQL database MongoDB.

The project is a web-site where user can post their adverts (similar to DoneDeal, Adverts, Gumtree...) and buy from others and also for companies or users to rent out side 
spaces on the pages to promote their bussines (that space is coloured ![#99D9EA](https://placehold.it/15/99D9EA/000000?text=+) `#99D9EA` in order to be visible from rest of the site and is clickable. When it is clicked, it will open a contact modal).

I choose the name Snoop as in "to snoop around" and all similarities with Snoop Dog is accidental.

 [Back to top](#summary)

---

## UX
### User Stories
#### As a new user of the web-site, I would like to be able to:

* **see all the ads**
  - user can see all adverts by clicking on `Marketplace` button. 

<p align="center">
  <img src="https://raw.githubusercontent.com/romangrubic/database-project/master/static/images/readme/user_stories/all-ads.png" width="500" height="300" alt="Marketplace image">
</p>

* **search for a specific advert**
  - user can use one of multiple options to search:

    - ![#FF8000](https://placehold.it/15/FF80000/000000?text=+) by category (it will show ALL adverts in selected category)
    - ![#228B22](https://placehold.it/15/228B22/000000?text=+) by keyword and/or county (this option filter adverts and show selected. It can show by keyword, by county, by both or if none selected, it will show ALL adverts)
    - ![#EE1C24](https://placehold.it/15/EE1C24/000000?text=+) by category and county (searches for BOTH category and county selected)

<p align="center">
  <img src="https://raw.githubusercontent.com/romangrubic/database-project/master/static/images/readme/user_stories/search.png" width="600" height="300" alt="Search options">
</p>

* **see for what I searched for if there's no results**
  - user can see what they searched for and have option to go to Home page. 

<p align="center">
  <img src="https://raw.githubusercontent.com/romangrubic/database-project/master/static/images/readme/user_stories/no-search.png" width="500" height="350" alt="User can see what they searched for">
</p>

* **view advert that I'm interested in**
  - user can view advert in full view by clicking anywhere on the advert. 
<p align="center">
  <img src="https://raw.githubusercontent.com/romangrubic/database-project/master/static/images/readme/user_stories/view-ad.png" width="400" height="600" alt="View advert">
</p>

* **share the URL of the advert easily with someone who might be interested**
  - user can share the URL of the advert by clicking on button which will copy the URL into users clipboard. 
<p align="center">
  <img src="https://raw.githubusercontent.com/romangrubic/database-project/master/static/images/readme/user_stories/share-ad.png" width="400" height="200" alt="Share URL">
</p>

* **view my location in relation to Home page**
  - user can see location just beneath navigation bar. 
<p align="center">
  <img src="https://raw.githubusercontent.com/romangrubic/database-project/master/static/images/readme/user_stories/breadcrumbs.png" width="600" height="200" alt="Location of the user">
</p>

* **place my own advert**
  - user can place their own advert just by going to Add advert in the navigation bar. 
<p align="center">
  <img src="https://raw.githubusercontent.com/romangrubic/database-project/master/static/images/readme/user_stories/add-advert.png" width="450" height="400" alt="Add advert">
</p>

* **change my advert**
  - user can edit adverts if something changed by pressing `Edit` button and entering `Access key`.
<p align="center">
  <img src="https://raw.githubusercontent.com/romangrubic/database-project/master/static/images/readme/user_stories/edit-advert.png" width="450" height="400" alt="Edit advert">
</p>

* **delete my advert**
  - user can delete adverts if the advert is no longer valid by pressing `Delete` button and entering `Access key`.
<p align="center">
  <img src="https://raw.githubusercontent.com/romangrubic/database-project/master/static/images/readme/user_stories/delete-advert.png" width="500" height="300" alt="Delete advert">
</p>

* **know if access key is wrong**
  - if user enters access key which is incorrect, a page 403 will load and instruct the user that their key was wrong and give them option to go back to the advert.
<p align="center">
  <img src="https://raw.githubusercontent.com/romangrubic/database-project/master/static/images/readme/user_stories/access_denied.png" width="500" height="350" alt="Page 403">
</p>

#### As a company, I would like to:
* **promote my product**
  - companies/users can promote their product or rent space to promote themselves by contacting me. Every page has dedicated places to rent coloured ![#99D9EA](https://placehold.it/15/99D9EA/000000?text=+) `#99D9EA`.
<p align="center">
  <img src="https://raw.githubusercontent.com/romangrubic/database-project/master/static/images/readme/user_stories/place-ad.png" width="500" height="300" alt="Place your ad!">
</p>

[Back to top](#summary)

### Strategy

**Snoop** web-site purpose is to be a marketplace where users can put their things to sell and earn money and for companies to promote their bussines by renting advertisement space. 
Also, for the owner of the page to earn money by renting out designated advertisement space (side spaces coloured ![#99D9EA](https://placehold.it/15/99D9EA/000000?text=+) `#99D9EA` ) to either companies/users or [Google ads](https://www.google.com/adsense/start/).

### Scope

In designing this page, I wanted for the user to have a positive experience and for the web-site to be simple to use. So I wanted to make a page like that. 
User can easily search with one click (by pressing Marketplace in navbar or by pressing one of the filter buttons to search for adverts in a certain category and certain county).



### Structure

When the user arrives on site, it will see buttons and search bar as a call to action. Navigation is centered and is always on top of the screen and has a logo which acts as a link to Home page,
Marketplace button where he can see all the adverts sorted by number of views and Add advert where new advert can be added with ease. There is also "Most viewed advert" and "Most recent advert" section with 4 of the most viewed or most recent adverts.

When user goes to Marketplace page, adverts will show up ranked by number of views they have. Also, there are only 12 adverts visible per page and a `Go to top` button at the end of the page. Adverts are presented as cards with a 
decent size picture and below their name, number of views, location and price. 
Adverts are clickable on all of their size so user can easily see the whole advert. If user clicks on advert, a new page will open where information will be presented in a bigger format and advert description will also be visible. 

There are buttons on the end of the page where user can delete the advert or edit it if neccessary. If user presses `Delete` button, a modal will show up asking the user for `Access key`. If the `Access key` is same as the advert key, 
advert is deleted. If they press `Edit` button, a modal will show up asking the user for `Access key`. If the `Access key` is same as the advert key, edit page will open
containing all the data of the advert in database and user can change all or any part of it. Otherwise, in both cases, if the access key is incorrect, they will be redirected to access_denied.html where 
they will be explained that their key is invalid and instructed to go back to advert.

User can click on filter buttons that are visible on all main pages, where he can fast search a specific category of adverts. If he wants to see `Motors`, all adverts in category of Motors will show. Same 
for the rest of the categories. Search bar where user can search for a keyword or part of the keyword. They can search by keyword and/or by county. If none is selected, then search will result in showing ALL adverts.
There is also `Addiotional` button where user can search by category and county.

There is also an `Add advert` link in the navigation where by clicking on it, new page will show up and user can put item for sale.

Footer is visible on any page and icons themselves are clickable and leading to my projects, my Github or my LinkedIn and opening a 
contact modal. 

As an addition, I have implemented a designated space (coloured ![#99D9EA](https://placehold.it/15/99D9EA/000000?text=+) `#99D9EA`) on all of the pages where companies or anyone can rent and promote themselves and me as an owner can earn some money on the side.

#### Further description of buttons, icons and elements used is in the next section [Features](#existing-features).

### Wireframes

* **Home page**
  
  <p align="center">
  <img src="https://raw.githubusercontent.com/romangrubic/database-project/master/static/images/readme/wireframe/wireframe-home.jpg" width="500" height="300" alt="Home page">
</p>

* **Marketplace page**
  
  <p align="center">
  <img src="https://raw.githubusercontent.com/romangrubic/database-project/master/static/images/readme/wireframe/wireframe-market.jpg" width="400" height="500" alt="Marketplace page">
</p>

* **View advert**
  
  <p align="center">
  <img src="https://raw.githubusercontent.com/romangrubic/database-project/master/static/images/readme/wireframe/wireframe-view.jpg" width="500" height="300" alt="View advert">
</p>

* **Add/Edit advert page**
  
  <p align="center">
  <img src="https://raw.githubusercontent.com/romangrubic/database-project/master/static/images/readme/wireframe/wireframe-add.jpg" width="400" height="500" alt="Add/Edit page">
</p>

### Surface 
Using light color scheme I'm creating an environment where user will stay as long as possible because there are no bright colors which will tired users eyes.
By making all the elements stand out correctly and are simple to use, I'm creating environment where 
user can see what it wants, look at adverts that interest it. Users experience of **Snoop** will be that it is simple and easy to use.


 + Main colors used throughout the web-site : 
    - Navigation bar - ![#FAFAFA](https://placehold.it/15/FAFAFA/000000?text=+) `#FAFAFA`
    - Body of the website - ![#EDEDED](https://placehold.it/15/EDEDED/000000?text=+) `#EDEDED`
    - Footer - ![#575757](https://placehold.it/15/575757/000000?text=+) `#575757`
    - Place to rent out for advertisement - ![#99D9EA](https://placehold.it/15/99D9EA/000000?text=+) `#99D9EA`

[Back to top](#summary)

---
## Features
### Existing Features
* Navigation bar
  - Navigation bar is visible on all pages and on all sizes. It contains a link to home page presented by logo, a link for marketplace where user can see all the ads sorted by views and an add advert page where user can place an advert. 

* Advert section
  - On each page, on medium screens and bigger sizes, there are parts where owner of the
   page can promote his own adverts or rent that space to companies for advertisement and earn money that way. They are coloured ![#99D9EA](https://placehold.it/15/99D9EA/000000?text=+) `#99D9EA` and when user clicks on it, a contact modal pops-up where user can contact me in relation with advertising space.

* Breadcrumbs
  - On every page excluding Home page, there are breadcrumbs just beneath navigation bar where user can see his/hers location in relation to Home page. If user decides to click on it,
  it will open that page.

* Filter buttons and search bar
  - They are visible on all pages and are used to filter ads. User can filter adverts by any combination or keyword, county and category.

* Most viewed and Most recent section 
  - Carousel which is showing 4 most viewed or most recent adverts on site. Each advert is clickable and if user clicks on it will open that advert in View_advert.html.

* Time and Date
  - Each advert has the time when it was entered or renewed which helps the user.

* Add advert 
  - User can add advert by typing all the required information that are neccessary.
   All fields are required and have to filled by the requirements. By pressing submit button, advert will be saved to database and will populate in Marketplace.

* Access key - security
  - On adding advert, user will be asked to put in "Access key" which will then be used for deleting or editing advert. It is made as a security measure from unauthorized deleting or editing on the site.

* Access denied - page 403
  - If user enters an incorrect access key when asked, they will get redirected to a page where they will see that their access is denied and a button to go back to advert.

* Adverts cards
  - Once the user searches or visits Marketplace, adverts will be presented in cards. User can see image of the advert and bellow it
  are tittle, number of views, location and price. The cards themselves are clickable and once clicked they 
  will open in a new page where user can see rest of information such as description and contact information.

* View advert
  - Once user clicks on an advert, a big page opens where user can see all the information about an advert and also can delete the advert or edit the advert if the information is not correct or have changed

* Edit advert
  - Edit advert is similar to add advert page except it already shows all the data of the advert that is in database. User can then either save the changes that were made or cancel the edit if it was misclicked or no changes added.

* Pagination 
  - I have added pagination to Marketplace.html and Search.html so that user can only see 12 adverts at a time. 

* "Go to top" button
  - Instead of user scrolling back to the top of the page when he reaches the bottom, I have put a button that will return to top once pressed.

* No results - page 404
  - If user search for an item that is not in database, they will see a message that searched item is not in database (they will see exactly what they typed in search bar or what filters they used) 
  and instruct user to search again or filter through categories. There is a button bellow message and it will redirect them to Home page.

* View counter
  - View counter is implemented in footer section and is only visible on medium and bigger screen sizes. It increments the counter by +1 every time Home page is visited.

* Social icons
  - In the footer are three social icons with links, one leading to my GitHub page, one for my LinkedIn profile (both of them open in a new tab because of 
  `target="_blank"` attribute) and last one opens a contact modal from which user can contact me.

* My projects icons
  - In the footer are two project icons with links,one leading to my **Portfolio** web-site, second leading to my **Weather 360°** project and third for my **Animals** project (all of them open in a new tab because of 
  `target="_blank"` attribute). Only visible on medium and bigger screen sizes.

* Contact modal
  - When user click on contact icon, it opens a new modal. User has to input all the requested information in order for e-mail to be sent. When the e-mail has been submitted, 
  the text in the submit button will go from red background color and `Submit` to green background color and `E-mail submitted! Closing...` and modal will close itself after 2seconds using `setTimeout` function. 
  If it was unsuccessful, it will turn gray background color with `Failed to submit. Refresh page` text.

[Back to top](#summary)

### Future Features
  - A login systems for users on the page would've provided another level of security to adverts on this page. This could be performed in the back end using conditional statements to check if the current user is logged in or not with the current user being gotten from the session. Only if these criteria were satisfied then the user would be allowed to edit, delete or add adverts etc.

  - Instead of renting advertising space to users and companies, there is an option to rent it to Google AdSense and therefore not worry about renting it to multiple users but instead to only one. Worth considering as a meaningful source of income. More on [link](https://www.google.com/adsense/start/).

[Back to top](#summary)

---
## Information Architecture

### Database
This project employs the NoSQL database [MongoDB](https://www.mongodb.com/). 

### Data Types

Below are the different data types in the MongoDB that I'm using:

- ObjectId
- String
- Integer

### Data Structure 

Below is the data base collection:

Adverts Collection

| Title              | DB Key       | Form Validation                           | Data type |
| ------------------ | ------------ | ----------------------------------------- | --------- |
| Advert Id          | _id          | None                                      | ObjectId  |
| Category name      | category_name| user chooses from a list of choices       | string    |
| Advert Name        | advert_name  | text, maxlength="9"                       | string    |
| Advert Description | advert_description | text/number , maxlength="300"       | string    |
| Price              | price        | number , min="0" max="99999"              | string    |
| Contact info       | contact_info | text/number/email, maxlength="25"         | string    |
| Location           | location     |  user chooses from a list of choices      | string    |
| Upload Image       | imageURL     | image, image/*                            | string    |
| Views              | views        | number                                    | integer   |
| Key                | key          | text/number/symbol, minlength="4", maxlength="15"    | string   |


[JSON file showing adverts collection structure](https://github.com/romangrubic/database-project/tree/master/data/database/adverts.json) 


[Back to top](#summary)

---
## Technology used

* HTML5 & CCS3: Essential languages used to build a websites foundations.
 
    - https://en.wikipedia.org/wiki/HTML5
    - https://en.wikipedia.org/wiki/Cascading_Style_Sheets
* Bootstrap: An easy to use, responsive framework. Bootstrap was used to allow easy implementation of the overall responsivness and contact modal. Bootstrap's 
grid system was also used for simplicity and efficiency.
    
    - https://getbootstrap.com/
* Font Awesome: A vast and free library of responsive icons. This library was used for the social link icons found in the footer.
    
    - https://fontawesome.com/
* JavaScript and jQuery: These technologies were essential for the functioning of Email.js in order for user to contact me.
    
    - https://jquery.com/
* EmailJS: Service that helps sending emails using client side technologies only. It only requires to connect EmailJS to one of the supported email services, 
create an email template, and use their Javascript library to trigger an email. This was used for contact modal so that user's can get in contact with me. 
    
    - https://www.emailjs.com/
* Python: Python is an interpreted, high-level, general-purpose programming language. In this project it was used to manage the back end development of the project.

    - https://www.python.org/
* Flask: Lightweight WSGI web application framework. It is designed to make getting
 started quick and easy, with the ability to scale up to complex applications.

    - https://palletsprojects.com/p/flask/
* MongoDB: NoSQL document-oriented database program that uses JSON like documents with schema used by the site to store user adverts.

    - https://www.mongodb.com/
* Github: Provides hosting for software development version control using Git and is used to store this projects repository.

    - https://github.com/
* Heroku: Cloud platform as a service supporting several programming languages and is used to deploy this project
    
    - https://www.heroku.com

[Back to top](#summary)

---

## Testing

### Testing section is located [here](https://github.com/romangrubic/database-project/blob/master/testing.md)

### Validating code
HTML
 - code is validated through [W3 validator](https://validator.w3.org/).

CSS
 - code is validated through [W3 Jigsaw](https://jigsaw.w3.org/css-validator/).

JavaScript
 - code is validated through [JS Hint](https://jshint.com/).

Python
 - code is validated through [PEP8](http://pep8online.com/).

 [Back to top](#summary)

---

## Deployment
The project was written and developed in the Gitpod IDE.

A local repository was intialized using Github. Regular changes were commited to the local repository.

The process for deployment on Heroku was:

  - Create a new unique app name in Heroku with “Europe” as the server.
  - In the workspace, log into Heroku with command Line and the set of commands provided to create a connection between the application and Heroku.
  - Create a new Git repository and add the files, then associate the Heroku application and push to Heroku once the requirements.txt file and Procfile have been created.
  - Configuration variables had to be set in order to get the project running. These had to be set in both the Gitpod IDE and on Heroku. These included, PORT, IP and Mongo URL.
  - Open the app to test successful deployment.

To run locally, you can clone this repository directly into the editor of your choice by pasting `git clone https://github.com/romangrubic/database-project.git` into your terminal. To cut ties with this GitHub repository, type `git remote rm origin` into the terminal.  

Further help with cloning can be found on this GitHub Help [page](https://help.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository).

[Back to top](#summary)

---

## Credits
### Content
+ All content was written by myself and by users.

### Acknowledgement
* Videos on [CodeInstitute](https://codeinstitute.net/).
* Thanks to my mentor Aaron Sinnott for feedback and ideas.
* Big thanks to [W3 Schools](https://www.w3schools.com/) for all the content and clarification of different methods.
* Background photos used in this site were obtained from [Pexels](https://www.pexels.com/), a stock image library.
* Other advertisement site like [DoneDeal](https://www.donedeal.ie/), [Advert](https://www.adverts.ie/), [Gumtree](https://www.gumtree.ie/) etc.

#### This is for educational use.
[Back to top](#summary)