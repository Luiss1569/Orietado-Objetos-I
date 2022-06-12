
class NomeDuplicado(Exception):
    pass

class MenorDeIdade(Exception):
    pass

class IdadeInvalida(Exception):
    pass

class EmailInvalido(Exception):
    pass


class Usuario:
    def __init__(self, nome, email):
        self.__nome = nome
        self.__email = email
        
    def getNome(self):
        return self.__nome
    
    def getEmail(self):
        return self.__email

if __name__ == "__main__":
    lista = [
        ("Paulo", "paulo@gmail.com", 21),
        ("Maria", "maria@gmail.com", 19),
        ("Antonio", "antonio@gmail.com", 25),
        ("Pedro", "pedro@gmail.com", 15),
        ("Marisa", "marisa@",23),
        ("Ana", "ana@gmail.com", -22),
        ("Maria", "maria@gmail.com", 27)
    ]
    
    cadastro = {}
    
    for nome, email, idade in lista:
        try:
            if nome in cadastro:
                raise NomeDuplicado()
            if idade < 0:
                raise IdadeInvalida()
            if idade < 18:
                raise MenorDeIdade()
            if len(email.split("@")) > 2 or not email.split("@")[0] or not email.split("@")[1]:
                raise EmailInvalido()
        except (NomeDuplicado):
            print("NomeDuplicado ", nome)
        except (IdadeInvalida):
            print("IdadeInvalida ", nome, idade)
        except (MenorDeIdade):
            print("MenorDeIdade ", nome, idade)    
        except (EmailInvalido):
            print("EmailInvalido ", nome, email)
        else:
            cadastro[nome] = Usuario(nome, email)
            print("Usuario Cadastrado", nome)
print("Usuarios cadastrados")