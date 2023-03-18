def mirror_reflection_fail(p: int, q: int) -> int:
    def flip(corner: int) -> int:
        r = [1, 0, 3, 2]
        return r[corner]

    def next_corner(this_corner: int, step: int, flipped: bool):
        return (this_corner + step) % 4 if not flipped else (this_corner - step) % 4

    def deflect(distance: float, k: float, this_corner: int, flipped: bool) -> (int):
        b = (p - distance) * k
        if b == 0:
            return this_corner
        if b == p:
            return next_corner(this_corner, 1, flipped)
        if b > p:
            return deflect(distance + q, k, flip(next_corner(this_corner, 2, flipped)), not flipped)
        return deflect(b, 1 / k, next_corner(this_corner, 1, flipped), flipped)

    return deflect(0, q / p, 0, False)


def mirror_reflection(p: int, q: int) -> int:
    from fractions import gcd
    g = gcd(p, q)
    p = (p / g) % 2
    q = (q / g) % 2

    return 1 if p and q else 0 if p else 2


if __name__ == '__main__':
    print(mirror_reflection(3, 1))
    print(mirror_reflection(2, 1))
    print(mirror_reflection(3, 2))
    print(mirror_reflection(3, 3))
    print(mirror_reflection(4, 3))
    print(mirror_reflection(4, 1))
    print(mirror_reflection(5, 1))
    print(mirror_reflection(6, 5))
