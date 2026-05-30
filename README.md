# Discord Pro Bot

Bot Discord em Python com painel web configuravel, moderacao, autorole, logs e musica.

## Recursos incluidos

- Painel web com senha administrativa.
- Configuracao por servidor/guild.
- Autorole para novos membros.
- Logs de entrada, saida, ban e unban.
- Comandos slash de moderacao: `/ban`, `/kick`, `/mute`, `/purge`, `/warn`, `/warnings`.
- Sistema simples de avisos persistido em SQLite local.
- Musica em canal de voz com `/play`, `/pause`, `/resume`, `/skip`, `/queue`, `/stop`.
- Arquitetura por cogs para expandir como um bot tipo MEE6.

## Como rodar

1. Crie o bot no Discord Developer Portal.
2. Ative `SERVER MEMBERS INTENT` e `MESSAGE CONTENT INTENT` no portal do bot.
3. Convide o bot com permissao de administrador durante o desenvolvimento.
4. Instale Python 3.11+ e FFmpeg.
5. Instale dependencias:

```bash
pip install -r requirements.txt
```

6. Copie `.env.example` para `.env` e preencha `DISCORD_TOKEN` e `WEB_ADMIN_PASSWORD`.
7. Rode:

```bash
python main.py
```

8. Abra o painel:

```text
http://plus-03.bedhosting.com.br:19071
```

## Banco de dados

Por padrao, o bot usa SQLite local:

```text
DATABASE_PATH=data/bot.sqlite3
```

Nao ha credenciais de banco externo no projeto.

## Observacoes

Musica depende de FFmpeg estar no PATH. O Discord tambem exige que o bot tenha permissao para entrar e falar no canal de voz.

Este projeto e uma base profissional inicial. Para producao publica, adicione login OAuth2 do Discord, HTTPS, rate limiting externo, fila de jobs e deploy com supervisao de processo.
