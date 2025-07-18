age = 16

if (age < 18):
    print("Берем в детский лагерь")

if (age > 18):
    print("Не берем в детский лагерь")

age = 19

if (age < 18):
    print("Берем в детский лагерь")
else:
    print("Не берем в детский лагерь")

rate_as_str = input("Оцените работу сотрудника от 1 до 5:")
rate = int(rate_as_str)

if (rate < 1):
    rate = 1

if (rate > 5):
    rate = 5

feedback = ' '

if rate == 1:
    feedback = input("Расскажите, что нам улучшить: ")
elif rate == 2:
    feedback = input("Расскажите, что вас смутило: ")
elif rate == 3:
    feedback = input("Расскажите, как нам стать лучше: ")
elif rate == 4:
    feedback = input("Расскажите, почему не 5: ")
else:
    feedback = input("Расскажите, за что похвалить сотрудника: ")

print(feedback)

for x in range(1, 10):
    print(x)

for x in range(1, 21):
    print("x= ", x, "x²= ", x*x)
