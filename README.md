# Bot do LAPPIS

## LAPPISUDO

Este projeto teve como base a [Tais](http://github.com/lappis-unb/tais). Com o objetivo de ser divertido e apresentar o laboratório.

## Bot

**Atenção**: Para funcionamento inicial das imagens docker citadas aqui, como "bot", "coach" e "requirements", é importante que em sua primeira execução deste repositório, seja executado:
```sh
sudo make first-run
```
Este script foi configurado para construir as imagens genéricas necessárias para execução deste ambiente. Caso seu projeto utilize este boilerplate e vá realizar uma integração contínua ou similar, é interessante criar um repositório para as imagens e substitua os nomes das imagens "bot", "coach" e "requirements" pelas suas respectivas novas imagens, por exemplo "<organização>/bot" em repositório público, não sendo mais necessário então a execução do script "first-run".

### Telegram

Para realizar este processo, recomenda-se a criação de um [Bot para o Telegram](https://core.telegram.org/bots#3-how-do-i-create-a-bot) para obter todas as informações necessárias.

Para rodar a _stack_ do bot pelo Telegram juntamente com os serviços anexados, é necessário comentar a parte relacionada ao Rocket.Chat e descomentar o serviço relacionado ao bot do telegram.

Após, é possível testar o bot utilizando o [ngrok](https://ngrok.com/download) para expor determinada porta para ser utilizado pelo Telegram.

Ao baixar, é só executar utilizando o seguinte comando:

```
./ngrok http {porta utilizada}
```

**Atenção:** O conector do Telegram está utilizando a porta 5001 como padrão. Caso queira mudar, somente altere a porta utilizada pelo no Makefile.

Ao executar, será gerado um link onde será usado para recuperar todas as informações obtidas pelo webhook do Bot pelo Telegram, semelhante a este link:

```
Exemplo:
https://283e291f.ngrok.io
```

Configure todas as informações necessárias no docker-compose para integrar o bot do telegram criado:

```yml
- TELEGRAM_ACCESS_TOKEN={token fornecido pelo BotFather}
- VERIFY={username do bot}
- WEBHOOK_URL={link do ngrok}/webhooks/telegram/webhook
```

Para executar somente o serviço do bot para o Telegram, utilize o seguinte comando:

# Tecnologias do Projeto:
- [Rasa](http://rasa.com) - Inteligência Artificial do Bot
- [RocketChat](https://rocket.chat) - Mensageiro de comunicação do Bot
- [Docker](https://www.docker.com) - Os ambientes são todos dockerizados

# Licença

Todo o framework do Rasa BoilerPlate é desenvolvido sob a licença [GPL3](https://github.com/lappis-unb/rasa-ptbr-boilerplate/blob/devel/LICENSE)
