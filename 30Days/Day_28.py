if __name__ == '__main__':
    N = int(input())
    name_list = []
    for N_itr in range(N):
        firstNameEmailID = input().split()

        firstName = firstNameEmailID[0]

        emailID = firstNameEmailID[1]
        if(emailID[-10:] == "@gmail.com"):
            name_list.append(firstName)
    name_list = sorted(name_list)
    for name in name_list:
        print(name)
