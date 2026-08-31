

def new_queue():
    new_queue ={"size": 0,
             "elements" : []
             }
    return new_queue

def enqueue (my_queue, element):
    my_queue["elements"].append(element)
    my_queue["size"] += 1
    return my_queue




    


