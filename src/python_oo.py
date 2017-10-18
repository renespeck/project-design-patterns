'''

## 1. Roteiro


    # * 2. Objetos e Tipos de dados

    # * 3. Nomes

    # * 3.1. Objeto None

    # * 4. Passagem de Parâmetros

    # * 5. Classes

    # * 5.1 Instâncias, Instância de Atributos e Métodos

    # * 5.2 Exemplo de classe

    # * 5.3 Método __init__

    # * 5.4 Propriedades, Acessores e Modificadores

    # * 5.5 Sobrecarga de Operadores

    # * 5.6 Sobrecarga de Operadores

    # * 6 Sobrecarga de Operadores

    # * 7 Herança e Polimorfismo

    # * 7.1 Derivação e Herança




## 2. Objetos e Tipos de dados

    # Um objeto em linguagem de programação abstrata representa a posição onde será armazenada.
    # Os objetos em Python apresentam os seguintes atributos:

    # * Tipo: O tipo de um objeto determina os valores que o objeto pode receber e as operações que podem ser executadas nesse objeto.

    # * Valor: O valor de um objeto é o índice de memória ocupada por essa variável.
    #           Como os índices das posições da memória são interpretados, isto é determinado pelo tipo da variável.

    # * Tempo de vida: A vida de um objeto é o intervalo de tempo de execução de um programa em Python,é durante este tempo que o objeto existe.

    # Python define uma extensa hierarquia de tipos.
    # Esta hierarquia inclui os tipos numéricos (tais como int, float e complex), 
    # seqüências (tais como a tupla e a lista), funções (tipo função), classes e métodos (tipos classobj e instancemethod)
    # e as instâncias da classe (tipo instance).

## 3. Nomes e Tipos

    # A fim de utilizar um objeto em um programa em Python, esse objeto deve ter um nome.
    # O nome de um objeto é uma variável usada para identificar esse objeto em um programa.
    # Em Python, um objeto não pode ter zero, um ou mais no nome.

    # Veja

i = 57

    # Esta indicação cría um objeto com nome i e liga vários atributos com esse objeto.
    # O tipo do objeto é int e seu valor é 57.

    # Alguns atributos de um objeto, tal como seu tipo, são limitados quando o objeto é criado e não podem serer mudados.
    # Isto é chamado ligação estática.

    # As ligações para outros atributos de um objeto, tais como seu valor, podem ser mudados durante a execução do programa onde o objeto está.
    # Isto é chamado de ligação dinâmica.

    # Veja:

'''

i = int(57)
'''

#     Se nós seguirmos esta indicação com uma indicação de atribuição como:
'''

j = i
'''

#     então os nomes i e j são o mesmo objeto!

#     A comparação ficaria:

'''

if i == j:
    print("valores iguais")
'''


    este é o teste se o valor do objeto i é o mesmo valor do objeto j (desde que sejam de mesmo valor).
    Entretanto, é possível para dois objetos distintos terem o mesmo valor.
    Para testar se os dois nomes são um mesmo objeto, é necessário utilizar o operador **is**:

'''

if i is j:
    print("mesmo objeto")
'''


    Para saber se os tipos de dados de dois objetos são iguais é necessário:
'''

i = 57
j = 47

if type(i) == type(j):
    print("mesmo tipo")

    '''
    # 3.1. Objeto None

    Em Python, um nome sempre será um objeto.
    Entretanto, às vezes é conveniente usar um nome chamado None ou nulo.
    Python fornece um tipo especial de objeto para esta finalidade chamada NoneType.
    Sempre há somente um objeto do tipo NoneType e o nome desse objeto é **None**.

    Nós podemos explicitamente atribuir um nome ao None
    '''


f = None
    '''


    Também, nós podemos testar explicitamente se um nome é None como:
    '''


if f is None:
    print("é nulo")

    '''

    # 4. Passagem de Parâmetros

    A passagem de parâmetro é um método em que os parâmetros são transferidos entre métodos quando um método chama outro. Python fornece somente um método da passagem de parâmetro, passagem-por-referência.

    Considere o par de funções definidos abaixo.
    Na linha 4, o método um chama o método dois. 
    Em geral, cada chamada do método inclui a lista de argumentos, possivelmente vazio.
    Os argumentos especificados em uma chamada do método são chamados parâmetros reais. 
    Neste caso, há somente um parâmetro divisor, o x.

    '''

