# Stream_dl dockerfile
# github link: https://github.com/dh4rm4/stream_dl

# Base Image
FROM debian:jessie
ARG secret_key=[TO DEFINE]

# Softwares dependancies
RUN apt-get update &&
    apt-get install python3.5 \
    	    	    pip3 \
    	    	    gunicorn \
		    nginx

# Set Flask Env Var
ENV FLASK_SECRET_KEY=$secret_key
ENV FLASK_APP=stream_dl.py

# Create Working Dir
RUN mkdir -p /webapps/stream_dl

# Add dependancies and install them
ADD requirements.txt /webapps/stream_dl/
WORKDIR /webapps/stream_dl
RUN pip3 install -r requirements.txt

#Setup Nginx
ADD ./nginx/stream_dl /etc/nginx/sites-available/
RUN ln -s /etc/nginx/sites-available/stream_dl /etc/nginx/sites-enabled/stream_dl &&
	service nginx restart


# Add source code
ADD . /webapps/stream_dl/


# Manage outside acces
EXPOSE 3000
VOLUME /app/log/stream_dl/

# Launch the app
CMD gunicorn --bind 0.0.0.0:5000 stream_dl:app --timeout 3500
