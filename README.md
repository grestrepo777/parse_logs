# parse_logs
A script to count failed ssh login attempts made by reading a log file

The script loads the file named auth.log. It goes through each line and when it says there's a failed password, that IP address gets added to a list of IPs. At the end it outputs the top 5 addresses with the most failed password attempts made. 

First, the script imports re which is regex used in the pattern object so it searches for an ipv4 format, and the script also imports counter which is used to count the number of ip address matches 
Second, the script loads the file and reads the entire file assigning it to logs, next the pattern object is created by checking for failed password and the ipv4 address
Then, a list to store IPs is created
Then, for each line in the logs object, it matches the pattern going line by line, if there is a match it returns whatver is inside the parentheses from the pattern object created which is the IPv4 address itself. That IPv4 address is added to the created list ip_list
ip_counts uses a counter to count each time in ip_list a certain address is added on
The top 5 addresses are printed out with the number of attempts. 
