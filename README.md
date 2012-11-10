Singly Python Django Skeleton
=============================
This is a skeleton of an django project that implements the [Singly API](https://singly.com) for authentication and data access. Feel free to use it however you want to start your project or simply take some ideas from.

The code that authenticates services, manages the Singly access_token, and fetches the available profiles can be found in the /singly webapp. I have used standard Django user authentication to persist sessions and a UserProfile to store the access_token for that user and the available profiles on Singly supported services. This means that a database is required. By default, we use SQLite, but this can be changed in settings.py. 


Getting Started
---------------
Enter the directory and install the required python packages with pip (django, request):

    cd python_django_skeleton
    pip install -r requirements.py

Register a new app on https://singly.com/apps. If you are testing on your local machine, the default Callback and App urls are correct.

Edit the file /python_django_skeleton/webapp/settings.py to include the SINGLY_CLIENT_ID and SINGLY_CLIENT_SECRET that you got in the previous step.

NOTE: (use local_settings.py for this)

Set up the database. In the root folder of the app, execute

    python manage.py syncdb

As prompted, you may set up an superuser if you plan on using the Django admin tools at some point.

Start the server

    python manage.py runserver
