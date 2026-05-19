import random

fix_score = 0
nefix_score = 0

print('========«Бросай и рискуй»========')
print("=========Цель: 100 очков.=========")
print("📌 Правила: 1 единица - теряешь временные очки")
print("📌 2 единицы - теряешь ПОЛОВИНУ постоянных очков + все временные\n")

while fix_score < 100:
    print(f"📊 Постоянные очки: {fix_score} | Временные: {nefix_score}")
    choice = input("'1' - бросить | '2' - забрать очки: ")

    if choice == '1':
        score1 = random.randint(1, 6)
        score2 = random.randint(1, 6)
        print(f"🎲 {score1} | 🎲 {score2}")

        if score1 == 1 and score2 == 1:
            lost = fix_score // 2
            fix_score = fix_score - lost
            print(f"💀 ДВЕ ЕДИНИЦЫ! Теряешь половину постоянных очков (-{lost})!")
            print(f"❌ И теряешь все временные очки (-{nefix_score})!")
            nefix_score = 0
            print(f"📊 Теперь постоянных: {fix_score}")
            
        elif score1 == 1 or score2 == 1:
            print(f"❌ Выпала единица! {nefix_score} временных очков потеряно.")
            nefix_score = 0
        else:
            nefix_score += score1 + score2
            print(f"✅ Добавлено {score1 + score2} очков. Всего временных: {nefix_score}")
        
        if fix_score + nefix_score >= 100:
            print(f"\n🎉 Ты набрал {fix_score + nefix_score} очков 1🎉")
            print(f"🏆 ПОБЕДА! Ты набрал {fix_score + nefix_score} очков! 🏆")
            break

    elif choice == '2':
        if nefix_score > 0:
            fix_score += nefix_score
            print(f"📌 Зафиксировано {nefix_score} очков! Всего: {fix_score}")
            nefix_score = 0
        else:
            print("⚠️ Нет временных очков для фиксации.")
    else:
        print("❌ Введи '1' или '2'!")