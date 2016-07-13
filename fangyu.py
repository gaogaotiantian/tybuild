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
    deltaRate = GetCriDefRate(currCriDef) - GetCriDefRate(prevCriDef)

    return deltaRate / (Cri/3150 + 1/CriPlus)

# Dodge
def GetDodgeRate(d):
    return d/(4350.0+d*0.7)

def GetDodgeImp(currDodge, prevDodge, cri, criDam):
    currDodgeRate = GetDodgeRate(currDodge)
    prevDodgeRate = GetDodgeRate(prevDodge)
    return (currDodgeRate - prevDodgeRate)*0.7 / (1 + cri*criDam - prevDodgeRate * 0.3) 

# Yuling
def GetYulingDamageRate(d):
    return 1-d/(d+3112.5)

def GetYulingImp(currYuling, prevYuling):
    return 1- GetYulingDamageRate(currYuling) / GetYulingDamageRate(prevYuling)
if __name__ == "__main__":
    print mpl.matplotlib_fname()
    DEF_CONST = 120*2
    HP_CONST = 432
    CRI_DEF_CONST = 54
    DODGE_CONST = 54
    YULING_CONST = 54
    fig = plt.figure()
    ax1 = fig.add_subplot(111)
    xa = []
    defense = []
    HP = []
    d = []
    defCri = []
    dodge = []
    yuling = []
    lastp = 0
    first = True
    for p in range(1, 100, 1):
        if first != True:
            xa.append(p)
            defense.append(GetDefImp(p*DEF_CONST, lastp*DEF_CONST, 0.75))
            HP.append(GetHPImp(p*HP_CONST, lastp*HP_CONST))
            defCri.append(GetCriDefImp(p*CRI_DEF_CONST, lastp*CRI_DEF_CONST, 0.5, 1.6))
            dodge.append(GetDodgeImp(p*DODGE_CONST, lastp*DODGE_CONST, 0.5, 1.6))
            yuling.append(GetYulingImp(p*YULING_CONST, lastp*YULING_CONST))
        else:
            first = False
        lastp = p
    ax1.set_xlabel(u"收益")
    fy, = ax1.plot(defense, xa, label=u"防御:" + str(DEF_CONST))
    hp, = ax1.plot(HP, xa, label=u"血量:" + str(HP_CONST))
    dc, = ax1.plot(defCri, xa, label=u"防暴:" + str(CRI_DEF_CONST))
    ds, = ax1.plot(dodge, xa, label=u"闪避:" + str(DODGE_CONST))
    yl, = ax1.plot(yuling, xa, label=u"御灵:" + str(YULING_CONST))
    ax1.set_xlim([0, 0.025])
    plt.legend(handles=[fy,hp,dc,ds,yl])
    plt.show()

