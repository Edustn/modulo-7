# Introdução

Esse projeto foi desneovlvido para prever em quais dias você deve comprar um Bitcoin e se essa semana é válida para comprar esse moeda nessa semana. Nesse sentido, temos um frontend interativo para que o usuário possa carregar a própria base de dados e fazer suas previsões de forma personalizada.

Nesse sentido, para ver mais aprofundamente sobre as especificações de como foi tratado a questão da limpeza dos dados, meétricas avaliadas, escolhas dos modelos para as previsões recomendo acessar o notebook `main.ipynb` localizando em `MODULO-7/atividade_1/src/main.ipynb`.

Sendo assim, os modelos escolhidos para esse projetos forma: GARCH e o Arima. Cabe auqi uma breve explicação de cada um dos modelos escolhidos. Nesse sentido, o GARCH foi escolhido por referências acâdemicas na área de ecnomia, pois ele é indicado para modelar a volatilidade variando no tempo de determiandas séries, assim podemos ter acesso a volatibilidade do Bitcoin pelo tempo e indicar para quando se deve comprar ou não. Já o Arima, foi utilizado para avaliar os valores futuros que o Bitcoin pode assumir para que se pudesse ter valores futuros a indicar para pessoa comprar.

# Execução do projeto:

Por fim esse projeto pode ser executado da seguindo os passos abaixo:

Entre em `atividade_1/src` e execute o comando `docker compose up --build`

Então na primeira tela terá dois botões, o botão `Base Treinada` que irá gerar resultados da base já disposta no sistema. Já o segundo botão, `Treinar` irá redirecionar para outra página que contêm três botões para escolha de uma nova base para haver o treino com os novos dados. Sendo assim, o botão `Escolher base` é responsável por entrar no explorar do sistema operacional Windows e possibilitar que o usuário possa selecionar a base desejada para retreino do modelo. Após esse processo o botão `Enviar base` aloca a nova base dentro da nossa pasta que está executando o modelo. Por fim, o botão `Base Treinada` realiza a previsão baseado nos dados da nova base e apresentam os resultados para o usuário. 

Obs: as novas bases devem ser salvas com o nome `bitcoins.csv` para que o sistema execute tudo com sucesso.

