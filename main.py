t = [[1,2,3,0,0,3,2,1],
     [4,4,4,4,4,4,4,4],
     [0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0],
     [14,14,14,14,14,14,14,14],
     [11,12,13,0,0,13,12,11]]
def hod(t):
     print("введите коардинаты фигуры х у")
     xf = int(input())
     yf = int(input())
     if t[xf][yf] == 0:
          print("там пусто...(как в моём кошельке)")
     if t[xf][yf] == 4 or t[xf][yf] == 14:
          print("введите куда сходить х у")
          x = int(input())
          y = int(input())
          if x + 1 != 0 or x - 1 != 0 or y + 1 != 0 or y - 1 != 0:
               return False
          elif x + 1 == 0 and y - 1 == 0 or x + 1 == 0 and y + 1 == 0 or x - 1 == 0 and y - 1 == 0 and x - 1 == 0 and y + 1 == 0:
               return False