def um():
    x = 1
    print(x)
    dois(x)
    print(x)

def dois(y):
    print(y)
    y = 2
    print(y)
    '''

    Na linha 7 o método dois é definido como um método que aceita um único argumento y.
    Os argumentos que aparecem na definição do método são chamados parâmetros formais.

    A semântica da passagem-por-referência é: O efeito da definição do parâmetro formal deve criar 
    um nome no namespace local da função e ligá-lo então o nome ao objeto pelo parâmetro divisor.
    Por exemplo, no método dois o parâmetro formal é y.
    Quando o método é chamado, o nome y está atribuído ao objeto x.

    A saída do método um ficará:

    1 1 2 1

    E a saída do método dois com o parâmetro 3 ficará:

    3 2

    #5. Classes

    Uma classe define uma estrutura de dados que contenha instância de atributos, instância de métodos e classes aninhadas. 
    Em Python a classe de um objeto e o tipo de um objeto são sinônimos. 
    Cada objeto do Python tem uma classe (tipo) que é derivada diretamente ou indiretamente da classe interna do objeto do Python.
    A classe (tipo) de um objeto determina o que é e como pode ser manipulado. Uma classe encapsula dados, operações e semântica.

    A classe é o que faz com que Python seja uma linguagem de programação orientada a objetos. 
    Classe é definida como um agrupamento de valores sua gama de operações. 
    As classes facilitam a modularidade e abstração de complexidade. 
    O usuário de uma classe manipula objetos instanciados dessa classe somente com os métodos fornecidos por essa classe.

    Frequentemente classes diferentes possuem características comuns.
    As classes diferentes podem compartilhar valores comuns e podem executar as mesmas operações. 
    Em Python tais relacionamentos são expressados usando derivação e herança.

    # 5.1 Instâncias, Instância de Atributos e Métodos

    Objetos são instanciados pelas classes. Cada instância (objeto) em uma programa Python tem seu próprio namespace.

    Um classe criada é chamada de classe objeto (tipo classobj). 
    Os nomes no namespace da classe objeto são chamados de atributos da classe. 
    Funções definidas dentro de uma classe são chamadas de métodos.

    Quando um objeto é criado, o namespace herda todos os nomes do namespace da classe onde o objeto está. 
    O nome em um namespace de instância é chamado de atributo de instância.

    Um método é uma função criada na definição de uma classe. 
    O primeiro argumento do método é sempre referenciado no início do processo.

    Por convenção, o primeiro argumento do método tem sempre o nome self.
    Portanto, os atributos de self são atributos de instância da classe.

    # 5.2 Exemplo de classe

    Agora vamos definir uma classe para representar carros.

    Definicao: Classe chamada Racional que utiliza dois atributos de instância, 
    _divisor and _dividendo, para representar a divisor e a dividendo de um carro (respectivamente). 

    A classe Racional definida é baixo:
'''

class Racional(object):
    def __init__(self, divisor, dividendo):
        self._divisor = divisor
        self._dividendo = dividendo
    '''

    Toda instância da classe Racional contém seus próprios atributos de instância:

    '''

c = Racional(1,2)
d = Racional(2,2)
e = Racional(3,2)

print(c._divisor)
print(d._divisor)
print(e._divisor)
    '''

    Ambas c e d se referem a duas instâncias diferentes da classe Racional. 
    Portanto, cada um dos dois _carro e _dividendo tem suas próprias instâncias de atributos.

    O atributo de instância de um objeto é acessado utilizando o operador .(ponto). 
    Por exemplo, c._carro referencia _carro, um atributo de instância de c e 
    d._dividendo referencia _dividendo, um atributo de isntância de d.


    # 5.3 Método __init__

    O método init é um método especial para classes. 
    O init é um método construtor, ele inicializa o estado de um objeto.
    O método init é invocado sempre que uma nova instância de uma classe é criada.
    Na verdade não estamos apenas definindo o método init mais sobrescrevendo o init da classe base(built-in).
    O método init na classe Racional é definido assim:
    '''

c = Racional(2, 3)

    # O efeito deste estado é equivalente a isto:

