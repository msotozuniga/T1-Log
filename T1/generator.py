import sys
import random as rn


def format_int(n):
    s = str(n)
    return '{}{}{}'.format('0' * (9 - len(s)), s, '\n')


def generate(p, t):
    p_lines = p
    P_array = [rn.randint(1, 10 ** 9) for _ in range(p_lines)]
    P_content = ''.join(list(map(format_int, P_array)))
    with open("P.txt", "w") as p:
        p.write(P_content)
        p.close()

    t_lines = int(t)
    T_array = [rn.randint(1, 10 ** 9) for _ in range(t_lines)]
    T_array.sort()

    T_content = ''.join(list(map(format_int, T_array)))

    with open("T.txt", "w") as t:
        t.write(T_content)
        t.close()


if __name__ == '__main__':
    generate(int(sys.argv[1]), int(sys.argv[2]))
