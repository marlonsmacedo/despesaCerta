from app.core.database import engine
from app.models.model import SQLModel

def main():
    SQLModel.metadata.create_all(engine)

if __name__ == "__main__":
    main()
