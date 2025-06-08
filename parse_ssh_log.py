# script to count failed ssh login attempts made by reading a log file

import re 
from collections import Counter



with open("auth.log", "r") as file: # load the file 
    logs = file.readlines()

pattern = r"Failed password.*from (\d+\.\d+\.\d+\.\d+)" # pattern the script searches for from the file, regex of the address

ip_list=[] # create a list to store IPs

for line in logs: 
    match = re.search(pattern, line) # match the pattern going line by line
    if match: 
        ip = match.group(1) # returns whatever is inside the parantheses from pattern
        ip_list.append(ip) # if there is a match, add the ip address to the created list ip_list

ip_counts = Counter(ip_list) # counts IP addresses

print("Top 5 brute-force IPs: ")
for ip, count in ip_counts.most_common(5): # top 5 most common ips in the list
    print(f"{ip}: {count} attempts") 
