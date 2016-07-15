class role_required(object):
    def __init__(self, role, user_arg_name, user_role_attr):
        self.role = role
        self.user_arg_name = user_arg_name
        self.user_role_attr = user_role_attr

    def __call__(self, fn):
        def wrapped(*args, **kwargs):
            user = kwargs[self.user_arg_name]
            if getattr(user, self.user_role_attr) != self.role:
                raise ValueError("Not authorized")
            return fn(*args, **kwargs)
        return wrapped
