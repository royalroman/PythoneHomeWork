# Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.


lines_n = 0
words_n = 0
f = open('task2.txt', 'r')
for line in f:
    lines_n += 1
    words = line.split()
    words_n += len(words)
f.close()
print(lines_n)
print(words_n)
