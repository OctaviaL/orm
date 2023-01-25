from models import Category, Product
import peewee

def post_category(category_name):
    try:
        category = Category(name=category_name)
        category.save()
        print('SAVED!!!!')
    except peewee.IntegrityError:
        print('ТАКАЯ КАТЕГОРИЯ УЖЕ СУЩЕСТВУЕТ!')

def get_categories():
    categories = Category.select()
    for category in categories:
        print(f'{category.id} -- {category.name} -- {category.created_at}')

def delete_category(category_id):
    try:
        category = Category.get(id=category_id)
        category.delete_instance()
        print('Deleted!')
    except peewee.DoesNotExist:
        print('Категория не найдена!')

def update_category(category_id, new_name):
    try:
        category = Category.get(id=category_id)
        category.name = new_name
        category.save()
        print('Обновили')
    except peewee.DoesNotExist:
        print('Категория не найдена!')

def detail_category(id_category):
    try:
        category = Category.get(id=id_category)
        print(category.id, end='\t')
        print(category.name, end='\t')
        print(category.created_at)
        # print(category.products)
        for i in category.products:
            print(f'{i.name} -- {i.price} -- {i.amount}')
    except peewee.DoesNotExist:
        print('Ты пидорас!!!')

def post_product(name, price, amount, category):
    try:
        product = Product(name=name, price=price, amount=amount, category=category)
        product.save()
    except peewee.IntegrityError:
        print('Иди нахуй!! Нет такой категории, жинди баш')

def get_products():
    products = Product.select()
    for i in products:
        print(f'{i.name}, {i.price},{i.amount}, {i.category.name}, {i.category.id}')

def get_product_by_name(name):
    products = Product.select().where(Product.name==name)
    for i in products:
        print(i.name, i.price)