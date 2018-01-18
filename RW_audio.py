# learn how to read and write .wav format audio
from scipy.io import wavfile
import numpy as np
import matplotlib.pyplot as plt

orate,data = wavfile.read('yly1.wav')
print(orate,data)

print(len(data))
newdata=data[::-1]
wavfile.write('test.wav',orate,newdata)


N=20
x=np.random.normal(0,1,(N,4))
print(x)
print(x[0,1])