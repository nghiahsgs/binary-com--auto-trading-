import numpy as np
import requests
import matplotlib.pyplot as plt
import io
def write_list_2_file(list_value,filename):
    file=io.open(filename,'a')
    for value in list_value:
        file.write('%s\n'%value)
    file.close()
    
time_start=0
time_end=1575490800
urlGet='http://localhost/binary%20com%20auto%20trade/select.php?start='+str(time_start)+'&end='+str(time_end)

kq=requests.get(urlGet)
data=kq.text
array_data=data.split('<br>')

list_average_price=[]
list_open=[]
list_close=[]
#tinh rsi
list_change=[0]
list_upward_moment=[0]
list_downward_moment=[0]
list_average_upward_moment=[]
list_average_downward_moment=[]
list_rsi=[]
for i in range(1,len(array_data)-1):
    data_line=array_data[i]
    open=data_line.split('|')[1]
    close=data_line.split('|')[2]
    open=float(open)
    close=float(close)
    list_open.append(open)
    list_close.append(close)
    
    #tinh gia tri trung binh cua 1 nen
    average_price=(open+close)/2
    list_average_price.append(average_price)

#tinh rsi
for i in range(1,len(list_close)):
    list_change.append(list_close[i]-list_close[i-1])
for i in range(1,len(list_change)):
    if list_change[i]>0:
        list_upward_moment.append(list_change[i])
    else:
        list_upward_moment.append(0)
for i in range(1,len(list_change)):
    if list_change[i]<0:
        list_downward_moment.append(-list_change[i])
    else:
        list_downward_moment.append(0)

for i in range(0,len(list_upward_moment)):
    if i<14:
        list_average_upward_moment.append(0)
    elif i==14:
        list_average_upward_moment.append(sum(list_upward_moment[1:15])/14)
    else:
        list_average_upward_moment.append((list_average_upward_moment[-1]*13+list_upward_moment[i])/14)
        
for i in range(0,len(list_downward_moment)):
    if i<14:
        list_average_downward_moment.append(0)
    elif i==14:
        list_average_downward_moment.append(sum(list_downward_moment[1:15])/14)
    else:
        list_average_downward_moment.append((list_average_downward_moment[-1]*13+list_downward_moment[i])/14)

for i in range(0,len(list_average_upward_moment)):
    if i<14:
        list_rsi.append(0)
    else:
        list_rsi.append(100-100/(list_average_upward_moment[i]/list_average_downward_moment[i]+1))

'''
write_list_2_file(list_close,'list_close.txt')
write_list_2_file(list_change,'list_change.txt')
write_list_2_file(list_upward_moment,'list_upward_moment.txt')
write_list_2_file(list_downward_moment,'list_downward_moment.txt')
write_list_2_file(list_average_upward_moment,'list_average_upward_moment.txt')
write_list_2_file(list_average_downward_moment,'list_average_downward_moment.txt')
'''

#thong ke neu dung rsi lam chi bao 
nb_dem_predict_success=0
nb_dem_predict_fail=0
for i in range(1,len(list_rsi)-1):
    
    if list_rsi[i-1]<70 and list_rsi[i]>70:
        print(i)
        if list_close[i+1]-list_open[i+1]<0:
            #chi so bao do, ket qua tiep theo ve do
            nb_dem_predict_success+=1
        else:
            nb_dem_predict_fail+=1
    '''
    if list_rsi[i-1]>30 and list_rsi[i]<30:
        print(i)
        if list_close[i+1]-list_open[i+1]>0:
            #chi so bao xanh, ket qua tiep theo ve xanh
            nb_dem_predict_success+=1
        else:
            nb_dem_predict_fail+=1
    '''
print('nb_dem_predict_success',nb_dem_predict_success)
print('nb_dem_predict_fail',nb_dem_predict_fail)

#ve gia tri trung binh va chi bao
'''
plt.subplot(2,1,1)
plt.plot(range(len(list_average_price)),list_average_price,'.')
plt.subplot(2,1,2)
nbs_point=len(list_rsi)

plt.plot(range(nbs_point),list_rsi)
plt.plot(range(nbs_point),np.ones((nbs_point,1))*30,'r')
plt.plot(range(nbs_point),np.ones((nbs_point,1))*70,'r')
plt.show()
#plt.savefig('demo.pdf')
'''