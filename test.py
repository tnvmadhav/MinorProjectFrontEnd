from firebase import firebase
from collections import OrderedDict

firebase = firebase.FirebaseApplication('https://text-summarizer-eb34c.firebaseio.com',None)
result = firebase.get('/texts',None)
els = list(result.items())
mytext = els[-1][1]['myt']
myindex = els[-1][0]
print(mytext)
f= open("input.txt","w+")
f.write(mytext)
f.close()
g = open("output.txt","r")
damn = g.read()
print(damn)
g.close()
result2 = firebase.post('/summaries',damn)
