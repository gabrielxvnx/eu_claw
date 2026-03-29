# FinBot v2 🤖

Assistente financeiro pessoal com suporte a áudio (Whisper), visão (Llama 3.2) e extração estruturada (PydanticAI). Focado em custo zero usando a Groq API.

## 🚀 Início Rápido (em < 2 min)

Este projeto usa **`uv`** para gerenciamento de pacotes e **Docker** para infraestrutura.

### 1. Requisitos
- [uv](https://github.com/astral-sh/uv) instalado.
- Docker e Docker Compose.

### 2. Configuração
```bash
cp .env.example .env
# Edite o .env com suas chaves da Groq, Telegram e Mongo
```

### 3. Rodando o Projeto
Com **uv**:
```bash
uv sync
uv run python main.py
```

Com **Docker**:
```bash
docker-compose up -d
```

## ✨ Funcionalidades

- ✅ **Áudios**: Transcrição via Groq Whisper.
- ✅ **Recibos**: Extração de fotos via Llama 3.2 Vision.
- ✅ **Inteligência**: Processamento via PydanticAI (Llama 3.1 70B).
- ✅ **Insights**: Feedback financeiro automático.

## 📁 Documentação

- [Arquitetura](./docs/architecture.md)
- [Guia de Instalação (Setup)](./docs/setup.md)
- [Referência de API (Bot)](./docs/api.md)

## 👤 Autor

- **gabrielxvnx**

## 📄 Licença

MIT
