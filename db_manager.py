import os
from sqlalchemy import create_engine, Column, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Konfigurasi Database
DB_FILE = "numbers.db"
engine = create_engine(f"sqlite:///{DB_FILE}", echo=False)
Session = sessionmaker(bind=engine)
Base = declarative_base()

class Number(Base):
    """
    Model for the numbers table in the database.
    """
    __tablename__ = 'numbers'
    id = Column(Integer, primary_key=True)
    angka = Column(String(50))

    def __repr__(self):
        return f"<Number(id={self.id}, angka='{self.angka}')>"

def init_db():
    """Initializes the database and creates the table."""
    Base.metadata.create_all(engine)

def seed_data(session):
    """Seeds the initial Indonesian word data into the database."""
    initial_data = [
        "dua", "empat", "delapan", "lima", "tujuh", 
        "satu", "tiga", "enam", "sepuluh", "sembilan"
    ]
    
    # Check if data already exists to avoid duplicates
    if session.query(Number).count() == 0:
        for idx, word in enumerate(initial_data, 1):
            session.add(Number(id=idx, angka=word))
        session.commit()
        print("Data awal berhasil dimasukkan.")
    else:
        print("Database sudah berisi data.")

def word_to_numeric(session):
    """
    Updates the 'angka' column from Indonesian words to numeric symbols.
    Example: "satu" -> "1"
    """
    mapping = {
        "satu": "1", "dua": "2", "tiga": "3", "empat": "4", "lima": "5",
        "enam": "6", "tujuh": "7", "delapan": "8", "sembilan": "9", "sepuluh": "10"
    }
    
    numbers = session.query(Number).all()
    for num in numbers:
        if num.angka in mapping:
            num.angka = mapping[num.angka]
    session.commit()
    print("Angka berhasil diperbarui menjadi simbol numerik.")

def get_sorted_numbers(session):
    """Returns the numbers sorted by their numeric value."""
    # We cast to integer for sorting if they are stored as strings
    from sqlalchemy import cast
    return session.query(Number).order_by(cast(Number.angka, Integer)).all()

def delete_by_parity(session, parity_type):
    """
    Deletes numbers based on parity.
    :param parity_type: 'even' or 'odd'
    """
    numbers = session.query(Number).all()
    deleted_count = 0
    for num in numbers:
        try:
            val = int(num.angka)
            if parity_type == 'even' and val % 2 == 0:
                session.delete(num)
                deleted_count += 1
            elif parity_type == 'odd' and val % 2 != 0:
                session.delete(num)
                deleted_count += 1
        except ValueError:
            continue
    session.commit()
    print(f"Berhasil menghapus {deleted_count} angka {parity_type}.")

if __name__ == "__main__":
    # Test initialization
    init_db()
    session = Session()
    seed_data(session)
    word_to_numeric(session)
    sorted_nums = get_sorted_numbers(session)
    print("Sorted numbers:", sorted_nums)
    session.close()
