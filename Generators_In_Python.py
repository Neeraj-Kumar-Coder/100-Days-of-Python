def infinite_generator():
    current_iteration = 0
    while True:
        current_iteration += 1
        yield current_iteration


def finite_generator(limit):
    current_iteration = 0
    while current_iteration < limit:
        current_iteration += 1
        yield current_iteration


inf_it = infinite_generator()
fin_it = finite_generator(100)

for it in fin_it:
    print(next(inf_it))
