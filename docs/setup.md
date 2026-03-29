# Guia de Configuração (Setup)

Este guia detalha como configurar e rodar o projeto do zero.

## 🛠 Pré-requisitos
- Python 3.12+
- `uv` (Astral Python Manager)
- Docker Desktop (opcional para rodar banco local)

## 📦 Instalação com `uv`

O `uv` é usado para garantir que o ambiente seja reprodutível e extremamente rápido.

1.  **Instale as dependências**:
    ```bash
    uv sync
    ```

2.  **Variáveis de Ambiente**:
    Crie o arquivo `.env` na raiz do projeto com:
    - `TELEGRAM_BOT_TOKEN`
    - `GROQ_API_KEY`
    - `MONGO_URI`

3.  **Inicie o Bot**:
    ```bash
    uv run python main.py
    ```

## 🐳 Rodando com Docker Compose

Recomendado para subir o Mongo local rapidamente.

```bash
docker-compose up -d
```

O comando acima vai subir:
- Um container para o bot.
- Um container `mongodb:6.0` com volume persistente.

## 📋 Lista de Dependências Principais
- `aiogram`: Telegram API.
- `pydantic-ai`: Orquestração de AGENTES e Validação.
- `groq`: Integração com LLMs open-source de baixa latência.
- `motor`: MongoDB assíncrono.
