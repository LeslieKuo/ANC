
##jupyter notebook
#Noise Cancelation（example with RLS filter）

import numpy as np
import matplotlib.pylab as plt
import padasip as pa
from scipy.io import wavfile


orate,data = wavfile.read('yly1.wav')
orate1,noise = wavfile.read('n10.wav')
print(orate)
print(orate1)
print(np.max(data))
l=len(data)//5
data=data[0:l]
n10 = noise[0:l]
# signals creation: u, v, d
N = len(data)
print(N)
print(np.max(data))
print(np.max(n10))
n = 20
#u = np.sin(np.arange(0, N/10., N/50000.))
u = data
#v = np.random.normal(0, 1, N) # AWGN noise
v = n10  #dryer noise
#v = v + 0.001*u #noise add small signal

d = u + v

# filtering
x = pa.input_from_history(v, n)[:-1]
# x=x[:-1]
# d = d[:l-n]
d=d[n-1:-1]
f = pa.filters.FilterRLS(mu=0.99, n=n)
y, e, w = f.run(d, x)

d=d.astype(data.dtype)
music=e.astype(data.dtype)
print(np.max(music),np.max(u))
wavfile.write('dANCtest.wav',orate,music)
wavfile.write('dcontaminate.wav',orate,d)
wavfile.write('dnoisewiths.wav',orate,v)



# results
# plt.figure(figsize=(12.5,6))
# plt.plot(u, "r:", linewidth=4, label="original")
# plt.plot(d, "b", label="noisy, MSE: {}".format(MSE_d))
# plt.plot(y, "g", label="filtered, MSE: {}".format(MSE_y))
# plt.xlim(N-100,N)
# plt.legend()
# plt.tight_layout()
# plt.show()