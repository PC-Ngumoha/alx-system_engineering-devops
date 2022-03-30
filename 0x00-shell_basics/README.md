# WHAT EACH SCRIPT DOES

## Basic Scripts

### 0-current_working_directory 
This script prints out the absolute path to the current working directory to the terminal on invocation by the user of the program. In order to use the script just open a terminal and type in the following command:

<p align="center">
<pre>
~$ ./0-current_working_directory
</pre>	
</p>



and then press ENTER. This should display the absolute path to the working directory on the terminal..

### 1-listit 
This script, on invocation, lists out the names of all the files and sub-directories in the working directory. In order to use the script, just open a terminal (Bash) and type the following command: 

<p align="center">
<pre>
~$ ./1-listit
</pre>	
</p>



press ENTER. The should then proceed to list out the contents (files and sub-directories) in the working directory.

### 2-bring_me_home 
This script, on invocation, changes the working directory from the current working directory to the Home directory of the user. To use it, just open a terminal and type: 


<p align="center">
<pre>
~$ source ./2-bring_me_home
</pre>	
</p>


press ENTER. and then type :


<p align="center">
<pre>
~$ pwd
</pre>	
</p>



To confirm that the current directory is indeed the user's home directory. If you are in the user's home directory, it should display something similar to the following: 


<p align="center">
<pre>
 /home/user  
</pre>	
</p>




### 3-listfiles
This script will, on invocation, list out all the files and/or sub-directories in the working directory in full-details (i.e read-write permissions, owner details, group details, size, date and time of creation/update, name of file) in the terminal. In order to use it, open up a terminal and type:


<p align="center">
<pre>
 ~$ ./3-listfiles  
</pre>	
</p>



press ENTER.


### 4-listmorefiles
This script will, on invocation, list out the full details (i.e read-write permissions, owner details, group details, size, date and time of creation/update, name of file) of all the files and/or sub-directories in the working directory, including the directories and/or files whose name begin with a "." (which are usually hidden). In order to use it, open up a terminal and type: 


<p align="center">
<pre>
 ~$ ./4-listmorefiles  
</pre>	
</p>


press ENTER.


### 5-listfilesdigitonly
This script will, on invocation, carry out the same operation ast the "4-listmorefiles" script above. The only difference being that it would display the "group" and "owner" details in a numeric format. In order to use it, open up a terminal and type:

<p align="center">
<pre>
 ~$ ./5-listfilesdigitonly  
</pre>	
</p>



press ENTER

### 6-firstdirectory
This script will, on invocation create a new directory named "my_first_directory" in the /tmp/ directory. In order to use it, open up a terminal and type:


<p align="center">
<pre>
 ~$ ./6-firstdirectory  
</pre>	
</p>



press ENTER


### 7-movethatfile
This script will, on invocation, move the file "betty" (If it does not exist, it will create it)in the /tmp/ directory into the "my_first_directory" sub-directory in the same /tmp/ directory. In order to use it, open up a terminal and type:

<p align="center">
<pre>
 ~$ ./7-movethatfile  
</pre>	
</p>


press ENTER


### 8-firstdelete
This script will, on invocation, delete the file "betty" (Which has already been created by the previous script) in the /tmp/ directory from the "my_first_directory" subdirectory in the same /tmp/ directory. In order to use it, open a terminal and type:

<p align="center">
<pre>
 ~$ ./8-firstdelete 
</pre>	
</p>


press ENTER


### 9-firstdirdeletion
This script will, on invocation, delete the "my_first_directory" subdirectory located in the /tmp/ directory. In order to use it, open a terminal and type:

<p align="center">
<pre>
 ~$ ./9-firstdirdeletion 
</pre>	
</p>


press ENTER



### 10-back
This script will, on invocation, return to the previous working directory.In order to use it, open a terminal and type:

<p align="center">
<pre>
 ~$ source ./10-back 
</pre>	
</p>


press ENTER.
**NOTE:** This particular script does not work as well as the *cd -* builtin command. It can only go back to the previous pwd and cannot come back to the one you were previously at before calling it.



### 11-lists
This script will, on invocation, print to the terminal, the content (files and subdirectories), including the hidden content (those whose names are prefixed with "."), of the current working directory, the parent of the working directory and the /boot directory, in that exact order. In order to use it, open up a terminal and type:

<p align="center">
<pre>
 ~$ ./11-lists 
</pre>	
</p>


press ENTER

### 12-file_type
The script will, on invocation, determine the type of file that the file "iamafile" is and displays a message to the terminal with that information. In order to use it, open up a terminal and type:

<p align="center">
<pre>
 ~$ ./12-file_type 
</pre>	
</p>


press ENTER


### 13-symbolic-link
This script will, on invocation, create a symbolic link `__ls__` which will link to the file **/bin/ls**. In order to use it, open up a terminal and type:
 
<p align="center">
<pre>
 ~$ ./13-symbolic_link 
</pre>	
</p>


press ENTER

### 14-copy_link 
This script will, on invocation, copy all the HTML files in the working directory to overwrite the contents of the html files in the parent of the working directory, but only when the files did not exist in the parent directory or when the content of the copied files are more recent than those in the parent directory. In order to use it, open up a terminal and type:


<p align="center">
<pre>
 ~$ ./14-copy_html 
</pre>	
</p>

press ENTER



## Advanced Scripts

### 100-lets_move
This script will, on invocation, move all the files that start with an uppercase letter to the directory `/tmp/u`. In order to use it, open up a terminal and type: 


<p align="center">
<pre>
 ~$ ./100-lets_move 
</pre>	
</p>




















. 
