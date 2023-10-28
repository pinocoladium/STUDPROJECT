import sqlalchemy
import sqlalchemy as sq
from models import *
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

login = input('Enter database login: ')
password = input('Enter database password: ')
name_base = input('Enter database name: ')

DSN = f"postgresql://{login}:{password}@localhost:5432/{name_base}"
engine = sqlalchemy.create_engine(DSN)

create_tables(engine)

Session = sessionmaker(bind=engine)
session = Session()

pub1 = Publisher(name='Пушкин')
pub2 = Publisher(name='Лермонтов')
pub3 = Publisher(name='Толстой')
book1 = Book(title='Капитанская дочка', publisher_id=1)
book2 = Book(title='Демон', publisher_id=2)
book3 = Book(title='Руслан и Людмила', publisher_id=1)
book4 = Book(title='Война и мир', publisher_id=3)
book5 = Book(title='Евгений Онегин', publisher_id=1)
shop1 = Shop(name='Лабиринт')
shop2 = Shop(name='Книжный бум')
shop3 = Shop(name='Буквоед')
shop4 = Shop(name='Книжный мир')
shop5 = Shop(name='Амодей')
stock1 = Stock(book_id=1, shop_id=4, count=213)
stock2 = Stock(book_id=3, shop_id=2, count=453)
stock3 = Stock(book_id=5, shop_id=3, count=45)
stock4 = Stock(book_id=2, shop_id=1, count=77)
stock5 = Stock(book_id=4, shop_id=5, count=9)
sale1 = Sale(price=450, data_sale='14.01.2023', stock_id=2, count=2)
sale2 = Sale(price=350, data_sale='17.01.2023', stock_id=5, count=1)
sale3 = Sale(price=390, data_sale='25.01.2023', stock_id=1, count=3)
sale4 = Sale(price=425, data_sale='31.01.2023', stock_id=3, count=1)
sale5 = Sale(price=490, data_sale='10.02.2023', stock_id=4, count=2)

session.add_all([pub1, pub2, pub3, book1, book1, book2, book3, book4, book5, shop1, shop2,
shop3, shop4, shop5, stock1, stock2, stock3, stock4, stock5, sale1, sale2, sale3, sale4, sale5])
session.commit() 

request = iput("Enter publisher's last name: ")

pub_id = session.query(Book).join(Publisher.books).filter(Publisher.name.like(f"%{request}%")).all()

for a in session.query(Book).join(Publisher.books).filter(Publisher.name.like(f"%{request}%")).all():
    for b in session.query(Stock).join(Book.stock).filter(Book.id == a.id).all():
        for c in session.query(Shop).filter(Shop.id == b.shop_id).all():
            for d in session.query(Sale).filter(Sale.stock_id == b.id).all():
                print(f'{a.title} | {b.id} | {c.name} | {d.price} | {d.data_sale}')
    




session.close()