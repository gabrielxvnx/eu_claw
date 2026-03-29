from pydantic_ai import Agent, RunContext
from services.models import AIAction
from config import Config
from datetime import datetime
import logging

# Reusing the legacy logic for the system prompt instructions
LEGACY_RULES = """
ATUE COMO: Um assistente financeiro pessoal e inteligente (FinBot).
DATA DE HOJE: {data_atual}

OBJETIVO: Extrair dados financeiros da mensagem do usuário.

REGRAS DE CLASSIFICAÇÃO:
- Saída: gastei, comprei, paguei, uber, ifood, etc.
- Entrada: recebi, ganhei, salário, pix, etc.
- Categorias Saída: Essenciais, Alimentação, Transporte, Casa, Lazer, Saúde, Educação, Compras, Outros.
- Categorias Entrada: Salário, Freelance, Investimento, Presente, Outros.
- Pagamento: Pix (padrão), Crédito, Débito, Dinheiro.
- Datas: hoje, ontem, anteontem, X dias atrás. Converta para YYYY-MM-DD.
"""

# Define the PydanticAI Agent
extraction_agent = Agent(
    f"groq:{Config.MODEL_EXTRACT}",
    result_type=AIAction,
    system_prompt=LEGACY_RULES.format(data_atual=datetime.now().strftime("%Y-%m-%d")),
)

class ParserService:
    async def parse_message(self, message: str) -> AIAction:
        try:
            result = await extraction_agent.run(message)
            return result.data
        except Exception as e:
            logging.error(f"PydanticAI Extraction Error: {e}")
            # Simple fallback if PydanticAI fails
            return AIAction(acao="ignorar")

parser_service = ParserService()
