# Fresh|vintage-Project.5







[Live Link to Fresh|vintage]()

# UX
I wanted to keep the colour scheme quite simpley so its easy for the user to navigate and not get distracted while on the website The colour i used is 

### Colour Scheme 



### Typography


# Wireframe's

To have a better plan for developing my website, I utilized Justinmind.com to produce wireframes that serve as a guide on how I want the website to be created
## Home-Page 



## Home-Next-Page 



## About-Page



## Sign-Up-Page



## login-Page



 ## Contact-Page



## Add-Recipe-Page



## 404-Error-Page 




## Feature's
* Home-Page 
  * 
  
* Search-Bar
  * 

*  
  * 
  


* 
  * 
  
  


* 
  * 


  
* 

  * 
  
  
* 
  * 
  
  

* 
  *  

  
*  
   * 


   
*
  * 


  
* 
  * 
  
  

* 
  * 
  

  
*  
  * 


* 
  
*
 



## Future Features's


## Agile Development Process

### GitHub Projects
This project utilized GitHub Projects as an Agile tool. Although not a dedicated tool, it was customized with appropriate tags, project creation, and issue assignments to fit the project's needs.

The tool was used to visualize the development progress of the project by mapping user stories onto a basic Kanban board. It enabled me to identify the work backlog and to move tasks across the board as they were being worked on, tested, and signed off upon completion.



## GitHub Issues

GitHub Issues served as an another Agile tool. There, I used my own User Story Template to manage user stories and created a Bug tag to track and monitor issues on the site to be worked on.

* [Open issues]()




* [Closed issues ])




### MoSCoW Prioritization
Prior to prioritizing and implementing the Epics, I broke them down into smaller stories using a decomposition approach. This method enabled me to apply the MoSCoW prioritization and labels to the individual user stories within the Issues tab

* **Must have** = Guaranteed delivery.
* **Could have** =  has small impact if left out.
* **Bug** 
* **Enhancement** = To make to site more user friendly.

## Testing 
For all testing, please refer to the [Testing.md]) file.


# Git terminal Commands Guide 

I used this guide throughout my project for solving terminal issues.

<img width="764" alt="Screen Shot 2023-05-15 at 16 06 13" src="https://github.com/MattyOL/Recipe-WorldWide-Project.4/assets/111317260/144ab711-d889-4f32-9390-81aab2436d78">

