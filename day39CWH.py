import sys
print("welcome to kon banega crore pati")
print("There will be total of 15 question  ")
print("After aeach  5 question you will move to next round ")
print("so, lets start")
def question(i,j):
    if (i==1 and j==1):
        print('''Q1: What is the capital of France?
        a) London
        b) Paris
        c) Rome
        d) Madrid''')
        k="b"
        return "b"
    
    
    
    if (i==1 and j==2):
        print('''Q2: Which planet is known as the Red Planet?
            a) Jupiter
            b) Mars
            c) Venus
            d) Saturn''')
        k="b"
        return "b"
    

    if (i==1 and j==3):
        print('''Q3: Who is known as the Father of the Nation in India?
        a) Mahatma Gandhi
        b) Jawaharlal Nehru
        c) Subhas Chandra Bose
        d) Bhagat Singh''')
        k="a"
        return "a"
    

    if (i==1 and j==4):
        print('''Q4: Which of these is a traditional Indian sweet dish?
       a) Sushi
       b) Pizza
       c) Samosa
       d) Gulab Jamun''')
        k="d"
        return "d"
    

    if (i==1 and j==5):
        print('''Q5: What is the chemical symbol for water?
        a) WO
        b) H2O
        c) HO
        d) WA''')
        k="b"
        return "b"
    

    if (i==2 and j==1):
        print('''Q6:Who wrote the famous play "Romeo and Juliet"?
        a) William Shakespeare
        b) Charles Dickens
        c) Mark Twain
        d) Jane Austen''')
        k="a"
        return "a"
    

    if (i==2 and j==2):
        print('''Q7:  Which of these is not a primary color?
        a) Red
        b) Blue
        c) Green
        d) Yellow''')
        k="c"
        return "c"
    

    if (i==2 and j==3):
        print('''Q8: What is the capital of Japan?
        a) Beijing
        b) Tokyo
        c) Seoul
        d) Bangkok''')
        k="b"
        return "b"
    

    if (i==2 and j==4):
        print('''Q9: Which is the smallest continent in the world?
        a) Europe
        b) Asia
        c) Africa
        d) Australia''')
        k="d"
        return "d"
    

    if (i==2 and j==5):
        print('''Q10: What is the national animal of India?
        a) Elephant
        b) Lion
        c) Tiger
        d) Giraffe''')
        k="c"
        return "c"
    

    if (i==3 and j==1):
        print('''Q11: Who painted the famous artwork "Mona Lisa"?
        a) Vincent van Gogh
        b) Pablo Picasso
        c) Leonardo da Vinci
        d) Michelangelo''')
        k="c"
        return "c"
    

    if (i==3 and j==2):
        print('''Q12: Which planet is closest to the Sun?
        a) Venus
        b) Mercury
        c) Mars
        d) Earth''')
        k="b"
        return "b"
    

    if (i==3 and j==3):
        print('''Q13: In which sport is the Davis Cup awarded?
        a) Tennis
        b) Soccer
        c) Cricket
        d) Golf''')
        k="a"
        return "a"
    

    if (i==3 and j==4):
        print('''Q14: What is the largest mammal on Earth?
        a) Elephant
        b) Giraffe
        c) Blue Whale
        d) Hippopotamus''')
        k="c"
        return "c"
    

    if (i==3 and j==5):
        print(''' Q.15- Which is the largest ocean in the world?
        a) Atlantic Ocean
        b) Indian Ocean
        c) Arctic Ocean
        d) Pacific Ocean''')
        k="d"
        return "d"
    
    else:
        return None




for i in range(4):
    print(f"ROUND-- {i}")
    for j in range(6):
        k = question(i, j)  # Get the correct answer for the current question
        if k is not None:  # Check if there's a question for this round
            print("What is your answer?")
            answer = input("Enter your answer: ")
            if answer.lower() == k.lower():
                print("Moving to the next question")
            
            else:
                print(f"you lost the round  {i} ")
                break
    else:
        continue  # Continue to the next iteration of the outer loop if the inner loop wasn't exited
    break  # 