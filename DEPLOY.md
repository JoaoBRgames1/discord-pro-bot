# Hospedagem

Este projeto ja esta pronto para rodar em host com Docker, VPS, Render ou Railway.

## Variaveis obrigatorias

Configure estas variaveis no painel da sua host:

```text
DISCORD_TOKEN=token_do_bot
WEB_ADMIN_PASSWORD=uma_senha_forte_para_o_painel
WEB_HOST=0.0.0.0
WEB_PORT=19071
DATABASE_PATH=data/bot.sqlite3
```

Em hosts como Render e Railway, a porta costuma vir pela variavel `PORT`. O projeto ja aceita isso automaticamente.

## Melhor opcao: VPS com Docker

Em uma VPS Ubuntu/Debian com Docker instalado:

```bash
git clone seu_repositorio.git
cd discord-pro-bot
cp .env.example .env
nano .env
docker compose up -d --build
```

O painel ficara em:

```text
http://plus-03.bedhosting.com.br:19071
```

Para ver logs:

```bash
docker compose logs -f
```

Para atualizar:

```bash
git pull
docker compose up -d --build
```

## Render

1. Suba o projeto para GitHub.
2. Crie um novo `Web Service`.
3. Selecione Docker.
4. Adicione as variaveis `DISCORD_TOKEN`, `WEB_ADMIN_PASSWORD` e `DATABASE_PATH`.
5. Use `/health` como health check.

Importante: free tier pode dormir. Bot de Discord precisa ficar online 24/7, entao prefira plano pago ou VPS.

## Railway

1. Suba o projeto para GitHub.
2. Crie um novo projeto no Railway.
3. Conecte o repositorio.
4. Adicione as variaveis obrigatorias.
5. O Railway detecta o Dockerfile e inicia o bot.

## Musica

O Dockerfile instala FFmpeg automaticamente. Se hospedar sem Docker, instale FFmpeg manualmente na host.

## Persistencia

SQLite funciona bem para uso inicial. Em Docker na VPS, o `docker-compose.yml` salva o banco em `./data`.
