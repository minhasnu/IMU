import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation



fig = plt.figure()
#creating a subplot 
ax1 = fig.add_subplot(1,1,1)

def animate(i):
    data = open('log.txt','r').read()
    lines = data.split('\n')
    xs = []
    ys = []
   
    for line in lines:
        if len(line) > 1:
            # print(line)
            y,x  = line.split(',') # Delimiter is comma    
            xs.append(float(x))
            ys.append(float(y))
    open("log.txt", "w").close()
   
    
    ax1.clear()
    ax1.plot(xs, ys)

    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.title('Live graph with matplotlib')	
	
    
ani = animation.FuncAnimation(fig, animate, interval=10) 
plt.show()





