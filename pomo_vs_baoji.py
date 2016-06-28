# -*- coding: utf-8 -*-
import numpy as np
from sympy import *
import matplotlib.pyplot as plt
def GetImp(b, total, fangyu):
    x = Symbol('x')
    y = Symbol('y')
    d = Symbol('d')
    p = Symbol('p')
    expr_p = (1-(1-p)*d/(3360+(1-p)*d))/(1-d/(3360+d))
    if b < 525:
        pp = total - b
        expr = (1+x*0.5/(3150))
    elif b < 2100:
        pp = total - 2*b + 525
        expr = (1+3*x*x/(3150*3150))
    elif b < 3150:
        pp = total - b - 1575
        expr = (1+x*2/(3150))
    else:
        return [-1, -1]
    if pp < 0:
        return [-1, -1]
    elif pp > 4780*0.75:
        return [-1, -1]
    pp = pp / 4780.0
    return [pp, expr.subs({x:b}).evalf() * expr_p.subs({p:pp, d:fangyu}).evalf()]


if __name__ == "__main__":
    for total in range(2000, 5500, 500):
        fig = plt.figure()
        ax1 = fig.add_subplot(111)
        ax2 = ax1.twinx()
        for fangyu in range(5000, 30000, 5000):
            xa = [] 
            ya = []
            ya2 = []
            for x in range(0, total+20, 4):
                p, imp = GetImp(x,total,fangyu)
                if imp != -1:
                    xa.append(x/3150.0)
                    ya2.append(p)
                    ya.append(imp)
            ax1.plot(xa, ya)
            ax1.set_xlabel("Critical Rate")
            ax1.set_ylabel("Damage Expectation")
            ax2.plot(xa, ya2)
            ax2.set_ylabel("Def Break")
        plt.show()

