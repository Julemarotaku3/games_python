import pygame

import sys

#Definição de uma classe para o jogo 
class Game:
    def __init__(self) -> None:
        #comando que inicaliza o pygame
        pygame.init()

        #Muda o título da janela
        pygame.display.set_caption("Jogo do ninja")

        #Definição de uma janela
        self.janela = pygame.display.set_mode((600, 400))

        #Instâncilaização de uma imagem
        self.img = pygame.image.load('data/images/clouds/cloud_1.png')

        #Ao analisar as pastas contendo imagens, é evidente a presença de um fundo preto que surge como resultado da importação dessas imagens para os arquivos no Visual Studio Code. Para contornar essa situação, existem várias abordagens possíveis, e neste caso, a solução escolhida é empregar o método interno colorkey().

        #O método colorkey() atua como uma solução para esse problema. Esse método requer um argumento, que é uma cor especificada em formato RGB. O propósito do método colorkey() é transformar qualquer pixel na imagem que corresponda à cor especificada em um pixel transparente. Esse processo é realizado alterando o canal alfa do pixel para o valor 0, efetivamente tornando-o transparente. 
        self.img.set_colorkey((0, 0, 0))

        #O comando pygame.Rect() cria uma imagem ou uma superfície retangular na interface principal. A classe Rect recebe (x, y, largura retangular,  altura retangular). 
        self.collision_area = pygame.Rect(50, 50 ,300, 50)

        self.img_pos = [100, 330]

        self.moviment = [False, False]

        #Instancialização do fps do jogo 
        self.fps = pygame.time.Clock()  

    def rum(self):
        #Loop onde o jogo vai rodar 
        while(True):
            
            print(self.collision_area[2])
            #O trecho de código self.janela.fill() assume a função de "limpar" o plano de fundo da interface gráfica. Como previamente observado, esse código opera a uma taxa de 60 ciclos por segundo. Isso implica que, a cada segundo em que a tecla K_UP permanece pressionada, a imagem é renderizada na interface gráfica em 60 ocasiões distintas, resultando em uma espécie de "rastro" de imagens.
            #Nesse contexto, o propósito do comando self.janela.fill() é precisamente evitar esse efeito de "rastro", ao preencher a interface em cada ciclo com uma cor específica. Essa cor é representada por valores no espaço RGB, no caso, (21, 214, 248). Portanto, essa instrução atua como uma medida preventiva para garantir uma interface gráfica livre de resquícios indesejados, conferindo-lhe um preenchimento constante que, por sua vez, elimina o efeito de rastro gerado pela rápida sucessão de renderizações. 
            self.janela.fill((21,214,248))
            
            #Conforme as regras sintáticas do Python, é possível realizar operações aritméticas com variáveis booleanas. Isso inclui adições e subtrações envolvendo os valores 1 e 0. Nesse contexto, o valor booleano True é considerado equivalente a 1, enquanto o valor False é equiparado a 0. Essa propriedade se reflete, por exemplo, em uma lista qualquer "n = [True, False]", na qual podemos observar a relação n[0] = True (ou 1) e n[1] = False (ou 0). Dessa forma, podemos expressar a equação "1 = 1 - 0" como "1 = n[0] - n[1]", onde os valores das posições n[0] e n[1] estão associados aos valores lógicos True e False, correspondendo respectivamente a 1 e 0.

            #Logo, O valor de self.moviment[0] é definido como True quando a tecla K_UP é pressionada. Isso, por sua vez, leva a uma operação de subtração entre 0 e 1. No contexto, o valor 0 corresponde a self.moviment[1], enquanto o valor 1 se relaciona com self.moviment[0], resultando em -1. Consequentemente, a imagem se movimentará no eixo y com uma diminuição de 1 unidade (para baixo).
            #Em contrapartida, self.moviment[1] assume o valor True quando a tecla K_DOWN é pressionada. Isso ocasiona uma subtração de 1 - 0, sendo 1 associado a self.moviment[1] e 0 a self.moviment[0]. Portanto, a subtração resulta em 1, resultando em um deslocamento da imagem no eixo y com um acréscimo de 1 unidade (para cima).


            self.img_pos[1] += (self.moviment[1] - self.moviment[0])*5
            
            #A etapa de renderização da imagem na tela envolve o uso da função "blit". Essencialmente, o blit executa a operação de copiar uma porção de memória (representada por self.img) para outra superfície (chamada de "imagem"). Nesse contexto, a "imagem" se refere à janela principal, e é importante notar que, no pygame, tanto a janela principal quanto qualquer outra imagem são consideradas superfícies.

            #Dessa maneira, o blit realiza uma espécie de "mesclagem" entre duas superfícies distintas, ou seja, combina o conteúdo da superfície de origem (self.img) com a da superfície de destino (janela principal), possibilitando a visualização da imagem renderizada na tela.
            self.janela.blit(self.img, self.img_pos)

            #
            img_r = pygame.Rect(self.img_pos[0], self.img_pos[1], self.img.get_width(), self.img.get_height())

            #self.collision_area retonna um lsita com informaçãose da s dimens~pes de um retangulo o metodo colliderest()
            if img_r.colliderect(self.collision_area):
                pygame.draw.rect(self.janela, (0, 100, 250), self.collision_area)
            else:
                pygame.draw.rect(self.janela, (0, 50, 250), self.collision_area)

            #Esse mesmo código pode ser feito utilizando uma propriedade no Python chmada de desempacotamentode pararametros veja:
            #img_r= pygame.Rect(*self.img_pos, *self.img.get_size)
            #Onde o comando self.img_pos retorna uma lista "[]" com valores de posição x e posição y respectivamente da imagem e o comando self.get_size retorna uma lista "[]" com a largura e altura da imagem respectivamente. a sintaxe "*" diz ao python que ele estáa recebendo uma lista de valores que precisisão ser desempacotados e atribuidos aos seus repectivos argumentos. 



            #Comando necessário para atualizar qualquer mudanção na tela, sem ela não conseguirimans ver mudanças.
            pygame.display.update()

            #O Window acha que o seu aplicativo  não está recebendo entrada por isso dará a tela "Aplicativo não está respondendo", ou seja se você não solicita as entradas de um aplicativo o windows considera que esse aplicatvo não possui entradas logo dará com sem resposta.

            #A função pygame.event.get() é responsável por capturar os inputs provenientes dos periféricos, estabelecendo a interação com o subsistema STL do Windows. Esse subsistema corresponde a uma API encarregada de fornecer funções e atributos públicos para esse propósito.

            #Na sequência, a variável event será destinada a armazenar um valor inteiro correspondente a cada input recebido. Por exemplo, o valor 765 pode representar a tecla de espaço pressionada, enquanto o valor 766 indica a liberação dessa mesma tecla. O módulo pygame também apresenta uma API ou um arquivo .pyi que contém valores constantes associados a cada input de entrada. Por exemplo, o valor constante QUIT pode ser representado pelo número 546.   
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    #Encerra o pygame 
                    pygame.quit()
                    #Encerra o aplicativo
                    sys.exit()
                #Retorn se alguma tecla do teclado foi precionada    
                if event.type == pygame.KEYDOWN:
                    #event.key retorna qual tecla foi precionada 
                    print("Você pressionou alguma tecla!")
                    if event.key == pygame.K_UP:
                        self.moviment[0] = True
                    if event.key == pygame.K_DOWN:
                        self.moviment[1] = True
                #Retorna se alguma tecla foi solta
                if event.type == pygame.KEYUP:
                    print("Você soltou alguma tecla!")
                    if event.key == pygame.K_UP:
                        self.moviment[0] = False
                    if event.key == pygame.K_DOWN:
                        self.moviment[1] = False

            print(self.moviment[0] + self.moviment[1])

            #forçará o loop while a rodar 60 vezes por segundo
            self.fps.tick(60)



            #print(fps)

Game().rum()