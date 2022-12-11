'''
1. Напишите программу, удаляющую из файла все слова, содержащие "абв".
'''

# path = 'home_work_5_1'
# f = open(path, 'r', encoding= 'utf-8')
# my_text = f.read()
# print(my_text)
# f.close

# find_text = "абв"

# def text_remover(lst, rt):
#     lst1= []
#     for i in lst.split():
#         if rt not in i:
#             lst1.append(i)
#     return lst1

# print(text_remover(my_text, find_text))

'''
2. Создайте программу для игры с конфетами человек против человека.

Условие задачи: На столе лежит 2021 конфета.
Играют два игрока делая ход друг после друга.
Первый ход определяется жеребьёвкой.
За один ход можно забрать не более чем 28 конфет.
Все конфеты оппонента достаются сделавшему последний ход.
Сколько конфет нужно взять первому игроку, чтобы забрать все
конфеты у своего конкурента?

a) Добавьте игру против бота
b) Подумайте как наделить бота "интеллектом"
'''
 
# CANDIES = 20
# MAX_STEP = 5

# human = True
# cur_candies = CANDIES

# def get_ai_step():
#     if cur_candies <= MAX_STEP:
#         return cur_candies
#     elif cur_candies <= MAX_STEP * 2:
#         return cur_candies - (MAX_STEP + 1)
#     elif cur_candies == MAX_STEP + 1:
#         return MAX_STEP
#     else:
#         return (MAX_STEP + 1) - cnt   
 
# def get_human_step():
#     while True:
#         cnt = input('Введите количество конфет: ')
#         if cnt.isdigit() and 1 <= int(cnt) <= min(MAX_STEP, cur_candies):
#             return int(cnt)
#         print('Введено некорректное значение')

# while cur_candies:
#     if human:
#         cnt = get_human_step()
#         cur_candies -= cnt
#         print(f'Пользователь взял {cnt} конфет. Осталось {cur_candies}.')
#     else:
#         cnt = get_ai_step()
#         cur_candies -= cnt
#         print(f'Бот взял {cnt} конфет. Осталось {cur_candies}.')
#     human = not human
 
# if human:
#     print('Победил БОТ')
# else:
#     print('Победил человек')

'''
3. Создайте программу для игры в "Крестики-нолики".
Вариант интерфейса:
 1  |  2 | 3
--------------
 4  |  5 | 6
--------------
 7  |  8 | 9
'''

# map = list(range(1,10))

# def draw_board(map):
#     print ('-------------')
#     for i in range(3):
#         print ("|", map[0+i*3], "|", map[1+i*3], "|", map[2+i*3], "|")
#         print ('-------------')

# def take_input(player_token):
#     valid = False
#     while not valid:
#         player_answer = input("Куда поставим " + player_token+"? ")
#         try:
#             player_answer = int(player_answer)
#         except:
#             print ("Некорректный ввод. Вы уверены, что ввели число?")
#             continue
#         if player_answer >= 1 and player_answer <= 9:
#             if (str(map[player_answer-1]) not in "XO"):
#                 map[player_answer-1] = player_token
#                 valid = True
#             else:
#                 print ("Эта клеточка уже занята")
#         else:
#             print ("Некорректный ввод. Введите число от 1 до 9 чтобы походить.")

# def check_win(board):
#     win_coord = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
#     for each in win_coord:
#         if board[each[0]] == board[each[1]] == board[each[2]]:
#             return board[each[0]]
#     return False

# def main(board):
#     counter = 0
#     win = False
#     while not win:
#         draw_board(board)
#         if counter % 2 == 0:
#             take_input("X")
#         else:
#             take_input("O")
#         counter += 1
#         if counter > 4:
#             tmp = check_win(board)
#             if tmp:
#                 print (tmp, "выиграл!")
#                 win = True
#                 break
#         if counter == 9:
#             print ("Ничья!")
#             break
#     draw_board(board)

# main(map)

'''
4. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
Входные и выходные данные хранятся в отдельных текстовых файлах.

aaaasssdddwwwwwwwwwwwweeeffffff -> 4a3s3d9w3w3e6f
4a3s3d9w3w3e6f-> aaaasssdddwwwwwwwwwwwweeeffffff
'''

# path = 'home_work_5_4'
# f = open(path, 'r')
# the_data = f.read()
# # print(the_data)
# f.close

# def rle_zip(s):
#     count = 1
#     result = ''
#     for i in range(len(s)-1):
#         if s[i] == s[i+1]:
#             count += 1
#         else:
#             result = result + str(count) + s[i]
#             count = 1
#     if count > 1 or (s[len(s)-2] != s[-1]):
#         result = result + str(count) + s[-1]
#     return result

# def rle_unzip(s):
#     count = ''
#     result = ''
#     for i in range(len(s)):
#         if not s[i].isalpha():
#             count += s[i]
#         else:
#             result = result + s[i] * int(count)
#             count = ''
#     return result

# print(f'{the_data} -> {rle_zip(the_data)}')
# print(f'{rle_zip(the_data)} -> {rle_unzip(rle_zip(the_data))}')

'''
5* Дан список чисел. Найдите все возрастающие последовательности. Порядок элементов менять нельзя.
*Пример:* 
[1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3] или [1, 7] или [1, 6, 7] и т.д.
'''

# numbers = [1, 5, 2, 3, 4, 6, 1, 7]

# def asc_seq(s):
#     result = [s[0]]
#     for i in s:
#         if i > max(result):
#             result.append(i)
#     return result
    
# print(numbers, '=>', asc_seq(numbers))