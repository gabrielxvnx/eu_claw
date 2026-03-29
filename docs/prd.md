# Product Requirements Document (PRD) - Eu Claw

## 1. Visão Geral
O **Eu Claw** é um assistente pessoal e financeiro inteligente, inspirado no `claw_bot`, projetado para ser operado com custo zero via Telegram. O objetivo é permitir que usuários registrem e gerenciem suas finanças através de voz, imagem e texto de forma natural e sem fricção.

## 2. Público-Alvo
- Usuários que buscam controle financeiro ágil.
- Entusiastas de IA que desejam um assistente multimodal (áudio/visão).
- Desenvolvedores interessados em arquiteturas de baixo custo com Groq e PydanticAI.

## 3. Requisitos Funcionais

### RF01: Registro Multimodal
- O sistema deve transcrever áudio em texto usando Whisper (Groq).
- O sistema deve extrair dados de recibos/fotos usando Llama Vision.
- O sistema deve processar comandos em linguagem natural.

### RF02: Inteligência de Extração (Parser)
- O sistema deve classificar automaticamente entre Entradas e Saídas.
- O sistema deve identificar itens, valores, categorias e formas de pagamento.
- O sistema deve lidar com datas relativas ("ontem", "semana passada").

### RF03: Relatórios e Insights
- O sistema deve gerar relatórios mensais, semanais e diários.
- O sistema deve fornecer insights baseados em padrões de gastos (ex: "Você gastou 20% mais com iFood este mês").

### RF04: Persistência
- O sistema deve armazenar dados de forma assíncrona em um banco MongoDB.

## 4. Requisitos Não-Funcionais

### RNF01: Latência
- O processamento de áudio/visão deve ser inferior a 3 segundos na API Groq.

### RNF02: Custos
- O sistema deve priorizar modelos gratuitos (Groq Free Tier).
- O sistema deve ter fallbacks automáticos para OpenRouter/Moonshot.

### RNF03: Segurança
- O sistema deve validar o `user_id` do Telegram para evitar acessos não autorizados.

## 5. Roadmap
- Integração com Google Sheets em tempo real.
- Agendamento estilo Calendly.
- Sumarização de Gmail.
