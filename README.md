
# Classes em Python

Python além de ser uma linguagem extremamente dinãmica ela também é bastante flexível com relação as suas estruturas de dados, controles e a estrutura da linguagem em si. Python é facil de aprender porque a linguem também se preocupa com o seu próprio aprendizado. Aprender é algo muito valorizado e estimulado tanto pela linguagem como também por todo o eco sistema que envolve uma comunidade forte e incrivelmente prestativa.

É possível aprender sozinho a usar a maioria das funções que python oferece. Quase tos o 'módulos' possuem uma documentação bem organizada e legível para todos.

Quando eu comecei a aprender python me senti mais como um detetive em busca de pistas para solucionar um caso, todas estas pistas estão dentro da própria linguem basta fuçar e ser muito curioso que logo você vai descobrir muita coisa. Por exemplo, veja o código abaixo:


```python
import urllib
dir(urllib)
```




    ['__builtins__',
     '__cached__',
     '__doc__',
     '__file__',
     '__loader__',
     '__name__',
     '__package__',
     '__path__',
     '__spec__',
     'error',
     'parse',
     'request',
     'response']



O comando `dir` me mostra todos os métodos que eu posso utilizar a partir da biblioteca `urllib`. Primeiro eu vejo algumas coisa que começam com dois underlines são coisas que dizem respeito a informações do pacote, por exemplo o `__name__` mostra o nome da biblioteca e o `__path__` retorna o caminho da bibliotaca no sistema. As outras coisas são de fato programas que eu posso utilizar. E se eu quiser saber o que cada uma dessas funções fazem? Basta eu procurar pela sua documentação.


```python
print(urllib.request.__doc__)
```

    An extensible library for opening URLs using a variety of protocols
    
    The simplest way to use this module is to call the urlopen function,
    which accepts a string containing a URL or a Request object (described
    below).  It opens the URL and returns the results as file-like
    object; the returned object has some extra methods described below.
    
    The OpenerDirector manages a collection of Handler objects that do
    all the actual work.  Each Handler implements a particular protocol or
    option.  The OpenerDirector is a composite object that invokes the
    Handlers needed to open the requested URL.  For example, the
    HTTPHandler performs HTTP GET and POST requests and deals with
    non-error returns.  The HTTPRedirectHandler automatically deals with
    HTTP 301, 302, 303 and 307 redirect errors, and the HTTPDigestAuthHandler
    deals with digest authentication.
    
    urlopen(url, data=None) -- Basic usage is the same as original
    urllib.  pass the url and optionally data to post to an HTTP URL, and
    get a file-like object back.  One difference is that you can also pass
    a Request instance instead of URL.  Raises a URLError (subclass of
    OSError); for HTTP errors, raises an HTTPError, which can also be
    treated as a valid response.
    
    build_opener -- Function that creates a new OpenerDirector instance.
    Will install the default handlers.  Accepts one or more Handlers as
    arguments, either instances or Handler classes that it will
    instantiate.  If one of the argument is a subclass of the default
    handler, the argument will be installed instead of the default.
    
    install_opener -- Installs a new opener as the default opener.
    
    objects of interest:
    
    OpenerDirector -- Sets up the User Agent as the Python-urllib client and manages
    the Handler classes, while dealing with requests and responses.
    
    Request -- An object that encapsulates the state of a request.  The
    state can be as simple as the URL.  It can also include extra HTTP
    headers, e.g. a User-Agent.
    
    BaseHandler --
    
    internals:
    BaseHandler and parent
    _call_chain conventions
    
    Example usage:
    
    import urllib.request
    
    # set up authentication info
    authinfo = urllib.request.HTTPBasicAuthHandler()
    authinfo.add_password(realm='PDQ Application',
                          uri='https://mahler:8092/site-updates.py',
                          user='klem',
                          passwd='geheim$parole')
    
    proxy_support = urllib.request.ProxyHandler({"http" : "http://ahad-haam:3128"})
    
    # build a new opener that adds authentication and caching FTP handlers
    opener = urllib.request.build_opener(proxy_support, authinfo,
                                         urllib.request.CacheFTPHandler)
    
    # install it
    urllib.request.install_opener(opener)
    
    f = urllib.request.urlopen('http://www.python.org/')
    


