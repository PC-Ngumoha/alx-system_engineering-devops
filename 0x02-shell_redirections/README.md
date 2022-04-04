# WHAT EACH SCRIPT DOES

## Basic Scripts

### 0-hello_world
This script will on execution print "Hello, World" followed by a newline to the standard output (In this case, the standard output is the terminal display). In order to use it, open up the terminal and type: 
<pre>
Chukwuemeka@Ubuntu~$ ./0-hello_world
</pre>

press ENTER.

### 1-confused_smiley
This script will on execution print `"(Ôo)'` followed by a newline to the terminal. In order to use it, open up a terminal and type: 
<pre>
Chukwuemeka@Ubuntu~$ ./1-confused_smiley
</pre>

press ENTER

### 2-hellofile
This script will on execution print out all the contents of the local `/etc/passwd` file to the terminal. In order to use it, open up a terminal and type: 
<pre>
Chukwuemeka@Ubuntu~$ ./2-hellofile
</pre>
press ENTER

### 3-twofiles
This script will on execution print out all the contents of the local `/etc/passwd` and `/etc/hosts` files to the terminal. In order to use it, open up a terminal and type: 
<pre>
Chukwuemeka@Ubuntu~$ ./3-twofiles
</pre>

press ENTER

### 4-lastlines
This script will on execution print out only the last `10` lines of the local `/etc/passwd` file to the terminal. In order to use it, open up a terminal and type: 
<pre>
Chukwuemeka@Ubuntu~$ ./4-lastlines
</pre>
press ENTER

### 5-firstlines
This script will on execution print out only the first 10 lines of the local `/etc/passwd` file to the terminal. In order to use it, open a terminal and type: 
<pre>
Chukwuemeka@Ubuntu~$ ./5-firstlines
</pre>
press ENTER

### 6-third_line
This script will on execution print out only the third line from the file provided to it during execution (In this case, it works with the "iacta" file which will be provided). In order to use it, open a terminal and type: 
<pre>
Chukwuemeka@Ubuntu~$ ./6-third_line
</pre>
press ENTER

### 7-file
This script will create the file named exactly `\*\\'"Best School"\'\\*$\?\*\*\*\*\*:)` and write the content `Best School` into it. In order to use it, open up a terminal and type: 

<pre>
Chukwuemeka@Ubuntu~$ ./7-file
</pre>
press ENTER

### 8-cwd_state 
This script will write the results of the command `ls -la` into the file `ls_cwd_content` (If the file does not exists, it will create it. If the file already exists, it will overwrite the contents of the file). In order to use this script, open up a terminal and type: 
<pre>
Chukwuemeka@Ubuntu~$ ./8-cwd_state
</pre>
press ENTER

### 9-duplicate_last_line
This script will duplicate the last line of the file `iacta`. In order to use this script, open up a terminal and type:
<pre>
Chukwuemeka@Ubuntu~$ ./9-duplicate_last_line
</pre>
press ENTER

### 10-no_more_js
This script will on execution, delete all the regular files with the `.js` extension in the working directory and it's subdirectories. In order to use it, open up a terminal and type: 
<pre>
Chukwuemeka@Ubuntu~$ ./10-no_more_js
</pre>
press ENTER

### 11-directories
This script will on execution, proceed to count all the subdirectories in the current working directory (including the hidden subdirectories) and display the count on the terminal. In order to use it, open up a terminal and type:
<pre>
Chukwuemeka@Ubuntu~$ ./11-directories
</pre>
press ENTER

### 12-newest_files
This script will on execution, proceed to list out the 10 newest files in the current working directory (Using the modification time of each of the files as a reference to determine which is the newest and which is the oldest) to the terminal. In order to use it, open up a terminal and type: 
<pre>
Chukwuemeka@Ubuntu~$ ./12-newest_files
</pre>
press ENTER

### 13-unique
This script will on execution, look through the items in a list and only print to the terminal the items which occur only once (which are unique). In order to use it, open up a terminal and type: 
<pre>
Chukwuemeka@Ubuntu~$ ./13-unique
</pre>
press ENTER

### 14-findthatword
This script will on execution, display to the terminal all the lines from the file `/etc/passwd` that contain the pattern `root`. In order to use it, open up a terminal and type: 
<pre>
Chukwuemeka@Ubuntu~$ ./14-findthatword
</pre>
press ENTER

### 15-countthatword
This script will on execution, proceed to count and display to the terminal the number of lines from the file `/etc/passwd` that match the pattern `bin`. In order to use it, open up a terminal and type:
<pre>
Chukwuemeka@Ubuntu~$ ./15-countthatword
</pre>
press ENTER

### 16-whatsnext
This script will on execution, print out to the terminal the lines from the file `/etc/passwd` that match with the pattern `root` as well as the next 3 lines after the matching line. In order to use it, open a terminal and type:
<pre>
Chukwuemeka@Ubuntu~$ ./16-whatsnext
</pre>
press ENTER

### 17-hidethisword
This script will on execution, print to the terminal the lines from the `/etc/passwd` file that do not contain the pattern; `bin`. In order to use it, open up a terminal and type:
<pre>
Chukwuemeka@Ubuntu~$ ./17-hidethisword
</pre>
press ENTER

### 18-letteronly 
This script will on execution, search through the file `/etc/ssh/sshd_config` for lines that begin with a letter and display same to the terminal. In order to use this, open up a terminal and type:
<pre>
Chukwuemeka@Ubuntu~$ ./18-letteronly
</pre>
press ENTER

### 19-AZ
This script will on execution, take as input the standard input and replace the characters `A` and `C` with `Z` and `e`respectively. For example:
<pre>
Chukwuemeka@Ubuntu~$ ./echo 'Replace all characters' | ./19-AZ
Replaee all eharaeters
</pre>

and that's that.





