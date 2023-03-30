
"""[0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 5, 0, 9, 4, 0, 0, 7],
    [0, 0, 0, 3, 0, 8, 2, 1, 9],
    [0, 4, 0, 6, 0, 0, 1, 8, 2],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [2, 3, 8, 0, 0, 7, 0, 5, 0],
    [9, 1, 6, 7, 0, 3, 0, 0, 0],
    [3, 0, 0, 9, 4, 0, 7, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]"""

"""1, 0, 0
   0, 2, 0
   0, 0, 3"""
   
   

"""sudoku = [
    [0, 6, 0, 0, 0, 0, 0, 8, 11, 0, 0 ,15, 14, 0, 0, 16],
    [15, 11, 0, 0, 0, 16, 14, 0, 0, 0, 12, 0, 0, 6, 0, 0],
    [13, 0, 9, 12, 0, 0, 0, 0, 2, 16, 14, 0, 15, 11, 10, 0],
    [2, 0, 16, 0, 11, 0, 15, 10, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 15, 11, 10, 0, 0, 16, 2, 13, 8, 9, 12, 0, 0, 0, 0],
    [12, 13, 0, 0, 4, 1, 5, 6, 2, 3, 0, 0, 0, 0, 11, 10],
    [5, 0, 6, 1, 12, 0, 9, 0, 15, 11, 10, 7, 16, 0, 0, 3],
    [0, 2, 0, 0, 0, 10, 0, 11, 6, 0, 5, 0, 0, 13, 0, 9],
    [10, 7, 15, 11, 16, 0, 0, 0, 12, 13, 0, 0, 0, 0, 0, 6],
    [9, 0, 0, 0, 0, 0, 1, 0, 0, 2, 0, 16, 10, 0, 0, 11],
    [1, 0, 4, 6, 9, 13, 0, 0, 7, 0, 11, 0, 3, 16, 0, 0],
    [16, 14, 0, 0, 7, 0, 10, 15, 4, 6, 1, 0, 0, 0, 13, 8],
    [11, 10, 0, 15, 0, 0, 0, 16, 9, 12, 13, 0, 0, 1, 5, 4],
    [0, 0, 12, 0, 1, 4, 6, 0, 16, 0, 0, 0, 11, 10, 0, 0],
    [0, 0, 5, 0, 8, 12, 13, 0, 10, 0, 0, 11, 2, 0, 0, 14],
    [3, 16, 0, 0, 10, 0, 0, 7, 0, 0, 6, 0, 0, 0, 12, 0 ]
]"""
sudoku = []

def create_sudoku(rozhrani):
    for i in range(rozhrani):
        sudoku.append([])
    return sudoku

print("\nPokud chceš napsat prázdné místo napiš 0\nVyber si jednu se tří možností sudoky - 3x3, 9x9, 16x16 (odpověď napiš ve vzoru 1 2 3)")
odpoved = input("Tvoje odpoved: ")



if odpoved == "1":
    create_sudoku(3)
    for i in range(1,4):
        print(f"Napiš čísla do {i}. řádku")
        for j in range(1,4):
            x = int(input(f"Zadej {j}. číslo: "))
            if x >= 0 and x < 10:
                sudoku[i-1].append(x)


elif odpoved == "2":
    create_sudoku(9)
    for i in range(1,10):
        print(f"Napiš čísla do {i}. řádku")
        for j in range(1,10):
            sudoku[i-1].append(int(input(f"Zadej {j}. číslo: ")))

elif odpoved == "3":
    #create_sudoku(16)
    for i in range(1,17):
        print(f"Napiš čísla do {i}. řádku")
        for j in range(1,17):
            sudoku[i-1].append(int(input(f"Zadej {j}. číslo: ")))

else:
    print("Nevibral jsi ani jednu z danych odpovedi")


#/usr/local/bin/ cmd + shift + .
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
    
    if odpoved == "1" or odpoved == "2":
    #   kontrola boxu
        box_radek = pos[0] // 3
        box_sloupec = pos[1] // 3

        for i in range(box_radek * 3, box_radek * 3 + 3):
            for j in range(box_sloupec * 3, box_sloupec * 3 + 3):
                if sudo[i][j] == num and (i, j) != pos:
                    return False
        return True
    
    if odpoved == "3":
        
        box_radek = pos[0] // 4
        box_sloupec = pos[1] // 4
        
        for i in range(box_radek * 4, box_radek * 4 + 4):
            for j in range(box_sloupec * 4, box_sloupec * 4 + 4):
                if sudo[i][j] == num and (i, j) != pos:
                    return False
        return True



def solve(sudo):
    find = find_empty(sudo)
    if not find:
        return True
    else: 
        radek, sloupec = find

    if odpoved == "1" or odpoved == "2":
        
        for i in range(1,10):
            if valid(sudo, i, (radek, sloupec)):
                sudo[radek][sloupec] = i
                if solve(sudo):
                    return True
                sudo[radek][sloupec] = 0
        return False
    
    if odpoved == "3":
        
        for i in range(1,17):
            if valid(sudo, i, (radek, sloupec)):
                sudo[radek][sloupec] = i
                if solve(sudo):
                    return True
                sudo[radek][sloupec] = 0
        return False


def print_sudoku_3x3(sudo):
    for i in range(len(sudo)):
        if i % 3 == 0 and i != 0:
            print("- - - - ")
        for j in range(len(sudo[0])):
            if j % 3 == 0 and j != 0:
                print("| ", end="")
            if j == 2 or j == 5 or j == 8:
                print(sudo[i][j])
            else:
                print(str(sudo[i][j]) + " ", end="")
        


def print_sudoku_9x9(sudo):
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


def print_sudoku_16x16(sudo):
    for i in range(len(sudo)):
        if i % 4 == 0 and i != 0:
            print("- - - - - - - - - - - -")
        for j in range(len(sudo[0])):
            if j % 4 == 0 and j != 0:
                print(" | ", end="")
            if j == 15:
                print(sudo[i][j])
            else:
                print(str(sudo[i][j]) + " ", end="")


if odpoved == "1":
    print()
    print_sudoku_3x3(sudoku)
    solve(sudoku)
    print("- - - - ")
    print_sudoku_3x3(sudoku)

elif odpoved == "2":
    print()
    print_sudoku_9x9(sudoku)
    solve(sudoku)
    print()
    print("- - - - - - - - - - - -")
    print()
    print_sudoku_9x9(sudoku)


elif odpoved == "3":
    print()
    print_sudoku_16x16(sudoku)
    solve(sudoku)
    print()
    print("- - - - - - - - - - - - - - - - -")
    print()
    print_sudoku_16x16(sudoku)
    