Note que além de uma explicação objetivo essa pequena documentação embutida também traz um exemplo completo de uso.

Para que ocê possa escrever a documentação dos seus módulos, classes e funções basta utilizar o `""" minha doc """`, ou também `''' minha doc '''` antes de qualquer códido, como por exeplo:


```python
def soma(a,b):
    """
        Esta função recebe dois argumentos numérios e retorna a sua soma.
        
        exemplo: soma(1,1)
        retorn: 2
    """
    return a+b

print(soma.__doc__)
```

    
            Esta função recebe dois argumentos numérios e retorna a sua soma.
            
            exemplo: soma(1,1)
            retorn: 2
        


Caso você tenha um arquivo que agregue várias funções, você pode adicioar uma documentação ou um índice logo no início do arquivo.

Bom, o assunto aqui não ẽ fução e sim classe, mas eu achei importante citar a questão da documentação pois isso vai deixar suas classes e funções muito flexível e mais fácil de usar.

## O que é uma classe?

### Anatomia básica de uma classe:


```python
class Rectangle(object):
    pass
```

Primeiro a gente usa a palavra reservada `class` em seguida o nome da classe no padrão CamelCase, ou seja, a primeira letra é em maiúculo e os demias termos sem espaços e com suas inicias em maiúculo. Por exemplo: `MyRectangle`. Entre parẽnteses foi inserido um tal de `object`, por enquanto não se procupe com ele, mas também não vai esquecer dele! O `pass` é apenas para indicar ao Python que ele deve simplesmente ignorar 

#### Atributos e Métodos

Método contrutor


```python
class Rectangle(object):
    def __init__(self, width, height):
        self.width = width
        self.height = height
```

Os métodos para calcular área e perímetro


```python
class Rectangle(object):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
    def perimeter():
        return 2 * ( self.width + self.height)
```

Criando uma a primeira instância


```python
rect1 = Rectangle(3,4)
print(rect1.area())
```

    12


Aprofundando mais ...


```python
print(rect1)
```

    <__main__.Rectangle object at 0x7ff74065e358>


Utilizando métodos internos 


```python
class Rectangle(object):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
    def perimeter():
        return 2 * ( self.width + self.height)
    
    ## métodos internos
    def __repr__(self):
        return f'Rectangle with width={self.width} and height={self.height}'
```

Testando novamente ... 


```python
rect1 = Rectangle(4,6)
```


```python
print(rect1)
```

    Rectangle with width=4 and height=6


Vamos brincar com esse retângulo?
Vou definir um segundo objeto


```python
rect2 = Rectangle(10,40)
```

O que acontece se eu tentar comparar esses dois?
Dessa forma:


```python
rect1 == rect2
```




    False



Hmm.. Deu falso, deve ser porque os valores de altura e largura são direntes.
Então vou criar um terceiro retângulo com os mesmos valores do retêngulo 1.


```python
rect3 = Rectangle(4,6)
```


```python
rect1 == rect3
```




    False



Continua dando False... 

Isso acontece porque o python está utilizando uma comparação meio padrão, ele está comparando valores de memória, e isso não é bem o que eu gostaria de fazer. No fundo eu gostaria de comparar as larguras e alturas de dois retêngulos e dizer se são iguais ou não. Eu poderia criar uma função separada que recebe dois retângulos e aí verificar, mas ficaria bem estranho...

Assim como o `__init__` é um método interno de cada classe para criar a configuração inicial desta classe, eximtem vários outros métodos internos que podem ser utilizados.

O método que vai salvar minha vida é o `__eq__` ( equals) é esse método que é chamado quando realizamos a operação de comparação ou igualdade entre valores, ele recebe por padrão dois argumentos: o self ( referência ao objeto atual) e o `other`.

Este argumento representa o segundo elemento após o operador, isso significa que ele estará acessível a partir da classe, ou seja, quando digitar `rect1 == rect2` o primeiro elemento terá acesso ao segundo de forma que o segundo possa ser utilizado comforme a necessidade.

Dito isto, sabemos que o `other` representa o `rect2` que por sua vez é uma instância da classe `Rectangle`, logo ele possuí os atributos `width` e `height` dando à classe `Rectangle` a possibilidade de acessar tanto a largura e altura do `rect1` quando a altura e largura do `rect2`.

