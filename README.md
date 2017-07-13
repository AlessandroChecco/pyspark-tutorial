# Pyspark tutorial
First, we will access the cluster master node and HDFS via SSH.
User accounts have been created for you to access the master.

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
More help: Each command has an attached manual explaining its usage and functionalities. It can be accessed by the command man, e.g., `` man ls ``

## Accessing spark in the cluster
After entering with ssh, simply use `` pyspark `` to run pyspark. The HDFS filesystem is accessible transparently (e.g. ``/user/li1dt/filename``).

## Submitting a batch job
Go to http://bigdata1.sheffield.ac.uk:8888/oozie/editor/workflow/new/ and submit your local py files (and any additional module), following the video here: https://github.com/AlessandroChecco/pyspark-tutorial/blob/master/create_action.mp4?raw=true. For fast prototyping (small dataset) you can run the batch on a single machine following the video here: https://github.com/AlessandroChecco/pyspark-tutorial/blob/master/create_local.mp4?raw=true

Alternatively use http://www.hypexr.org/linux_scp_help.php to copy your script on your home folder, and from your ssh shell run ``spark-submit --master local[*] filename.py`` for small datasets and ``spark-submit filename.py`` to run on the whole cluster.

## Visualize logs
To visualize the log of an action run with oozie, follow https://github.com/AlessandroChecco/pyspark-tutorial/blob/master/view_logs.mp4?raw=true

# Workflow for the student project
I suggest to prototype the script locally on your computer first on a small sample of the dataset. When the script is ready you can exectute it on the cluster.

## Downloading files from HDFS
Download the needed files (work only on few files locally) from http://bigdata1.sheffield.ac.uk:8888/filebrowser/

## Install pyspark locally

### On Mac
https://gist.github.com/ololobus/4c221a0891775eaa86b0
### On Windows
https://ysinjab.com/2015/03/28/hello-spark/
To use ipython with Spark try setting IPYTHON environment variable to 1 . For ipython notebook try setting IPYTHON_OPTS to :
IPYTHON_OPTS=”notebook”
### On Ubuntu
https://medium.com/@GalarnykMichael/install-spark-on-ubuntu-pyspark-231c45677de0

## Speeding up the prototyping workflow
use ``df = df.limit(1000)`` to test the scripts only the first 1000 lines of the file.

## Saving to file
```
# this saves to the workspace
out = df.toPandas() # it's a collect: careful with size
out.to_csv('out.csv')
# this saves to the hdfs
df.coalesce(1).write.format('com.databricks.spark.csv').save("/user/username/outout.csv") # use coalesce only if the final file can fit in one node!
```

## Matching a hashtag
Look up https://regex101.com/r/4HYf3E/3
use it with rlike command:
``` df2.filter(col('text').rlike("(?i)(#hi.*)")).show()```
