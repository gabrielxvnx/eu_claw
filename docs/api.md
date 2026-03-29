# Bot Commands & Logic (API)

O FinBot não possui uma API HTTP pública, mas responde a comandos e mensagens no Telegram.

## 🤖 Comandos do Telegram

| Comando | Descrição |
|---------|-----------|
| `/start` | Inicia o bot e mostra as boas-vindas. |
| `/report` | Gera um resumo financeiro do mês atual. |

## 🧠 Lógica de Processamento de Mensagens

O bot processa três tipos de entrada:

### 1. Mensagens de Voz (`F.voice`)
- **Ação**: Download do áudio `.ogg`.
- **Transcrição**: Groq `whisper-large-v3`.
- **Lógica**: O texto transcrito é enviado para o analisador financeiro.

### 2. Fotos de Recibos (`F.photo`)
- **Ação**: Captura da imagem de maior resolução.
- **Visão**: Groq `llama-3.2-11b-vision`.
- **Lógica**: Os itens extraídos da imagem são enviados para o analisador financeiro.

### 3. Texto Simples (`F.text`)
- **Ação**: Envio direto para o `parser_service`.

---

## 🏗️ Estrutura de Resposta (PydanticAI)

A IA sempre tenta converter a entrada em um dos seguintes modelos:

### SAVE (Salvar)
```json
{
  "acao": "salvar",
  "data": {
    "tipo": "entrada" | "saida",
    "item": "nome do item",
    "valor": 0.00,
    "categoria": "...",
    "forma_pagamento": "...",
    "data": "YYYY-MM-DD"
  }
}
```

### CONSULT (Consultar)
```json
{
  "acao": "consultar",
  "periodo": "hoje" | "semana" | "mes"
}
```

### IGNORE (Ignorar)
Mensagens de saudação ou memes são ignoradas pela lógica financeira.
