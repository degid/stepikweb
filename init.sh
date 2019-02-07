sudo unlink /etc/nginx/sites-enabled/default
sudo rm -rf /etc/nginx/site-enabled/default
sudo ln -sf /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/test.conf
sudo /etc/init.d/nginx restart

sudo rm -rf /etc/gunicorn.d/*
sudo sudo ln -sf /home/box/web/etc/hello.py   /etc/gunicorn.d/hello.py
sudo /etc/init.d/gunicorn restart
