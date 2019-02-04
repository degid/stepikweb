#sudo unlink /etc/nginx/sites-enabled/default
sudo rm -rf /etc/nginx/site-enabled/default
sudo ln -sf /home/nyan/web/etc/nginx.conf /etc/nginx/sites-enabled/test.conf
sudo /etc/init.d/nginx restart
