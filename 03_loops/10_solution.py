# EXPONENTIAL BACKOFF
import time

wait_time = 1 # in secs
max_retries = 5
attempts = 1

password = "Prabhjot"

while True: # attempts <= max_retries can also be done
    input_val = input("Enter your password : ")
    if(input_val == password):
        print("Welcome, User")
        break
    if(attempts==max_retries): # if implemented the other condition for while loop then this part will be outside the loop
        print("Invalid password in 5 attempts!!!")
        print("Access Denied!!!")
        break
    # print(f"Attempts : {attempts}, Wait-Time : {wait_time} secs")
    print(f"Try again after {wait_time} secs")
    time.sleep(wait_time)
    wait_time *= 2
    attempts += 1


# print("Program END")