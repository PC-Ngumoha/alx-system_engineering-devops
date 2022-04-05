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
press ENTER

### 3-paths
This script will on execution, count the number of directories in the `$PATH` environment variable and print the result to the terminal. In order to use it, open up a terminal and type:
<pre>
Chukwuemeka@Ubuntu~$ . ./3-paths
</pre>  
press ENTER

### 4-global_variables
This script will on execution, list out all the environment variables (global variables) that have been defined for this particular user. In order to use it, open a terminal and type: 
<pre>
Chukwuemeka@Ubuntu~$ ./4-global_variables
</pre>  
press ENTER

### 5-local_variables
This script will on execution, list out all the global variables, local variables and functions that have been defined for this particular user. In order to use it, open up a terminal and type: 
<pre>
Chukwuemeka@Ubuntu~$ ./5-local_variables
</pre>  
press ENTER

### 6-create_local_variable
This script will on execution, create a local variable called `$BEST` set to the value `School`. In order to run the script, type in the following code into the terminal: 
<pre>
Chukwuemeka@Ubuntu~$ source ./6-create_local_variable
</pre>  
press ENTER

### 7-create_global_variable
This script will on execution, create a global variable called `BEST` set to the value `School`. To run this script, type: 
<pre>
Chukwuemeka@Ubuntu~$ source ./7-create_global_variable
</pre>  
press ENTER

In order to verify that what was created was actually a global variable as opposed to a local variable, open up the terminal and type the following:
<pre>
Chukwuemeka@Ubuntu~$ printenv
...
BEST="School"
...
</pre>  

### 8-true_knowledge
This script will on execution, display the result of summing up the value of the global variable `TRUEKNOWLEDGE` and `128` to the terminal. For example: 
<pre>
Chukwuemeka@Ubuntu~$ export TRUEKNOWLEDGE=62
Chukwuemeka@Ubuntu~$ ./8-true_knowledge
190
</pre>

### 9-divide_and_rule
This script will on execution, display the result of dividing the value in the global variable `POWER` by the value in the global variable `DIVIDE` on the terminal. For example: 
<pre>
Chukwuemeka@Ubuntu~$ export POWER=128
Chukwuemeka@Ubuntu~$ export DIVIDE=2
Chukwuemeka@Ubuntu~$ ./9-divide_and_rule
64
</pre>  

### 10-love_exponent_breath
This script will on execution, display the result of raising the value in the global variable `BREATH` to the value in the global variable `LOVE` on the terminal. For example: 
<pre>
Chukwuemeka@Ubuntu~$ export BREATH=4
Chukwuemeka@Ubuntu~$ export LOVE=3
Chukwuemeka@Ubuntu~$ ./10-love_exponent_breath
64
</pre>  


### 11-binary_to_decimal
This script will on execution, convert the binary number stored in the global variable `BINARY` to decimal form and display the result on the terminal. For example:
<pre>
Chukwuemeka@Ubuntu~$ export BINARY=101001110010
Chukwuemeka@Ubuntu~$ ./11-binary_to_decimal
2674
</pre>
  


























