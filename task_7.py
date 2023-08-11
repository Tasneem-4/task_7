#السؤال الاول
# def print_number(row):
#     for i in range(1, row + 1):
#         for j in range(i):
#             print(j +1 , end="")
#         print()
# def main():
#     rows = 5
#     print_number(rows)
#
# if __name__ == "__main__":
#     main()

#السؤال الثاني
# def count_sum(x):
#     sum=0
#     for i in range(1,x+1):
#         sum+=i
#     return sum
#
# def main():
#     number=int(input('Enter the number:'))
#     result = count_sum(number)
#     print('The sum of numbers from 1 to ',number ,'is:',result)
# if __name__=="__main__":
#     main()

# السؤال الثالث
# def name():
#     name=input('Enter your name :')
#     rows=len(name)
#     for i in range(1,rows+1):
#         print(name[:i])
#     for i in range(rows -1,0,-1):
#         print(name[:i])
# if __name__=="__main__":
#      name()

# السؤال الرابع
# def words():
#     word=input("Enter Any Word : ")
#     reversed_word = word[::-1]
#     print('Reversed Word :',reversed_word)
# if __name__=="__main__":
#     words()

#السؤال الحامس
# def decending():
#     number= int(input("Enter the value : "))
#
#     while number >= 1:
#         print(number, end=" ")
#         number -= 1
#
# if __name__ == "__main__":
#     decending()

# السؤال السادس
# def multiple():
#     for i in range(1,11):
#      mul=5*i
#      print(mul)
#
# if __name__=="__main__":
#     multiple()

#السؤال السابع
def main():
    Limit_number = int(input("Enter Limit_number: "))
    Max_output = int(input("Enter Maximum output: "))
    Target_number = int(input("Enter Target_number: "))
    count = 0

    for i in range(Target_number, Limit_number + 1, Target_number):
        if count < Max_output:
            print(i, end=" ")
            count += 1
        else:
            break

    print()
if __name__ == "__main__":
    main()
