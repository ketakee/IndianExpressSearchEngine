# -*- coding: utf-8 -*-
"""
Created on Sat Oct 08 21:16:32 2016

@author: Ketakee Nimavat


"""

from urllib.request import urlopen
import re

x="https://en.wikipedia.org/wiki/"
y="gilmore girls"
y=y.split()
y="_".join(y)


response=urlopen(x+y)
content=response.read()
cont=re.findall(b"<p>.*</p>",content)
b=str(cont[0])[1:]
b=re.sub("<[^>]+>"," ",b)
print(b)