'''
(DONE) 1. Need to resize images to fit desktop background, some are too big
(DONE) 2. It looks like the album cover will only switch when it goes from .png to .jpg,
if it hits .jpg twice in a row or .png twice in a row it won't switch
(DONEish) 3. I'd prefer it if it only picked covers that got more than 100 upvotes ever.
(DONE) 4. Need to build a try/exceot in for when it hits a file that isn't a .jpg or .png
(i.e. it crashed because it received a .com/ extension)

5. Need to determine if running this for an extended amount of time blows up the amount
of storage used, since it seems like it's just saving images over and over.


'''
from os.path import basename
from urllib.parse import urlsplit
from appscript import app, mactypes
from PIL import Image

import urllib
import time
import praw
import os
import random
import string

client_pass = 
secret_pass =
user_agent = 
username = 
password1 =


def getwallpaperurl():
	user = praw.Reddit(client_id = client_pass, 
		client_secret = secret_pass,
		user_agent = user_agent, 
		username = username, 
		password = password1)

	#Recursive function so that only covers with more than
	#10 upvotes get set because I don't want any trash covers here
	sub = user.subreddit('fakealbumcovers').random()
	if sub.score < 10:
		getwallpaperurl()

	return sub.url

#This function essentially just changes the wallpaper on mac and is janky as hell
def changeWallpaper(filename):
	app('Finder').desktop_picture.set(mactypes.File(filename))

#Downloads file
#Not sure if this try/except statement works
def downloadfile(url, filename):
	try:
		urllib.request.urlretrieve(url, filename)
	except FileNotFoundError:
		getwallpaperurl()

#Determines file extension
def getextension(filename):
	print(filename[filename.rfind("."):])
	return filename[filename.rfind("."):]

#This function is needed to generate completely different
#filenames for the images otherwise they won't change
def randomFile(stringLength = 5):
	letters = string.ascii_lowercase
	return ''.join(random.choice(letters) for i in range(stringLength))

while True:
	#The next 5 lines are all for getting and downloading the original
	#image file off of reddit and saving it to temp
	url = getwallpaperurl()
	extension = getextension(url)

	#I'm not sure if there's a better way to do what this if
	#statement is accomplishing, but essentially sometimes in
	#getextension(url) it returns some weird .com/xxxxxx which
	#i think is an ad or txt post. So by checking if it's an image
	#file it gets around that error which was causing a lot of issues
	if extension == ".png" or extension == ".jpg":
		myfile = randomFile()
		filename = "/tmp/" + myfile + extension
		downloadfile(url, filename)

		#This block is for resizing every image to a resolution that fits
		#my laptop screen
		image = Image.open(filename)
		newFile = randomFile()
		new_image = image.resize((2400,1400))
		newFileName = "/tmp/" + newFile + extension
		new_image.save(newFileName)

		#This function officially changes the desktop background
		changeWallpaper(newFileName)

	#I'm using this to reset the filename variable because otherwise I don't think the
	#thing will switch over.
	filename = " "
	extension = " "
	url = " "

	#Right now it changes every 10 seconds I don't really care what the time is.
	time.sleep(10)






















