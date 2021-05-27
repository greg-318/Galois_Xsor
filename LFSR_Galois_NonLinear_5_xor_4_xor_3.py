
# Составной генератор псевдослучайных двоичных последовательностей
# Нелинейный выход
# Конфигурация Галуа (5 xor 4 xor 3)
# Рисунок 2.5.1

# Регистр 1 (5 bit)
reg1=[1,0,1,0,1]
scheme1=[1,0,1,0,0]
gamma1=[]

# Регистр 2 (4 bit)
reg2=[1,0,1,1]
scheme2=[1,0,0,1]
gamma2=[]

# Регистр 3 (3 bit)
reg3=[0,1,1]
scheme3=[1,0,1]
gamma3=[]

# Общий выход составного генератора
gamma=[]

# Работа генератора (4096 циклов)
for i in range (1,4096):

    gamma.append((reg1[0]^reg1[4]^(reg1[2]&reg1[3]))^(reg2[0]^reg2[3]^(reg2[1]&reg2[2]))^(reg3[0]^reg3[2]^(reg3[0]&reg3[1])))

    gamma1.append(reg1[0]^reg1[4]^(reg1[2]&reg1[3]))
    s1=reg1[4]
    for j in range (4,0,-1):
        reg1[j]=(s1*scheme1[j])^reg1[j-1]
    reg1[0]=s1*scheme1[0]

    gamma2.append(reg2[0]^reg2[3]^(reg2[1]&reg2[2]))
    s2=reg2[3]
    for j in range (3,0,-1):
        reg2[j]=(s2*scheme2[j])^reg2[j-1]
    reg2[0]=s2*scheme2[0]

    gamma3.append(reg3[0]^reg3[2]^(reg3[0]&reg3[1]))
    s3=reg3[2]
    for j in range (2,0,-1):
        reg3[j]=(s3*scheme3[j])^reg3[j-1]
    reg3[0]=s3*scheme3[0]

# Выходные гаммы
print(gamma1)
print(gamma2)
print(gamma3)
print(gamma)