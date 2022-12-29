for multiplier in range(1, 101, 1):
    if (multiplier > 10):
        break
    elif (multiplier == 5):
        continue
    print("{} X {} = {}".format(multiplier, multiplier, multiplier * multiplier))

# break: loop ko chhor do
# continue: iteration ko chhor do

# Emulation of do-while loop
# while True:
#     loop body
#     if (condition):
#         break