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

