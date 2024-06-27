def main():
    numbers = []
    result = False
    id = 0
    previous = 0
    while result == False:
        user_num = int(input('Enter a number: '))
        if id != 0:
            if user_num<previous:
                numbers.append(user_num)
                result = False
            else:
                result = True
                break
        else: 
            numbers.append(user_num)
        previous = user_num
        id = id + 1
        
    print('Output ')

    print(numbers)
    ########################################
    # Do not delete the return statement
    ########################################
    return numbers


if __name__ == '__main__':
    main()
