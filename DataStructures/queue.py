

def new_queue():
    new_queue ={"size": 0,
             "elements" : []
             }
    return new_queue

def enqueue (my_queue, element):
    my_queue["elements"].append(element)
    my_queue["size"] += 1
    return my_queue

def dequeue (my_queue, element):
    remove = my_queue["elements"].pop(0)
    my_queue["size"] -= 1
    return remove

def is_empty (my_queue):
    vacia = True
    if my_queue["size"] == 0:
        vacia = False
    return vacia
    


    


