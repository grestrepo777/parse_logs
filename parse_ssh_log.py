# script to count failed ssh login attempts made by reading a log file

import re 
from collections import Counter


# load the file
with open("auth.log", "r") as file: 
    logs = file.readlines()

pattern = r"Failed password.*from (\d+\.\d+\.\d+\.\d+)"

ip_list=[]

for line in logs: 
    match = re.search(pattern, line)
    if match: 
        ip = match.group(1)
        ip_list.append(ip)

ip_counts = Counter(ip_list)

print("Top 5 brute-force IPs: ")
for ip, count in ip_counts.most_common(5): 
    print(f"{ip}: {count} attempts")