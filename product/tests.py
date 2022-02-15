from django.test import TestCase
from .models import Product, Category, Discount


# Create your tests here.
class ProductTest(TestCase):
    def setUp(self) -> None:
        self.c1 = Category.objects.create(cat_title='digital product')
        self.c = Category.objects.create(cat_title='clothes')
        self.c2 = Category.objects.create(parent_cat=self.c, cat_title='sport_clothes')
        self.d1 = Discount.objects.create(discount_title='winter'
                                     , discount_amount=100000, type='price')
        self.p1 = Product.objects.create(pro_name='asusx611', price=20000000
                                    , brand='asus', stock=10, discount=self.d1, category=self.c1)
        self.p2 = Product.objects.create(pro_name='phone frame', price=90000
                                    , brand='asus', stock=10, discount=self.d1, category=self.c1)
        self.d2 = Discount.objects.create(discount_title='spring'
                                     , discount_amount=20, type='percent')
        self.p3 = Product.objects.create(pro_name='adidas T-shirt', price=200000
                                     ,brand='adidas', stock=10, discount=self.d2, category=self.c2)
        self.d3 = Discount.objects.create(discount_title='spring'
                                     , discount_amount=30, type='percent', max_value=50000)
        self.p4 = Product.objects.create(pro_name='adidas T-shirt', price=200000
                                     ,brand='adidas', stock=10, discount=self.d3, category=self.c2)


    def test_price_profit_product(self):
        self.assertEqual(self.p1.profit(), 100000)
        self.assertEqual(self.p2.profit(), 90000)

    def test_percent_profit_product(self):
        self.assertEqual(self.p3.profit(), 40000)
        self.assertEqual(self.p4.profit(), 50000)


