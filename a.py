import json 
import requests
from p import etiles
j = requests.get('https://olimp.miet.ru/ppo_it/api/coords').content
tile=json.loads(j)['message']['sender']
sx,sy  =  map(int,tile)
tile=json.loads(j)['message']['listener']
print(sx,sy)
lx,ly=map(int,tile)
ncsx=(sx%16)+1
ncsy=(sy%16)+1
for i in range(0,17):
	ncsi=i%16
	if ncsi!=0:

		ncs=[i%ncsi,ncsi]
	else:
		ncs=[i,0]
	ncli=i%16
	if ncli!=0:

		ncl=[i%ncsi,ncsi]
	else:
		ncl=[i,0]








