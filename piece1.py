# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from urllib.request import urlopen
import re

def preprocessing():
        i=0
        website = "http://indianexpress.com/section/opinion/columns/"
        f="C:\\Users\\Ketakee Nimavat\\Desktop\\description.txt"
        f1 = open(f,'a',encoding='utf-8')
        for j in range(1,268):
            appnd="page/"+str(j)
            wb=website+appnd
            print(wb)
            openwebsite = urlopen(wb)
            html = openwebsite.read().decode('utf-8')
            links=re.findall("<h6><a href=\"(.*)\">(.*)</a></h6>[\t\n\r\f\v]*<p>(.*)</p>",html)
            for elem in links:
                f1.write(str(i))
                f1.write("\t")
                f1.write(elem[2])
                f1.write("\n")
                i+=1
        f1.close()
        
preprocessing()
                