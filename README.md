# Projeto Letras

Este projeto exibe um texto na tela como se estivesse sendo digitado, mostrando cada caractere gradualmente.

## Como funciona

A função `soletrar` percorre o texto recebido e:

- adiciona um caractere por vez à saída;
- espera `0,1` segundo entre os caracteres;
- espera `0,3` segundo ao encontrar uma vírgula;
- espera `0,8` segundo ao encontrar uma quebra de linha;
- limpa o console antes de atualizar a exibição.

O texto demonstrado no programa está armazenado na variável `musica`.

## Como executar

Dentro desta pasta, execute:

```bash
python letras.py
```

Ou, dependendo da instalação do Python:

```bash
py letras.py
```

> A função `limpar_tela` usa `cls` no Windows e `clear` no Linux/macOS, permitindo executar o programa nesses sistemas.

## Requisitos

- Python 3 instalado.
- Um terminal compatível com o comando de limpeza do sistema operacional.