c = object.__new__(Racional)
Racional.__init__(c, 2, 3)

    '''
    O método new pertence a classe base built-in(interno do Python) e é chamada para criar uma nova instância de object.
    O método init dentro da classe Racional é chamada para inicializar o estado da nova instância.

    # 5.4 Propriedades, Acessores e Modificadores

    Continuando com o exemplo da classe Racional.
    Incluímos quatro métodos: getDivisor, setDivisor, getDividendo e setDividendo e duas propriedades: divisor e dividendo.
    '''

class Racional(object):
    def getDivisor(self):
        return self._divisor

    def setDivisor(self, valor):
        self._divisor = valor

    divisor  = property(
            fget = getDivisor,
            fset = setDivisor)

    def getDividendo(self):
        return self._dividendo

    def setDividendo(self, valor):
        self._dividendo = valor

    dividendo = property(
            fget = getDividendo,
            fset = setDividendo)

    '''
    Os métodos getDivisor e setDividendo promovem o acesso dos atributos _divisor e _dividendo, respectivamente.

    Um método que acessa uma instância mas não modifica a instância é chamado de accessor ou acessor.
    Portanto, getDivisor e getDividendo são accessors.

    Os métodos setDivisor e setDividendo promovem a modificação dos atributos _divisor e _dividendo, respectivamente.
    Um método que modifica uma instância é um modificador ou mutador. Portanto, setDivisor e setDividendo são modificadores.

    O operador .(ponto) é utilizado para especificar o objeto em que o método também é invocado. Por exemplo:
    '''

c.setDivisor(2)
print(c.getDivisor())

    # isto é equivalente a:

Racional.setDivisor(c, 2)
print(Racional.getDivisor(c))

    '''
    Uma propriedade é um atributo de classe que promove o método de acesso e/ou método modificador.
    O argumento fget é uma propriedade específica do método accessor chamada de "getter" e o argumento 
    fset é uma propriedade específica do método modificador chamada de "setter".

    Por exemplo, a propriedade getter de 'divisor' é o método accessor getDivisor e a propriedade setter 
    de 'divisor' é um método modificador setDivisor. 
    Similarmente, a propriedade getter de 'dividendo' é getDividendo e a propriedade setter de 'dividendo' é setDividendo.

    Você pode usar propriedades instanciando atributos e utilizando a notação de invocação dos métodos accessor e modificador.
    Novamente, o operador .(ponto) é utilizado para especificar o objeto, por exemplo:
    '''
c.dividendo = 3
print(c.dividendo)

    '''    
    é equivalente a:    
    '''

Racional.setDividendo(c, 3)

print(Racional.getDividendo(c))
    '''
    # 5.5 Sobrecarga de Operadores

    Abaixo um exemplo de sobrecarga:
    '''

    def __str__(self):
      return str(self.divisor) + '/' + str(self.dividendo)

    def __mul__(self, outro):
        divisor = self.divisor*outro.divisor
        dividendo = self.dividendo*outro.dividendo
        return Racional(divisor, dividendo)

    def __add__(self, outro):
        divisor = self.divisor * outro.dividendo + outro.divisor * self.dividendo
        dividendo = self.dividendo * outro.dividendo
        return Racional(divisor, dividendo)

    '''
    Por exemplo: Para sobrecaregar os operadores + e * dentro da classe Racional
    definimos os métodos chamados de add, sub e mul, respectivamente.

    Utilizamos agora as variáveis c, d, e, na expressão:

    c + d * e
    é equivalente a:
    '''

Racional.__add__(c, Racional.__mul__(d, e))
    '''
    Alguns métodos que poderiamos sobrecarregar:

    * __add__: Adição. A+B
    * __sub__: Sutração. A-B
    * __mul__: Multiplicação. A*B
    * __div__: Divisão. A/B
    * __mod__: Resto da divisão. A%B
    * __pos__: Identidade. +A
    * __neg__: Negativo. -A
    * __abs__: Absoluto. |A|

    # 5.6 Métodos Estáticos

    Um método estático é uma atribuição a classe que não precisa do primeiro argumento para ser instanciado na classe.
    (Normalmente os métodos precisam do primeiro argumento como self, para ser uma instância da classe).
    '''

