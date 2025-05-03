def calculate(x, y):
    return x * y


def calculate_auto(str_, x, y):
    if str_ == "substract":
        return x-y
    elif str_ == "addistion":
        return x+y
    elif str_ == "multiply":
        return x*y
    elif str_ == "divide":
        try:
            return x/y
        except ValueError:
            return "Invalid Value error"
        except TypeError:
            return "Invalid pass variable value"
        except ZeroDivisionError:
            return "Invalid Zero divisor"

