
"""[0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 5, 0, 9, 4, 0, 0, 7],
    [0, 0, 0, 3, 0, 8, 2, 1, 9],
    [0, 4, 0, 6, 0, 0, 1, 8, 2],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [2, 3, 8, 0, 0, 7, 0, 5, 0],
    [9, 1, 6, 7, 0, 3, 0, 0, 0],
    [3, 0, 0, 9, 4, 0, 7, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]"""


sudoku = []

def create_sudoku(rozhrani):
    for i in range(rozhrani):
        sudoku.append([])
    return sudoku

print("Pokud chceš napsat prázdné místo napiš 0\nVyber si jednu se tří možností sudoky - 3x3, 9x9, 16x16 (odpověď napiš ve vzoru 1 2 3)")
odpoved = input("Tvoje odpoved: ")



if odpoved == "1":
    create_sudoku(3)
    for i in range(1,4):
        print(f"Napiš čísla do {i}. řádku")
        for j in range(1,4):
            sudoku[i-1].append(int(input(f"Zadej {j}. číslo: ")))


elif odpoved == "2":
    create_sudoku(9)
    for i in range(1,10):
        print(f"Napiš čísla do {i}. řádku")
        for j in range(1,10):
            sudoku[i-1].append(int(input(f"Zadej {j}. číslo: ")))

elif odpoved == "3":
    create_sudoku(16)
    for i in range(1,17):
        print(f"Napiš čísla do {i}. řádku")
        for j in range(1,17):
            sudoku[i-1].append(int(input(f"Zadej {j}. číslo: ")))

else:
    print("Nevibral jsi ani jednu z danych odpovedi")



def find_empty(sudo):
    #   kontrola radku
    for i in range(len(sudo)):
        for j in range(len(sudo[0])):
            if sudo[i][j] == 0:
                return (i, j)
    return None


    #   kontrola sloupce
def valid(sudo, num, pos):
    for i in range(len(sudo)):
        if sudo[pos[0]][i] == num and pos[1] != i:
            return False

    for i in range(len(sudo[0])):
        if sudo[i][pos[1]] == num and pos[0] != i:
            return False
    
    #   kontrola boxu
    box_radek = pos[0] // 3
    box_sloupec = pos[1] // 3

    for i in range(box_radek * 3, box_radek * 3 + 3):
        for j in range(box_sloupec * 3, box_sloupec * 3 + 3):
            if sudo[i][j] == num and (i, j) != pos:
                return False
    return True


def solve(sudo):
    find = find_empty(sudo)
    if not find:
        return True
    else: 
        radek, sloupec = find

    for i in range(1,10):
        if valid(sudo, i, (radek, sloupec)):
            sudo[radek][sloupec] = i
            if solve(sudo):
                return True
            sudo[radek][sloupec] = 0
    return False


def print_sudoku(sudo):
    for i in range(len(sudo)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - -")
        for j in range(len(sudo[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")
            if j == 8:
                print(sudo[i][j])
            else:
                print(str(sudo[i][j]) + " ", end="") 


if __name__ == "__main__":
    print_sudoku(sudoku)
    solve(sudoku)
    print()
    print("- - - - - - - - - - - -")
    print()
    print_sudoku(sudoku)

