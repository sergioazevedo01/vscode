
acum = 0

for n in range(2, 51, 2) :
        acum += n
        print(n, end='\033[31m -> \033[0m')         
print("\033[31mACABOU\033[0m")
print(f"\033[33mAcumulado :\033[0m {acum}")
