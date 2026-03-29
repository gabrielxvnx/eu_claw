# Estratégia de Custos e Configuração (Deep Dive)

O **Eu Claw** foi construído sob o mantra do "Custo Zero". Abaixo detalhamos como isso é alcançado e as chaves necessárias.

## 💰 Estratégia de Custos (Zero-Dollar Stack)

| Componente | Provedor | Plano | Benefício |
|------------|----------|-------|-----------|
| **LLM (Texto)** | Groq | Free | Llama 3.1 70B com latência < 1s sem custo. |
| **LLM (Visão)** | Groq | Free | Llama 3.2 11B Vision para fotos de recibos. |
| **STT (Áudio)** | Groq | Free | Whisper Large v3 (o melhor do mercado) grátis. |
| **Database** | MongoDB Atlas | M0 Free | Clustrer Sandbox com 512MB (suficiente p/ anos de gastos). |
| **Hospedagem** | Local/Docker | Provedor de sua escolha | Pode rodar em uma Raspberry Pi ou Free Tiers da Oracle/AWS. |

### Lógica de Fallback
Caso você atinja os limites (Rate Limits) da Groq em um dia de uso intenso:
1.  O sistema tenta o fallback para o **OpenRouter** (que pode usar modelos gratuitos como Gemini 2.0 Flash ou Llama 3.x de outros provedores).
2.  Você pode configurar o **Moonshot AI** (Kimi) como uma terceira camada de redundância.

---

## 🔑 Variáveis de Ambiente (.env)

O arquivo `.env` é o coração da sua configuração. Abaixo explicamos **o que** é cada chave e **porque** ela é necessária.

### 1. Telegram
- `TELEGRAM_BOT_TOKEN`: 
    - **O que é**: O token único do seu bot (pego no @BotFather).
    - **Por que**: Sem ele, o código não consegue se autenticar com os servidores do Telegram para ouvir mensagens.
- `ALLOWED_USER_IDS`:
    - **O que é**: IDs numéricos dos usuários (seu ID e de quem você permitir).
    - **Por que**: Evita que estranhos usem seu bot e gastem seus tokens/armazenamento. É a segurança básica do assistente pessoal.

### 2. Provedores de IA
- `GROQ_API_KEY`: 
    - **O que é**: Sua chave da [Groq Console](https://console.groq.com).
    - **Por que**: É quem faz toda a "mágica" de entender áudio e texto. Sem ela, o bot fica "surdo" e "burro".
- `OPENROUTER_API_KEY` (Opcional):
    - **O que é**: Chave do [OpenRouter](https://openrouter.ai).
    - **Por que**: Serve como porto seguro caso a Groq caia ou atinja o limite. É o seu plano B.

### 3. Banco de Dados
- `MONGO_URI`:
    - **O que é**: A string de conexão (ex: `mongodb+srv://...`).
    - **Por que**: Onde todos os seus suados centavos registrados serão salvos para sempre.

---

## 📦 Gerenciamento de Pacotes: Por que `uv`?

Substituímos o tradicional `pip` pelo **`uv`** porque:
1.  **Velocidade**: O `uv` é escrito em Rust e é até 100x mais rápido que o pip.
2.  **Reprodutibilidade**: Gerencia dependências de forma muito mais rigorosa, garantindo que o bot rode igual no seu PC e no servidor/Docker.
