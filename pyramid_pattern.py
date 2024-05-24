def create_pyramid(n):
    for i in range(n):
        for j in range(n - i - 1):
            print(' ', end=' ')
        for k in range(2 * i + 1):
            print('*', end=' ')
        print()

n = 5
create_pyramid(n)
