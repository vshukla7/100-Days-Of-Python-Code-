def greet(fx):
    def mfx():
        print("good morning mai pahale run hounga")
        fx(*args , **kwargs)
        print("thanks jo function maine liya tha wo uper play ho gaya as fx ")
        return mfx 
@greet
def add(a , b):
    print (a + b)

# def hello ():
#     print ("hlo i am a sample function")
# add(2 , 3)