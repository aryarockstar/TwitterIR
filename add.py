import json
import copy

for i in range(83747, 125000):
	with open('doc'+str(i)+'.json') as json_data:
		data = json.load(json_data)
		data2 = copy.deepcopy(data)
		for x in data2:
			if (x != 'id') and (x != 'text') and (x != 'screen_name') and (x != 'lang') and (x != 'timestamp_ms') and (x != 'retweet_count') and (x != 'favorite_count'):
				del data[x]
		#del data['entities']
		f = open('doc'+str(i)+'.json','w')
		f.write('[')
		json.dump(data,f)
		f.write(']')
