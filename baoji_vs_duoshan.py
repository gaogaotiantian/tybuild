import matplotlib.pyplot as plt
from pylab import *

def Imp(extra_baoji, baoji, baojia, duoshan):
    if duoshan + baoji < 1:
        return extra_baoji*baojia / (1+baoji*baojia-duoshan*0.3)
    return extra_baoji*(baojia+0.3) / (baoji+duoshan+baoji*baojia-duoshan*0.3)

def ImpOrig(extra_baoji, baoji, baojia, duoshan):
    return extra_baoji*baojia / (1+baoji*baojia-duoshan*0.3)

if __name__ == "__main__":
    mpl.rcParams['font.sans-serif'] = ['SimHei'] #指定默认字体  
    mpl.rcParams['axes.unicode_minus'] = False #解决保存图像是负号'-'显示为方块的问题  
    fig = plt.figure()
    ax1 = fig.add_subplot(111)
    yb = []
    xa = []
    yc = []
    for duoshan in range(0, 35, 10):
        for p in range(60, 150, 1):
            yb.append(Imp(0.05, p/100.0, 1.8, duoshan/100.0))
            yc.append(ImpOrig(0.05, p/100.0, 1.8, duoshan/100.0))
            xa.append(p)
        ax1.plot(xa, yb)
        ax1.plot(xa, yc)
    plt.show()

