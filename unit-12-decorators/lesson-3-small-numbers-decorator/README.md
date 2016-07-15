# Small numbers decorator

Implement a `@small_numbers` decorator that changes enforces numeric arguments passed to a function to be less or equal than a given passed parameter. If any numeric argument is greater than that specified limit, a ValueError should be raised. The default limit should be 50. Example:

```python
@small_numbers(limit=50)
def my_func(number_param, string_param):
  pass
```
