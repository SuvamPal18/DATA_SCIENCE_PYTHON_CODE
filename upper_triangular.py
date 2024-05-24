def create_upper_triangular(n):
    for i in range(n):
        for j in range(n):
            if j >= i:
                print('*', end=' ')
            else:
                print(' ', end=' ')
        print() 

n = 5
create_upper_triangular(n)
