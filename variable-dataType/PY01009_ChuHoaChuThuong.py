if __name__ == '__main__':
    n = str(input())
    dem_thuong, dem_hoa = 0, 0
    for i in n:
        if i.islower():
            dem_thuong += 1
        else:
            dem_hoa += 1
    if dem_thuong >= dem_hoa:
        print(n.lower())
    else:
        print(n.upper())
    