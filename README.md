made the serialisers correct
mongod
mongosh
correction: use mongosh -u sirshendu -p 271828
brew services start mongodb-community
mysql -u root -p(need to use "mysql.server start" before mysql -u root -p. Because mysql.server will start the mysql server and then the mysql -u root -p can access it.)
mysql.server start
brew services restart mysql
correct the mongod line: mongod --dbpath .
correction 2: mongod --auth --dbpath .
python manage.py runserver
python manage.py migrate
brew services stop mongodb-community
sudo brew services start mongodb-community
brew services stop mysql
alternatively mysql can be stopped using by first logging inside the mysql server with mysql -u username -p
mysql -u root -p
mysql.server stop


