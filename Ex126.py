import inspect


def get_module_object(obj):
    module = inspect.getmodule(obj)
    return module


# Test case
import math

module_obj = get_module_object(math.sqrt)
print("Module Object: ", module_obj)
