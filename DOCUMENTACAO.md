# DOCUMENTACAO.md

## 1. Introdução
Bem-vindo ao LunMoon! LunMoon é uma linguagem de programação divertida e fácil de aprender. Com LunMoon, você pode criar jogos, contar histórias e muito mais! Vamos começar essa aventura juntos!

## 2. Instalação
Para começar a usar LunMoon, você precisa instalar algumas coisas. Siga estas etapas:

1. **Baixe o LunMoon**: Vá para o site oficial e baixe o instalador.
2. **Instale o LunMoon**: Clique duas vezes no arquivo que você baixou e siga as instruções na tela.
3. **Abra o LunMoon**: Agora, procure o ícone do LunMoon e clique nele para começar a programar!

## 3. Variáveis
Variáveis são como caixas onde você pode guardar coisas. Por exemplo, se você quiser guardar seu nome, pode fazer assim:

```lunmoon
meuNome = "Maria"
```

Agora, `meuNome` tem dentro o valor "Maria".

## 4. Operadores
Os operadores são usadas para fazer cálculos. Aqui estão alguns operadores simples:

- Adição: `+`
- Subtração: `-`
- Multiplicação: `*`
- Divisão: `/`

Exemplo:
```lunmoon
resultado = 10 + 5
```
Agora `resultado` será `15`.

## 5. Estruturas de Controle
Estruturas de controle ajudam você a decidir o que fazer. Por exemplo, `se` e `enquanto`:

### Se
```lunmoon
se (idade > 10) {
    mostrar("Você é mais velho que 10 anos!")
}
```

### Enquanto
```lunmoon
enquanto (contagem < 5) {
    contagem = contagem + 1
    mostrar(contagem)
}
```

## 6. Funções
Funções são grupos de códigos que você pode chamar quando precisar deles. Aqui está um exemplo de uma função chamada `saudar`:

```lunmoon
funcao saudar(nome) {
    mostrar("Olá, " + nome + "!")
}

saudar("Carlos")
```

## 7. Exemplos Práticos
Vamos fazer um pequeno jogo. Neste jogo, você adivinha um número de 1 a 10.

```lunmoon
numeroSecreto = 7
adivinha = ler("Adivinhe o número de 1 a 10: ")

se (adivinha == numeroSecreto) {
    mostrar("Você acertou!")
} senao {
    mostrar("Tente novamente!")
}
```
