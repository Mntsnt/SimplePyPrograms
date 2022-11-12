
r = int(input("Enter the number of rows you want : "))
def pyfunc(r):
    for x in range(r):
        print(' ' *(r-x-1) + '*' *(2*x+1))
  #  for y in range()
pyfunc(r)

# Adding or removing space on 3rd line determines whether our stars form triangle or pyramid
# When space is added it forms pyramid and if we don't add space it will form just a triangle