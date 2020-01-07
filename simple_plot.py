import matplotlib.mlab as mlab
import matplotlib.pyplot as plt    

#load data first
bins = np.linspace(0, 2, 50) #bin density
plt.subplot(2, 1, 1) #plot multiple figures in one canvas
plt.hist(np.array(vec_label), facecolor='blue', bins='auto', histtype='bar', bins)
plt.xlabel('Label')
plt.ylabel('Number')
plt.title(r'$\mathrm{Histogram of Labels}$')
plt.grid(True)

print(np.unique(np.array(vec_label)))
axes = plt.gca()
axes.set_xlim([33,40])
#axes.set_ylim([0,150000])

plt.savefig('label_hist.png')
plt.figure(figsize=(8, 8)). #image resolution 800 by 800

#draw mulitple curves
t = np.linspace(1, 200000, num=200)
plt.plot(t, data, label='--1')
plt.legend()

#to display multi figures use this at the end of the code
plt.show()
