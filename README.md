# 42FilesStamper

Python script to fast add 42 headers at top of files.

Preliminaries:
chmod u+x stamper.py

Usage:
This line add header at top of all c/h and Makefile files in the current directory:
./stamper.py *.c *.h Makefile

Example:
see MakefileExample

You can create your own fileType/Headers by adding them in /samples
dont't forget to actualize stamper.py map.

Implemented tokens:

"filename________________________________________"

"user____________"

"userMail________________________________"

"creation_date______"

"update_date________"
