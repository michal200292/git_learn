print("Tak")
for i in range(10):
    print(i,end=" ")

print("Tak")
for i in range(10):
    print(i, end=" ")



def my_dec(f):
    def wrapper():
        print("Follow the white rabbit")
        f()
    return wrapper

@my_dec
def ff():
    try:
        print("Hello from Filip")
    except:
        pass

ff()
