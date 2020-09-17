list_test = [[1, 1, 1, 0, 0, 0], [0, 1, 0, 0, 0, 0], [1, 1, 1, 0, 0, 0], [
    0, 0, 2, 4, 4, 0], [0, 0, 0, 2, 0, 0], [0, 0, 1, 2, 4, 0]]


def sum_def(grid, y, x):
    sum = 0
    sum += grid[y][x]
    sum += grid[y + 1][x]
    sum += grid[y + 1][x - 1]
    sum += grid[y + 1][x + 1]
    sum += grid[y - 1][x]
    sum += grid[y - 1][x - 1]
    sum += grid[y - 1][x + 1]
    return sum


grid = []
for i in range(6):
    array = list(map(int, input().split()))
    grid.append(array)

my_list = []
for i in range(1, 5):
    sum = 0
    for j in range(1, 5):
        sum = sum_def(grid, i, j)
        my_list.append(sum)
print(max(my_list))