O código deve ficar assim: 


```python
def __eq__(self, other):
    return (self.width == other.width) and (self.height == other.height)
```

Explicando melhor essa função ela funciona assim:

Quando o operador `==` é invocado entre dois objetos e ele chama o método `__eq__` do primeiro objeto ( neste caso o `rect1`) e passa o segundo objeto como parâmetro desta função.

Como a função `__eq__` é uma função da classe `Rectangle` eu posso acessar os atributos de altura e largura normalmente e também acessar os atributos de altura e largura do outro objeto, logo, basta conferir se todos os valores são igual e retornar um Booleano.

A classe completa deve ficar assim:


```python
class Rectangle(object):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.height + self.width)

    def __repr__(self):
        return f'Rectangle with width={self.width} and height={self.height}'

    def __eq__(self, other):
        return (self.width == other.width) and (self.height == other.height)

rect1 = Rectangle(4,6)
rect2 = Rectangle(10,40)
rect3 = Rectangle(4,6)
```

Vamos conferir ... 


```python
print(rect1 == rect3)
```

    True


Note que agora a saída foi `True`

Mas, e se eu tentar...


```python
print(rect1 == 3)
```


    ---------------------------------------------------------------------------

    AttributeError                            Traceback (most recent call last)

    <ipython-input-47-a0806ed57729> in <module>
    ----> 1 print(rect1 == 3)
    

    <ipython-input-45-dd568b0a47d1> in __eq__(self, other)
         14 
         15     def __eq__(self, other):
    ---> 16         return (self.width == other.width) and (self.height == other.height)
         17 
         18 rect1 = Rectangle(4,6)


    AttributeError: 'int' object has no attribute 'width'


Ops! Isso aí dá um erro malucão!


O erro em questão é um erro do tipo `AttributeError`, e ele diz o seguinte: `'int' object has no attribute 'width'`

Ou seja, como o segundo argumento passado foi um objeto do tipo int é claro que ele não vai ter o atributo `width` nem o `height` pois estes dois atributos são exclusivos de um objeto do tipo `Rectangle`.

De certa forma o erro está correto, mas podemos melhorar mais o código prevenindo a classe desse tipo de situação. Para isso, basta utilizar a funçãp `isinstance` que recebe dois parâmetros: o objeto e a classe, esta função retorna `True` caso o objeto seja uma instância de uma determinada classe.

O método deve ficar assim:


```python
def __eq__(self, other):
    if isinstance(other, Rectangle):
        return (self.width == other.width) and (self.height == other.height)
    else:
        raise ArithmeticError(f'{type(other)} is not a Rectangle class instance')
```

Ou seja ...

Caso o segundo objeto seja uma intância da classe `Rectangle` a operação é realizar normalmente, caso contrário um erro do tipo `ArithmeticError` é lançado com a mensagem: "<class 'int'> is not a Rectangle class instance". Bem melhor, não?

### Recaputulando o que foi feito até aqui:
- Anatomia básica de uma classe
- Atributos e Métodos
- Método construtor
- Como criar atributos
- Como criar Métodos
- Como utilizar métodos internos

## Brincanado um pouco com a minha classe ...

Agora que a minha classe já é capaz de fazer coisas como: calcular a sua área, calcular seu perímetro e verificar se dois retângulos são iguais, que tal deixar a classe mais inteligente?

Agora eu gostaria de realizar a soma de dois retêngulos... Como fazer isso?

Se você pensou em utilizar um método interno, parabéns, é isso mesmo! O método para a soma é o `__add__`  é ele que vamos utilizar para realizar a soma de dois retângulos.

Assim como o `__eq__` o `__add__` recebe dois argumentos o __self__ e o __other__ o self diz respeito ao primeiro objeto e o other ao segundo, como já foi dito antes.

Vamos fazer o seguinte:
- Criar o método `__add__`
- Realizar a soma da aluta e largura de dois retângulos

O Método: 


```python
def __add__(self, other):
    width = self.width + other.width
    height = self.height + other.height
    return width, height
```

Instnciando novamentos os dois triângulos:

