def pattern():
    rows=5
    spaces=0
    stars=0
    for i in range(rows,0,-1):
        spaces=rows-i
        stars=2*i-1
        print(" "* spaces +"*"*stars)
pattern()