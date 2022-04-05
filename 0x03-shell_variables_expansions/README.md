# WHAT EACH SCRIPT DOES?

## Basic Script

### 0-alias 
This script will create an alias called `ls` set to the command `rm *`. This particular alias changes the meaning of the `ls` command to mean `rm *` which means that whenever `ls` is called up, everything in the working directory will be permanently deleted. In order to run the script, type: 
<pre>
Chukwuemeka@Ubuntu~$ source ./0-alias
</pre>  
and press ENTER.
***NOTE:*** once the script is run, the meaning of `ls` will be changed throughout the current working directory. In order to revert back to the original meaning and use of `ls`, you need to unalias the `ls` command. You can do that with the following command: 
<pre>
Chukwuemeka@Ubuntu~$ unalias ls
</pre>  
press ENTER.

