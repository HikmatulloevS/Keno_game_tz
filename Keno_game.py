from random import sample


class Keno:
    # Свойства класса
    __MIN_BET = 0.5
    __MAX_BET = 5
    __money = 100
    __list_of_nums = [i for i in range(1, 81)]
    __count_of_guess = 10

    # Метод для ввода ставки
    def to_bet(self) -> float:
        bet = input(f'Делайте ставку!(мин: {self.__MIN_BET}, макс: {self.__MAX_BET}) -> ')

        # Проверка на валидность
        while not bet.replace('.', '').isnumeric() or not self.__MIN_BET <= float(bet) <= self.__MAX_BET:
            print(f'Ставка должна быть от {self.__MIN_BET} до {self.__MAX_BET}')
            bet = input(f'Делайте ставку!(мин: {self.__MIN_BET}, макс: {self.__MAX_BET}) -> ')
        self.__money -= float(bet)
        return float(bet)

    @classmethod
    # Метод для генерации рандомных чисел
    def get_random_nums(cls) -> list[int]:
        list_of_random_nums = sample(cls.__list_of_nums, 20)
        return list_of_random_nums

    # Метод для ввода чисел
    def entering_nums(self) -> list[int]:
        # Список введённых чисел
        entered_nums = []
        for i in range(self.__count_of_guess):
            a = input('Введите ваше число(от 1 до 80 включительно) -> ')

            # Проверка на валидность
            while not a.isnumeric() or int(a) in entered_nums or int(a) < 1 or int(a) > 80:
                a = input(
                    "Введены данные неправильного формата. Пж повторите попытку.Введите ваше число(от 1 до 80 включительно) -> ")
            entered_nums.append(int(a))
        return entered_nums

    @staticmethod
    # Метод для поиска совпадений
    def matching_choices(random_nums: list, guessed_nums: list) -> list[int]:
        matches = list(set(random_nums) & set(guessed_nums))
        return matches

    @staticmethod
    # Метод для определения вознаграждения
    def award(bet, matches) -> int:
        # Количество совпадений
        amount_of_matches = len(matches)
        match amount_of_matches:
            case 5:
                return bet
            case 6:
                return bet * 24
            case 7:
                return bet * 142
            case 8:
                return bet * 1000
            case 9:
                return bet * 4500
            case 10:
                return bet * 10000
            case _:
                return 0

    @property
    # Функция для просмотра баланса
    def money(self):
        return self.__money

    # Процесс игры
    def start_game(self):
        print('Welcome to game')

        # Ставка
        bet = self.to_bet()
        print(f'Ваша ставка: {bet}')

        # Введённые числа
        entered_nums = self.entering_nums()
        print(f'Введённые числа: {entered_nums}')

        # Рандомные числа
        nums = self.get_random_nums()
        print(f'Все рандомные числа: {nums}')

        # Совпадения
        matched = self.matching_choices(nums, entered_nums)
        print(f'Угаданные числа: {matched}')

        # Выигрыш
        win = self.award(bet, matched)
        self.__money += win
        print(f'Ваш выигрыш состовляет: {win}')
        print(f'Ваш текущий баланс: {self.__money}')


if __name__ == '__main__':

    kn = Keno()
    answer = 'Y'
    while answer == 'Y' and kn.money > 0:
        kn.start_game()
        answer = input('Хотите продолжить игру?(Y/N) -> ').upper()
