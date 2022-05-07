import sys

def main():
    rows = int(input())
    columns = int(input())
    matrix = []
    for i in range(rows):
        row = sys.stdin.readline().rstrip().split()
        matrix.append(row)

    i = int(input())
    j = int(input())
    neighbours = []
    if i < rows - 1:
        neighbours.append(matrix[i+1][j])
    if i > 0:
        neighbours.append(matrix[i - 1][j])
    if j < columns - 1:
        neighbours.append(matrix[i][j + 1])
    if j > 0:
        neighbours.append(matrix[i][j - 1])

    neighbours = sorted(neighbours, key=int)
    res = ' '.join(neighbours)
    print(res)

if __name__ == '__main__':
    main()