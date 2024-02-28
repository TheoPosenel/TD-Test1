import unittest
from unittest.mock import Mock
from allClass import Pizza, CartePizzeria, CartePizzeriaException

class TestCartePizzeria(unittest.TestCase):
    def test_is_empty(self):
        c = CartePizzeria()
        self.assertTrue(c.is_empty())

        pizza_mock = Mock()
        c.add_pizza(pizza_mock)
        self.assertFalse(c.is_empty())

    def test_nb_pizzas(self):
        c = CartePizzeria()
        self.assertEqual(c.nb_pizzas(), 0)

        pizza_mock1 = Mock()
        pizza_mock2 = Mock()
        c.add_pizza(pizza_mock1)
        c.add_pizza(pizza_mock2)
        self.assertEqual(c.nb_pizzas(), 2)

    def test_add_pizza(self):
        c = CartePizzeria()
        pizza_mock = Mock()
        c.add_pizza(pizza_mock)
        self.assertEqual(c.nb_pizzas(), 1)

    def test_remove_pizza(self):
        c = CartePizzeria()
        pizza_mock = Mock()
        pizza_mock.nom = "Test Pizza"
        c.add_pizza(pizza_mock)
        
        c.remove_pizza("Test Pizza")
        self.assertEqual(c.nb_pizzas(), 0)

    def test_remove_non_existing_pizza(self):
        c = CartePizzeria()
        with self.assertRaises(CartePizzeriaException):
            c.remove_pizza("Non Existing Pizza")

if __name__ == '__main__':
    unittest.main()