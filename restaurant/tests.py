from django.test import TestCase
from restaurant.models import Menu
# Create your tests here.

class MenuTest(TestCase):
    def test_get_item(self):
        menu_item = Menu.objects.create(
          name='Sea Food',
          price= 14,
          menu_item_description= 'Fresh Sea Food'
        )
        item_str = menu_item.get_item()
        self.assertEqual(item_str, "Sea Food : 14")