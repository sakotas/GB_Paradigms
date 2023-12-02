class TicTacToe:
    def __init__(self):
        """Инициализирует игровое поле и устанавливает текущего игрока."""
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.current_turn = 'X'

    def print_board(self) -> None:
        """Выводит текущее состояние игрового поля с учетом размеров и табуляции."""
        for row in self.board:
            print(' | '.join(row))
        print()

    def is_valid_move(self, row: int, col: int) -> bool:
        """Проверяет, является ли ход допустимым. Нумерация начинается с 1."""
        return 0 <= row - 1 < 3 and 0 <= col - 1 < 3 and self.board[row - 1][col - 1] == ' '

    def make_move(self, row: int, col: int) -> bool:
        """Осуществляет ход игрока. Нумерация начинается с 1."""
        if self.is_valid_move(row, col):
            self.board[row - 1][col - 1] = self.current_turn
            self.current_turn = 'O' if self.current_turn == 'X' else 'X'
            return True
        return False

    def check_winner(self) -> str:
        """Проверяет, есть ли победитель в игре."""
        for i in range(3):
            # Проверка строк
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != ' ':
                return self.board[i][0]
            # Проверка столбцов
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != ' ':
                return self.board[0][i]
        # Проверка диагоналей
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != ' ':
            return self.board[0][0]
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != ' ':
            return self.board[2][0]
        return None

    def is_draw(self) -> bool:
        """Проверяет, наступила ли ничья в игре."""
        return all(self.board[row][col] != ' ' for row in range(3) for col in range(3))


def play_game() -> None:
    """Запускает игровой процесс с учетом отображения и нумерации."""
    game = TicTacToe()
    while True:
        game.print_board()
        try:
            row = int(input('Введите номер строки (1-3): '))
            col = int(input('Введите номер столбца (1-3): '))
        except ValueError:
            print('Пожалуйста, введите число.')
            continue

        if game.make_move(row, col):
            winner = game.check_winner()
            if winner:
                game.print_board()
                print(f'Игрок {winner} выиграл!')
                break
            elif game.is_draw():
                game.print_board()
                print('Ничья!')
                break
        else:
            print('Некорректный ход, попробуйте еще раз.')


if __name__ == '__main__':
    play_game()
