from django.test import TestCase
from .models import DiscountCode, OrderItem, Basket
from customer.models import Customer
from product.models import Product, Category, Discount


# Create your tests here.
class OrderTest(TestCase):
    def setUp(self) -> None:
        # create a customer object for test
        self.c1 = Customer.objects.create(first_name='akbar', last_name='babii',
                                          password='12345678', phone='09123456789')

        # create a discount code and basket related to a customer for test
        self.d2 = DiscountCode.objects.create(code_title='تخفیف پاییزی', code_amount=30000)
        self.b1 = Basket.objects.create(basket_customer=self.c1, basket_code=self.d2)
        # create basket without discount code
        self.b2 = Basket.objects.create(basket_customer=self.c1)
        self.b3 = Basket.objects.create(basket_customer=self.c1)

        # create product for order item to test
        self.c1 = Category.objects.create(cat_title='digital product')
        self.d1 = Discount.objects.create(discount_title='winter'
                                          , discount_amount=100000, type='price')
        self.p1 = Product.objects.create(pro_name='asusx611', price=20000000
                                         , brand='asus', stock=10, discount=self.d1, category=self.c1)
        # create product without discount
        self.p2 = Product.objects.create(pro_name='asusx611', price=20000000
                                         , brand='asus', stock=10, category=self.c1)

        # create order item to test
        self.o1 = OrderItem.objects.create(number=2, order_product=self.p1, basket=self.b1)
        self.o2 = OrderItem.objects.create(number=1, order_product=self.p1, basket=self.b1)
        # create order item by a basket without discount code
        self.o3 = OrderItem.objects.create(number=1, order_product=self.p1, basket=self.b2)
        self.o4 = OrderItem.objects.create(number=1, order_product=self.p2, basket=self.b3)

    # DiscountCode profit function returns true profit
    def test_DiscountCode_profit_fun(self):
        self.assertEqual(self.d2.profit_value(15000), 15000)
        self.assertEqual(self.d2.profit_value(40000), 30000)

    # total basket value calculated truely
    def test_total_basket_price_no_discount(self):
        self.assertEqual(self.b1.total_no_discount, 60000000)

    # total basket valeu without
    # discount code for basket calculated truely
    def test_total_basket_price_no_discount_code(self):
        self.assertEqual(self.b1.basket_total_value, 59670000)
        self.assertEqual(self.b2.basket_total_value, 19900000)

    # total basket valeu without
    # any discount for basket calculated truely
    def test_basket_value_any_discount(self):
        self.assertEqual(self.b3.basket_total_value, 20000000)