A classe `Rectangle` deve ficar assim:


```python
class Rectangle(object):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.height + self.width)

    def __repr__(self):
        return f'Rectangle with width={self.width} and height={self.height}'

    def __eq__(self, other):
        if isinstance(other, Rectangle):
            return (self.width == other.width) and (self.height == other.height)
        else:
            raise ArithmeticError(f'{type(other)} is not a Rectangle class instance')

    def __add__(self, other):
        width = self.width + other.width
        height = self.height + other.height
        return width, height

```

Os dois objetos:


```python
rect1 = Rectangle(4,6)
rect2 = Rectangle(10,40)
```

Agora, é só somar:


```python
print(rect1 + rect2)
```

    (14, 46)


Perfeito! ele fez certinho! somou as alturas e larguras dos triângulos e me retornou os valores. Mas... O ideal serial ele retornar um novo retêngulo, certo? Para fazer isso é muito fácil, basta retornar um novo retângulo com os novos valores:


```python
def __add__(self, other):
        width = self.width + other.width
        height = self.height + other.height
        return Rectangle(width=width, height=height)
```


```python
class Rectangle(object):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.height + self.width)

    def __repr__(self):
        return f'Rectangle with width={self.width} and height={self.height}'

    def __eq__(self, other):
        if isinstance(other, Rectangle):
            return (self.width == other.width) and (self.height == other.height)
        else:
            raise ArithmeticError(f'{type(other)} is not a Rectangle class instance')

    def __add__(self, other):
        width = self.width + other.width
        height = self.height + other.height
        return Rectangle(width=width, height=height)
    
rect1 = Rectangle(10, 40)
rect2 = Rectangle(40, 10)
```

Rodando novamente


```python
print(rect1 + rect2)
```

    Rectangle with width=50 and height=50


Maravilha! Agora eu posso salvar no rect3, por exempo, `rect3 = rect1 + rect2`

Note como é incrível uma classe em python! Agora...

##### Que tal você implementar na classe a capacidade dela realizar as 4 operações básica? Neste caso envolvendo retêngulos! Implemente as funções:

- Soma (Já implementada), função: `__add__`
- Subtração ( note que não existe altura nem largura negativa), função: `__sub__`
- Divisão ( Note que não é possível dividir nenhum número por zero), função: `__truediv__`
- Multiplicação, função: `__sub__`

Uau! Que demais! Essa classe é mesmo muito esperta, ela é capaz de executar as 4 operações matemáticas e ainda é capaz de dizer se um retângulo é igual ao outro.

Mais ela pode ficar ainda mais esperta, que tal ensinarmos a ela como determinar se um retângulo é maior ou menor do que o outro? Sabemos que para um retângulo ser maior do o outro a sua área precisa ser maior.

É laro que para isso vamos utilizar mais um método interno das classes python, o `__lt__`, ou less than, __menor que__.

A função deve ficar assim:


```python
def __lt__(self, other):
    return self.area() < other.area()
```

A classe deve ficar assim:


```python
class Rectangle(object):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.height + self.width)

    def __repr__(self):
        return f'Rectangle with width={self.width} and height={self.height}'

    def __eq__(self, other):
        if isinstance(other, Rectangle):
            return (self.width == other.width) and (self.height == other.height)
        else:
            raise ArithmeticError(f'{type(other)} is not a Rectangle class instance')

    def __add__(self, other):
        width = self.width + other.width
        height = self.height + other.height
        return Rectangle(width=width, height=height)

    def __sub__(self, other):
        width = self.width - other.width
        height = self.height - other.height
        return Rectangle(width=width, height=height)

    def __mul__(self, other):
        width = self.width * other.width
        height = self.height * other.height
        return Rectangle(width=width, height=height)

    def __truediv__(self, other):
        width = self.width / other.width
        height = self.height / other.height
        return Rectangle(width=width, height=height)

    def __lt__(self, other):
        return self.area() < other.area()


rect1 = Rectangle(4, 5)
rect2 = Rectangle(3, 4)
```

Agora basta eu rodar:


```python
print(rect2 < rect1)
```

    True


Incrível! Perceba que esse resultado é um resultado que representa um cálculo, ou seja, para que seja verdadeiro ele efetua os cálculos de áreas e depois os compara! Tornando a classe mais robusta e mais inteligente.

