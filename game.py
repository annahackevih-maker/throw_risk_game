import random

fix_score = 0
nefix_score = 0

print('========«Бросай и рискуй»========')
print("=========Цель: 100 очков.=========")

while fix_score < 100:
    choice = input("'1' - бросить \ '2' - забрать очки")

    if choice == '1':
        score = random.randint(1, 6)
        print(f'Выпало :{score}. Всего: {fix_score}')
        if score == 1:
            nefix_score == 0
            print(f"Выпала 1. {nefix_score} очков потеряно. Всего: {fix_score}")
        else:
            nefix_score += score

    elif choice == '2':
        fix_score += nefix_score
        print(f"Ты зафиксировал {nefix_score} очков! Всего: {fix_score}")
        nefix_score = 0
    else:
        print("Введит '1' или '2'!")
if fix_score == 100:
    print('ПОБЕДА! Ты набрал 100 очков')
if fix_score >= 100:
    print('ПОБЕДА! Ты набрал больше 100 очков')