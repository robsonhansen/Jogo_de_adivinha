import os 

palavra_secreta = input(f'Digite a palavra secreta{' -'+'-'*5 +'>'}\n ').lower() #INPUT PARA RECEBER A PALAVRA SECRETA 

letras_acertadas = '' # VARIALVEL QUE RECEBE AS LETRAS ACERTADAS
tentativas = 0 #VARIALVEL QUE RECEBE AS TENTATIVAS

while True:
  letra_digitada = input('Qual a letra da palavra? \n') #INPUT QUE RECEBE A LETRA DIGITADA
  tentativas += 1
  
  if len(letra_digitada) > 1: #VERIFICA SE A LETRA DIGITADA É SOMENTE UM CARACTER
    print('digite apenas uma letra')
    continue
  elif letra_digitada in palavra_secreta: #VERIFICA SE A LETRA DIGITADA ESTÁ NA PALAVRA SECRETA
    letras_acertadas += letra_digitada
  
  palavra_formada = '' #VARIALVEL QUE RECEBE A PALAVRA FORMADA

  for letra_secreta in palavra_secreta: #FOR QUE PERCORRE A PALAVRA SECRETA 

    if letra_secreta in letras_acertadas: #VERIFICA SE A LETRA ESTÁ NA VARIAVEL LETRAS_ACERTADAS
      palavra_formada += letra_secreta #CASO SEJA, ADICIONA A LETRA NA PALAVRA_FORMADA
    else:
      palavra_formada += '*'   

  print(palavra_formada) 

  if palavra_formada == palavra_secreta: #CONDIÇÃO PARA VERIFICAR SE A PALAVRA_FORMADA ESTÁ IGUAL A PALAVRA_SECRETA
    os.system('cls') #LIMPA A TELA
    print(f'PARABÉNS, VOCÊ GANHOUUUUUU!!!🎉')
    print(f'A PALAVRA SECRETA ERA {palavra_secreta.upper()}!!')
    print(f'Você acertou após {tentativas} tentativas.')

    restart = input('DESEJA JOGAR NOVAMENTE? [S/N] ').upper() #INPUT PARA REINICIAR O JOGO

    if restart == 'S': #CONDICIONAL PARA REINICIAR O JOGO
      letras_acertadas = ''
      tentativas = 0
      os.system('cls')
      palavra_secreta = input(f'Digite a palavra secreta{' -'+'-'*5 +'>'} ').lower()
      continue
    else:
      break
    
   


  