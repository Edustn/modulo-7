# Introdução

Esse projeto foi desneovlvido para prever em quais dias você deve comprar um Bitcoin e se essa semana é válida para comprar esse moeda nessa semana. Nesse sentido, temos um frontend interativo para que o usuário possa carregar a própria base de dados e fazer suas previsões de forma personalizada.

Nesse sentido, para ver mais aprofundamente sobre as especificações de como foi tratado a questão da limpeza dos dados, meétricas avaliadas, escolhas dos modelos para as previsões recomendo acessar o notebook `main.ipynb` localizando em `MODULO-7/atividade_1/src/main.ipynb`.

Sendo assim, os modelos escolhidos para esse projetos forma: GARCH e o Arima. Cabe auqi uma breve explicação de cada um dos modelos escolhidos. Nesse sentido, o GARCH foi escolhido por referências acâdemicas na área de ecnomia, pois ele é indicado para modelar a volatilidade variando no tempo de determiandas séries, assim podemos ter acesso a volatibilidade do Bitcoin pelo tempo e indicar para quando se deve comprar ou não. Já o Arima, foi utilizado para avaliar os valores futuros que o Bitcoin pode assumir para que se pudesse ter valores futuros a indicar para pessoa comprar.

Obs: A implmentação da base de dados não foi exatmaente por uma API, pois como falado com o orientador o site que disponibilizava os dados não possuia uma API para fazer a requisição dos dados. Sendo assim, foi baixada uma base do site para realizar o retreinamento.


# Execução do projeto:

Por fim esse projeto pode ser executado da seguindo os passos abaixo:

Entre em `atividade_1/src` e execute o comando `docker compose up --build`

Então na primeira tela terá dois botões, o botão `Base Treinada` que irá gerar resultados da base já disposta no sistema. Já o segundo botão, `Treinar` (que faz o retreino do modelo) irá redirecionar para outra página que contêm três botões para escolha de uma nova base para haver o treino com os novos dados. Sendo assim, o botão `Escolher base` é responsável por entrar no explorar do sistema operacional Windows e possibilitar que o usuário possa selecionar a base desejada para retreino do modelo. Após esse processo o botão `Enviar base` aloca a nova base dentro da nossa pasta que está executando o modelo. Por fim, o botão `Base Treinada` realiza a previsão baseado nos dados da nova base e apresentam os resultados para o usuário. 

Obs: as novas bases devem ser salvas com o nome `bitcoins.csv` para que o sistema execute tudo com sucesso.

Sendo assim, no vídeo diponível no link abaixo é possível visualizar o funcionamento do treino e do retreino do modelo: [https://drive.google.com/file/d/1dB_KSsSZLV9lGZQabTRPLVcSxlyI9nq8/view?usp=sharing](https://drive.google.com/file/d/1dB_KSsSZLV9lGZQabTRPLVcSxlyI9nq8/view?usp=sharing) 

# Backend e PostgreSQL

Analisando o arquivo `main.py` disposto na pasta backend é nesse arquivo que estão dispostas as rotas desse sistema que executam a preição do modelo, acessam o banco de dados para o salvamento dos logs e faz o upload dos arquivos selecionados para que o modelo possa ser retreinado.

Com base nessa breve explicação do backend, optou-se por utilizar um banco de dados relacional, o PostgreSQL, para armazenar os logs do sistema sempre que uma rota do backend é acessada. A escolha de não adotar um datalake foi fundamentada pela natureza dos dados e os objetivos do projeto. Como os logs já são gerados em um formato estruturado e refinado, o uso de um datalake, que geralmente é mais adequado para lidar com grandes volumes de dados brutos e não estruturados, não se mostrou necessário. Além disso, bancos de dados relacionais, como o PostgreSQL, oferecem melhor performance e eficiência na consulta e manipulação de dados estruturados, o que se alinha perfeitamente à necessidade de rastrear e gerenciar logs de maneira organizada e rápida.

Por fim, para ver o funcionamento dos logs do sistema que foi a escolha de armazanar no PostgreSQL pode-se ver nesse link: [https://drive.google.com/file/d/1lER2wdU0iyqiWp08jSyshyLiGdRFNZHA/view?usp=sharing](https://drive.google.com/file/d/1lER2wdU0iyqiWp08jSyshyLiGdRFNZHA/view?usp=sharing). No vídeo fica claro que os dados são estruturados e reforça ainda mais o do motivo da escolha de um banco de dados relacional.