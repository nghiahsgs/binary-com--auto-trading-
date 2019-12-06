import numpy as np
import requests
import matplotlib.pyplot as plt
import io
def write_list_2_file(array_value,filename):
	file=io.open(filename,'a')
	for i in range(array_value.shape[0]):
		value=array_value[i,0]
		file.write('%s\n'%value)
	file.close()
    
#1575614409 thoi diem dang code (December  06 2019)
#1544078374 thoi diem 1 nam trc (December  06 2018)

#kq=requests.get('https://poloniex.com/public?command=returnChartData&currencyPair=USDT_BTC&start=1544078374&end=1546670374&period=1800') #30p 1 ket qua
kq=requests.get('https://poloniex.com/public?command=returnChartData&currencyPair=USDT_BTC&start=1544078374&end=1575614409&period=1800') #30p 1 ket qua
array_data=kq.json()

print(len(array_data)) #17521 data point


list_open=np.empty((len(array_data)-2,1))
list_close=np.empty((len(array_data)-2,1))

#tinh rsi
list_change=np.empty((len(array_data)-2,1))
list_change[0]=0

list_upward_moment=np.empty((len(array_data)-2,1))
list_upward_moment[0]=0

list_downward_moment=np.empty((len(array_data)-2,1))
list_downward_moment[0]=0

list_average_upward_moment=np.empty((len(array_data)-2,1))
list_average_downward_moment=np.empty((len(array_data)-2,1))
list_rsi=np.empty((len(array_data)-2,1))
for i in range(1,len(array_data)-1): #ignore first data point
	data_point=array_data[i]
	open=data_point['open']
	close=data_point['close']
	#print('open',open)
	#input('nghiahsgs')

	#list_open.append(open)
	#list_close.append(close)
	list_open[i-1]=open
	list_close[i-1]=close
    
    

#tinh rsi
for i in range(1,len(list_close)):
    list_change[i]=list_close[i]-list_close[i-1]
for i in range(1,len(list_change)):
    if list_change[i]>0:
        list_upward_moment[i]=list_change[i]
    else:
        list_upward_moment[i]=0
for i in range(1,len(list_change)):
    if list_change[i]<0:
        list_downward_moment[i]=-list_change[i]
    else:
        list_downward_moment[i]=0

for i in range(0,len(list_upward_moment)):
    if i<14:
        list_average_upward_moment[i]=0
    elif i==14:
        list_average_upward_moment[i]=np.sum(list_upward_moment[1:15])/14
    else:
        list_average_upward_moment[i]=(list_average_upward_moment[i-1]*13+list_upward_moment[i])/14
        
for i in range(0,len(list_downward_moment)):
    if i<14:
        list_average_downward_moment[i]=0
    elif i==14:
        list_average_downward_moment[i]=np.sum(list_downward_moment[1:15])/14
    else:
        list_average_downward_moment[i]=(list_average_downward_moment[i-1]*13+list_downward_moment[i])/14

for i in range(0,len(list_average_upward_moment)):
    if i<14:
        list_rsi[i]=0
    else:
        list_rsi[i]=100-100/(list_average_upward_moment[i]/list_average_downward_moment[i]+1)

'''
write_list_2_file(list_close,'list_close.txt')
write_list_2_file(list_change,'list_change.txt')
write_list_2_file(list_upward_moment,'list_upward_moment.txt')
write_list_2_file(list_downward_moment,'list_downward_moment.txt')
write_list_2_file(list_average_upward_moment,'list_average_upward_moment.txt')
write_list_2_file(list_average_downward_moment,'list_average_downward_moment.txt')
'''

#thong ke neu dung rsi lam chi bao 
#cho vong lap de tim ra chi so rsi toi uu
for optimal_rsi in range(70,90):
	nb_dem_predict_success=0
	nb_dem_predict_fail=0
	#array_over_bought=[]
	for i in range(1,len(list_rsi)-1):

		if list_rsi[i-1,0]<optimal_rsi and list_rsi[i]>optimal_rsi:
		#if list_rsi[i,0]>70:
			#print(i)
			if list_close[i+1,0]-list_open[i+1,0]<0:
				#chi so bao do, ket qua tiep theo ve do
				nb_dem_predict_success+=1
				#array_over_bought.append(list_rsi[i,0])
			else:
				nb_dem_predict_fail+=1
	'''
	if list_rsi[i-1]>20 and list_rsi[i]<20:
		#print(i)
		if list_close[i+1]-list_open[i+1]>0:
			#chi so bao xanh, ket qua tiep theo ve xanh
			nb_dem_predict_success+=1
		else:
			nb_dem_predict_fail+=1
	'''
	print('nb_dem_predict_success',nb_dem_predict_success)
	print('nb_dem_predict_fail',nb_dem_predict_fail)
	print('optimal_rsi:%s and % success'%(optimal_rsi,nb_dem_predict_success/(nb_dem_predict_fail+nb_dem_predict_success)))

#ve gia tri trung binh va chi bao

plt.subplot(2,1,1)
plt.plot(range(len(list_close)),list_close,'.')

plt.subplot(2,1,2)
nbs_point=len(list_rsi)

plt.plot(range(nbs_point),list_rsi)
plt.plot(range(nbs_point),np.ones((nbs_point,1))*30,'r')
plt.plot(range(nbs_point),np.ones((nbs_point,1))*70,'r')


plt.show()
#plt.savefig('demo.pdf')
