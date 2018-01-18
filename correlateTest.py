
from scipy.io import wavfile
import numpy as np

#z1:5-7s z2:6-8s
#z3:6-7s

orate1, data1 = wavfile.read('z1.wav')
orate2, data2 = wavfile.read('z3.wav')
N=len(data1)


cor = np.correlate(data1, data2)

ref=np.where(cor == np.max(cor))
print(np.max(cor))
print(cor[0], cor[44099],cor[6118])
print(len(data1), len(cor), ref)
