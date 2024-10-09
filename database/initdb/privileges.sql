# TODO: Make compatible for non-dev envs; this is just for local development atm
GRANT ALL PRIVILEGES ON *.* TO 'movie_manager_user'@'%' IDENTIFIED BY pass1234;
GRANT ALL PRIVILEGES ON *.* TO 'movie_manager_user'@'localhost' IDENTIFIED BY pass1234;
GRANT ALL PRIVILEGES ON *.* TO 'movie_manager_user'@'192.168.0.0/255.255.0.0' IDENTIFIED BY pass1234;
GRANT ALL PRIVILEGES ON *.* TO 'movie_manager_user'@'10.0.0.0/255.0.0.0' IDENTIFIED BY pass1234;
FLUSH PRIVILEGES;
