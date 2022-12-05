
for i in range(5, 10):
    print(i)

# cost1 = False
# while True:
#     try:
#         cost1 = int(input("Введіть ціну товару, без копійок (X): "))
#     except ValueError:
#         print("Використовуйте тільки цілі числа")
#         continue
#     if cost1 >= 0:
#         break
#
# cost2 = False
# while True:
#     try:
#         cost2 = int(input("Введіть остаток від ціни товару (копійки) (Y): "))
#     except ValueError:
#         print("Використовуйте тільки цілі числа")
#         continue
#     if cost2 >= 0:
#         break
#
# num = False
# while True:
#     try:
#         num = int(input("Введіть необхідну кількість товару (N): "))
#     except ValueError:
#         print("Використовуйте тільки цілі числа")
#         continue
#     if num >= 1:
#         break
#     else:
#         print('Кількість повинна бути більша за 0')
#
# price = float(((cost1 * 100) + cost2) * num)
# print("=" * 50)
# print("Необхідна сума у гривнях: {:.2f}".format(float(price / 100)))
# print("Необхідна сума к копійках: {:.0f}".format(float(price)))
