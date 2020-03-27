import requests
import numpy as np
import matplotlib.pyplot as plt

api_key="" #generate your api key from data.gov.in
url="https://api.data.gov.in/resource/3b01bcb8-0b14-4abf-b6f2-c1bfd384ba69?api-key="+api_key+"&format=json&offset=0&limit=10000"
response=requests.get(url)

#print(response.json())

data= response.json()

values=data["records"]

"""for value in values:
	if value["pollutant_id"]=="PM2.5":
		print(value["state"]+"   "+value["city"]+"    "+value["pollutant_id"]+"   "+value["station"]+"   "+value["pollutant_avg"])"""
		
dummy_state="Andhra_Pradesh"
pm_val=0.0
count=0
bar_chart={}
j=0
cities=[values[0]["city"]]
avg_sample=[int(values[0]["pollutant_avg"])]
for i in range(len(values)):
	value=values[j]
	if value["pollutant_id"]=="PM2.5" and value["pollutant_avg"]!="NA":
		if value["state"]==dummy_state:
			pm_val=pm_val+int(value["pollutant_avg"])
			count=count+1
		else:
			#print(dummy_state+"  "+str(pm_val)+"   "+str(count))
			bar_chart[dummy_state]=pm_val
			single_sample=int(value["pollutant_avg"])
			cities.append(value["city"])
			avg_sample.append(single_sample)
			dummy_state=value["state"]
			count = 0
			pm_val=0
			j=j
	j=j+1

print(bar_chart)

x_axis=cities
y_axis=avg_sample

print(x_axis,y_axis)

"""for key in bar_chart.keys():
	x_axis.append(key)
for value in bar_chart.values():
	y_axis.append(round(value))"""

y_pos=np.arange(len(x_axis))
plt.bar(y_pos,y_axis,align='center',width=0.8)
plt.xticks(y_pos,x_axis,fontsize=6)
plt.ylabel('PM2.5 PPM Levels')
plt.title('PM2.5 Levels in Major Indian Cities')
plt.show()

#print(x_axis,y_axis)


			
		
