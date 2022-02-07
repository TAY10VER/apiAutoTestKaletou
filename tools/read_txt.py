def read_txt(filename):
    filepath = "./data/"+filename
    with open(filepath, "r", encoding="utf-8")as f:
        return f.readlines()


if __name__ == '__main__':
    print(read_txt("find_pwd_email.txt"))
    print(" - -" * 50)
    arrs = []
    for data in read_txt("find_pwd_email.txt"):
        arrs.append(tuple(data.strip().split(",")))

    print(arrs[1:])