# Eu Claw 🤖

O **Eu Claw** é minha versão do claw_bot. Ele foi projetado para ser um assistente pessoal e financeiro inteligente, processando áudio, imagens e texto com custo zero de operação.

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

### 3. Rodando o Projeto (Local)
O `uv` gerencia seu ambiente virtual automaticamente.

```bash
# 1. Cria o ambiente e instala dependências de uma vez
uv sync

# 2. (Opcional) Ativar o ambiente virtual manualmente
source .venv/bin/activate

# 3. Rodar o bot
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

## 🚀 Próximas Funcionalidades (Roadmap)

- 📊 **Planilha em Tempo Real**: Sincronização automática de despesas com Google Sheets/Excel.
- 📅 **Gestão de Calendário**: Agendamento e consulta de compromissos (estilo Calendly) com notificações proativas.
- 📧 **Resumo de Gmail**: Consulta e sumarização de e-mails recentes com alertas inteligentes.

## 📁 Documentação

- [Arquitetura](./docs/architecture.md)
- [Guia de Instalação (Setup)](./docs/setup.md)
- [Referência de API (Bot)](./docs/api.md)

## 👤 Autor

- **gabrielxvnx**

## 📄 Licença

MIT
