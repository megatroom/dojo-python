
def rgb(list):
    result = {
        "R": [],
        "G": [],
        "B": [],
    }

    for item in list:
        result[item].append(item)

    return result["R"] + result["G"] + result["B"]


if __name__ == "__main__":
    list = input("Digite as letras separadas por vírgula: ").split(",")
    print(rgb(list))