@staticmethod
def main(*argv):
    "Programa para o tesste do Racional"
    c = Racional(2, 3)
    print(c)

    c.divisor = 1
    c.divisor = 2
    print(c)

    c = Racional(1,2)
    d = Racional(3,4)
    print(c, d, c+d, c*d)
    return 0

    '''
    O exemplo acima definiu o método main na classe Racional.
    Este método é um teste simples para a classe Racional.
    Por exemplo, este método estático poderia ser invocado assim:
    '''

import sys


if __name__ == "__main__":
    sys.exit(Racional.main(*sys.argv))

    '''
    # 6 Classes Aninhadas

    Em Python é possível definir uma classe dentro de outra, 
    chamada de classes aninhadas.

    Veja:
    '''

class A(object):
    def __init__(self):
        self.y = 0

    class B(object):

        def __init__(self):
            self.x = 0

        def f(self):
                print('called chained class')
    '''
    Uma classe aninhada comporta-se como qualquer "classe externa" (não-aninhada).
    Pode conter métodos e atributos, e pode ser instanciada assim:
    '''

obj = A.B()

    '''
    Este exemplo cria uma nova instância da classe B. Uma vez tendo B instanciado, nós podemos invocar o método f utilizando:
    '''

obj.f()

    '''
    Note que não é necessário instanciar a classe externa A para criar uma instância da classe interna.

    Os métodos de uma classe aninhada podem acessar os atributos da classe interna mas não das classes externas,
    o método f pode acessar o atributo x do exemplo acima, mas não pode acessar o atributo y.

    # 7 Herança e Polimorfismo

    # 7.1 Derivação e Herança

    Esta seção revê o conceito de classe derivada. 
    As classes derivadas são uma característica extremamente útil em Python
    porque permitem que o programador defina classes novas estendendo classes existentes.
    Usando classes derivadas, o programador pode explorar as comunalidades que existem entre as classes de um programa.
    As classes diferentes podem compartilhar valores e operações.

    A derivação é a definição de uma classe nova estendendo uma classe existente.
    A classe nova é chamada de classe derivada e a classe existente de quem é derivada é chamada de classe base.

    Em Python, uma classe deve estender pelo menos uma classe base. 
    Se uma classe estender mais de uma classe base, esta forma uma **herança múltipla**.

    Python suporta classes clássicas (old-style classes) e classes de novo-estilo (new-style classes).
    Uma new-style class é uma classe que é derivada da classe interna do objeto.
    Uma old-style class é uma classe que não tem uma classe base ou uma que é derivada somente de outras classes old-style.

    Considere a classe Pessoa e a classe Pais abaixo.
    Porque Pais também são Pessoas, a classe Pai é derivada da classe Pessoa.
    A derivação em Python é indicada incluindo o(s) nome(s) da class(es) base em
     parênteses na declaração da classe derivada.
    '''

class Pessoa(object):
    FEMALE = 0
    MALE = 1

    def __init__(self, nome, idade):
        super(Pessoa, self).__init__()
        self._nome = nome
        self._idade = idade

    def __str__(self):
        return str(self._nome)

class Pais(Pessoa):

    def __init__(self, nome, idade, crianca):
        super(Pais, self).__init__(nome, idade)
        self._crianca = crianca

    def getCrianca(self, i):
        return self._crianca[i]

    def __str__(self):
        pass

    '''
    Uma classe derivada herda todos os atributos de sua classe base.
    Isto é, a classe derivada contém todos os atributos da classe contidos na classe base e a 
    classe derivada suporta todas as operações fornecidas pela classe base.
    Por exemplo, veja:
    '''

