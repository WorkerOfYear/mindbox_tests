def check_value(*args, **kwargs) -> bool:
    for item in args:
        if not isinstance(item, (int, float)):
            raise ValueError("Value must be numbers")
        if item <= 0:
            raise ValueError("Value must be greater than 0")

    return True