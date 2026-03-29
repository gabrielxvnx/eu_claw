from pydantic import BaseModel, Field
from typing import List, Optional, Literal
from datetime import datetime

class FinancialEntry(BaseModel):
    tipo: Literal["entrada", "saida"]
    item: str = Field(description="Descrição curta do gasto ou ganho")
    valor: float = Field(description="Valor monetário positivo")
    categoria: str = Field(description="Categoria do lançamento (ex: Alimentação, Transporte, Lazer)")
    forma_pagamento: Literal["Pix", "Crédito", "Débito", "Dinheiro", "N/A"]
    data: str = Field(description="Data no formato YYYY-MM-DD")

class MultiFinancialEntry(BaseModel):
    lancamentos: List[FinancialEntry]

class FinanceConfig(BaseModel):
    tipo: Literal["salario", "fatura"]
    dia: Optional[int]
    valor: Optional[float]
    dia_fechamento: Optional[int]
    dia_debito: Optional[int]

class AIAction(BaseModel):
    acao: Literal["salvar", "multiplo", "consultar", "apagar", "configurar", "ignorar"]
    data: Optional[FinancialEntry]
    multiplo: Optional[List[FinancialEntry]]
    config: Optional[FinanceConfig]
    periodo: Optional[str]
    filtro: Optional[str]
    alvo: Optional[str]
