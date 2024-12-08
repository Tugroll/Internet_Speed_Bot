from selenium import webdriver
from internet_speed import InternetSpeedTwitterBot


bot = InternetSpeedTwitterBot()
bot.get_internet_speed()
bot.tweet_at_provider()