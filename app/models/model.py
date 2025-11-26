from datetime import datetime
from decimal import Decimal
from sqlmodel import SQLModel, Field, Relationship

class UserBase(SQLModel):
    """ data model schema"""
    nome: str
    budget: int
    created_at: datetime

class UserCreate(UserBase):
    pass

class UserResponse(UserBase):
    id: int
    expenses: list["Expense"]

class User(UserBase, table=True):
    """
        Modelo que gera tabela User no banco
        Demais campos Herdam do schema UserBase
    """
    id: int | None = Field(default=None, primary_key=True) # Relacionamento com a tabela Expense
    created_at: datetime = Field(default_factory=datetime.now)
    expenses: list["Expense"] = Relationship(back_populates='user')

class ExpenseBase(SQLModel):
    """ data model schema"""
    title: str = Field(index=True)
    description: str
    value: Decimal = Field(default=Decimal(0), index=True)
    created_at: datetime = Field(default_factory=datetime.now)

class ExpenseCreate(ExpenseBase):
    user_id: int

class ExpenseResponse(ExpenseBase):
    id: int

class Expense(ExpenseBase, table=True):
    """
        Modelo que gera tabela Expense no banco
        Demais campos Herdam do schema ExpenseBase
    """
    id: int | None = Field(default=None, primary_key=True)
    user_id: int | None = Field(default=None, foreign_key='user.id')
    user: User = Relationship(back_populates='expenses') # Relacionamento com a tabela User