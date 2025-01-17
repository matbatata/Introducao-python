# O que eu aprendi no ex06?

## Matemática
``` python
imc = peso / (altura * altura)
``` 

## O que é IMC?
Indíce de massa corporal

## Como funcional função em python
    
Temos dois termos-chave:

- `def:` de definir a função;
- `return:` retorna valor para a `main()` 

## Estrutura para exemplo
Vamos analisar a função `imc`:

``` python
def imc(peso, altura):
    return round(peso / (altura * altura), 2)

``` 

1. O `def` ele define a função;
2. `imc` é o nome da função e como vai chamar;
3. `peso` e `altura` são paramêtros;
4. A função retorna o IMC arrendodado com duas casas.

## Maneira genérica
``` python
def nome_da_funcao(parametro1, parametro2):
    comandos com parametro1 e parametro 2
    return resultado dos comandos
```

Feito em colaboração com [@lucasamtaylor01](https://github.com/lucasamtaylor01)

