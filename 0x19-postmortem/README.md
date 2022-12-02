![401 Error Image For The Postmortem](https://kinsta.com/wp-content/uploads/2020/06/401-error.jpg)
# Orupay Development Server Failure Report
A few days ago, the entire *Orupay* web application refused to load up in the browser and kept returning 401 messages on test. As a result, all further development of the web application by the team had to be suspended until the problem could be rectified. It turns out that all this was caused by an Nginx configuration file which had not been properly linked with the running process of the server.

## Timeline
On Wednesday, 30<sup>th</sup> November 2022 1:00pm (West African Time), this problem was identified and reported by one of the engineers responsible for the reliability of the site. As it turns out, all HTTP requests to the site were returning only 401 messages. After doing his best to resolve the problem and not being able to, the engineer ended up forwarding it to me on Thursday, 1<sup>st</sup> December, 2022 11:00am (West African Time).

Initially, I thought that it was an issue with the network ports through which HTTP requests are handled, namely port 80. Working on this assumption, I spent the better part of the day working on this bug to no avail. It was finally resolved on Friday, 2<sup>nd</sup> December 2022 when I created a new symbolic link to the new configuration file.

## Root Cause & Resolution
The Nginx server relies on a configuration file (Usually located at **/etc/nginx/sites-available/default**) which gives it information on which ports to use for HTTP requests, and the server accesses this configuration file through the use of a symbolic link  (Usually located at **/etc/nginx/sites-enabled/default**) which points to that configuration file. Now, in this particular case, one of the engineers most likely forgot to delete the old symbolic link and create a new one when he/she made changes to the configuration file as is standard practice. Hence, the server kept making use of the older incorrect configuration file to which the current symbolic link pointed to.

The problem was resolved by first turning off the server, deleting the currently available symbolic link and then creating a new symbolic link pointing to said configuration file, then I restarted the server and voila, the development server was back to normal operation. 

## What Can Be Done To Prevent Future Occurences 
- Whenever configuration file is updated, always delete the old symbolic link to this file and create a new one.
- Try to regularly turn off, maintain and update the server.
- Using a monitoring tool to determine if the page returns a 401 error code on load and configure said monitor to notify one of the developers about this if need be. 
