# WHAT EACH SCRIPT DOES

## Basic Scripts

### 0-iam_betty 
This script will on invocation, switch the current user to `betty` (If such a user exists). If there is no user existing named `betty`, the terminal indicates that the user does not exist: 

<p align="center"><pre>
su: user betty does not exist.
</pre></p>

In order to run the script, open up a terminal and type:

<p align="center"><pre>
~$ ./0-iam_betty
</pre></p>

press ENTER

### 1-who_am_i
This script will on invocation, print the valid username of the current user to the screen. For example: 
Running a code like :

<p align="center"><pre>
Chukwuemeka@Ubuntu~$ ./1-who_am_i
</pre></p>

will produce the following output on the terminal: 

<p align="center"><pre>
Chukwuemeka
</pre></p>

So, in this case, `Chukwuemeka` is the valid username of the current user using the system.

### 2-groups
This script will on invocation, print the names of all the groups that the current user belongs to. So If the user belongs to the groups; `godzilla`, `spiderman`, `james_bond` and he enters the code: 

<p align="center"><pre>
Chukwuemeka@Ubuntu~$ ./2-groups
</pre></p>

and press ENTER, the following will be displayed on the terminal:

<p align="center"><pre>
godzilla spiderman james_bond
</pre></p>

So, in this case, `godzilla` , `spiderman` and `james_bond` are all groups that `Chukwuemeka` belongs to

### 3-new_owner 
This script will change the owner of the file; `hello` from `root` to `betty`. In order to run this script, open up a terminal and enter: 

<p align="center"><pre>
~$ ./3-new_owner
</pre></p>

Then press ENTER. If the user exists, the change happens quietly. If not, the terminal displays a message like :

<p align="center"><pre>
chown: no such user called 'betty'
</pre></p>


### 4-empty
This script will create an empty file called `hello` in the current working directory. In order to run the script, open up a terminal and type: 

<p align="center"><pre>
~$ ./4-empty
</pre></p>

press ENTER


### 5-execute
This script when executed, will add execute permissions to the owner of the file `hello`. For example:

<p align="center"><pre>
Chukwuemeka@Ubuntu~$ ls -l
</pre></p>

displays: 

<p align="center"><pre>
-rw-r--r-- 1 Chukwuemeka Chukwuemeka 28 Sep 20 14:26 hello
</pre></p>

In order to add execute permissions to this `hello` file, enter the following code into the terminal 


<p align="center"><pre>
Chukwuemeka@Ubuntu~$ ./5-execute
</pre></p>

This will make the `hello` file executable. In order to confirm this , type :


<p align="center"><pre>
Chukwuemeka@Ubuntu~$ ls -l
</pre></p>

This will produce the following line: 

<p align="center"><pre>
-rwxr--r-- 1 Chukwuemeka Chukwuemeka 28 Sep 20 14:26 hello
</pre></p>

Also, if the `hello` file does not exist, the terminal will display the following message: 


<p align="center"><pre>
chmod: Cannot access 'hello': No such file or directory.
</pre></p>


### 6-multiple_permissions
This script when executed, will add execute permissions to the owner and group owners, and read permission to all other users to the file `hello`. For example:

Type: 

<p align="center"><pre>
Chukwuemeka@Ubuntu~$ ls -l
</pre></p>

You will get: 

<p align="center"><pre>
-r--r--r-- 1 Chukwuemeka Chukwuemeka 28 Sep 20 14:26 hello
</pre></p>

In order to add execute permissions to the owner and group owners of the `hello` file in this directory, open up a terminal and type:


<p align="center"><pre>
Chukwuemeka@Ubuntu~$ ./6-multiple_permissions
</pre></p>

press ENTER. In order to verify that the permissions have been added to the file, type: 

<p align="center"><pre>
Chukwuemeka@Ubuntu~$ ls -l
</pre></p>

And you will get: 

<p align="center"><pre>
-rwxr-xr-- 1 Chukwuemeka Chukwuemeka 28 Sep 20 14:26 hello
</pre></p>

Also, if the `hello` file does not exist, the terminal will display the following message: 

<p align="center"><pre>
chmod: Cannot access 'hello': No such file or directory.
</pre></p>



### 7-everybody
This script when executed, will add execution permissions to the owner, the group owner and the other users, to the file `hello`. For example: 
Type: 

<p align="center"><pre>
Chukwuemeka@Ubuntu~$ ls -l
</pre></p>

You will get: 


<p align="center"><pre>
-r--r--r-- 1 Chukwuemeka Chukwuemeka 28 Sep 20 14:35 hello
</pre></p>

In order to add execution permissions to the owner, group owner and the other users to the file `hello` in the current working directory. Type: 


<p align="center"><pre>
Chukwuemeka@Ubuntu~$ ./7-everybody
</pre></p>

