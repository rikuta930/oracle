import random


def draw_oracle(num):
    if not num % 2 == 0 and num >= 90:
        output = '大吉'

    if num % 2 == 0 and num <= 10:
        output = '大凶'

    if not num % 2 == 0:
        output = '吉'

    if num % 2 == 0:
        output = '凶'

    return output


num = random.randint(1, 100)

print(draw_oracle(num))
