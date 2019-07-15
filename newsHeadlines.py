import requests
import urllib.request
import bs4 as bs
import re
import mysql.connector


# create a list with 10 popular news websites
newsWebPages = ['https://www.bbc.co.uk/',
                'https://www.dailymail.co.uk/news/index.html',
                'https://www.thesun.co.uk/news/uknews/',
                'https://www.theguardian.com/uk-news',
                'https://www.mirror.co.uk/news/uk-news/',
                'https://news.sky.com/uk',
                'https://www.express.co.uk/news/uk',
                'https://www.telegraph.co.uk/news/',
                'https://www.independent.co.uk/news/uk',
                'https://metro.co.uk/news/']
