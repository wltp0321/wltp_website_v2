sudo /home/odroid/wltp_website_v2/venv/bin/hypercorn config.asgi:application --bind 127.0.0.1:8000 --certfile django.crt --keyfile django.key
