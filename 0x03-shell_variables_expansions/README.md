# WHAT EACH SCRIPT DOES?

## Basic Script

### 0-alias 
This script will create an alias called `ls` set to the command `rm *`. This particular alias changes the meaning of the `ls` command to mean `rm *` which means that whenever `ls` is called up, everything in the working directory will be permanently deleted. In order to run the script, type: 
<pre>
Chukwuemeka@Ubuntu~$ source ./0-alias
</pre>  
and press ENTER.

**NOTE:** once the script is run, the meaning of `ls` will be changed throughout the current working directory. In order to revert back to the original meaning and use of `ls`, you need to unalias the `ls` command. You can do that with the following command: 
<pre>
Chukwuemeka@Ubuntu~$ unalias ls
</pre>  
press ENTER.

### 1-hello_you
This script when executed, will print the message; `hello {Current user's name}` to the terminal followed by a newline. In order to use this script, run it in the terminal by typing: 
<pre>
Chukwuemeka@Ubuntu~$ ./1-hello_you
</pre>  
press ENTER

### 2-path
This script when executed, will add the directory path `/action` as the last directory path of the `$PATH` variable. In order to run the script, open up a terminal and type:
<pre>
Chukwuemeka@Ubuntu~$ source ./2-path
</pre>  
press ENTER.


