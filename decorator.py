def decorator(funcao):
    def funcao_superior():
        print('decorator')
        funcao()

    return funcao_superior

@decorator
def minha_funcao():
    print('função base')

minha_funcao()

def decorator_classe(funcao):
    def funcao_superior(*arg, **kwargs):
        print('decorator')
        funcao(*arg, **kwargs)
    return funcao_superior


class minha_classe:
    
    @decorator_classe
    def metodo(self):
        print('minha classe')

cl = minha_classe()
cl.metodo()
