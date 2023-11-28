def badge_maker(name):
    return f"Hello, my name is {name}."

def batch_badge_creator(names):
    return [f"Hello, my name is {name}." for name in names]

def assign_rooms(names):
    room = 1
    assign_house_number = []

    for name in names:
        assign = f"Hello, {name}! You'll be assigned to room {room}!"
        assign_house_number.append(assign)
        room += 1
    return assign_house_number

def printer(names):
    for batch in batch_badge_creator(names):
        print(batch)

    for room in assign_rooms(names):
        print(room)
    


print(printer(['joj', 'joe', 'jim', 'jil', 'jay']))
