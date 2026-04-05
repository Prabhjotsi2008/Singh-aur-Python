from typing import List, Tuple, Dict, Set, Union


# TYPE-HINTS to specify that the parameter l should be a list of integers or floats, and the return type can also be an integer or a float.
def get_max(l: List[int | float]) -> int | float:
    return max(l)

print(get_max([1,2,3.3,4,5])) # 5

# TYPE-HINTS to specify that the parameter t should be a tuple containing a string and an integer, and the return type is a string.
def format_name(t: Tuple[str, int]) -> str:
    name, age = t
    return f"{name} is {age} years old"

print(format_name(("Prabhjot", 18))) # Prabhjot is 18 years old.


# TYPE-HINTS to specify that the parameter d should be a dictionary with string keys and integer values, and the return type is None (indicating that the function does not return anything).
def dict_printer(d: Dict[str, int]) -> None:
    for k, v in d.items():
        print(f"{k} : {v}")
  
shop = {
    "laptop" : 77000,
    "mobile" : 24000,
    "earbuds" : 3400
}

dict_printer(shop)