# parse_logs
A script to count failed ssh login attempts made by reading a log file

The script loads the file named auth.log. It goes through each line and when it says there's a failed password, that IP address gets added to a list of IPs. At the end it outputs the top 5 addresses with the most failed password attempts made. 
