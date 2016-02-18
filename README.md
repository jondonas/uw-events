#uw-events

##Dependencies

###This application uses python 2.x

```
sudo apt-get install mysql-server python-mysqldb
sudo pip install Flask Flask-Mail itsdangerous requests feedparser
```

###Configuration for MySQL DB:

```
CREATE DATABASE uwevents;

USE uwevents;

CREATE TABLE users (
 id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
 name VARCHAR(100),
 email VARCHAR(100),
 confirmed BOOLEAN NOT NULL DEFAULT 0);
```

NGINX is now implented as a reverse proxy to uWSGI. uWSGI serves instance of the Flask application. Supervisor ensures that uWSGI is always running. This will make the website significantly faster and more reliable.