press ENTER. To confirm, type: 


<p align="center"><pre>
Chukwuemeka@Ubuntu~$ ls -l
</pre></p>

You should get: 

<p align="center"><pre>
-r-xr-xr-x 1 Chukwuemeka Chukwuemeka 28 Sep 20 14:35 hello
</pre></p>


Also, if the `hello` file does not exist, the terminal will display the following message: 

<p align="center"><pre>
chmod: Cannot access 'hello': No such file or directory.
</pre></p>


### 8-James_Bond
This script will on execution set the permissions to the file `hello` such that the `owner` and `group` will have no permission at all while the `other` users get all the permissions. For example: If we have 


<p align="center"><pre>
Chukwuemeka@Ubuntu~$ ls -l
</pre></p>

and should get: 

<p align="center"><pre>
-r-xr-xr-x 1 Chukwuemeka Chukwuemeka 28 Sep 20 14:35 hello
</pre></p>

When you type: 

<p align="center"><pre>
Chukwuemeka@Ubuntu~$ ./8-James_Bond
</pre></p>

and press ENTER, you should be able to type the following into the terminal: 

<p align="center"><pre>
Chukwuemeka@Ubuntu~$ ls -l
</pre></p>

 and get: 

<p align="center"><pre>
-------rwx 1 Chukwuemeka Chukwuemeka 28 Sep 20 14:40 hello
</pre></p>


Also, if the `hello` file does not exist, the terminal will display the following message: 

<p align="center"><pre>
chmod: Cannot access 'hello': No such file or directory.
</pre></p>


### 9-John_Doe 
This script on execution, will set the mode of the file `hello` to :

<p align="center"><pre>
-rwxr-x-wx 1 Chukwuemeka Chukwuemeka 28 Sep 20 14:40 hello
</pre></p>

Enter the following into the terminal:

<p align="center"><pre>
Chukwuemeka@Ubuntu~$ ./9-John_Doe
</pre></p>

press ENTER


### 10-mirror_permissions
This script will set the permissions of the file `hello` to be the same as those of the file `olleh` in the same working directory. For example: 
If you could type: 


<p align="center"><pre>
Chukwuemeka@Ubuntu~$ ls -l
</pre></p>

and get the following: 


<p align="center"><pre>

-------rwx 1 Chukwuemeka Chukwuemeka 28 Sep 20 14:40 hello
-rw--w-rwx 1 Chukwuemeka Chukwuemeka 28 Sep 20 14:40 olleh
</pre></p>

When you enter the following into the terminal: 


<p align="center"><pre>
Chukwuemeka@Ubuntu~$ ./10-mirror_permissions
</pre></p>

and press ENTER, you would get: 


<p align="center"><pre>
Chukwuemeka@Ubuntu~$ ls -l
-rw--w-rwx 1 Chukwuemeka Chukwuemeka 28 Sep 20 14:40 hello
-rw--w-rwx 1 Chukwuemeka Chukwuemeka 28 Sep 20 14:40 olleh
</pre></p>


### 11-directories_permissions
This script when executed, will add execute permission to the owner, group and other of the subdirectories in the current directory. Regular files will be unaffected. For example: 
If we have : 

<p align="center"><pre>
Chukwuemeka@Ubuntu~$ ls -l
drw--w-rw- 1 Chukwuemeka Chukwuemeka 28 Sep 20 14:40 dir0
-rw--w-rwx 1 Chukwuemeka Chukwuemeka 28 Sep 20 14:40 olleh
</pre></p>

Once we run the command: 


<p align="center"><pre>
Chukwuemeka@Ubuntu~$ ./11-directories_permissions
</pre></p>

We get: 


<p align="center"><pre>
Chukwuemeka@Ubuntu~$ ls -l
drwx-wxrwx 1 Chukwuemeka Chukwuemeka 28 Sep 20 14:40 dir0
-rw--w-rwx 1 Chukwuemeka Chukwuemeka 28 Sep 20 14:40 olleh
</pre></p>

You'll notice that the `olleh` file wasn't affected by the script


### 12-directory_permissions
This script will create a directory `my_dir` with permissions set to 751 in the current working directory. In order to use it, open up a terminal and enter: 


<p align="center"><pre>
Chukwuemeka@Ubuntu~$ ./12-directory_permissions
</pre></p>

and press ENTER


### 13-change_group
This script will on execution, change the group owner of a file `hello` from the default group owner to the new group `school`. In order to use it, open up a terminal and type: 


<p align="center"><pre>
Chukwuemeka@Ubuntu~$ ./13-change_group
</pre></p>

then press ENTER.

Also, if the group does not exist, then a warning like the one below is displayed on the terminal: 

<p align="center"><pre>
chgrp: Invalid group 'school'
</pre></p>













