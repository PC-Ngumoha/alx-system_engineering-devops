# Fix PHP file typo mistake in a LAMP wordpress setup

exec {'correct typo':
  provider => shell,
  command  => "sed -i 's/phpp/php/' /var/www/html/wp-settings.php"
}
