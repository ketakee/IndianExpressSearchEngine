# -*- coding: utf-8 -*-
"""
Created on Tue Oct 11 10:30:09 2016

@author: Ketakee Nimavat
"""
#GETS THE PAGE CONTENT FOR A PARTICULAR PAGE. SHALL BE USEFUL WHEN CONTENT WILL BE SCANNED FOR PROXIMITY TO THE REQUIRED TOPICS.
#AND SHALL BE USEFUL TO PROVIDE A SUMMARY OF THE ARTICLE.
import re
import urllib2
url="http://indianexpress.com/article/opinion/columns/narendra-modi-government-performance-growth-opposition-rahul-nitish-kumar-kejriwal-elections-3031502/"

openwebsite = urllib2.urlopen(url)
html = openwebsite.read()
match=re.findall("<p>.*</p>",html)
for elem in match:
    z=re.search("<strong>.*</strong>",elem)
    if z:
        continue
    else:
        m=re.search("<p>(.*)</p>",elem)
        if m:
            m=m.group(1)
            n=re.sub("<a href.*\">"," ",m)
            n=re.sub("</a>"," ",n)
            print(n)
