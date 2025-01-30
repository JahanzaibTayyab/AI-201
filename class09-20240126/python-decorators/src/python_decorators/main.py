from functools import wraps
import time

# 
# 
# 
def log_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling function: {func.__name__}")
        result = func(*args, **kwargs)
        print(f"Function {func.__name__} finished execution")
        return result
    return wrapper

@log_decorator
def say_hello(name):
    print(f"Hello, {name}!")
    
#
# 
#  
def repeat(num_times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(num_times):
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(3)
def greet(name):
    print(f"Hi {name}!")

# 
# 
# 
@log_decorator
def add(a, b):
    """Adds two numbers."""
    return a + b

#
#
#
def uppercase_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.upper()
    return wrapper

def exclamation_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result + "!"
    return wrapper

@uppercase_decorator
@exclamation_decorator
def greeting():
    return "hello"

# 
# 
# 
class LogDecorator:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print(f"Calling {self.func.__name__}")
        result = self.func(*args, **kwargs)
        print(f"{self.func.__name__} finished execution")
        return result

@LogDecorator
def say_hello(name):
    print(f"Hello, {name}!")
#
#
#

def require_authentication(func):
    def wrapper(user, *args, **kwargs):
        if not user.get("authenticated", False):
            raise PermissionError("User is not authenticated")
        return func(user, *args, **kwargs)
    return wrapper

@require_authentication
def view_profile(user):
    print(f"User profile: {user['name']}")

user1 = {"name": "Alice", "authenticated": True}

# 
# 
# 

def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Execution time: {end_time - start_time:.2f} seconds")
        return result
    return wrapper

@timing_decorator
def slow_function():
    time.sleep(2)
    print("Finished")


if __name__ == "__main__":
    print("**********")
    say_hello("Alice")
    print("**********")
    greet("Bob")
    print("**********")
    print(add.__name__)
    print(add.__doc__)
    add(2, 3)
    print("**********")
    print(greeting())
    print("**********")
    print(greeting())
    print("**********")
    say_hello("Alice")
    print("**********")
    view_profile(user1)
    print("**********")
    slow_function()
    print("**********")
    
    
    
    
    
    
    
    
    
    