# Architecture Decision Records (ADR) - Eu Claw

Este documento lista as decisões arquiteturais tomadas durante o desenvolvimento do Eu Claw.

## ADR-001: Seleção de Framework de IA (PydanticAI)
**Status: Aceito**

### Contexto
Precisávamos de uma forma robusta de transformar linguagem natural em dados JSON tipados para o banco de dados.

### Decisão
Optamos pelo **PydanticAI** em vez de LangGraph ou prompts puros.

### Consequências
- **Vantagens**: Validação rigorosa via Pydantic, suporte nativo a ferramentas (tools) e tipagem estática.
- **Desvantagens**: Framework novo, documentação em evolução.

## ADR-002: Estratégia de Provedores de LLM (Groq First)
**Status: Aceito**

### Contexto
O requisito primordial é "Custo Zero".

### Decisão
Priorizar a **Groq API** para Llama 3.1 (Texto), Llama 3.2 (Visão) e Whisper v3 (Áudio). Adicionar fallback para OpenRouter.

### Consequências
- **Vantagens**: Velocidade incrível e 100% gratuito (dentro dos limites de rate limit).
- **Desvantagens**: Risco de rate limit em horários de pico.

## ADR-003: Interface do Usuário (Telegram Bot via aiogram)
**Status: Aceito**

### Contexto
O assistente deve ser acessível via celular de forma rápida.

### Decisão
Utilizar o **Telegram** como interface via biblioteca `aiogram 3.x`.

### Consequências
- **Vantagens**: Gratuito, suporta áudio nativo, fotos e comandos. Dispensar o desenvolvimento de um App mobile.

## ADR-004: Banco de Dados (MongoDB Assíncrono)
**Status: Aceito**

### Contexto
Necessidade de esquema flexível para diferentes tipos de registros financeiros e configurações.

### Decisão
Utilizar **MongoDB Atlas** com o driver `motor` (async).

### Consequências
- **Vantagens**: Escalabilidade horizontal e facilidade para evoluir o esquema no futuro (ex: novos campos extras).
