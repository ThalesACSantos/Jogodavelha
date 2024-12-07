# Jogo da Velha em Python

<img src="Jogo_da_velha.ico" alt="logo" />

## Descrição
Este é um jogo da velha clássico implementado em Python utilizando a biblioteca Pygame. O jogo permite que dois jogadores se enfrentem em um tabuleiro 3x3.

## Como Jogar
1. **Inicie o jogo:** Execute o arquivo `jogo_da_velha.py` em seu terminal.
2. **Clique nas células:** Clique em uma célula vazia do tabuleiro para fazer sua jogada.
3. **Vence o jogo:** O primeiro jogador a alinhar três peças iguais (X ou O) na horizontal, vertical ou diagonal vence.
4. **Empate:** Se todas as células forem preenchidas sem um vencedor, o jogo termina em empate.

## Tecnologias Utilizadas
* **Python:** Linguagem de programação principal.
* **Pygame:** Biblioteca para criação de jogos 2D.

## Instalação
Para executar este jogo, você precisará ter o Python e o Pygame instalados.

**Instalando o Python:**
* Baixe e instale a versão mais recente do Python em https://www.python.org/downloads/

**Instalando o Pygame:**
* Abra o terminal e execute o seguinte comando:
  ```bash
  pip install pygame

**Instalando o Pyinstaller:**
* Abra o terminal e execute o seguinte comando:
  ```bash
  pip install pyinstaller

## Gerando um arquivo único com Pyinstaller:
* Após instalar o Pyinstaller, para gerar um arquivo único (executável), já com a logo, faça o seguinte: 
* Abra o terminal e execute o seguinte comando:
  pyinstaller --onefile Jogo_da_velha.py --icon="Jogo_da_velha".ico

  
