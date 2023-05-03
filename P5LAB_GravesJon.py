# Define your function here.

if __name__ == '__main__':
    # Type your code here. Your code must call the function.
    
    def days_in_feb(user_year):
        days = 28
        year = int(user_year)
        #leap year if perfectly divisible by 400 
        #leap year if the year is non century year and divisible by 4
        #for leap year february will have 29 days
        if (year % 400 == 0) or (year % 100 != 0 and year % 4 == 0):
            days = 29
        return days
#end of function

    
    if __name__ == '__main__':
        user_input = int(input())
        days_print = days_in_feb(user_input)
        
        print(f'{user_input} has {days_print} days in February.')