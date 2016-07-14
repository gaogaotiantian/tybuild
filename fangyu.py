# coding:utf-8
import matplotlib.pyplot as plt
import matplotlib as mpl
# Def
def GetDefRate(d):
    if d/(3360.0+d) > 0.9:
        return 0.9
    return d/(3360.0+d)
def GetDamageRate(d):
    return 1-GetDefRate(d)
def GetDefImp(currDef, prevDef, pofang):
    return 1 - GetDamageRate(currDef*(1-pofang)) / GetDamageRate(prevDef*(1-pofang))
# HP
def GetHPImp(currHP, prevHP):
    return 1 - float(prevHP) / currHP

# CriDef
def GetCriDefRate(d):
    if d/(4410.0+d) > 0.9:
        return 0.9
    return d/(4410.0+d)
def GetCriDefImp(currCriDef, prevCriDef, Cri, CriPlus):
    prevRate = GetCriDefRate(prevCriDef)
    currRate = GetCriDefRate(currCriDef) 
    deltaRate = currRate - prevRate 

    return deltaRate / ((Cri-prevRate) + 1/CriPlus)

# CriDec
def GetCriDecRate(d):
    return d/(1050+d)
def GetCriDecImp(currCriDec, prevCriDec, Cri, CriPlus):
    prevRate = GetCriDecRate(prevCriDec)
    currRate = GetCriDecRate(currCriDec)
    deltaRate = currRate - prevRate

    return deltaRate / ((CriPlus - prevRate) + 1/Cri)

# Dodge
def GetDodgeRate(d):
    return d/(4350.0+d*0.7)

def GetRealDodgeRate(d, cri):
    if d+cri < 1:
        return d
    else:
        return d/(d+cri)

def GetDodgeImp(currDodge, prevDodge, cri, criDam):
    currDodgeRate = GetRealDodgeRate(currDodge, cri)
    prevDodgeRate = GetRealDodgeRate(prevDodge, cri)
    return (currDodgeRate - prevDodgeRate)*1.7 / (1 + cri*criDam - prevDodgeRate * 0.7) 

# Yuling
def GetYulingDamageRate(d):
    return 1-d/(d+3112.5)

def GetYulingImp(currYuling, prevYuling):
    return 1- GetYulingDamageRate(currYuling) / GetYulingDamageRate(prevYuling)

def GetVal(xo, yo, x, const):
    ret_x = []
    ret_y = []
    assert(len(xo) == len(yo))
    lastx = xo[0]
    for x_curr in x:
        for i in range(1, len(xo)):
            thisx = xo[i]
            lastx = xo[i-1]
            if lastx <= x_curr <= thisx or lastx >= x_curr >= thisx:
                ret_x.append(x_curr)
                ret_y.append((((yo[i] - yo[i-1])/(xo[i]-xo[i-1]))*(x_curr-lastx)+yo[i-1])*const)

    return [ret_x, ret_y]

if __name__ == "__main__":
    print mpl.matplotlib_fname()
    DEF_CONST = 120
    HP_CONST = 432
    CRI_DEF_CONST = 54
    DODGE_CONST = 54
    YULING_CONST = 54
    fig = plt.figure()
    ax1 = fig.add_subplot(111)
    xa = []
    defense_0 = []
    defense_75 = []
    HP = []
    d = []
    defCri_s = []
    defCri_l = []
    dodge = []
    yuling = []
    lastp = 0
    first = True
    for p in range(1, 170, 1):
        if first != True:
            xa.append(p)
            defense_0.append(GetDefImp(p*DEF_CONST, lastp*DEF_CONST, 0))
            defense_75.append(GetDefImp(p*DEF_CONST, lastp*DEF_CONST, 0.75))
            HP.append(GetHPImp(p*HP_CONST, lastp*HP_CONST))
            defCri_s.append(GetCriDefImp(p*CRI_DEF_CONST, lastp*CRI_DEF_CONST, 0.3, 1.0))
            defCri_l.append(GetCriDefImp(p*CRI_DEF_CONST, lastp*CRI_DEF_CONST, 0.75, 1.9))
            dodge.append(GetDodgeImp(p*DODGE_CONST, lastp*DODGE_CONST, 0.7, 1.9))
            yuling.append(GetYulingImp(p*YULING_CONST, lastp*YULING_CONST))
        else:
            first = False
        lastp = p
    print "d0:",GetVal(defense_0, xa, [x*0.001 for x in range(0, 20, 1)], DEF_CONST)
    print "d75:",GetVal(defense_75, xa, [x*0.001 for x in range(0, 20, 1)], DEF_CONST)
    print "hp:",GetVal(HP, xa, [x*0.001 for x in range(0, 20, 1)], HP_CONST)
    print "fb1:",GetVal(defCri_s, xa, [x*0.001 for x in range(0, 20, 1)], CRI_DEF_CONST)
    print "fb2:",GetVal(defCri_l, xa, [x*0.001 for x in range(0, 20, 1)], CRI_DEF_CONST)
    print "sb:",GetVal(dodge, xa, [x*0.001 for x in range(0, 20, 1)], DODGE_CONST)
    print "yl:",GetVal(yuling, xa, [x*0.001 for x in range(0, 20, 1)], YULING_CONST)
    ax1.set_xlabel(u"收益")
    fy1, = ax1.plot(defense_0, xa, label=u"防御(0%):" + str(DEF_CONST))
    fy2, = ax1.plot(defense_75, xa, label=u"防御(75%):" + str(DEF_CONST))
    hp, = ax1.plot(HP, xa, label=u"血量:" + str(HP_CONST))
    dc1, = ax1.plot(defCri_s, xa, label=u"暴防(30%, 100%):" + str(CRI_DEF_CONST))
    dc2, = ax1.plot(defCri_l, xa, label=u"暴防(75%, 190%):" + str(CRI_DEF_CONST))
    ds, = ax1.plot(dodge, xa, label=u"闪避:" + str(DODGE_CONST))
    yl, = ax1.plot(yuling, xa, label=u"御灵:" + str(YULING_CONST))
    ax1.set_xlim([0, 0.025])
    plt.legend(handles=[fy1,fy2,hp,dc1,dc2,ds,yl])
    plt.show()

