x = int ( input("Enter a number: ") ) #ASK THE USER TO ENTER A NUMBER

if ( x > 0 ): #CHECK IF THE NUMBER IS VALID
    sum = 0   #DECLARE A NEW VARIABLE TO DO THE SUMMATION
    for i in range ( 1,x+1 ):
         if ( i%2 != 0 ): #CHECK IF THE NUMBER IS ODD
            sum += i      # ADD THE ODD NUMBERS TO THE SUM
    print("The sum of all odd numbers up to ", x , "is", sum)    #DISPLAY THE RESULT
else:
    print ("Please enter a valid number!") # PRINT AN ERROR MESSAGE IF THE INPUT IS NOT VALID