# Simulador de Dispositivos IoT com MQTT

Este projeto é um simulador de dispositivos IoT que utiliza o protocolo MQTT para publicar dados de sensores simulados. Atualmente, suporta a simulação de um sensor de radiação solar.

## Pré-requisitos

- Python 3.x
- Biblioteca Paho MQTT

## Instalação

Instale as dependências necessárias:

```bash
pip install -r requirements.txt
```

## Execução

Para executar o simulador, você precisará iniciar tanto o publisher quanto o subscriber.

### Iniciar o Publisher

Abra um terminal e navegue até o diretório do projeto. Execute o seguinte comando:

```bash
python3 publisher.py
```

### Iniciar o Subscriber

Abra um novo terminal e execute o seguinte comando:

```bash
python3 subscriber.py
```

Você deverá ver mensagens sendo publicadas pelo publisher e recebidas pelo subscriber.

## Demonstração
[Link do vídeo](https://youtu.be/mvigfNvgJ_4)

## Extensões

O sistema foi projetado com abstrações que permitem a fácil adição de novos tipos de sensores. Para adicionar um novo sensor, crie uma nova classe que herda de `SensorSimulator` e implemente o método `simulate_data`.