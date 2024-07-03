# api_crossfit
Desafio API assíncrona de um academia para uma competição de crossfit. Usando o framework FastAPI -Bootcamp Python AI Backend Developer 

Esta é uma API de competição de crossfit chamada WorkoutAPI (isso mesmo rs, eu acabei unificando duas coisas que gosto: codar e treinar). É uma API pequena, devido a ser um projeto mais hands-on e simplificado nós desenvolveremos uma API de poucas tabelas, mas com o necessário para você aprender como utilizar o FastAPI.

Para executar a api, no terminal, execute:

# Stack da API
A API foi desenvolvida utilizando o `fastapi (async)`, junto das seguintes libs: `alembic`, `SQLAlchemy`, `pydantic`. Para salvar os dados está sendo utilizando o `postgres`, por meio do `docker`,  `poetry`, `ruff` e `taskipy` para automatizar algumas tarefas junto com o `poetry`.

Entre essas tarefas, temos os comandos definidos no poetry:

- lint = 'ruff check .&& ruff check . --diff'

- format = 'ruff check . --fix; ruff format .'

- run = 'fastapi dev api/app.py'

- revision_alembic = 'alembic revision --autogenerate'

- upgrade_alembic = 'alembic upgrade head'



Comandos para lint e formata o codigo

```bash
task lint
```
```bash
task format
```

Comandos dos alembic
```bash
task revision_alembic
```

```bash
task upgrade_alembic
```

O bando de dados esta configurado no docker-compose 

Execução da API
```
task run
```
e acesse: http://127.0.0.1:8000/docs