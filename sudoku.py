from random import choice

difficulty = [50, 40, 30]


def user_table(t, d):
    if d == 'easy':
        d = difficulty[0]
    elif d == 'medium':
        d = difficulty[1]
    elif d == 'hard':
        d = difficulty[2]

    user_t = []
    create_t = []

    for r in range(1, 10):
        c = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        user_t.append(c)

    row = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    col = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    n = 0

    while n < d:
        r = choice(row)
        c = choice(col)

        if user_t[r][c] != 0:
            continue

        if d == 40:
            nums_row = 0
            nums_col = 0
            nums_in_col = [user_t[0][c], user_t[1][c], user_t[2][c], user_t[3][c], user_t[4][c], user_t[5][c],
                           user_t[6][c], user_t[7][c], user_t[8][c]]
            for j in user_t[r]:
                if j != 0:
                    nums_row += 1
            for j in nums_in_col:
                if j != 0:
                    nums_col += 1
            if nums_col >= 5 or nums_row >= 5:
                continue

        elif d == 32:
            nums_row = 0
            nums_col = 0
            nums_in_col = [user_t[0][c], user_t[1][c], user_t[2][c], user_t[3][c], user_t[4][c], user_t[5][c],
                           user_t[6][c], user_t[7][c], user_t[8][c]]
            for j in user_t[r]:
                if j != 0:
                    nums_row += 1
            for j in nums_in_col:
                if j != 0:
                    nums_col += 1
            if nums_col >= 4 or nums_row >= 4:
                continue

        elif d == 28:
            nums_row = 0
            nums_col = 0
            nums_in_col = [user_t[0][c], user_t[1][c], user_t[2][c], user_t[3][c], user_t[4][c], user_t[5][c],
                           user_t[6][c], user_t[7][c], user_t[8][c]]
            for j in user_t[r]:
                if j != 0:
                    nums_row += 1
            for j in nums_in_col:
                if j != 0:
                    nums_col += 1
            if nums_col >= 4 or nums_row >= 4:
                continue

        user_t[r][c] = t[r][c]
        n += 1

    for i in user_t:
        create_t.append(i)

    return create_t