p = Pessoa() 
q = Pais()

    '''
    Assim p é uma Pessoa, tem os atributos _nome e _idade e o método str.
    Além disso, a classe Pais é derivado de Pessoa, então o objeto q também é uma instância de atributos _nome _idade 
    e do método str.

    Uma classe derivada pode estender a classe base de diversas maneiras:
        Os novos atributos podem ser usados
        os novos métodos podem ser definidos
         e os métodos existentes podem ser sobrescritos. 

     Por exemplo, a classe Pais adiciona uma atributo _crianca e um método getChild.

    Se um método for definido em uma classe derivada que tenha o mesmo nome que um método na classe base,
    o método na classe derivada sobrescreve ele na classe base.
    Por exemplo, o método str na classe Pais sobrescreve o método str na classe Pessoa.
    Conseqüentemente, str(p) invoca Pessoa.str , visto que o str(q) invoca Pais.str .

    Uma instância de uma classe derivada pode ser usada em qualquer lugar em um programa onde uma instância da 
    classe base possa ser usado. 
    
    Por exemplo, isto significa que a classe Pais pode ser passado como um parâmetro real a um método que espere 
    receber uma Pessoa.

    # 7.2 Polimorfismo

    Polimorfismo significa ter algo único em vários lugares.
    O polimorfismo é usado em classes distintas compartilhando funções em comum.
    Porque as classes derivadas são distintas, suas execuções podem diferir.
    Entretanto, as classes derivadas compartilham de uma relação comum, instâncias daquelas classes são usadas 
    exatamente na mesma maneira.


    # 7.2.1 Objetos Gráficos

    Considere um programa para criar desenhos simples. 
    Suponha que o programa forneça vários objetos gráficos primitivos, tais como círculos, retângulos e quadrados. 
    O programador seleciona os objetos desejados e invoca-os para extrair, apagar ou movê-los. 
    Idealmente, todos os objetos gráficos suportam os mesmos tipos de operações. Não obstante, 
    a maneira que as operações são executadas varia de um objeto a outro.

    Nós executamos assim: definimos uma classe que representa as operações comuns fornecidas por todos os objetos gráficos. 
    O programa define a classe ObjetoGrafico. Esta classe fornece quatro métodos, init , desenho, apaga e movePara.
    '''


class ObjetoGrafico(object):
    def __init__(self, centro):
        super(ObjetoGrafico, self).__init__()
        self._centro = centro

    @abstractmethod
    def desenha(self):
        pass

    def apaga(self):
        self.setPenColor(self.BACKGROUND_COLOR)
        self.desenha()
        self.setPenColor(self.FOREGROUND_COLOR)

    def movePara(self, p):
        self.apaga()
        self._centro = p
        self.desenho()
    '''

    O método desenho é invocado a fim de extrair um objeto gráfico. O método apaga é invocado a fim de 
    apagar um objeto gráfico. O método moverPara é usado para mover um objeto para uma posição especifica 
    no desenho. O argumento do método moverPara é um ponto. O programa abaixo define a classe do ponto que 
    representa uma posição em um desenho.

    A classe ObjetoGrafico tem um único atributo _centro, que é um ponto que representa a posição em um 
    desenho no ponto central do objeto gráfico.

    O exemplo abaixo mostra uma execução possível para o método apaga: neste caso supomos que a imagem 
    extraída está usando uma caneta imaginária.

    Assumindo que nós sabemos extrair um objeto gráfico, nós podemos apagar o objeto mudando a cor da caneta 
    de modo que combine a cor do fundo e então redesenhamos o objeto.

    Uma vez que nós podemos apagar um objeto, mais fácil ainda será movê-lo.

    Nós vimos que a classe ObjetoGrafico fornece execuções para os métodos apaga e movePara. Entretanto, a 
    classe não fornece uma execução para o método desenha. Então o método é declarado para ser abstrato. 
    Nós fazemos isto porque até que nós saibamos que tipo de objeto é, nós não podemos desenhá-lo!

    Considere a classe Circulo abaixo. A classe Circulo estende a classe ObjetoGrafico. Conseqüentemente, 
    herda o atributo centro e os métodos apaga e movePara. A classe Circulo adiciona um atributo _raio que 
    sobrescreve o método desenha. O corpo do método desenha não é mostrado no exemplo, entretanto, nós vamos 
    assumir um desenho de um circulo com um raio e o ponto centro dados.
    '''


class Circulo(ObjetoGrafico):
    def __init__(self, centro, raio):
        super(Circulo, self).__init__(centro)
        self._raio = raio

    def desenha(self):
        pass

    '''
    Observe a maneira que o método init na classe Circulo é executado. 
    Este método chama primeiramente o método init da superclasse Circulo, que é um ObjetoGrafico. 
    O método init do ObjetoGrafico inicializa o atributo _centro. 
    Então o método init do Circulo inicializa o atributo _raio.

    Usando a calsse Circulo definida acima podemos escrever algo assim agora:
    '''


