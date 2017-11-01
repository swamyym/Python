
#horizontal and vertical lines
#This script calculates the number of squares given square size and number of missing places and places where the lines are missing.


square_size = int(input("enter a number between 4 and 20 inclusive: "))
#square_size = 4

number_of_missing = int(input("enter the number of missing lines: "))
#==============================================================================
# hor_miss_line = [3]
# ver_miss_line = [1,3]
#==============================================================================
places_missing_hor=[]
places_missing_ver = []
for i in range(number_of_missing):
    missing_lines = input("enter missing lines in format:")
    missing_in_lines = missing_lines.split(',')
    print(missing_in_lines)
    if missing_in_lines[0].upper() == "H":
        places_missing_hor.append((int(missing_in_lines[1]),int(missing_in_lines[2])))
    elif missing_in_lines[0].upper() == "V":
        places_missing_ver.append((int(missing_in_lines[1]),int(missing_in_lines[2])))
#places_missing_hor = [(3,3)]
#places_missing_ver = [(3,2),(3,3)]
#print((3,2) in places_missing_ver)
print(places_missing_hor)
print(places_missing_ver)
squares= 0

def square(x,y,tot_lin):
  sq=0
  for i in range(1,tot_lin-max(x,y)+1):
    if (x,y+i-1) in places_missing_hor or (y,x+i-1) in places_missing_ver:
      print("missing",x,x+i-1,y,y+i-1)
      break
    if all([True if a in places_missing_hor else False for a in [(x+i,y+j) for j in range(i)]]) or all([True if a in places_missing_ver else False for a in [(y+i,x+j) for j in range(i)]]) :
      print(x+1,y+i-1,y+1,x+i-1)
      continue
    else:
      #print(x+1,y+i-1,y+1,x+i-1)
      sq += 1
    #print(squares)

  return sq

for i in range(1,square_size):
    for j in range(1,square_size):
        ij_squares = square(i,j,square_size)
        squares = squares+ ij_squares
        print("{0},{1} th squares is {2}".format(i,j,ij_squares))

print("total number of squares: ",squares)
