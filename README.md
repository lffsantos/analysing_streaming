# analysing_streaming

Esse projeto tem como objetivo a prática e aprendizado de diversas staks.

Faz a coleta de mensagens do twitter para processamento e analyse*(futuramente)


**Alguns código são copiados de links de referências.

Tecnologias:
    - Docker
    - Kafka
    - ElasticSearch
    - Kibana
    - MongoDB
    - Python 3.8

Como Rodar o projeto:

1 - rodar o comndo `make run_all_services`
- vai subir todos os serviços necessários para relizar o processamento de dados.

3 - Criar e Entrar na [VirtualEnv](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/#creating-a-virtual-environment)

2 - rodar o `consumer.py`
- vai ser o responsável por fazer o processamento das mensagens.

3- rodar o `stream_tweets.py`
- responsável por coletar os dados no twtiter.

> make run_all_services

> source .venv/bin/activate
> python consumer.py

Abrir outro terminal e rodar o comando

> source .venv/bin/activate
> python stream_tweets.py


Links de referências:

- https://www.analyticsvidhya.com/blog/2020/08/analysing-streaming-tweets-with-python-and-postgresql/
- https://elkhayati.me/kafka-python-twitter/
- https://realpython.com/twitter-bot-python-tweepy/
- https://www.earthdatascience.org/courses/use-data-open-source-python/intro-to-apis/twitter-data-in-python/
- https://www.youtube.com/watch?v=wlnx-7cm4Gg&ab_channel=LucidProgramming
- https://github.com/vprusso/youtube_tutorials/tree/master/twitter_python
