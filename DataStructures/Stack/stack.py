
def new_stack():
    stack = {
        "size": 0,
        "first": None,
        "last": None
    }
    return stack

def push(my_stack, element):
    new_node = {
        "info": element,
        "next": my_stack["first"]
    }

    my_stack["first"] = new_node

    if my_stack["size"] == 0:
        my_stack["last"] = new_node

    my_stack["size"] += 1

    return my_stack

