import numpy as np
import matplotlib.pylab as plt
import padasip as pa
from scipy.io import wavfile

orate,data = wavfile.read('jANCtest.wav')
a = np.random.normal(0,1,100)
u = np.arange(10)
N=2
print(u)
u1 = u[N:]
print(u1)
u2 = u[:len(u)-N]
print(u2)
print(u2.dtype)
b = a* 32768 // np.max(a)
b = b.astype(data.dtype)
print(a.dtype,np.max(a))

print(np.max(b))
print(data.dtype, np.max(data))
if data.dtype == np.int16:
    print("yes")
else:
    print("no")
a,b = a.astype(np.float64), b.astype(np.float64)
a = a/np.max(abs(a))
print(a.dtype,np.max(a))
print(a)
a =a * 32768
print(a)
a = a.astype(np.int16)
print(np.max(a))
print(a)