## Getters e Setters

utilizando getter e setter

Ótimo, a nossa classe já está inteligente de mais, mas agora ainda temos um problema grave.

Percaba que o cóidigo abaixo, deveria, mas não dá nenhum erro.


```python
rect1 = Rectangle(10, 20)
rect1.height = -20
```


```python
rect1.area()
```




    -200



Note que eu criei uma nova instância de um retângulo, mas eu passei a altura como __-20__, e para o cálculo de área esse valor também fui utilizado de forma errônea, logo o resultado -200 não faz nenhum sentido.

Eu preciso me prevenir para que a classe não aceite esse tipo de argumento negativo, para isso será necessário utilizar os famosos __getters e setters__

Sempre que alguém falar em getter e setter, estamos nos referindo ao acesso direto de atributos de uma classe as vezes o acesso a estes tais atributos precisam ser restringidos ou validados, no caso da classe `Rectangle` nem a altura nem a largura podem ser valores negativos.

Quando eu utilizo


```python
rect1.width
```




    10



Neste caso eu estou acessando os valores diretamente, ou seja, eu posso fazer isso porque eles são público, logo é necessário que esse atributo seja protegido para que eu posso aplicar regras de validações nele. Veja a classe abaixo:


```python
class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
john = Person('John', 30)
john.age
```




    30



A classe `Person` possui dois atributos: nome e idade. Perceba que a idade é um número, logo esse número precisa de um tratamento especial, então eu vou proteger ele, ou seja, vou torna-lo `protected`, talvez você já tenha visto essa palavram em linguagem como Java, as classes do Python também possuem suporte a modificadores de acesso e para isso basta utilizar o `_` ( underline ) antes do nome do atributo. Veja como a classe `Person` ficou:


```python
class Person(object):
    def __init__(self, name, age):
        self.name = name
        self._age = age
    
john = Person('John', 30)
john.age
```


    ---------------------------------------------------------------------------

    AttributeError                            Traceback (most recent call last)

    <ipython-input-63-ab377b849d55> in <module>
          5 
          6 john = Person('John', 30)
    ----> 7 john.age
    

    AttributeError: 'Person' object has no attribute 'age'


Note que assim que eu modifiquei o acesso ao atributo não é mais possível acessá-lo diretamente. Agora como eu posso saber a idade do John? Um solução seria:


```python
class Person(object):
    def __init__(self, name, age):
        self.name = name
        self._age = age
        
    def get_my_age(self):
        return self._age
    
john = Person('John', 30)
john.get_my_age()
```




    30



Até rodou, mas o ideal mesmo seria eu só usar: `john.age`. Bom uma parte já foi feita que seria proteger o atributo, agora o __getter__ para acessar o atributo `age`

Para isso, basta criar uma função com o mesmo nome do atribututo adicionado o decorator `@property`


```python
class Person(object):
    def __init__(self, name, age):
        self.name = name
        self._age = age
    
    @property
    def age(self):
        return self._age
    
john = Person('John', 30)
john.age
```




    30



Agora para aletrar a idade, como seria?


```python
class Person(object):
    def __init__(self, name, age):
        self.name = name
        self._age = age
    
    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, new_age):
        self._age = new_age
    
john = Person('John', 30)
john.age
john.age = 10
john.age
```




    10



Feito, agora vamos adicionar a validação na idade? A classe deve ficar dessa forma:


```python
class Person(object):
    def __init__(self, name, age):
        self.name = name
        self._age = age
    
    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, new_age):
        if new_age > 0:
            self._age = new_age
        else:
            raise ValueError('Invalide value')
    
john = Person('John', 30)
john.age
john.age = -10
john.age
```


    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    <ipython-input-76-b2bcbca77f5b> in <module>
         17 john = Person('John', 30)
         18 john.age
    ---> 19 john.age = -10
         20 john.age


    <ipython-input-76-b2bcbca77f5b> in age(self, new_age)
         13             self._age = new_age
         14         else:
    ---> 15             raise ValueError('Invalide value')
         16 
         17 john = Person('John', 30)


    ValueError: Invalide value



```python

```
