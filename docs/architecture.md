# Arquitetura do FinBot

O FinBot foi projetado para ser modular, extensível e ter custo zero de operação.

## 🧱 Componentes Principais

### 1. Comunicação (aiogram)
O bot utiliza a biblioteca `aiogram 3.x` para interações assíncronas no Telegram. Ele rastreia mensagens de voz, fotos e texto simples.

### 2. Orquestração de IA (PydanticAI)
Diferente dos prompts de texto tradicionais, utilizamos o **PydanticAI** para garantir que a extração de dados seja tipada e validada.
- **Modelos**: Primariamente Llama-3.1-70b (Groq).
- **Extração**: Transforma linguagem natural em objetos `FinancialEntry`.

### 3. Gateway de Serviços (Groq / OpenRouter)
- **Audio**: `whisper-large-v3` para transcrição instantânea.
- **Vision**: `llama-3.2-11b-vision` para leitura de recibos.
- **Fallbacks**: Lógica implementada para alternar para OpenRouter/Moonshot caso os limites da Groq sejam atingidos.

### 4. Persistência (MongoDB)
Utilizamos MongoDB Atlas (Free Tier) com a biblioteca `motor` para operações assíncronas.
- Coleções: `gastos`, `ganhos`, `configuracoes`.

## 🔄 Fluxo de Dados

1. **Input**: Usuário envia áudio/texto/foto.
2. **Pre-process**: Download e transcrição/visão via Groq.
3. **Parsing**: PydanticAI interpreta o texto + regras de data.
4. **Action**: Gravação no Mongo ou Geração de Relatório.
5. **Output**: Confirmação visual no Telegram.
