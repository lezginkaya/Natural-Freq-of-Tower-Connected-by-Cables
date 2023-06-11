import numpy as np
import pandas as pd
import xlsxwriter

E=200000000000 #modulus of elasticity of beam
#dimensions of beam
b=0.05
h=0.05
L=20
L1=10
x0=30
mtotal=((b*h)*(L+L1))*775
Itow=(b*h**3)/12
ktow=(3*E*Itow)/(L+L1)**3
teta=np.arctan2(L,x0)
teta_degree=np.rad2deg(teta)
Lc=np.cos(teta)*x0
yl1_yl=(L1**2*(3*L-L1))/(2*L**3)
list1=[]
list2=[]
list3=[]
for D in range(10,110,10):
    d=D/1000 #dia of cable
    list1.append(d)
    Ac=(np.pi*(d**2))/4
    kc=(Ac*E)/Lc
    keq_c=kc*(np.cos(teta)**2)
    keq_system=ktow+(4*keq_c*(yl1_yl)**2)
    w=np.sqrt(keq_system/mtotal)
    wn=w/60
    wn=round(wn,2)
    period=1/wn
    list3.append(period)
    list2.append(wn)
    data = pd.DataFrame({"Dia of cable": list1,
                         "Natural Freq of the system": list2,
                         "Period": list3})

    dataexcel = pd.ExcelWriter("Tower Freq.xlsx",
                               engine="xlsxwriter")

    data.to_excel(dataexcel, sheet_name="Tower Freq")

    dataexcel.close()
















