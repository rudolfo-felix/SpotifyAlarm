# Spotify Alarm
# Wake up with your favorite music and with your best sound system!
# 31/03/2020
# https://github.com/rudolfovmf
from selenium import webdriver
from time import sleep

class SpotifyBot:
    def __init__(self, username, pw, playlist):
        # get the browser driver
        self.driver = webdriver.Chrome(executable_path=r'F:\rudyr\Documents\VS\chromedriver.exe')
        # open the spotify on the web
        self.driver.get("https://open.spotify.com/")
        sleep(2)
        # find and click on the 'Log In button' (change the word 'Accedi', that's italian, for your prefer language)
        self.driver.find_element_by_xpath("//button[contains(text(),'Accedi')]")\
            .click()
        sleep(5)
        # write username
        self.driver.find_element_by_xpath("//input[@name=\"username\"]")\
            .send_keys(username)
        # write password
        self.driver.find_element_by_xpath("//input[@name=\"password\"]")\
            .send_keys(pw)
        sleep(3)
        # find and click on the 'Log In button' (change the word 'Accedi', that's italian, for your prefer language)
        self.driver.find_element_by_xpath("//button[contains(text(),'Accedi')]")\
            .click()
        sleep(5)
        # find and click on your favorite playlist
        playlist_path = "//span[contains(text(),'"+ playlist +"')]"
        self.driver.find_element_by_xpath(playlist_path)\
            .click()
        # to use the direct playlist link
        # comment lines 31-33 and 52
        # uncomment lines 37 and 54
        self.driver.get(playlist)
        sleep(3)
        # play the music
        self.driver.find_element_by_xpath("//button[contains(text(),'PLAY')]")\
            .click()
        # time in seconds until it closes
        sleep(600)
        # to run until it closes
        # 1. comment line 43
        # 2. uncomment line 58

# to change
username = 'auto_spotify'
password = 'xxxx9999xxxx'
# playlist name
playlist = 'Global Funk'
# playlist link
#playlist = "https://open.spotify.com/playlist/37i9dQZF1DWUS3jbm4YExP"

SpotifyBot(username, password, playlist)

#input()
