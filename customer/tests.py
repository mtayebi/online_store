from django.test import TestCase
from customer.models import Address, Customer


# Create your tests here.
class AddressTest(TestCase):
    def setUp(self) -> None:
        self.c1 = Customer.objects.create(first_name='akbar', last_name='babaii', password='12345678', phone='09154321567')
        self.a1 = Address.objects.create(province='tehran', city='tehran', alley='saatdat abad-bonbast dovom pelak2', customer=self.c1)

    def test_assign_customer(self):
        self.assertEqual(self.a1.customer, self.c1)

    def test_change_customer_address(self):
        self.c2 = Customer.objects.create(first_name='asgar', last_name='babaii', password='12345678', phone='09154321567')
        self.a1.customer = self.c2
        self.assertEqual(self.a1.customer, self.c2)

    def test_logical_delete_address(self):
        self.a1.is_delete()
        self.assertNotIn(self.a1, list(Address.objects.all()))

    def test_archive_deleted_addresses(self):
        self.a1.is_delete()
        print(list(Address.objects.archiev()))
        self.assertIn(self.a1, list(Address.objects.archiev()))

