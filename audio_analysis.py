import wave 
import numpy as np
import drawsvg as draw

BAR_COUNT = 28 # defines the number of audio bars we want to be visible in the final svg
X_WIDTH = 300
Y_HEIGHT = 80

wav_obj = wave.open('Aragainz.wav', 'rb')
sample_freq = wav_obj.getframerate()
n_samples = wav_obj.getnframes()
signal_wave = wav_obj.readframes(n_samples)
signal_array = np.frombuffer(signal_wave, dtype=np.int16) # half the length of signal_wave bytes array

lc = abs(signal_array[0::2]) # grab left channel, make all values positive

bin_size = len(lc)//BAR_COUNT #floor divion to produce integer result

lc_subarrays = [lc[i:i + bin_size] for i in range(0, len(lc), bin_size)]

result = [sum(i)/len(i) for i in lc_subarrays]

normalisation_factor = Y_HEIGHT/max(result)
normed_result = [i*normalisation_factor for i in result]

# Drawing the bar graphs to an svg file

d = draw.Drawing(X_WIDTH, Y_HEIGHT, origin=(0,0))
d2 = draw.Drawing(X_WIDTH, Y_HEIGHT, origin=(0,0))

width = X_WIDTH/BAR_COUNT
x = 0
max_height = 80


for i in normed_result:
    val = round(i)
    d.append(
         draw.Rectangle(x+2, (max_height - val)/2, width-2, val, fill='#467877')

    )
    d2.append(
         draw.Rectangle(x+2, (max_height - val)/2, width-2, val, fill='#FF0078')

    )
    x += width 


d.save_svg('wave-grey6.svg')
d2.save_svg('wave-pink6.svg')

print("finished")
