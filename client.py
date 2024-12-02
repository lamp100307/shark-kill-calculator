import matplotlib.pyplot as plt

# Настройки сетки
grid_size = 15  # Размер сетки 15x15
crossword_grid = [[" " for _ in range(grid_size)] for _ in range(grid_size)]

words = [
    (0, 0, "горизонтально", "ФУДЗИЯМА"),
    (2, 0, "горизонтально", "ЦИНЬ"),
    (4, 0, "горизонтально", "ВЕДЫ"),
    (6, 0, "горизонтально", "КАТАНА"),
    (8, 0, "горизонтально", "ТАДЖМАХАЛ"),
    (10, 0, "горизонтально", "КОНФУЦИЙ"),
    (12, 0, "горизонтально", "НО"),
    (1, 10, "вертикально", "ЧАНЬАНЬ"),  # OK
    (3, 10, "вертикально", "ЛАКШМИ"),   # OK
    (5, 10, "вертикально", "СУМИ"),     # OK
    (7, 10, "вертикально", "БУДДИЗМ"),  # OK
    (9, 10, "вертикально", "БУШИДО"),   # OK
    (11, 10, "вертикально", "ПАГОДА"),   # OK
    (13, 10, "вертикально", "НАРА"),     # OK
    (10, 6, "вертикально", "МАХАБХАРА")
]

# Заполнение сетки словами
for x, y, direction, word in words:
    if direction == "горизонтально":
        for i, char in enumerate(word):
            crossword_grid[x][y + i] = char
    elif direction == "вертикально":
        for i, char in enumerate(word):
            crossword_grid[x + i][y] = char

# Построение визуализации
fig, ax = plt.subplots(figsize=(10, 10))
ax.set_xlim(0, grid_size)
ax.set_ylim(0, grid_size)
ax.set_xticks(range(grid_size + 1))
ax.set_yticks(range(grid_size + 1))
ax.grid(True)

# Отображение букв
for i in range(grid_size):
    for j in range(grid_size):
        if crossword_grid[i][j] != " ":
            ax.text(j + 0.5, grid_size - i - 0.5, crossword_grid[i][j],
                    ha="center", va="center", fontsize=12, color="black")

ax.set_xticklabels([])
ax.set_yticklabels([])
ax.tick_params(left=False, bottom=False)
plt.show()
