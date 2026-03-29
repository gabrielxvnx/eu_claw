# Arquitetura do Eu Claw

O Eu Claw foi projetado para ser modular, extensível e ter custo zero de operação.

## 🧱 Componentes Principais

```mermaid
graph TD
    User((Usuário)) -->|Áudio/Foto/Texto| Telegram[Telegram Bot - aiogram]
    Telegram -->|Download| LocalStorage[(Storage Temporário)]
    Telegram -->|API Call| Groq[Groq API - Whisper/Llama]
    Groq -->|Transcrição/Extração| AI_Agent[PydanticAI Agent]
    AI_Agent -->|Validação/Parsing| DB[(MongoDB Atlas)]
    AI_Agent -->|Feedback| Telegram
    Telegram -->|Confirmação| User
```

### 1. Comunicação (aiogram)
O bot utiliza a biblioteca `aiogram 3.x` para interações assíncronas no Telegram. Ele rastreia mensagens de voz, fotos e texto simples.

### 2. Orquestração de IA (PydanticAI)
Diferente dos prompts de texto tradicionais, utilizamos o **PydanticAI** para garantir que a extração de dados seja tipada e validada.
- **Modelos**: Primariamente Llama-3.1-70b (Groq).
- **Extração**: Transforma linguagem natural em objetos `FinancialEntry`.

## 🔄 Fluxo de Dados (Multimodal)

```mermaid
sequenceDiagram
    participant U as Usuário
    participant T as Bot (aiogram)
    participant G as Groq AI
    participant P as PydanticAI Parser
    participant M as MongoDB

    U->>T: Envia Áudio/Foto
    T->>G: Solicita Transcrição/Visão
    G-->>T: Retorna Texto Extraído
    T->>P: Envia Texto para Parsing
    P->>P: Extrai Entidades (Valor, Item, Categoaria)
    P->>M: Salva no Banco de Dados
    M-->>P: Sucesso
    P-->>T: Resposta Estruturada
    T-->>U: Confirmação "💸 Registrado!"
```
