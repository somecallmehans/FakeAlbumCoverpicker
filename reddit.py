'''
1. Need to resize images to fit desktop background, some are too big
2. It looks like the album cover will only switch when it goes from .png to .jpg,
if it hits .jpg twice in a row or .png twice in a row it won't switch


'''
from os.path import basename
from urllib.parse import urlsplit
from appscript import app, mactypes
from resizeimage import resizeimage
from PIL import Image

import urllib
import time
import praw
import os

wallpaperSub = 'fakealbumcovers'

client_pass = #Client password for app dev
secret_pass = #Secret password for app dev
user_agent = #Brief description of the script
username = #Account username
password1 = #Account password


def getwallpaperurl():
	user = praw.Reddit(client_id = client_pass, 
		client_secret = secret_pass,
		user_agent = user_agent, 
		username = username, 
		password = password1)

	#sub = user.get_random_submission(wallpaperSub)
	#for submission in user.subreddit('fakealbumcovers').top('day'):
		#sub = submission

	sub = user.subreddit('fakealbumcovers').random()
	return sub.url

#This function essentially just changes the wallpaper on mac and is janky as hell
def changeWallpaper(filename):
	'''
	gsettings = Gio.Settings.new("org.gnome.desktop.background")
	gsettings.set_string("picture-uri", "file://" + filename)
	gsettings.apply()
	'''
	#im = Image.open(filename)
	#im = im.resize(2600,1600)
	#im.save(filename, format='JPEG', quality = 95)
	app('Finder').desktop_picture.set(mactypes.File(filename))

	'''
	fd_img = open(filename, 'rb')
	img = Image.open(filename)
	img = resizeimage.resize_contain(img, [2600, 1600])
	img.save(filename, img.format)
	app('Finder').desktop_picture.set(mactypes.File(filename))
	fd_img.close()
	'''

def downloadfile(url, filename):
	urllib.request.urlretrieve(url, filename)

def getextension(filename):
	return filename[filename.rfind("."):]

while True:
	url = getwallpaperurl()
	extension = getextension(url)
	filename = "/tmp/TempWallpaper" + extension

	downloadfile(url, filename)
	changeWallpaper(filename)

	#I'm using this to reset the filename variable because otherwise I don't think the
	#thing will switch over.
	filename = " "
	#Right now it changes every minute I don't really care what the time is.
	time.sleep(60)






















