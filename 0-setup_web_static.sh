#!/usr/bin/env bash
# a script that set up my web server for the deployement of web_static
data="/data/"
shared="/data/web_static/shared/"
test_folder="/data/web_static/releases/test/"
test_file="/data/web_static/releases/test/index.html"
symbolic_link="/data/web_static/current"
CONFIGFILE="/etc/nginx/sites-available/default"
if ! command -v nginx >/dev/null 2>&1; then
	apt-get update
	apt-get -y install nginx
fi
if [ ! -d "$data" ]; then
	mkdir -p $test_folder $shared
	touch $test_file
	echo "Hello World" > $test_file
fi
if [ -L "$symbolic_link" ]; then
	rm $symbolic_link
else
	ln -s $test_folder $symbolic_link
fi
chown -R ubuntu:ubuntu /data/
sed -i "53i\ \n\tlocation /hbnb_static {\n\t\talias $symbolic_link;\n\t}\n" $CONFIGFILE
service nginx restart
