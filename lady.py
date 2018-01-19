# correlation operation between zj1 &zj2
from scipy.io import wavfile
import numpy as np
import padasip as pa
from scipy.io import wavfile
#z1:5-7s z2:6-8s
orate1, data1 = wavfile.read('s1.wav')
orate2, data2 = wavfile.read('n1.wav')
print(orate1,orate2)


# same length
if len(data1)>len(data2):
    data1 = data1[:len(data2)]
else:
    data2 = data2[:len(data1)]
print(len(data1),len(data2))

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

print(len(a),half_len)
d = abs(ref - half_len)
print(d)
a, b = data1, data2
print(len(a),len(b))
if ref < half_len :
    a = a[:len(a)-d]
    b = b[d:]
    print("a=1234")
elif ref > half_len:
    b = b[:len(a)-d]
    a = a[d:]
    print("b=1234")
print(len(a),len(b))
wavfile.write("signal.wav", orate1, a)
wavfile.write("noise.wav", orate1, b)

#print(" same",csame, "\n","valid", cvalid, "\n","full", cfull)

n = 200
v = b
dd = a[n-1:-1]
x = pa.input_from_history(v, n)[:-1]
f = pa.filters.FilterRLS(mu=0.99, n=n)
y, e, w = f.run(dd, x)

music=e.astype(data1.dtype)

wavfile.write('ladygaga.wav', orate1, music)