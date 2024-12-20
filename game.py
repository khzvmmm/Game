def draw(board):
    """Выводит текущее состояние игрового поля."""
    for row in board:
        print(" | ".join(row))
    print("\n")

def win(board, player):
    """Проверяет, выиграл ли указанный игрок."""
    # Проверка строк
    for row in board:
        if all(cell == player for cell in row):
            return True

    # Проверка столбцов
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    # Проверка диагоналей
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

def is_draw(board):
    """Проверяет, закончилась ли игра вничью."""
    return all(all(cell != " " for cell in row) for row in board)

def move(board):
    """Запрашивает у игрока корректный ход и обновляет игровое поле."""
    while True:
        try:
            coords = input("Введите свой ход в формате строки и столбца (например, 1 2): ")
            row, col = map(int, coords.split())
            if row < 1 or row > 3 or col < 1 or col > 3:
                print("Координаты должны быть от 1 до 3. Попробуйте снова.")
            elif board[row - 1][col - 1] != " ":
                print("Эта ячейка уже занята. Попробуйте снова.")
            else:
                return row - 1, col - 1
        except ValueError:
            print("Некорректный ввод. Введите два числа, разделенные пробелом.")

def main():
    """Основная функция для запуска игры 'Крестики-нолики'."""
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    current_player = 0

    print("Добро пожаловать в игру 'Крестики-нолики'! Игрок 1 играет 'X', игрок 2 играет 'O'.\n")

    while True:
        draw(board)
        print(f"Ход игрока {current_player + 1} ({players[current_player]}).")

        row, col = move(board)
        board[row][col] = players[current_player]

        if win(board, players[current_player]):
            draw(board)
            print(f"Игрок {current_player + 1} ({players[current_player]}) победил!")
            break
        elif is_draw(board):
            draw(board)
            print("Ничья!")
            break

        current_player = 1 - current_player

main()
