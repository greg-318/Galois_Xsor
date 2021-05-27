# Гамма

# Ввод гаммы из файла
import pickle
f=open(r'GammaFile.txt','rb')
new_gamma=pickle.load(f)
f.close()

L=0
for index in new_gamma:
    L=L+1
print("Длина гаммы =",L)

print("Кол-во'0'в гамме =",new_gamma.count(0))
print("Кол-во'1'в гамме =",new_gamma.count(1))

i=0

series_0=0
series_1=0

series_00=0
series_01=0
series_10=0
series_11=0

series_000=0
series_001=0
series_010=0
series_011=0
series_100=0
series_101=0
series_110=0
series_111=0

series_x=0

for index in new_gamma:

    if(new_gamma[i:i+2]==[0,1]):
        series_0=series_0+1

    if(new_gamma[i:i+2]==[1,0]):
        series_1=series_1+1


    if(new_gamma[i:i+3]==[0,0,1]):
        series_00=series_00+1

    if(new_gamma[i:i+3]==[0,1,0]):
        series_01=series_01+1

    if(new_gamma[i:i+3]==[1,0,1]):
        series_10=series_10+1

    if(new_gamma[i:i+3]==[1,1,0]):
        series_11=series_11+1

    if(new_gamma[i:i+4]==[0,0,0,1]):
        series_000=series_000+1

    if(new_gamma[i:i+4]==[0,0,1,0]):
        series_001=series_001+1

    if(new_gamma[i:i+4]==[0,1,0,1]):
        series_010=series_010+1

    if(new_gamma[i:i+4]==[0,1,1,0]):
        series_011=series_011+1

    if(new_gamma[i:i+4]==[1,0,0,1]):
        series_100=series_100+1

    if(new_gamma[i:i+4]==[1,0,1,0]):
        series_101=series_101+1

    if(new_gamma[i:i+4]==[1,1,0,1]):
        series_110=series_110+1

    if(new_gamma[i:i+4]==[1,1,1,0]):
        series_111=series_111+1

    if(new_gamma[i:i+14]==[0,0,0,0,0,0,0,0,0,0,0,0,0,1]):
        series_x=series_x+1

    i=i+1

print("Кол-во серий '0'в гамме =",series_0)
print("Кол-во серий '1'в гамме =",series_1)

print("Кол-во серий '00'в гамме =",series_00)
print("Кол-во серий '01'в гамме =",series_01)
print("Кол-во серий '10'в гамме =",series_10)
print("Кол-во серий '11'в гамме =",series_11)

print("Кол-во серий '000'в гамме =",series_000)
print("Кол-во серий '001'в гамме =",series_001)
print("Кол-во серий '010'в гамме =",series_010)
print("Кол-во серий '011'в гамме =",series_011)
print("Кол-во серий '100'в гамме =",series_100)
print("Кол-во серий '101'в гамме =",series_101)
print("Кол-во серий '110'в гамме =",series_110)
print("Кол-во серий '111'в гамме =",series_111)
print("Кол-во серий 'xxx'в гамме =",series_x)

series_max=1
max=0

i=0
for index in new_gamma:

    if (i+1)<L:
        if new_gamma[i+1]==new_gamma[i]:
            series_max=series_max+1
        else:

            if series_max>max:
                max=series_max
            series_max=1
    i=i+1

print(max)
print(series_max)

