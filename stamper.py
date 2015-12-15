#!/usr/bin/python

import os
import time
import sys

sampleDir = "samples/"

# add ext or file in this map with the corresponding sample file:
fileTypes =	{
				".c" : "CSample",
				".h" : "CSample",
				"Makefile" : "MakefileSample"
			}

login = os.environ['USER']

def	InitHeader(filePath):
	filename , ext = os.path.splitext(filePath)
	if filename in fileTypes:
		SampleFileName = fileTypes[filename]
	elif ext in fileTypes:
		SampleFileName = fileTypes[ext]
	else:
		return None
	with open(sampleDir + SampleFileName, 'r') as SampleFile:
		data = SampleFile.read()
	return data

def	GetFile(sample, filename):
	SampleStr = "filename________________________________________"
	return sample.replace(SampleStr, filename + (' ' * (len(SampleStr) - len(filename))))

def	GetUser(sample):
	SampleStr = "user____________"
	return sample.replace(SampleStr, login + (' ' * (len(SampleStr) - len(login))))

def	GetUserMail(sample):
	SampleStr = "userMail________________________________"
	MailStr = " <" + login + "@student.42.fr>"
	return sample.replace(SampleStr, login + MailStr + (' ' * (len(SampleStr) - (len(login) + len(MailStr)))))

def GetCreated(sample, date):
	SampleStr = "creation_date______"
	return sample.replace(SampleStr, date);

def GetUpdated(sample, date):
	SampleStr = "update_date________"
	return sample.replace(SampleStr, date);

def	CreateHeader(filePath):
	sample = InitHeader(filePath)
	creationDate = time.strftime('%Y/%m/%d %H:%M:%S', time.gmtime(os.path.getctime(filePath)))# doesn't work on nix ...
	updateDate = time.strftime('%Y/%m/%d %H:%M:%S', time.gmtime(os.path.getmtime(filePath)))
	sample = GetFile(sample, filePath)
	sample = GetUser(sample)
	sample = GetUserMail(sample)
	sample = GetCreated(sample, creationDate)
	sample = GetUpdated(sample, updateDate)
	return sample

if __name__ == '__main__':
	fileLen = len(sys.argv)
	i = 1
	while (i < fileLen):
		if os.path.exists(sys.argv[i]):
			fd = open(sys.argv[i], 'r+')
			fileContent = fd.read()
			fd.write(CreateHeader(sys.argv[i]) + fileContent)
			fd.close()
		i += 1
