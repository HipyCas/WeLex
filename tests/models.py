import unittest

from app import create_app
from app.models import User


class UserTests(unittest.TestCase):
    def test_fields(self):
        app = create_app()
        app.app_context().push()
        
        print('> Creating 3 test users (with name, last name and username)')
        user1 = User(nombre='Primero', apellidos='Usuario', alias='primi')
        user2 = User(nombre='Segundo', apellidos='Usuario', alias=)
        self.assertEqual(user1.nombre, 'Primero')
        self.assertEqual(user1.apellidos, 'Usuario')
        self.assertEqual(user1.alias, 'primi')


if __name__ == '__main__':
    unittest.main()
