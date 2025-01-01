cnt = 0

def print_numbers():
    global cnt  

    if cnt == 3:
        return
    print(cnt)
    cnt += 1
    print_numbers()

print_numbers()
