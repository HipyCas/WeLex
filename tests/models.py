import unittest

from app import create_app
from app.models import User


class UserTests(unittest.TestCase):
    def test_fields(self):
        app = create_app()
        app.app_context().push()

        user1 = User(nombre='Primer', apellidos='Usuario', alias='primi')
        self.assertEqual(user1.nombre, 'Primer')
        self.assertEqual(user1.apellidos, 'Usuario')
        self.assertEqual(user1.alias, 'primi')


if __name__ == '__main__':
    unittest.main()
