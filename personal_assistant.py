name_assistant = 'Денис'
name_assistant = 'Денис'
name_assistant = 'Денис'
name_assistant = 'Денис'
name_assistant = 'Денис'
name_assistant = 'Денис'
name_assistant = 'Денис'
name_assistant = 'Денис'
print('Здраствуйте я ваш ассистент, меня зовут', name_assistant)
name_user = input('Как тебя звать: ')

print('Приятно познакомиться,', name_user, '\n')
age_user = int(input('Сколько тебе лет: '))

print('ого ты взрослый человек, Представляешь через 10 лет тебе будет', age_user + 10)
rise_user = float(input('какой у тебя рост в метрах: '))

print('Да уж, ты очень высокий мой рост всеголишь 0.53! \
      \nПолучаеться ты выше меня на ', rise_user - 0.53, '\n')

print('я столько о тебе узнала! Я в восторге! \
      \nТебя зовут: ', name_user,
      '\nТвой возраст:', age_user,
      '\nТвой рост:', rise_user
      )

choice = int(input('Тебе уже не терпиться узнать что я умею , вот список того , чем я могу помочь \
      \n\n1. Поднять настроение\n2. Напомнить когда кормить когда\n3. Рассказать историю \
      \nЧто ты выберешь(напиши цифру): '))

if choice == 1:
    print('Настроение поднято')
elif choice == 2:
    cat_age = int(input('Сколько коту лет?'))
    if 5 >= cat_age >= 0:
        print('Кота надо кормить всегда')
    elif 0 <= cat_age <= 15:
        print('Очень много , очень много кормить')
    else:
        print('это не кот это самолёт ?')
elif choice == 3:
    print('Жил был колобок, а потом его лиса съела')
else:
    print('что ты я ..... error')

