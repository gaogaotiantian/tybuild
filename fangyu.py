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
def GetDefImp(currDef, prevDef):
    return 1 - GetDamageRate(currDef) / GetDamageRate(prevDef)
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
def GetDodgeDamageRate(d):
    if d/(4410.0+d) > 0.9:
        return 0.9
    return d/(4410.0+d)

def GetDodgeImp(currDodge, prevDodge):
    return (currDodge-prevDodge)/4410.0*0.7

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
            defense.append(GetDefImp(p*DEF_CONST, lastp*DEF_CONST))
            HP.append(GetHPImp(p*HP_CONST, lastp*HP_CONST))
            defCri.append(GetCriDefImp(p*CRI_DEF_CONST, lastp*CRI_DEF_CONST, 0.6, 1.9))
            dodge.append(GetDodgeImp(p*DODGE_CONST, lastp*DODGE_CONST))
            yuling.append(GetYulingImp(p*YULING_CONST, lastp*YULING_CONST))
        else:
            first = False
        lastp = p
    ax1.set_xlabel(u"收益")
    fy, = ax1.plot(defense, xa, label=u"防御")
    hp, = ax1.plot(HP, xa, label=u"血量")
    dc, = ax1.plot(defCri, xa, label=u"防暴")
    ds, = ax1.plot(dodge, xa, label=u"闪避")
    yl, = ax1.plot(yuling, xa, label=u"御灵")
    plt.legend(handles=[fy,hp,dc,ds,yl])
    plt.show()

