# Role required decorator

Write a **class based decorator** `role_required` that takes a role (eg: _admin, staff, superuser, etc_) and restricts the decorated function or method to be executed or not based on the user that's being passed. This decorator should be generic, and could be used in any function, that's why it requires some configuration to be used. Examples:

```python
@role_required(role='owner', user_arg_name='user', user_role_attr='level')
def delete_bank_account(start_date, end_date, user=user):
  # The user's role is stored under the 'level' attribute
  print(user.level)  # owner


@role_required(role='admin', user_arg_name='account', user_role_attr='role')
def delete_records(start_date, end_date, account=account):
  # The user is stored in the 'account' param
  # The user's role is stored under the 'role' attribute
  print(account.role)  # admin
```
