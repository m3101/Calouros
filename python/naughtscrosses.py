matrix=[
    ["X","O","X"],
    ["O","X","O"],
    ["O","X","-"]
]
lines = [matrix[0],matrix[1],matrix[2],
         [matrix[0][i] for i in range(3)],
         [matrix[1][i] for i in range(3)],
         [matrix[2][i] for i in range(3)],
         [matrix[i][i] for i in range(3)],
         [matrix[i][2-i] for i in range(3)]]
repetitions = list(map(lambda a:len(set(a)),lines))
try:
    empate = not any(["-" in line for line in lines])
    if empate:
        print("Jogo empatado.")
    else:
        print(f"Jogo terminado, {lines[repetitions.index(1)][0]} ganha")
except:
    print("Jogo em andamento")