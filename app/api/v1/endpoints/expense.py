from fastapi import APIRouter, HTTPException, status
from app.models.model import Expense, ExpenseCreate, ExpenseResponse
from app.core.database import SessionDep

router = APIRouter()


@router.post('/expense', response_model=ExpenseResponse)
async def create_expense(expense: ExpenseCreate, session: SessionDep):
    db_expense = Expense.model_validate(expense)
    session.add(db_expense)
    session.commit()
    session.refresh(db_expense)
    return db_expense


@router.get('/expense/{expense_id}')
def get_expense(expense_id: int, session: SessionDep):
    expense = session.get(Expense, expense_id)
    if not expense:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Despesa não existe")
    return expense