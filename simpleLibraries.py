import sounddevice
from scipy.io.wavfile import write
fs=44100
second = int("enter the time duration in second :")
print("recording ...\n")
record_voice=sounddevice.rec(int(second*fs),samplerate=fs,channels=2)
sounddevice.wait()
write("cybrride",fs,record_voice)