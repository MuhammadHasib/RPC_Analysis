import csv
import datetime
from RPCHVLabel_cfi import *

reader = csv.reader(open("RPC_all.csv"))
data0 = []

vmon=0.
imon=0.
for row in reader:
    if len(row) != 4 :
        continue
    id = int(str(row[0]))
    dd2 = datetime.datetime.strptime(str(row[3]),  "%Y.%m.%d %H:%M:%S")

    if  not  len(str(row[2]).strip()) is 0 :  imon = float("%.4f"%float(row[2]))
    else                                  :  imon = -1.
    if  not len(str(row[1]).strip()) is 0 :  vmon = float(row[1])
    else                                  :  vmon = -1.

    adata = {"id":id,"imon":imon,"vmon":vmon,"date":str(row[3]),"dateN":dd2}
    data0.append(adata)


data0.sort(key=lambda x: x['dateN'] )

#print "len(data):"+str(len(data0))+"; " 
#print "data:"+str(data0)+"; " 

aaa = set()
names = {}
vmons = {}
imons = {}
dates = {}
dates2 = {}
for row in data0:
   if not endcap.has_key(int(row["id"])) :
       continue
   id  = int(row["id"])
   if row["imon"] != -1   : imon = row["imon"]
   elif imons.has_key(id) : imon = imons[id]
   else                   : imon = -1.

   if row["vmon"] != -1   : vmon = row["vmon"]
   elif vmons.has_key(id) : vmon = vmons[id]
   else                   : vmon = -1.
   #print "test"

   name = endcap[int(row["id"])]
   date = row["date"]
   date2 = datetime.datetime.strptime(date, "%Y.%m.%d %H:%M:%S")
   if (not names.has_key(id)) or (names.has_key(id) and dates2[id]<=date2):
       names[id] =name
       vmons[id] =vmon
       imons[id] =imon
       dates[id] =date
       dates2[id]=date2
   aaa.add(id)

print "check len(aaa):"+str(len(aaa))+";"
for id in names.keys():
  #print id,names[id],str(round(vmons[id]*100)/100),dates[id]
  #print id,names[id],str(round(imons[id]*100)/100),str(round(vmons[id]*100)/100),dates[id]
  #print str(round(imons[id]*100)/100),str(round(vmons[id]*100)/100),dates[id]
  #print names[id]
  #print str(round(imons[id]*100)/100)
  print str(round(vmons[id]*100)/100)