c = Circulo(Ponto(0, 0), 5)
c.desenha()
c.movePara(Ponto(10, 10))
c.apaga()

    '''
    Esta seqüência do código declara um objeto Circulo com seu centro inicialmente na posição 
    (0,0) e no raio 5. O círculo é desenhado, movido e para (10,10), e depois apagado.

    O exemplo abaixo define uma classe Retangulo. A classe Retangulo estende também a classe ObjetoGrafico. 
    Conseqüentemente, herda o atributo centro e os métodos apaga e movePara. 
    A classe Retangulo adiciona dois atributos adicionais, _altura e _largura, e sobrescreve o método desenha. 
    O corpo do método desenha não é mostrado, entretanto, nós vamos supor que desenha um retângulo com as dimensões dadas.
    '''


class Retangulo(ObjetoGrafico):
    def __init__(self, centro, altura, largura):
        super(Retangulo, self).__init__(centro)
        self._altura = altura
        self._largura = largura

    def desenha(self):
        pass    

    '''
    A classe Quadrado estende a classe Retangulo abaixo. Nenhum atributo ou método novo são 
    inicializados -- aqueles herdados de ObjetoGrafico ou de Retangulo são suficientes. 
    O método do init simplesmente certificar que a altura e largura de um quadrado são iguais!
    '''

class Quadrado(Retangulo):
    def __init__(self, centro, largura):
        super(Quadrado, self).__init__(centro, largura, largura)
    '''
    7.2.2 Definição de Método

    Considere a seguência abaixo:
    '''

    g1 = Circulo(Ponto (0,0), 5)
    g2 = Quadrado(Ponto (0,0), 5)
    g1.desenha()
    g2.desenha()

    '''
    A instrução g1.desenha() chama Circulo.desenha visto que a instrução g2.desenha() chama Retangulo.desenha.

    É como se cada objeto de uma classe "soubesse" o método real a ser invocado quando um método é 
    convidado de objet. Por exemplo, um círculo "sabe" chamar Circulo.desenha, ObjetoGrafico.apaga e 
    ObjetoGrafico.movePara, visto que um quadrado "sabe" chamar Retangulo.desenha, ObjetoGrafico.apaga e 
    ObjetoGrafico.movePara.


    7.2.3 Métodos Abstratos

    O método de desenha nunca deve ser chamado. 
    Isto porque se espera que cada classe derivada da classe ObjetoGrafico sobrescreverá o método desenha. 
    Conseqüentemente, nós definimos o método desenha na classe ObjetoGrafico para ser um método abstrato (abstractmethod).

    Ao contrário do staticmethod, a classe do abstractmethod não é uma classe interna do Python. 
    A fim compreender o que a classe do abstractmethod faz, é necessário compreender como a máquina virtual do 
    Python invoca métodos de instância. Considere a seguinte chamada do método:
    '''


g.desenha()

    '''
    O interpretador do Python executa uma seqüência de operações que seja equivalente ao seguinte:

    '''

func = ObjetoGrafico.desenha.__get__(g, ObjetoGrafico)
func.__call__()

    '''
    A finalidade do método get é retornar um objeto método que seja limitado a uma instância. 
    O objeto método é chamado como uma função normal invocando o método call.

    O método get na classe abstractmethod retorna uma instância da classe interna chamada de método. 
    O método call na classe interna levanta uma exceção de TypeError quando chamado.

    7.2.4 Algoritmos Abstratos

    Uma classe abstrata é uma classe que contem um ou mais métodos abstratos. 
    As classes abstratas podem ser usadas em muitas maneiras interessantes. 
    Um dos paradigmas mais úteis é o uso de uma classe abstrata para algorítmo abstrato. 
    Os métodos apaga e movePara definidos na classe ObjetoGrafico são exemplos disso.

    Os métodos apaga e movePara são executados na classe abstrata ObjetoGrafico.
    Os algoritmos executados são projetados para trabalhar em qualquer classe concreta derivada de ObjetoGrafico, 
    podendo ser ele Circulo, Retangulo ou Quadrado. 
    De fato, nós escrevemos os algoritmos que trabalham na classe real do objeto. 
    Conseqüentemente, tais algoritmos são chamados algoritmos abstratos.

    Os algoritmos abstratos invocam tipicamente métodos abstratos. 
    Por exemplo, o movePara e apaga invocam desenha para fazer a maioria do trabalho real. 
    Neste caso, as classes derivadas esperam-se herdar o algoritmo abstrato movePara e apaga e 
    sobrescrevem o método abstrato desenha. 
    Assim, a classe derivada customiza o comportamento do algoritmo abstrato sobrescrevendo os métodos apropriados. 
    O mecanismo da definição do método do Python assegura de que o método "correto" sempre seja chamado.

    7.3 Herança Múltipla

    Em Python uma classe pode ser derivada de uma ou mais classes base. Por exemplo, veja:
    '''

