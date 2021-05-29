import random

a = 0

user_point = 0
computer_point = 0

while not(user_point == 5) and not(computer_point == 5) :
    if a == 0 :
        user_input = input("Choose from anyone of the options, (rock,paper,scissors) :")
        options = ['rock','paper','scissors']
        computer_input = random.choice(options)

        print(user_input)
        print(computer_input)
    if user_input == 'rock' and computer_input == 'rock':
        print("draw")
        user_point += 0
        computer_point += 0
        user_input = input("Choose from anyone of the options, (rock,paper,scissors) :")
        options = ['rock','paper','scissors']
        computer_input = random.choice(options)

        print(user_input)
        print(computer_input)
       

    elif user_input == 'rock' and computer_input == 'paper' :
        print("Computer wins")
        user_point += 0
        computer_point += 1
        user_input = input("Choose from anyone of the options, (rock,paper,scissors) :")
        options = ['rock','paper','scissors']
        computer_input = random.choice(options)

        print(user_input)
        print(computer_input)
        

    elif user_input == 'rock'  and computer_input == 'scissors' :
        print("User wins") 
        user_point += 1
        computer_point += 0 
        user_input = input("Choose from anyone of the options, (rock,paper,scissors) :")
        options = ['rock','paper','scissors']
        computer_input = random.choice(options)

        print(user_input)
        print(computer_input)
              

    elif user_input == 'scissors' and computer_input == 'scissors' :
        print("Draw")
        user_point += 0
        computer_point += 0
        user_input = input("Choose from anyone of the options, (rock,paper,scissors) :")
        options = ['rock','paper','scissors']
        computer_input = random.choice(options)

        print(user_input)
        print(computer_input)
        

    elif user_input == 'scissors' and computer_input == 'rock' :
        print("Computer wins")
        user_point += 0
        computer_point += 1
        user_input = input("Choose from anyone of the options, (rock,paper,scissors) :")
        options = ['rock','paper','scissors']
        computer_input = random.choice(options)

        print(user_input)
        print(computer_input)
        

    elif user_input == 'scissors' and computer_input == 'paper' :
        print("User wins")
        user_point += 1
        computer_point += 0
        user_input = input("Choose from anyone of the options, (rock,paper,scissors) :")
        options = ['rock','paper','scissors']
        computer_input = random.choice(options)

        print(user_input)
        print(computer_input)
        

    elif user_input == 'paper' and computer_input == 'paper' :
        print("Draw")
        user_point += 0
        computer_point += 0
        user_input = input("Choose from anyone of the options, (rock,paper,scissors) :")
        options = ['rock','paper','scissors']
        computer_input = random.choice(options)

        print(user_input)
        print(computer_input)
        

    elif user_input == 'paper' and computer_input == 'scissors' :
        print("Computer wins")
        user_point += 0
        computer_point += 1
        user_input = input("Choose from anyone of the options, (rock,paper,scissors) :")
        options = ['rock','paper','scissors']
        computer_input = random.choice(options)

        print(user_input)
        print(computer_input)
        

    else  :
        print("User wins")
        user_point += 1
        computer_point += 0
        user_input = input("Choose from anyone of the options, (rock,paper,scissors) :")
        options = ['rock','paper','scissors']
        computer_input = random.choice(options)

        print(user_input)
        print(computer_input)
           
    a += 1
                           

print("Game stopped") 
print(f"User points :{user_point}")
print(f"Computer_points : {computer_point}")       