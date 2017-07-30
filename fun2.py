def draw_1d_old():
    n = int(input("how many stars?"))
    print("*"* n)
    

def draw_1d():
    sign = input("Which sign do you want?")
    times = int(input("How many times?"))
    print(sign*times)


def draw_1d_2(nu):
    sign = str(input("Which sign do you want?"))
    print(sign*nu)

def draw_2d(b , c ):
    sign = input("Which sign do you want?")
    for b in range(b):
        print(c*sign)

def special_draw_2d(n , m , border , fill):
    print(m*border)
    for n in range(n - 2):
        print(border + fill*(m-2) + border)
    print(m*border)
   
      
