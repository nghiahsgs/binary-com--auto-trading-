import requests
import matplotlib.pyplot as plt
print('aa')
time_start=0
time_end=1575490800
urlGet='http://localhost/binary%20com%20auto%20trade/select.php?start='+str(time_start)+'&end='+str(time_end)

kq=requests.get(urlGet)
data=kq.text
array_data=data.split('<br>')

list_average_price=[]

for i in range(1,len(array_data)-1):
    data_line=array_data[i]
    open=data_line.split('|')[1]
    close=data_line.split('|')[2]
    average_price=(float(open)+float(close))/2
    list_average_price.append(average_price)
    
plt.plot(range(len(list_average_price)),list_average_price)
plt.show()
