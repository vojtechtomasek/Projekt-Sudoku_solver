

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
    
