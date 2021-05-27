
# Генератор псевдослучайных двоичных последовательностей
# Составной генератор: Фибоначчи (4) ^ Галуа (3)

reg_F=[1,0,0,0]
reg_G=[1,0,0]

scheme_F=[0,0,1,1]
scheme_G=[1,1,0]

gamma_F=[]
gamma_G=[]
gamma=[]

for i in range (1,256):

    gamma_F.append(reg_F[3])
    gamma_G.append(reg_G[2])
    gamma.append(reg_F[3]^reg_G[2])

    F_s=0
    for j in range (3,-1,-1):
        F_s=F_s^(reg_F[j]*scheme_F[j])

    for j in range (3,-1,-1):
        reg_F[j]=reg_F[j-1]

    reg_F[0]=F_s


    G_s=reg_G[2]
    for j in range (2,0,-1):
        reg_G[j]=(G_s*scheme_G[j])^reg_G[j-1]

    reg_G[0]=G_s*scheme_G[0]



print(gamma_F)
print(gamma_G)
print(gamma)