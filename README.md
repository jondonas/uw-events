#uw-events

Create by Jonathan Donas, Ryan Newman, Neo Chen, Rolina Wu, and Joe Wang

##Flask and MySQL

###This application uses python 2.x

```
sudo apt-get install mysql-server python-mysqldb php5-fpm
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

##NGINX, uWGSI, Supervisor
NGINX is now implented as a reverse proxy to uWSGI. uWSGI serves instance of the Flask application. Supervisor ensures that uWSGI is always running. This will make the website significantly faster and more reliable.

```
sudo apt-get install nginx python-dev supervisor
sudo pip install uwsgi
```

###Configuration:

####/etc/nginx/nginx.conf

Add in http{} block

```
server {

        # Running port
        listen 80;
        server_name www.uwevents.gq;
        root /home/bogo/uw-events/code/static/;

        # Settings to by-pass for static files
        location  /static  {
            alias /home/bogo/uw-events/code/static/;
        }

        location  /~  {
            include            uwsgi_params;
            uwsgi_pass         127.0.0.1:8080;
        }

        # Proxying connections to application servers
        location / {
            index index.php index.html index.htm;
        }

        location ~ \.php$ {
            fastcgi_split_path_info ^(.+\.php)(/.+)$;
            fastcgi_pass unix:/var/run/php5-fpm.sock;
            fastcgi_index index.php;
            include fastcgi_params;
        }
    }
```

####/etc/supervisor/supervisord.conf

Add to bottom of file

```
[program:uw-events]
command=sudo uwsgi --socket 127.0.0.1:8080 --enable-threads --single-interpreter --vacuum --master --chdir /home/bogo/uw-events/code/ --processes 2 -w wsgi:app
stopsignal=QUIT
autostart=true
autorestart=true
startsecs=2
```

####/etc/init/supervisor.conf

Create this file to start supervisor on reboot

```
description     "supervisord"
start on runlevel [2345]
stop on runlevel [!2345]
respawn
respawn limit 10 5
umask 022
env SSH_SIGSTOP=1
expect stop
console none
pre-start script
        test -x /usr/bin/supervisord || { stop; exit 0; }
end script
exec /usr/bin/supervisord
```
