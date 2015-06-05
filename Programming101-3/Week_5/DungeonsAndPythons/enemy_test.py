from enemy import Enemy
import unittest


class EnemyTests(unittest.TestCase):

    def setUp(self):
        self.enemy = Enemy()

    def test_is_alive(self):
        self.assertEqual(self.enemy.is_alive(), True)

    def test_get_health(self):
        self.assertEqual(self.enemy.get_health(), 100)

    def test_get_mana(self):
        self.assertEqual(self.enemy.get_mana(), 100)

    def test_can_cast(self):
        self.assertEqual(self.enemy.can_cast(), True)

    def test_take_healing(self):
        e = Enemy(80, 100, 20)
        e.take_healing(15)
        self.assertEqual(e.get_health(), 95)

    def test_take_mana(self):
        e = Enemy(100, 80, 20)
        e.take_mana(15)
        self.assertEqual(e.get_mana(), 95)

if __name__ == '__main__':
    unittest.main()
