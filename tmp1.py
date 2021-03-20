
def dfs(x, y, prev_c, m, n, arr, g):
    if x < m and y < n and x > -1 and y > -1 and g[x][y] == 0 and prev_c == arr[x][y]:
            g[x][y] = 1
            dfs(x-1, y, prev_c, m, n, arr, g)
            dfs(x+1, y, prev_c, m, n, arr, g)
            dfs(x, y-1, prev_c, m, n, arr, g)
            dfs(x, y+1, prev_c, m, n, arr, g)

def ans():
    arr = [['a','a','b','b','a'], ['a','a','b','b','c'], ['a','b','b','b','b']]
    m, n = len(arr), len(arr[0])
    g = [[0] * n for _ in range(m)]
    color = 0
    for i in range(m):
        for j in range(n):
            if g[i][j] == 0:
                color += 1
                dfs(i, j, arr[i][j], m, n, arr, g)
    return color

def main():
    color = ans()
    print(color)

if __name__ == '__main__':
    main()
    