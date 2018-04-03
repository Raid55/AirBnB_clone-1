#!/usr/bin/env bash
# sets up the static server and all of its stuff and yea

# installing the thing
sudo apt-get -y update
sudo apt-get -y install nginx

# creating the dirs and folders
mkdir -p /data
mkdir -p /data/web_static
mkdir -p /data/web_static/shared
mkdir -p /data/web_static/releases
mkdir -p /data/web_static/releases/test

# creating the dummy html
echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html

# creating a link
ln -sf /data/web_static/releases/test/ /data/web_static/current

# giving custody
chown -hR ubuntu:ubuntu /data

sudo sed -i "38i location /hbnb_static {\n\t\talias /data/web_static/current;\n\t}\n" /etc/nginx/sites-available/default

# nginx restart
sudo service nginx restart
