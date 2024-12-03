#  Дан список размера N и целые числа K и L (1 < K ≤ L ≤ N). Найти среднее
# арифметическое всех элементов списка, кроме элементов с номерами от K до L   6
# включительно

def LST(lst, K, L):
    L_list = lst[:K-1] + lst[L:]  # элементы с начала списка до К и с L до конца

    if not L_list:
        return 0
    return sum(L_list) / len(L_list) # среднее арифметическое

while True:
 try:
   N = int(input("Введите размер списка N: "))
   lst = [int(input(f"Введите элемент {i+1}: ")) for i in range(N)]
   K = int(input("Введите K (индекс, начиная с 1): "))
   L = int(input("Введите L (индекс, начиная с 1): "))
   break
 except ValueError:
   print("Неправильно ввели!")

result = LST(lst, K, L)
print(f"Среднее арифметическое всех элементов, кроме элементов с номерами от {K} до {L}: {result}")