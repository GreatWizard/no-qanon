# This script converts domains.txt into a hosts file format.
# Usage:
#	python domains_to_hosts.py > hosts.txt

text_file = open("domains.txt", "r")
lines = text_file.readlines()
text_file.close()

for line in lines:
	print('0.0.0.0 ' + line.strip() + ' www.'+ line.strip())
