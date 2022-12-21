# Python Web Framework Project @ SoftUni

This Project was created for the final exam of SoftUni Python Web Framework course.
It contains one Django web application.

The Web Application is to serve users, who play the game Counter Strike GO and buy/exchange weapon skins, agents and containers in the game.

The idea behind the web project is to make a Social Platform for the users to share their skins and experience about them.

The Application has Login/Register and Logout functionality.

Every Logged-in user can upload a name, picture, description etc. of his skins and share them with the community.

For the users who want to share their experience with the others, is made a "Share Experience" page where every user can post a comment with his opinion and experience about the skins.

The web application uses PostgreSQL DB. All Templates are made with Bootstrap.
The application can send emails, working with AWS SEService. 

The operation to send an email is async-operation using Celery and Redis.

You need to install following packages to run the project:

 - Django Bootstrap
 - Pillow
 - Django Cleanup
 - Psycopg 2
 - Boto 3
 - Celery
 - Redis
 - Django REST Framework

Please make sure to install requirements.txt before running the project.

Please consider that the project is NOT for commercial use, and only for educational purpose.
Many features haven't been tested and are not for production.

For questions about the project please feel free to contact me.