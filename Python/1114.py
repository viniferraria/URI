while True:
    x = int(input())
    password = [2002]
    if x in password:
        print("Acesso Permitido")
        break
    else:
        print("Senha Invalida")