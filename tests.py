from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # тестируем add_two_books - добавление двух книг и появление двух книг в словаре
    def test_add_new_book_add_two_books_dict_has_two_books(self):
        # создаем экземпляр класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две книги
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_rating()) == 2

    # тестируем add_two_books - добавление двух одинаковых книг и появление одной книги в словаре
    def test_add_new_book_add_same_book_twice_dict_has_one_book(self):
        collector = BooksCollector()

        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Гордость и предубеждение и зомби')

        # проверяем, что добавилось именно одна книга
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 1
        assert len(collector.get_books_rating()) == 1

    # тестируем set_book_rating - нельзя выставить рейтинг книге, которой нет в списке
    def test_set_book_rating_rate_book_not_in_dict_returns_none(self):
        collector = BooksCollector()
        # выставляем рейтинг книге, которой нет в списке
        collector.set_book_rating('Что делать, если ваш кот хочет вас убить', 5)
        # проверяем, что её рейтинг соответствует None
        assert collector.get_book_rating('Что делать, если ваш кот хочет вас убить') == None

    # тестируем set_book_rating - нельзя выставить рейтинг меньше 1
    def test_set_book_rating_less_than_one_rating_not_set(self):
        collector = BooksCollector()
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        # выставляем рейтинг 0, хотя в функции set_book_rating range начинается с 1
        collector.set_book_rating('Что делать, если ваш кот хочет вас убить', 0)
        # проверяем, что её рейтинг не равен 0
        assert collector.get_book_rating('Что делать, если ваш кот хочет вас убить') != 0

    # тестируем set_book_rating - нельзя выставить рейтинг больше 10
    def test_set_book_rating_more_than_ten_rating_not_set(self):
        collector = BooksCollector()
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        # выставляем рейтинг 11, хотя в функции set_book_rating range заканчивается 10
        collector.set_book_rating('Что делать, если ваш кот хочет вас убить', 11)
        # проверяем, что её рейтинг не равен 11
        assert collector.get_book_rating('Что делать, если ваш кот хочет вас убить') != 11

    # тестируем get_book_rating - у не добавленной книги нет рейтинга
    def test_get_book_rating_not_added_book_has_no_rating(self):
        collector = BooksCollector()
        # проверяем, что у не добавленной книги нет рейтинга
        assert collector.get_book_rating('Что делать, если ваш кот хочет вас убить') == None

    # тестируем add_book_in_favorites - добавление книги в избранное
    def test_add_book_in_favorites_add_one_book_it_is_in_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        # добавляем книгу из списка в избранное
        collector.add_book_in_favorites('Что делать, если ваш кот хочет вас убить')
        # проверяем, что список favorites имеет длину 1
        assert len(collector.get_list_of_favorites_books()) == 1

    # тестируем add_book_in_favorites - добавление книги в избранное
    def test_delete_book_from_favorites_list_is_empty(self):
        collector = BooksCollector()
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        # добавляем книгу из списка в избранное
        collector.add_book_in_favorites('Что делать, если ваш кот хочет вас убить')
        # удалеяем книгу из списка избранного
        collector.delete_book_from_favorites('Что делать, если ваш кот хочет вас убить')
        # проверяем, что список favorites имеет длину 0
        assert len(collector.get_list_of_favorites_books()) == 0

    # тестируем add_book_in_favorites - нельзя добавить книгу в избранное, если ее нет в словаре
    def test_add_book_in_favorites_book_not_in_dict_is_not_added_to_favorites(self):
        collector = BooksCollector()
        # добавляем книгу из списка в избранное
        collector.add_book_in_favorites('Что делать, если ваш кот хочет вас убить')
        # проверяем, что список favorites имеет длину 0
        assert len(collector.get_list_of_favorites_books()) == 0

    #тестируем get_books_with_specific_rating - получение двух книг с одинаковым рейтингом
    def test_get_books_with_specific_rating_add_three_books_return_two_books(self):
        collector = BooksCollector()
        # добавляем три книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.add_new_book('Кулинарная книга Хогвартса')
        # устанавливаем их рейтинг
        collector.set_book_rating('Гордость и предубеждение и зомби', 5)
        collector.set_book_rating('Что делать, если ваш кот хочет вас убить', 5)
        collector.set_book_rating('Кулинарная книга Хогвартса', 8)
        # проверяем, что список возвращает две книги
        assert len(collector.get_books_with_specific_rating(5)) == 2















