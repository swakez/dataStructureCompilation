def create_triangle(n):
    pl = []
    for i in range(n):
        pl.append([0]*(i+1))
    #print(pl)
    for i in range(n):
        pl[i][0] = 1
        for j in range(1,i):
            pl[i][j] = pl[i-1][j-1] + pl[i-1][j]
        pl[i][i] = 1
    return pl


if __name__ == "__main__":
    pt = create_triangle(int(input("Enter level: ")))
    for i in pt:
        print(i)
