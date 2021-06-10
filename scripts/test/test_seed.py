import unittest
# Test target
from scripts.seed import Seed

class TestSeed(unittest.TestCase):
    def setUp(self):
        self.seed = Seed()
        self.number_of_users = 150
        # I will try to save requests cause are limited
        self.users_result = self.seed.get_users(
            num_users=self.number_of_users
        )

    def test_correct_number_of_users(self):
        number_of_users = len(self.users_result)
        self.assertEqual(number_of_users, self.number_of_users)

    def test_sub_pagination_of_users(self):
        button_user_id = 500
        result = self.seed.get_users(
            num_users=99,
            since_id=button_user_id
        )
        ids = [reg['id'] for reg in result]
        for id in ids:
            self.assertTrue(id > button_user_id)

    def unique_users(self):
        user_ids = [
            reg['id'] for reg in self.users_result
        ]
        users_retuned = len(users_ids)
        unique_userts_returded = len(set(users_retuned))
        self.assertEqual(users_retuned, unique_userts_returded)
