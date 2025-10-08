que = [
    [
        "What is the capital of France? ", "1-delhi", "2-paris", "3-junagadh", "4-london", '2'
    ]
    [
        "What is the highest mountain in the world? " , "girnar" , "chotila" , "abu" , "mount Everest" , "4"

    ]
]
levels = [1000,2000,3000,4000,5000]

levels = 0
for i in range (0,len(que)):
    print(f"your first que for {levels[i]}")
    print(que[i])
    a=int(input("enter your Ans:"))
    if a==que[i-1]:
        print("you win")
    else:
        print("you loose")