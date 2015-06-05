import unittest
from account import Account


class AccountTest(unittest.TestCase):

    def setUp(self):
        self.test_account = Account("Peter", 125, "$")

    def test_create_new_account(self):
        self.assertTrue(isinstance(self.test_account, Account))

    def test_create_new_account_without_argumnets(self):
        with self.assertRaises(TypeError):
            Account()

    def test_deposit_int_money_check_balance(self):
        self.test_account.deposit(100)
        self.assertEqual(self.test_account.balance(), 225)

    def test_deposit_float_money_check_balance(self):
        self.test_account.deposit(100.55)
        self.assertEqual(self.test_account.balance(), 225.55)

    def test_deposit_zero_money(self):
        with self.assertRaises(ValueError):
            self.test_account.deposit(0)

    def test_deposit_negative_money(self):
        with self.assertRaises(ValueError):
            self.test_account.deposit(-10)

    def test_deposit_negative_float_money(self):
        with self.assertRaises(ValueError):
            self.test_account.deposit(-10.55)

    def test_witdraw_money_less_than_balance_should_return_true(self):
        self.assertTrue(self.test_account.withdraw(10.5))

    def test_witdraw_money_more_than_balance_should_return_false(self):
        self.assertFalse(self.test_account.withdraw(2000))

    def test_witdraw_money_same_than_balance_should_return_false(self):
        self.assertFalse(
            self.test_account.withdraw(self.test_account.balance()))

    def test_print_account(self):
        self.assertEqual(
            str(self.test_account),
            "Bank account for Peter with balance of 125$")

    def test_int_account(self):
        self.assertEqual(int(self.test_account), 125)

    def test_transfer_money_to_another_account_with_different_currency(self):
        with self.assertRaises(TypeError):
            second_account = Account("Tosho", 100, "BGN")
            self.test_account.transfer_to(second_account, 25)

    def test_transfer_money_to_another_account_with_same_currency(self):
        second_account = Account("Tosho", 100, "$")
        transfer_result = self.test_account.transfer_to(second_account, 25)
        self.assertTrue(transfer_result)

    def test_transfer_more_money_than_balance_to_another_account_with_same_currency(self):
        second_account = Account("Tosho", 100, "$")
        transfer_result = self.test_account.transfer_to(second_account, 2220)
        self.assertFalse(transfer_result)

    def test_account_history_create_account(self):
        the_account = Account("Gogo", 125, "BGN")
        self.assertEqual(the_account.getHistory(), ['Account was created'])

    def test_account_history_deposit_money(self):
        self.test_account.deposit(100)
        self.assertEqual(self.test_account.getHistory(), ['Account was created', 'Deposited 100$'])

    def test_account_history_withdraw_money_should_succes(self):
        self.test_account.withdraw(25)
        self.assertEqual(self.test_account.getHistory(), ['Account was created', '25$ was withdrawed'])

    def test_account_history_withdraw_more_money_than_ballnace_should_failed(self):
        self.test_account.withdraw(225)
        self.assertEqual(self.test_account.getHistory(), ['Account was created', 'Withdraw for 225$ failed.'])

    def test_account_history_balance_check(self):
        self.test_account.balance()
        self.assertEqual(self.test_account.getHistory(), ['Account was created', 'Balance check -> 125$'])

    def test_account_history_int_check(self):
        int(self.test_account)
        self.assertEqual(self.test_account.getHistory(), ['Account was created', '__int__ check -> 125$'])

if __name__ == '__main__':
    unittest.main()
