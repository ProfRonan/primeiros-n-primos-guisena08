numero = int(input('Digite um numero: '))
def primo(n):
    if n <2:
        return False
    for i in range (2,n):
        if n % i == 0:
            return False
    return True
count = 0
i = 2
while count < numero:
    if primo(i):
        print(i)
        count +=1
    i +=1    

