from unittest import TestCase

from Collections.task1.Mentors2courses import Mentors2courses
from Collections.task1.Namesakes import Namesakes
from Collections.task1.Top3Name import Top3Name

from Collections.task2.main import check_folder, create_folder

import pytest

class Test_Task1(TestCase):

    def test_ok_Mentors2courses(self):
        result = Mentors2courses()

        expected = [
            "На курсах 'Python-разработчик с нуля' и 'Java-разработчик с нуля' преподают: Антон, Евгений, Максим",
            "На курсах 'Python-разработчик с нуля' и 'Fullstack-разработчик на Python' преподают: Александр, Евгений, Елена, Кирилл, Максим, Олег, Роман",
            "На курсах 'Python-разработчик с нуля' и 'Frontend-разработчик с нуля' преподают: Александр, Евгений",
            "На курсах 'Java-разработчик с нуля' и 'Fullstack-разработчик на Python' преподают: Денис, Евгений, Максим",
            "На курсах 'Java-разработчик с нуля' и 'Frontend-разработчик с нуля' преподают: Денис, Евгений",
            "На курсах 'Fullstack-разработчик на Python' и 'Frontend-разработчик с нуля' преподают: Александр, Алена, Владимир, Денис, Евгений, Эдгар"
        ]

        self.assertListEqual(result, expected)

    def test_fail_Mentors2courses(self):
        result = Mentors2courses()
        expected = [
            "На курсах 'Python-разработчик с нуля' и 'Java-разработчик с нуля' преподают: Антон, Евгений, Максим",
            "На курсах 'Python-разработчик с нуля' и 'Fullstack-разработчик на Python' преподают: Александр, Евгений, Елена, Кирилл, Максим, Олег, Роман",
            "На курсах 'Java-разработчик с нуля' и 'Fullstack-разработчик на Python' преподают: Денис, Евгений, Максим",
            "На курсах 'Java-разработчик с нуля' и 'Frontend-разработчик с нуля' преподают: Денис, Евгений",
            "На курсах 'Fullstack-разработчик на Python' и 'Frontend-разработчик с нуля' преподают: Александр, Алена, Владимир, Денис, Евгений, Эдгар"
        ]
        self.assertListEqual(result, expected)

    def test_err_Mentors2courses(self):
        result = Mentors2courses()
        expected = 0
        self.assertListEqual(result, expected)

    def test_skip_Mentors2courses(self):
        self.skipTest('skip')

    def test_ok_Namesakes(self):
        result = Namesakes()
        expected = [
            'На курсе Java-разработчик с нуля есть тёзки: Иван Бочаров, Иван Маркитан, Максим Батырев, Максим Воронцов, Сергей Индюков, Сергей Сердюк',
            'На курсе Fullstack-разработчик на Python есть тёзки: Александр Бардин, Александр Иванов, Александр Ульянцев, Александр Шлейко, Евгений Шек, Евгений Шмаргунов',
            'На курсе Python-разработчик с нуля есть тёзки: Александр Бардин, Александр Иванов, Александр Ульянцев',
            'На курсе Frontend-разработчик с нуля есть тёзки: Александр Беспоясов, Александр Фитискин, Александр Шлейко'
        ]
        self.assertEqual(result, expected)

    def test_fail_Namesakes(self):
        result = Namesakes()
        expected = [
            'На курсе Java-разработчик с нуля есть тёзки: Иван Бочаров, Иван Маркитан, Максим Батырев, Максим Воронцов, Сергей Индюков, Сергей Сердюк',
            'На курсе Python-разработчик с нуля есть тёзки: Александр Бардин, Александр Иванов, Александр Ульянцев',
            'На курсе Frontend-разработчик с нуля есть тёзки: Александр Беспоясов, Александр Фитискин, Александр Шлейко'
        ]
        self.assertEqual(result, expected)

    def test_err_Namesakes(self):
        result = Namesakes()
        expected = 0
        self.assertEqual(result, expected)

    def test_skip_Namesakes(self):
        self.skipTest('skip')

    def test_ok_Top3Name(self):
        result = Top3Name()
        expected = 'Александр: 10 раз(а), Евгений: 5 раз(а), Максим: 4 раз(а)'
        self.assertEqual(result, expected)

    def test_fail_Top3Name(self):
        result = Top3Name()
        expected = 'Александр: 9 раз(а), Евгений: 5 раз(а), Максим: 4 раз(а)'
        self.assertEqual(result, expected)

    def test_err_Top3Name(self):
        result = Top3Name()
        expected = 0
        self.assertEqual(result, expected)

    def test_skip_Top3Name(self):
        self.skipTest('skip')

class Test_Task2:

    def __init__(self, access_token_YD):
        self.access_token_YD = access_token_YD

    def test_ok_check_folder(self):
        result = check_folder(self.access_token_YD, 'test')
        expected = 200
        assert result == expected

    def test_ok_create_folder(self):
        result = create_folder(self.access_token_YD, 'test')
        expected = 201
        assert result == expected

if __name__ == '__main__':

    access_token_YD = '???'

    TT2 = Test_Task2(access_token_YD)

    TT2.test_ok_create_folder()
    TT2.test_ok_check_folder()


