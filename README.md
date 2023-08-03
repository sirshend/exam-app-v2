In each of shells, first do
cd .. (go to the previous level ```exam_blockchains``` for activating the virtual env)
source v1/bin/activate
cd exam_approval_backend
Once all work is done, deactivate the virtual-env with ```deactivate```


sudo mongod --dbpath .
mongosh
sudo brew services start mongodb-community
While stopping:
exit from mongosh shell by pressing Ctrl+C twice
Ctrl+C from mongod.
sudo brew services stop mongodb-community

mysql.server start
sudo brew services start mysql
mysql -u root -p (and not ```mysql -u sirshendu -p 271828``` or any combination of sirshendu and/or 271828, like ```mysql -u sirshendu -p```  or ```mysql -u root -271828```)
While stopping:
```exit``` from the shell after ```mysql -u root -p```
sudo brew services stop mysql
mysql.server stop

in exam_approval_backend with virtualenv on, use
python manage.py migrate
python manage.py runserver
