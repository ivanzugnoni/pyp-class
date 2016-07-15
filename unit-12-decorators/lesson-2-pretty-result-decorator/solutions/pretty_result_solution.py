def pretty_result(original_function):
    def new_function(a, b):
        return "The result of the function '{}' is: {}".format(
            original_function.__name__,
            original_function(a, b))
    return new_function
