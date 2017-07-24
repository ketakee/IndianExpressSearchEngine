# -*- coding: utf-8 -*-
"""
Created on Sat Oct 08 15:30:42 2016

@author: Ketakee Nimavat
"""

from urllib.request import urlopen
import re
import operator

def search(s,keysearchdict):
    s=s.split()
    result={}
    for elem in s:
        if (keysearchdict.get('b'+elem)):
            l=keysearchdict.get(elem)
            for num in l:
                if num in result:
                    result[num]=result[num]+1
                else:
                    result[num]=1

    result=sorted(result.items(), key=operator.itemgetter(1),reverse=True)    
    return result
        
            
    


def buildkeylist(keys,keydict):
    for elem in keydict:
        for word in keydict[elem]:
            if word in keys:
                keys[word]+=[elem,]
            else:
                keys[word]=[elem] 
    return keys
    
    

#n = number of pages of the column section that you want to search through    
def preprocessing(n):
        i=0
        url=[]
        title=[]
        description=[]
        urldict={}
        keydict={}
        keysearchdict={}
        website = "http://indianexpress.com/section/opinion/columns/"
        for j in range(1,n):
            appnd="page/"+str(j)
            wb=website+appnd
            print(wb)
            urldict={}
            openwebsite = urlopen(wb)
            html = openwebsite.read()
            links=re.findall(b"<h6><a href=\"(.*)\">(.*)</a></h6>[\t\n\r\f\v]*<p>(.*)</p>",html)
            for elem in links:
                url+=[elem[0]]
                title+=[elem[1]]
                description+=[elem[2]]
                keywords=re.findall(b"http://indianexpress.com/article/opinion/columns/(.*)/",elem[0])
                keywords=keywords[0].split(b"-")
                linkid=i
                i+=1
                urldict[linkid]=(elem[0],elem[1],elem[2])
                keydict[linkid]=keywords
    
    
            keysearchdict.update(buildkeylist(keysearchdict,keydict))
            
                
                
        return keysearchdict,urldict
        

#n = number of pages of the column section that you want to search through. here n=5.
k,u=preprocessing(5)
l=search("india",k)
print(l)


f="Keydict.txt"
f1=open(f,'w')
for elem in k:
    f1.write(str(elem))
    f1.write("\t")
    for l in k[elem]:
        f1.write(str(l))
        f1.write("\t")
    f1.write("\n")
f1.close()
 

w="output.html"
w=open(w,'w')
#html page content
message = """<html>
<head></head>
<body>
<p>"""


for elem in l:
    ahref="<a href=\"website\" target=\"_blank\">Substitute</a>"
    ahref=ahref.replace("website",u[elem[0]][0])
    ahref=ahref.replace("Substitute",u[elem[0]][1])
    message+=ahref
    message+="<br>"
    message+=u[elem[0]][2]
    message+="<br> <br>"
    
message+="""</p>
</body>
</html>"""

w.write(message)
w.close()
  
#opening the output.html file would show all the relevant links.
    



#A test module to get the keywords from the link of the news article itself. ****CAN BE IGNORED****

"""
print(links[0])
l=links[0][0]
print(l)
for elem in l:
    keywords=re.findall("http://indianexpress.com/article/opinion/columns/[a-zA-Z]*[-.*-]+[0-9]+/",l)
    print(keywords)
"""


#alternate way of implementing link storage where links are stored in a text file and then retreived from there. As opposed to the current impractical way where everything is stored in alist temporarily.

"""
openwebsite1 = urllib2.urlopen(l)
site = openwebsite1.read()
f="list.txt"
f1 = open(f,'w')
match=re.findall("<p>.*</p>",site)
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
            f1.write(n)

            
"""     
#f1.close

    


