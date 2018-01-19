# correlation operation between zj1 &zj2
from scipy.io import wavfile
import numpy as np
#z1:5-7s z2:6-8s
orate1, data1 = wavfile.read('z1.wav')
orate2, data2 = wavfile.read('z2.wav')

#wavfile.write('zj3.wav', orate1, data2)
a = data1
b = data2
# 需要归一化再求互相关！
a,b = a.astype(np.float64), b.astype(np.float64)
a_max = np.max(np.abs(a))
b_max = np.max(np.abs(b))
a /= a_max
b /= b_max

csame = np.correlate(a, b, "same")
# ref = np.where(csame == np.max(csame))
ref = np.argmax(csame)
print(ref)
half_len = len(a) // 2
d = abs(ref - half_len)
print(d)
a, b = data1, data2
if ref < half_len :
    a = a[:len(a)-d-1]
    b = b[d:]
else:
    b = b[:len(a)-d-1]
    a = a[d:]


wavfile.write("t1.wav", orate1, a)
wavfile.write("t2.wav", orate2, b)

#print(" same",csame, "\n","valid", cvalid, "\n","full", cfull)