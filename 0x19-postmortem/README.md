![401 Error Image For The Postmortem](https://kinsta.com/wp-content/uploads/2020/06/401-error.jpg)
# *NaijaEats* Development Server Failure Report
A few days ago, the *NaijaEats* web application refused to load up in the browser and kept returning 401 messages on request from the browser. As a result, all further development of the web application by the team had to be suspended until the problem could be rectified. I finally discovered that all this was caused by an Nginx configuration file which had not been properly linked with the server's running process.

## Timeline
On Wednesday, 1<sup>st</sup> February 2023 at 1:00pm (West African Time), this problem was identified and reported by one of the engineers responsible for the reliability of the site. As it turns out, all HTTP requests to the site were returning a 401 error status code and message. After doing his best to resolve the problem and not being able to, the engineer ended up forwarding it to me on Thursday, 2<sup>nd</sup> February, 2023 at 11:00am (West African Time).

My initial suspicions were that this particular problem was caused by the HTTP port, namely port 80 being unavailable. Working with this suspicion in mind, I spent the better part of the day working on this bug to no avail. It was finally resolved on Friday, 3<sup>rd</sup> February 2023 when I discovered that the problem was that the Nginx web server's running process was running off a symbolic link which linked to an older and inherently incorrect configuration file. So, I deleted the symbolic link in question and created a new one linking to the new and correct configuration file.

## Root Cause & Resolution
All Nginx server rely on a server blocks configuration file (Usually located at **/etc/nginx/sites-available/default**) which gives it information on which ports to use for HTTP requests, and the server accesses this configuration file through the use of a symbolic link  (Usually located at **/etc/nginx/sites-enabled/default**) which points to that configuration file. Now, in this particular case, one of the engineers most likely forgot to create a symbolic link to the newly created configuration file and hence the Nginx server kept running off of the older configuration file that stipulated the use of the 8080 port for listening to HTTP requests from the client. This was most likely done in error.

The problem was resolved by first turning off the server, deleting the currently available symbolic link and then creating a new symbolic link pointing to said configuration file stipulating the correct port number for listening to HTTP requests (port 80 in this case), then I restarted the server and voila, the development server was back to normal operation. 

## What Can Be Done To Prevent Future Occurences 
- Endeavour to delete and recreate old symlinks to configuration file whenever it is updated
- Regular maintenance of the Nginx web server
- Extensive use in future versions of the app of monitoring tools such as DataDog, NewRelic and the likes to automate the process of monitoring App performance and sending alerts when the need arise. 
