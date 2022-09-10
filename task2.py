# Есть массив состоящий из слов и чисел, нужно записать в файл сначала
# слова в порядке их длины, а после слов цифры в порядке возрастания.

a=[123,"file","name",555,78,"age"]
str1=[]
str2=[]
for i in a:
    if type(i)==int:
        str1.append(i)
    else:str2.append(i)
print(str1, str2)
str11=sorted(str1)
str22=sorted(str2)
print(*str11, *str22)
f=open('Borisenko.lesson_8.Task_2.txt','w+')
f.write(f'\n {str22}')
f.write(f'\n {str11}')
print(*f)
f.close()
