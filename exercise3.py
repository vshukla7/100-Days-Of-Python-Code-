# a simple KBC QUIZ  which prints the questions from list and then decide the prize money
questions = [
    [
        "What is the capital of India?",
        "New Delhi",
        "Mumbai",
        "Chennai",
        "Kolkata", 1]
    ,
    [
        "What is the capital of USA?",
        "New Delhi",
        "Washington",
        "Chennai",
        "Kolkata",2]
    ,
    [
        "What is the capital of Canada?",
        "New Delhi",
        "Washington",
        "Chennai",
        "Ottawa", 4]
    ,
    [
        "What is the capital of Australia?",
        "Canberra",     
        "Washington",
        "Chennai",
        "Kolkata", 1]
    ]
prizemoney = [1000, 5000, 10000, 50000]
print("namashkar aadar aadab abhinanadan aabhar mai aabhitab baachan swagat karta hu aapka kaun banega crorepati me ")
for question in questions:
    print("Q.", question[0])
    print("1.", question[1])
    print("2.", question[2])        
    print("3.", question[3])
    print("4.", question[4])    
    answer = int (input ('enter your answer as 1 / 2 / 3 / 4 : '));
    if answer == question[-1]:
        print("or ye galat jawab nahi hai, aap jeet gaye",prizemoney[questions.index(question)],"rupaye")
    else:
        print("aapka jawab galat hai ghar ja sakte hain")
        break
    
