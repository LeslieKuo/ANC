
##jupyter notebook
#Noise Cancelation（example with RLS filter）

import numpy as np
import matplotlib.pylab as plt
import padasip as pa
from scipy.io import wavfile

#
# orate,data = wavfile.read('yly1.wav')
# #orate1,noise = wavfile.read('n10.wav')
# print(orate, data)
# #print(orate1)
# l=len(data)//5
# data=data[0:l]
# #n10 = noise[0:l]
# # signals creation: u, v, d
# N = len(data)
# print(N)
# n = 20
# #u = np.sin(np.arange(0, N/10., N/50000.))
# v = data
# u = np.random.normal(0, 1, N) # AWGN noise
# v2 = np.arange(300)
# v1 = v[:N-300]
# vd = np.append(v2,v1)
# #v = v + 0.0001*ud #noise add small signal
# u = u #noise add small signal
# print(np.max(u))
# d = vd + 100000*u
# u = 100000*u #normalization
# # filtering
# x = pa.input_from_history(u, n)[:-1]
# # x=x[:-1]
# # d = d[:l-n]
# d=d[n-1:-1]
# f = pa.filters.FilterRLS(mu=0.99, n=n)
# y, e, w = f.run(d, x)
#
# d=d.astype(data.dtype)
# music=e.astype(data.dtype)
# print(np.max(music),np.max(u))
# wavfile.write('aANCtest.wav',orate,music)
# wavfile.write('acontaminate.wav',orate,d)
# wavfile.write('anoisewiths.wav',orate,u)


def DelayConcat(oarray, num, toh):
    """origin array delay x s .
       Namely, add something at the front . then concat the origin array which is cut the tail or head"""
    N = len(oarray)
    something = np.arange(num)
    if toh == 0:
        cutTail = u[:N - num]
        Delay = np.append(something, cutTail)
    elif toh == 1:
        cutHead = u[N:]
        Delay = np.append(something, cutHead)

    return Delay
#
# def Normalizaiton(array):
#     if

orate,data = wavfile.read('yly1.wav')
#orate1,noise = wavfile.read('n10.wav')
print(orate, data)
#print(orate1)
l = len(data)//5
data = data[0:l]
#n10 = noise[0:l]
# signals creation: u, v, d
N = len(data)
print(N)
n = 20
#u = np.sin(np.arange(0, N/10., N/50000.))
v = data
u = np.random.normal(0, 1, N) # AWGN noise
print(v.dtype, u.dtype)

print(np.max(u))
print(np.max(v))
delayNoise = DelayConcat(u, 10, 0)
delaySign = DelayConcat(v, 10, 0)

d = v + 10000*delayNoise
u = u + 0.1 * delaySign    #noise add small  delay signal
v1 = v[1000]
# filtering
x = pa.input_from_history(u, n)[:-1]
# x=x[:-1]
# d = d[:l-n]
d=d[n-1:-1]
f = pa.filters.FilterRLS(mu=0.99, n=n)
y, e, w = f.run(d, x)

d=d.astype(data.dtype)
music=e.astype(data.dtype)
print(np.max(music),np.max(u))
wavfile.write('jANCtest.wav',orate,music)
wavfile.write('jcontaminate.wav',orate,d)
wavfile.write('jnoisewiths.wav',orate,u)

