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


let's see
don't use the ```mongod --auth --dbpath .```  and ```mongosh -u sirshendu -p 271828```
Instead use the normal ```sudo mongod --dbpath .``` and ```mongosh``` 
Remember to stop and restart the mongodb community and mysql services .
Incase the mongod --dbpath . doesn't work , use sudo.

The error can be this 

exam_approval_backend git:(main) ✗ mongod --dbpath .
{"t":{"$date":"2023-07-25T15:22:23.615+05:30"},"s":"I",  "c":"NETWORK",  "id":4915701, "ctx":"thread2","msg":"Initialized wire specification","attr":{"spec":{"incomingExternalClient":{"minWireVersion":0,"maxWireVersion":17},"incomingInternalClient":{"minWireVersion":0,"maxWireVersion":17},"outgoing":{"minWireVersion":6,"maxWireVersion":17},"isInternalClient":true}}}
{"t":{"$date":"2023-07-25T15:22:23.616+05:30"},"s":"I",  "c":"CONTROL",  "id":23285,   "ctx":"thread2","msg":"Automatically disabling TLS 1.0, to force-enable TLS 1.0 specify --sslDisabledProtocols 'none'"}
{"t":{"$date":"2023-07-25T15:22:23.616+05:30"},"s":"I",  "c":"NETWORK",  "id":4648602, "ctx":"thread2","msg":"Implicit TCP FastOpen in use."}
{"t":{"$date":"2023-07-25T15:22:23.617+05:30"},"s":"I",  "c":"REPL",     "id":5123008, "ctx":"thread2","msg":"Successfully registered PrimaryOnlyService","attr":{"service":"TenantMigrationDonorService","namespace":"config.tenantMigrationDonors"}}
{"t":{"$date":"2023-07-25T15:22:23.617+05:30"},"s":"I",  "c":"REPL",     "id":5123008, "ctx":"thread2","msg":"Successfully registered PrimaryOnlyService","attr":{"service":"TenantMigrationRecipientService","namespace":"config.tenantMigrationRecipients"}}
{"t":{"$date":"2023-07-25T15:22:23.617+05:30"},"s":"I",  "c":"REPL",     "id":5123008, "ctx":"thread2","msg":"Successfully registered PrimaryOnlyService","attr":{"service":"ShardSplitDonorService","namespace":"config.tenantSplitDonors"}}
{"t":{"$date":"2023-07-25T15:22:23.617+05:30"},"s":"I",  "c":"CONTROL",  "id":5945603, "ctx":"thread2","msg":"Multi threading initialized"}
{"t":{"$date":"2023-07-25T15:22:23.617+05:30"},"s":"I",  "c":"CONTROL",  "id":4615611, "ctx":"initandlisten","msg":"MongoDB starting","attr":{"pid":34654,"port":27017,"dbPath":".","architecture":"64-bit","host":"Sirshendus-MBP.Dlink"}}
{"t":{"$date":"2023-07-25T15:22:23.618+05:30"},"s":"I",  "c":"CONTROL",  "id":23403,   "ctx":"initandlisten","msg":"Build Info","attr":{"buildInfo":{"version":"6.0.6","gitVersion":"26b4851a412cc8b9b4a18cdb6cd0f9f642e06aa7","modules":[],"allocator":"system","environment":{"distarch":"x86_64","target_arch":"x86_64"}}}}
{"t":{"$date":"2023-07-25T15:22:23.618+05:30"},"s":"I",  "c":"CONTROL",  "id":51765,   "ctx":"initandlisten","msg":"Operating System","attr":{"os":{"name":"Mac OS X","version":"22.5.0"}}}
{"t":{"$date":"2023-07-25T15:22:23.618+05:30"},"s":"I",  "c":"CONTROL",  "id":21951,   "ctx":"initandlisten","msg":"Options set by command line","attr":{"options":{"storage":{"dbPath":"."}}}}
{"t":{"$date":"2023-07-25T15:22:23.618+05:30"},"s":"E",  "c":"NETWORK",  "id":23024,   "ctx":"initandlisten","msg":"Failed to unlink socket file","attr":{"path":"/tmp/mongodb-27017.sock","error":"Permission denied"}}
{"t":{"$date":"2023-07-25T15:22:23.618+05:30"},"s":"F",  "c":"ASSERT",   "id":23091,   "ctx":"initandlisten","msg":"Fatal assertion","attr":{"msgid":40486,"file":"src/mongo/transport/transport_layer_asio.cpp","line":1126}}
{"t":{"$date":"2023-07-25T15:22:23.618+05:30"},"s":"F",  "c":"ASSERT",   "id":23092,   "ctx":"initandlisten","msg":"\n\n***aborting after fassert() failure\n\n"}
➜  exam_approval_backend git:(main) ✗ rm /tmp/mongodb-27017.sock
override rwx------ root/wheel for /tmp/mongodb-27017.sock? y
rm: /tmp/mongodb-27017.sock: Permission denied
➜  exam_approval_backend git:(main) ✗ sudo rm /tmp/mongodb-27017.sock
Password:
➜  exam_approval_backend git:(main) ✗ sudo mongod --dbpath .
{"t":{"$date":"2023-07-25T15:23:42.231+05:30"},"s":"I",  "c":"NETWORK",  "id":4915701, "ctx":"-","msg":"Initialized wire specification","attr":{"spec":{"incomingExternalClient":{"minWireVersion":0,"maxWireVersion":17},"incomingInternalClient":{"minWireVersion":0,"maxWireVersion":17},"outgoing":{"minWireVersion":6,"maxWireVersion":17},"isInternalClient":true}}}
{"t":{"$date":"2023-07-25T15:23:42.232+05:30"},"s":"I",  "c":"CONT


Once you do theese 2, it generally works. ChatGPT was actually able to solve this problem instantly, so take help there. 
```
➜  exam_approval_backend git:(main) ✗ rm /tmp/mongodb-27017.sock
override rwx------ root/wheel for /tmp/mongodb-27017.sock? y
rm: /tmp/mongodb-27017.sock: Permission denied
➜  exam_approval_backend git:(main) ✗ sudo rm /tmp/mongodb-27017.sock
Password:

```



```
 exam_approval_backend git:(main) ✗ brew services start mysql
==> Successfully started `mysql` (label: homebrew.mxcl.mysql)
➜  exam_approval_backend git:(main) ✗ code .
➜  exam_approval_backend git:(main) ✗ brew services start mongodb-community
Bootstrap failed: 5: Input/output error
Try re-running the command as root for richer errors.
Error: Failure while executing; `/bin/launchctl bootstrap gui/501 /Users/sirshendu/Library/LaunchAgents/homebrew.mxcl.mongodb-community.plist` exited with 5.
➜  exam_approval_backend git:(main) ✗ sudo brew services start mongodb-community
Password:
Warning: Taking root:admin ownership of some mongodb-community paths:
  /usr/local/Cellar/mongodb-community/6.0.6/bin
  /usr/local/Cellar/mongodb-community/6.0.6/bin/mongod
  /usr/local/opt/mongodb-community
  /usr/local/opt/mongodb-community/bin
  /usr/local/var/homebrew/linked/mongodb-community
This will require manual removal of these paths using `sudo rm` on
brew upgrade/reinstall/uninstall.
Warning: mongodb-community must be run as non-root to start at user login!
==> Successfully started `mongodb-community` (label: homebrew.mxcl.mongod
➜  exam_approval_backend git:(main) ✗ sudo brew services stop mongodb-community
Password:
Stopping `mongodb-community`... (might take a while)
==> Successfully stopped `mongodb-community` (label: homebrew.mxcl.mongod
➜  exam_approval_backend git:(main) ✗ cd ..
➜  exam-blockchains touch api_models_details.txt
➜  exam-blockchains code api_models_details.txt
➜  exam-blockchains cd exam_approval_backend
➜  exam_approval_backend git:(main) ✗ code .
➜  exam_approval_backend git:(main) ✗
➜  exam_approval_backend git:(main) ✗ sudo brew services stop mysql
Password:
Error: Service `mysql` is started as `root`. Try:
  brew services stop mysql
➜  exam_approval_backend git:(main) ✗ brew services stop mysql
Stopping `mysql`... (might take a while)
==> Successfully stopped `mysql` (label: homebrew.mxcl.mysql)
```