# Tools & Technologie Used in this project 
1. [HTML](https://en.wikipedia.org/wiki/HTML) used for the main site content.

2. [CSS](https://en.wikipedia.org/wiki/CSS) used for the main site design and layout.

3. [CSS:root variables](https://www.w3schools.com/css/css3_variables.asp) :root variables used for reusable styles throughout the site.

4. [Bootstrap](https://getbootstrap.com/) used as the front-end CSS framework for modern responsiveness and pre-built components.

5. [Python](https://www.python.org/) used as the back-end programming language.

6. [Git](https://git-scm.com/) used for version control. (git add, git commit, git push)

7. [GitHub](https://github.com/) used for secure online code storage.

8. [Gitpod](https://gitpod.io/workspaces) used as a cloud-based IDE for development.

9. [Django](https://www.djangoproject.com/) used as the Python framework for the site.

10. [PostgreSQL](https://www.postgresql.org/) used as the relational database management.

11. [ElephantSQL](https://www.elephantsql.com/) used as the Postgres database.

12. [Heroku](https://dashboard.heroku.com/apps) used for hosting the deployed back-end site.

13.[Cloudinary](https://cloudinary.com/) used for online static file storage.

14. [Code Spell Checker](https://marketplace.visualstudio.com/items?itemName=streetsidesoftware.code-spell-checker)[diff checker](https://www.diffchecker.com/) used to check for typos in my README and TESTING files.# Deployment 
15. Jquery

# ElephantSQl DataBase
The live Link to deployment can be found on [Live link Heroku](https://project-4-fsf.herokuapp.com/)

This project uses [ElephantSQL](https://www.elephantsql.com/) for the PostgreSQL Database.

To obtain your own Postgres Database, sign-up with your GitHub account, then follow these steps:

* Click Create New Instance to start a new database.
* Provide a name (this is commonly the name of the project: tribe).
* Select the Tiny Turtle (Free) plan.
* You can leave the Tags blank.
* Select the Region and Data Center closest to you.
* Once created, click on the new database name, where you can view the database URL and Password.

# Cloudinary API
This project uses the Cloudinary API to store media assets online, due to the fact that Heroku doesn't persist this type of data.

To obtain your own Cloudinary API key, create an account and log in.

* For Primary interest, you can choose Programmable Media for image and video API.
* Optional: edit your assigned cloud name to something more memorable.
* On your Cloudinary Dashboard, you can copy your API Environment Variable.
* Be sure to remove the CLOUDINARY_URL= as part of the API value; this is the key.

# Heroku Deployment
Heroku, a platform as a service (PaaS), was employed for this project. This cloud-based platform enables developers to build, run, and manage applications entirely on the cloud.

Deployment steps are as follows, after account setup:

* Select New in the top-right corner of your Heroku Dashboard, and select Create new app from the dropdown menu.
* Your app name must be unique, and then choose a region closest to you (EU or USA), and finally, select Create App.
* From the new app Settings, click Reveal Config Vars, and set your environment variables.

1. CLOUDINARY_URL - 	insert your own Cloudinary API key here
2. DATABASE_URL - insert your own ElephantSQL database URL here
3. DISABLE_COLLECTSTATIC - 1 (this is temporary, and can be removed for the final deployment)
4. SECRET_KEY - this can be any random secret key

Heroku needs two additional files in order to deploy properly.

* requirements.txt
* Procfile
You can install this project's requirements (where applicable) using:

* pip3 install -r requirements.txt
If you have your own packages that have been installed, then the requirements file needs updated using:

* pip3 freeze --local > requirements.txt
The Procfile can be created with the following command:

* echo web: gunicorn app_name.wsgi > Procfile
* replace app_name with the name of your primary Django app name; the folder where settings.py is located
For Heroku deployment, follow these steps to connect your own GitHub repository to the newly created app:

Either:

* Select Automatic Deployment from the Heroku app / You Can also Manual deploy.

Or:

* In the Terminal/CLI, connect to Heroku using this command: heroku login -i
* Set the remote for Heroku: heroku git:remote -a app_name (replace app_name with your app name)
* After performing the standard Git add, commit, and push to GitHub, you can now type:
* git push heroku main

The project should now be connected and deployed to Heroku & everything should deploy correctly!

 # local Deployment 
This project can be cloned or forked in order to make a local copy on your own system.

For either method, you will need to install any applicable packages found within the requirements.txt file.

* pip3 install -r requirements.txt.
You will need to create a new file called env.py at the root-level, and include the same environment variables listed above from the Heroku deployment steps.

Sample env.py file:
import os

os.environ.setdefault("CLOUDINARY_URL", "insert your own Cloudinary API key here")
os.environ.setdefault("DATABASE_URL", "insert your own ElephantSQL database URL here")
os.environ.setdefault("SECRET_KEY", "this can be any random secret key")


Once the project is cloned or forked, in order to run it locally, you'll need to follow these steps:

* Start the Django app: python3 manage.py runserver
* Stop the app once it's loaded: CTRL+C or ⌘+C (Mac)
* Make any necessary migrations: python3 manage.py makemigrations
* Migrate the data to the database: python3 manage.py migrate
* Create a superuser: python3 manage.py createsuperuser
* Load fixtures (if applicable): python3 manage.py loaddata file-name.json (repeat for each file)
* Everything should be ready now, so run the Django app again: python3 manage.py runserver

## Cloning

You can clone the repository by following these steps:

1. Go to the ur Github repository
2. Locate the Code button above the list of files and click it
3. Select if you prefer to clone using HTTPS, SSH, or GitHub CLI and click the copy button to copy the URL to your clipboard
4. Open Git Bash or Terminal
5. Change the current working directory to the one where you want the cloned directory
6. In your IDE Terminal, type the following command to clone my repository:
7. git clone 
8. Press Enter to create your local clone.

## Forking

To avoid affecting the original owner's repository, a copy of the original repository is made on our GitHub account by forking the GitHub Repository. This enables us to view and/or make changes without modifying the original repository. The following steps can be used to fork this repository:

 1. Log in to GitHub and locate the repository 

 2. At the top of the Repository (not top of page) just above the "Settings" Button on the menu, locate the "Fork" Button.

 3. Once clicked, you should now have a copy of the original repository in your own GitHub account!

# credits 
 * I used code institutes project 5 Boutique Ado E commerence tutorial to get me up and running with a template so i can then add new features to Create a fully functionaly website applcation. 
 * I wanna Thank Ben Kanvanagh for the guidance in this project , Helping me to test my boundiers. 
 * All photos used on throughout the site are used from www.pexels.com and www.upslash.com .
 * I used Django: The web framework for perfectionists with deadlines https://www.djangoproject.com. 
 *  I used flexbox to make the website more easier and to make it mote responsive i used a guide from csstrick.com to be able to implement this to suit my site. to create the about and donation page - flexbox tricks 
 *  I wanna Thank slack communtiy were i could easily search a problem that a previous student might have had Meaning i could fix this.
 *  I want to thank any tutor that had helped me along the way ith getting past errors in the terminal. 
  

