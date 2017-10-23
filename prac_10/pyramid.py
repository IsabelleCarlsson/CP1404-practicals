
def main():

    n = int(input("How big? "))

    print(do_it(n))


def calculate_n_blocks(n):
    total = 0
    for n in range(1, n+1):
        total += n
    return total


def do_it(n):
    if n <= 0:
        return 0
    return n + do_it(n-1)

main()
