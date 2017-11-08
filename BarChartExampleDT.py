#import the modules that are needed
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

#data that needs to be charted
objects = ('Uncharted 4', 'Doom', 'Minecraft', 'LoL', 'AC Syndicate', 'FIFA17')
y_pos = np.arange(len(objects))
performance = [120,80,60,40,20,18]
