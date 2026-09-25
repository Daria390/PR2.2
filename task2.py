def run_task2():
    
    # зчитуємо рядок чисел з клавіатури через пробіл
    user_input = input("Enter numbers separated by space: ")
    
    # перетворюємо введений рядок у список цілих чисел
    numbers_list = [int(item) for item in user_input.split()]
    
    # виводимо початковий список на екран, щоб перевірити
    print("Initial list:", numbers_list)
    
    # запускаємо цикл, який повторюватиметься, доки ми не видалимо існуючий елемент
    while True:
        # питаємо у юзера, яке число треба видалити
        val_to_remove = int(input("Enter the value of the element to delete: "))
        
        # перевіряємо, чи є взагалі таке число в списку
        if val_to_remove in numbers_list:
            # видаляємо всі входження цього значення за допомогою циклу
            while val_to_remove in numbers_list:
                numbers_list.remove(val_to_remove)
            print(f"Element {val_to_remove} was successfully deleted.")
            break  # виходимо з циклу, бо все успішно видалили
        else:
            # якщо такого числа немає, виводимо попередження і показуємо список знову
            print(f"Element {val_to_remove} was not found in the list. Try again!\n")
            print("Current list:", numbers_list)
        
    # виводимо вже змінений список на екран
    print("Updated list:", numbers_list)