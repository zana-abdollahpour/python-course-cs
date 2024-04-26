# coords = [[10, 9], [37, -14], [21, 32]]
# for loc in coords:
#     for coord in loc:
#         print(coord)


# demo_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# [[print(val) for val in l] for l in demo_list]


# board = [[num for num in range(1, 4)] for val in range(1, 4)]
# print(board)


board = [["X" if num %
          2 == 0 else "O" for num in range(3)] for num in range(3)]

print(board)
