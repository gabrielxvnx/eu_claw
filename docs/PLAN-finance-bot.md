# PLAN-finance-bot

## Overview
Personal finance assistant Telegram bot focusing on zero-cost infrastructure using Groq free tier and OpenRouter fallbacks.

## Project Type
BACKEND / TELEGRAM BOT

## Success Criteria
- [ ] Transcribe audio messages into text.
- [ ] Extract date, value, and category from receipt images.
- [ ] Store data in MongoDB.
- [ ] Answer financial questions based on history.
- [ ] $0.00 operating cost (Groq Free Tier).

## Tech Stack (Updated)
- **Language**: Python 3.12+ (aiogram for Telegram)
- **Framework**: **PydanticAI** (for type-safe structured extraction)
- **Database**: MongoDB (Atlas Free Tier) - *Reusing legacy schema (gastos, ganhos, configs)*
- **AI Infrastructure**:
  - Audio: Groq (Whisper Large v3)
  - Vision: Groq (Llama-3.2-11b-vision)
  - Chat/Extract: Groq (Llama-3-70b) or OpenRouter (GPT-OSS 120b)
  - Fallback: Moonshot (Kimi 2.5) via OpenRouter

## Legacy Porting
- **Prompt Logic**: Port the date calculation rules ("ontem", "semana passada") and classification types from `main.py` legacy.
- **Insights**: Re-implement the "Financial Secretary/Coach" advice flow using a second AI turn.
- **Schema**: Maintain 100% compatibility with existing MongoDB collections.

## File Structure
```
.
├── main.py              # Bot entry point & handlers
├── config.py            # Environment configuration
├── database/
│   └── mongo.py         # MongoDB client & operations
├── services/
│   ├── ai_gateway.py    # Unified AI interface (Groq/OpenRouter)
│   ├── parser.py        # Logic to structure finance data
│   └── telegram.py      # Messaging formatting
├── requirements.txt
└── .env                 # Secrets (not committed)
```

## Task Breakdown

### Phase 1: Foundation
- [ ] **Task 1**: Setup Environment & Config → Agent: `backend-specialist`
  - Skills: `clean-code`, `python-patterns`
  - Input: API requirements
  - Output: `config.py`, `.env.example`, `requirements.txt`
  - Verify: Dependencies install correctly.

- [ ] **Task 2**: MongoDB Connection → Agent: `database-architect`
  - Skills: `database-design`
  - Input: Mongo URI
  - Output: `database/mongo.py`
  - Verify: Connection test script passes.

### Phase 2: AI Services
- [ ] **Task 3**: Groq Integration (Audio/Vision) → Agent: `backend-specialist`
  - Skills: `api-patterns`
  - Input: Groq API Key
  - Output: `services/ai_gateway.py` (Whisper & Llama-Vision)
  - Verify: Script transcribing a 5s audio file.

- [ ] **Task 4**: OpenRouter/Moonshot Fallback → Agent: `backend-specialist`
  - Skills: `api-patterns`
  - Input: OpenRouter API Key
  - Output: Enhanced `services/ai_gateway.py`
  - Verify: Logic switches to fallback when Groq fails (Mock).

### Phase 3: Bot Implementation
- [ ] **Task 5**: Telegram Handlers (aiogram) → Agent: `backend-specialist`
  - Skills: `python-patterns`
  - Input: Bot Token
  - Output: `main.py`
  - Verify: Bot responds to `/start`.

- [ ] **Task 6**: Structured Registration Logic → Agent: `backend-specialist`
  - Skills: `clean-code`
  - Input: AI outputs
  - Output: `services/parser.py`
  - Verify: "Spent $50 on coffee" -> `{amount: 50, category: "coffee"}`.

### Phase X: Verification
- [ ] **Task 7**: End-to-End Test → Agent: `test-engineer`
  - Verify: Voice -> DB -> Query.
- [ ] **Task 8**: Security Scan → Agent: `security-auditor`
  - Verify: `security_scan.py` passes.
