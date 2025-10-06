try:
    value = int(input("Enter a number:"))
    print(10/0)
except Exception as e:
    print(e)
finally :
    print("Execution completed")