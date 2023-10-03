import sqlite3
from pathlib import Path
from pprint import pprint


def init_db():
    global db, cursor
    db = sqlite3.connect(Path(__file__).parent.parent / "db.sqlite3")
    cursor = db.cursor()


def create_tables():
    cursor.execute(
        """
        DROP TABLE IF EXISTS product
        """
    )
    cursor.execute(
        """
        DROP TABLE IF EXISTS category
        """
    )
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS category (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT
        )
        """
    )
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS product (
            productId INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            year TEXT,
            categoryId INTEGER,
            FOREIGN KEY (categoryId) REFERENCES category (id)
        )
    
        """
    )
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS subscribers (
             INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            year TEXT,
            categoryId INTEGER,
            FOREIGN KEY (categoryId) REFERENCES category (id)
        ) 
        """
    )
    db.commit()


def populate_tables():
    cursor.execute(
        """
        INSERT INTO category (name)
        VALUES ('Драма'), ('Боевик'), ('Криминал'), ('Комедия'), ('Фантастика'), ('Ужасы'),
        ('Анмация'), ('Приключения'), ('Мюзикл'), ('Аниме'), ('Фантастика'), ('Mi')
        """
    )
    cursor.execute(
        """
        INSERT INTO product (name, year, categoryId)
        VALUES ('Зеленая миля', 1999, 1),
        ('По соображениям совести', 1995, 2),
        ('Форрест Гамп', 1994, 3),
        ('Побег из Шоушенка', 1994, 4),
        ('Джон Уик', 2014, 5),
        ('Драйв', 2011, 6),
        ('Матрица', 1999, 7),
        ('Мад Макс: Дорога ярости', 2015, 8),
        ('Железный человек', 2008, 9),
        ('Крестный отец', 1972, 10),
        ('Гудфеллас', 1990, 11),
        ('Лицо со шрамом', 1983, 12)
        """
    )
    db.commit()


def get_products():
    cursor.execute(
        """
        SELECT p.name, c.name FROM product p JOIN category c ON p.categoryId = c.id
        """
    )
    return cursor.fetchall()


def get_product_by_category(category_id):
    cursor.execute(
        """
        SELECT * FROM product WHERE categoryId = :c_id
        """,
        {"c_id": category_id},
    )
    return cursor.fetchall()


if __name__ == "__main__":
    init_db()
    create_tables()
    populate_tables()

