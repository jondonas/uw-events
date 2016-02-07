#uw-events

##Dependencies

###This application uses python 2.x

```
sudo apt-get install mysql-server python-mysqldb
sudo pip install Flask Flask-Mail itsdangerous requests
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
