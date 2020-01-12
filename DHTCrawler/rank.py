import json
import operator
import libtorrent as lt
import time

def rank():
    jsonObj = open("DHTCrawler/pretty.json")

    dictObj = json.load(jsonObj)

    newdict = {}
    x={}
    for movie, val in dictObj.items():
        newdict.setdefault(val, []).append(movie)
    q = 1
    f = open('list.txt','w')
    for val in sorted(newdict.keys()):
        if val > 30:
            for i in range(len(newdict[val])):
                 magneturl='magnet:?xt=urn:btih:%s'%newdict[val][i]
		 
                 #print("%d"&q,val,"magneturl=%s" %magneturl)
		 print("{0}: {1} times : {2}".format(q,val,magneturl))
		 q = q+1
		 f.write(magneturl)
		 f.write("\n")

if __name__ =="__main__":
    rank()

