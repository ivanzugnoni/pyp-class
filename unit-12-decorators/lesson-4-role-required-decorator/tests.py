import unittest
from collections import namedtuple


Account = namedtuple('Account', ['name', 'role'])


class User(object):
    def __init__(self, name, level):
        self.name = name
        self.level = level


@role_required(role='owner', user_arg_name='user', user_role_attr='level')
def f1(random_arg, user):
    return "User {} with role {} doing {}".format(
        user.name, user.level, random_arg)


@role_required(role='admin', user_arg_name='account', user_role_attr='role')
def f2(random_arg, account):
    return "Account {} with role {} doing {}".format(
        account.name, account.role, random_arg)


class AssignmentTestCase(unittest.TestCase):
    def test_user_and_level_params_succesful(self):
        res = f1('stuff', user=User(name='John', level='owner'))
        self.assertEqual(res, "User John with role owner doing stuff")

    def test_user_and_level_params_raises(self):
        with self.assertRaises(ValueError):
            f1('playing hockey', user=User(name='Robert', level='staff'))

    def test_account_and_role_params_succesful(self):
        res = f2('stuff', account=Account(name='John', role='admin'))
        self.assertEqual(res, "Account John with role admin doing stuff")

    def test_account_and_role_params_raises(self):
        with self.assertRaises(ValueError):
            f2('playing hockey', account=Account(name='Robert', role='staff'))
