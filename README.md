# Pyspark tutorial
First, we will access the cluster master node and HDFS via SSH.
User accounts have been created for you to access the master. The username is your university username (e.g., li1gd) and your temporary password can be found here: https://docs.google.com/a/sheffield.ac.uk/spreadsheets/d/1kqx9CFG6u7mFGAna5E8Z- NUaFczaZSiFIl3RTsRwppM/edit?usp=sharing

To use this account, you will need to install PuTTy from the Software Center.
Then create a new SSH connection to the host bigdata1.sheffield.ac.uk using your username and password. After you have changed the password you will need to connect again using your new password.
Basic SSH commands
```
pwd - tells you your current location in the local filesystem, e.g., /home/li1gd
mkdir - allows you to create a new directory, e.g., mkdir myfolder
cd – allows you to change your current location to another directory e.g., cd myfolder ls – lists the content of the current folder
cp – copies files from a place to another, e.g., cp /home/li1gd/filename /home/li1gd/myfolder/filename
mv – moves files from a place to another, e.g., mv /home/li1gd/filename /home/li1gd/myfolder/filename
unzip – decompresses zip files, e.g., unzip file.zip
df –h – shows you the local disk usage
wget – downloads data from a web URL, e.g., wget http://bbc.com /home/li1gd
```

and much more. See, e.g.:
https://www.hostinger.com/tutorials/ssh/basic-ssh-commands
More help: Each command has an attached manual explaining its usage and functionalities. It can be accessed by the command man, e.g., man ls
