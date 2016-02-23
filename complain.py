#!/usr/bin/python
import random
import sys
import zipfile
import tarfile
from os import system


NAME = sys.argv[1]
RESPONSES = [
    "That really sucks, {}".format(NAME),
    "Who do you want me to destroy?",
    "You are the light of my life, " + NAME,
]#need to add more responses

def main():
	f  = open('complaints', 'w')

	print "Hello {}".format(NAME)
	resp = raw_input("What troubles you today, {}?\n".format(NAME))

	while resp.lower() != "no" and resp.lower() != "nothing":
		pass
		f.write(resp+'\n')
		print random.choice(RESPONSES)
		resp = raw_input("Anything else, {}?\n".format(NAME))
	f.close()
	print "Thank you for your complaints - we are putting them in a very special place"
	
	#grab platform, assuming windows or linux
	plat = sys.platform

    if play.startswith("win"):
        windows()
    else:
        unix()
        
def windows():
    print "Archiving file."
    with tarfile.open('complaints.tar', mode='a') as tar:
        tar.addfile('complaints.txt')
        system("DEL complaints.txt")
    print "Zipping file."
    with zipfile.ZipFile('complaints.tar.zip', mode='a') as zf:
        z.write('complaints.tar')
        system("DEL complaints.tar")
    print "Deleting file."
    system("DEL complaints.tar.zip")
    

def unix():
	print "Archiving file."
	system("tar -cvf complaints.tar complaints.txt && rm -r complants.txt > /dev/null")
	print "Zipping file."
	system("gzip complaints.tar")
	print "Deleting file."
	system("rm -r complaints.tar.gz")
	print "Thank you for complaining to me and not real people. Goodbye!"
    
if __name__ == "__main__":
    main()
