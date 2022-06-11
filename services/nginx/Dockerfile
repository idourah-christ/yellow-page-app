FROM nginx:alpine 

# remove default ngnix conf from /etc
RUN rm /etc/nginx/conf.d/default.conf

# set new conf file
COPY nginx.conf /etc/nginx/conf.d