class A(object):
    def f():
        pass

class B(object):
    pass

    def f(): pass

class C(A, B):
    pass

    '''
    A classe C estende as classes A e B. Conseqüentemente, a classe C herda atributos da classe de ambas as classes base.

    Uma pergunta interessante é levantada quando mais de uma classe base define um atributo com o mesmo nome.
    Por exemplo, A e B, ambos definem um método nomeado f. Dado um exemplo c da classe C, que método a expressão c.f() chama?

    O método chamado é determinado por um conjunto de réguas chamadas de Ordem de Resolução de Métodos Python.
    Em caso geral, as réguas são completamente complexas e não serão explicadas neste artigo(para uma explanação 
    completa, veja http://www.python.org/2.3/mro.html).
    Entretanto, os casos simples como o exemplo acima, as réguas são fáceis: para encontrar um nome, 
    procure primeiramente no namespace da classe C, e então procure na ordem das classes base dadas. Isto é, 
    procura A primeiramente e depois procure B. 
    Conseqüentemente, neste caso a função invocada pela expressão c.f() é a função A.f.

    8. Exceções

    Há situações inesperadas durante a execução de um programa, isto ocorrerá com todos. 
    Os programadores cuidadosos escrevem o código que detecta erros o que é apropriado. 
    Entretanto, um algoritmo simples pode tornar-se ininteligível quando checamos muitos erros 
    isto pode obscurecer a operação normal do algoritmo.

    As exceções fornecem uma maneira limpa de detectar e assegurar situações inesperadas. 
    Quando um programa detecta um erro, levanta uma exceção.

    Quando uma exceção é levantada, o controle está transferido a alimentar a exceção.
    Definindo um método que trave a exceção, o programador pode escrever o código para segurar o erro.

    Em Python, uma exceção é um objeto. Todas as exceções no Python são derivadas da classe base interna chamada Exception.
    Por exemplo, considere a classe A definida abaixo.
    Desde que a classe A estende a classe da exceção, A é uma exceção que pode ser levantada.
    '''

class A(Exception):
    pass

def f():
    raise A

def g():
    try:
        f()
    except A:
        pass
    '''
    Um método levanta uma exceção usando o identificador raise: 
    Um identificador raise é similar a um identificador return.
    Uma identificador return representa a terminação normal de um método e 
    o objeto retornado combina o valor do retorno do método. 
    Um identificador raise representa a terminação anormal de um método e 
    o objeto levantado representa o tipo de erro encontrado. O método f levanta uma exceção de A.

    Os alimentadores da exceção são definidos usando um bloco try: 
    O corpo do bloco try está executado qualquer um até que uma exceção esteja levantada ou 
    até que termine normalmente. Um ou mais alimentadores de exceção seguem em um bloco try. 
    Cada alimentador de exceção consiste na cláusula que especifica as exceções a serem travadas, 
    e um bloco do código, que é executado quando a exceção ocorre. Quando o corpo do bloco try levanta uma exceção 
    para que uma exceção está definida, o controle é transferido ao corpo do alimentador da exceção.

    No exemplo acima, a exceção levantada pelo método f é travada pelo método g. Em geral, quando uma exceção 
    é levantada, a corrente dos métodos chamados é procurada ao contrário (da chamada até quem chamou o método) 
    para encontrar a exceção mais próxima. Quando um programa levanta uma exceção que não esteja travada, o programa termina.
    '''
## Referência

# http://wiki.python.org.br/ProgramacaoOrientadaObjetoPython

# http://eupodiatamatando.com/2007/04/09/sobrecarga-de-operadores-em-python/
