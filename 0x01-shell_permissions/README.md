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

So, in this case, `godzilla` , `spiderman` and `james_bond` are all groups that `Chukwuemeka` belongs to.




