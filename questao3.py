


def power(x, y):
    if y == 0:
        return 0
    if y == 1:
        return x
    if y<0:
        return 1/power(x, -y)
    if x == 1:
        return x

    return x * power(x, y-1)

if __name__ == "__main__":

    print(f"power(1,0) == {power(1,0)}")
    print(f"power(0, 1) == {power(0,1)}")
    print(f"power(1, 1) == {power(1,1)}")
    print(f"power(-1, 2) == {power(-10, 2)}")
    print(f"power(2, -1) == {power(2, -10)}")
    print(f"power(2, 3) == {power(2, 3)}")
