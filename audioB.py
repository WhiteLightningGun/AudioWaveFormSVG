import wave 
import numpy as np
import drawsvg as draw

wav_obj = wave.open('Aragainz.wav', 'rb')
sample_freq = wav_obj.getframerate()
n_samples = wav_obj.getnframes()
signal_wave = wav_obj.readframes(n_samples)

signal_array = np.frombuffer(signal_wave, dtype=np.int16) # half the length of signal_wave bytes array

l_channel = signal_array[0::2]
r_channel = signal_array[1::2]

sample_bin_size = len(l_channel)//60

result = []
n = 0
sample_bin = 0

for i in l_channel:
    if n < sample_bin_size:
        sample_bin += abs(l_channel[i]) 
        n += 1
    else:
        n = 0
        result.append(sample_bin/sample_bin_size)
        sample_bin = 0

normalisation_factor = 80/max(result)

normed_result = [i*normalisation_factor for i in result]

d = draw.Drawing(300, 80, origin=(0,0))
d2 = draw.Drawing(300, 80, origin=(0,0))

width = 5
gap = 0
x = 0
max_height = 80

for i in normed_result:
    val = round(i)
    d.append(
         draw.Rectangle(x, (max_height - val)/2, width, 0.8*val, fill='#245b5a')

    )
    d2.append(
         draw.Rectangle(x, (max_height - val)/2, width, 0.8*val, fill='#FF0078')

    )

    x += width + gap


d.save_svg('wave-grey3.svg')
d2.save_svg('wave-pink3.svg')

print("finished")
