FROM abiosoft/caddy:0.10.6

COPY ./Caddyfile /etc/Caddyfile
COPY ./320-django/staticfiles /static