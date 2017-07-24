# -*- coding: utf-8 -*-
"""
Created on Sat Oct 08 15:30:42 2016

@author: Ketakee Nimavat
"""

import urllib2
import re

website = "http://indianexpress.com/opinion/"
openwebsite = urllib2.urlopen(website)
html = openwebsite.read()
links=re.findall("<a href=\"http://indianexpress.com/article/opinion/.*\"><img src.*alt=.*></a></div>",html)

print(len(links))
for link in links:
    s=re.search("<a href=\"(http://indianexpress.com/article/opinion/.*)\"><img src.*alt=(.*)></a></div>",link)
    print(s.group(2))