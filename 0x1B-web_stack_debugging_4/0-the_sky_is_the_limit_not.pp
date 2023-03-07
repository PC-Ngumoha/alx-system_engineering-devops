# Solution To Webstack Debugging #4 project

exec{'Fix file read limit on System level':
  provider => shell,
  command  => "sed -i 's/ULIMIT=\"-n 15\"/ULIMIT=\"-n 65535\"/g' /etc/default/nginx"
}

exec{'Increase file read limit on Nginx level':
  provider => shell,
  command  => "sed -i '3 a worker_rlimit_nofile 30000;' /etc/nginx/nginx.conf"
}

exec{'Increase active work-connections':
  provider => shell,
  command  => 'sed -i "s/\tworker_connections 768;/\tworker_connections 65535;/g" /etc/nginx/nginx.conf'
}

exec{'Restart Nginx server':
  provider => shell,
  command  => 'service nginx restart'
}
