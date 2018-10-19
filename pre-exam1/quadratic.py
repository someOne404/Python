def big_root(a, b, c):
    x = (-b + (b ** 2 - 4 * a * c) ** (1 / 2)) / (2 * a)
    y = (-b - (b ** 2 - 4 * a * c) ** (1 / 2)) / (2 * a)
    return max(x,y)

def small_root(a, b, c):
    x = (-b + (b ** 2 - 4 * a * c) ** (1 / 2)) / (2 * a)
    y = (-b - (b ** 2 - 4 * a * c) ** (1 / 2)) / (2 * a)
    return min(x,y)   # I found the idea from the students' answer on Piazza https://piazza.com/class/j6m7hyps7tx66x?cid=63

