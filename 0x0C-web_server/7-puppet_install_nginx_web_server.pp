# Installs Nginx Web Server

$redirection = "\tlocation /redirect_me {\n\t\treturn 301 https://www.youtube.com/watch?v=QH2-TGUlwu4\$request_uri;\n\t}"

exec {'install nginx':
  provider => shell,
  command  => 'sudo apt-get update; sudo apt-get -y install nginx; echo "Hello World!" | tee /var/www/html/index.html; sudo sed -i "s/\tserver_name _;/\tserver_name _;\n\tlocation /redirect_me {\n\t\treturn 301 https://www.youtube.com/watch?v=QH2-TGUlwu4\$request_uri;\n\t}/" /etc/nginx/sites-available/default; sudo service nginx restart'
}
