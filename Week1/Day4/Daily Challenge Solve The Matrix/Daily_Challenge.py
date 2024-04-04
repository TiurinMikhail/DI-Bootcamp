#Daily Challenge: Solve The Matrix
def print_matrix(matrix,rows,cols,width=1):
    for r in range(rows):
        for c in range(cols):
            print(str(matrix[r][c]).ljust(width), end=' ')
        print()

#Daily Challenge: Solve The Matrix
def transp(matrix,rows,cols,width=1):
    for c in range(cols):
        for r in range(rows):
            print(str(matrix[r][c]).ljust(width), end=' ')
        print()

def del_spaces(list_str):
    for i in list_str:
        if i == []:
            list_str.remove(i)
    for i in range(len(list_str)):
        list_str[i] = list_str[i][:3]
def format_str(stroke):
    stroke_final = ''
    for i in stroke:
        if i.isalpha():
            stroke_final += i
        else:
            stroke_final += ' '
    return ' '.join(stroke_final.split())


def decode_matrix(matrix,rows,cols,width=1):
    final_sp = []
    stroke = ''
    for c in range(cols):
        for r in range(rows):
            if matrix[r][c].isalpha():
                stroke += str(matrix[r][c])
            else:
                stroke += ' '

    final_sp.append(stroke.strip())
    final_message = format_str(final_sp[0])
    return print(final_message)

stroke = """7ii
Tsx
h%?
i #
sM 
$a 
#t%
^r!""".split('\n')

rows = int(input())
columns = int(input())

matrix = [list(i) for i in stroke]
del_spaces(matrix)
print_matrix(matrix,rows,columns)
print()
transp(matrix,len(matrix),3)

decode_matrix(matrix,len(matrix),3)


