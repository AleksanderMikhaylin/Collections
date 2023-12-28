# Это вы мне? Подсчитываем тёзок на каждом курсе

courses = ["Java-разработчик с нуля", "Fullstack-разработчик на Python", "Python-разработчик с нуля",
           "Frontend-разработчик с нуля"]
mentors = [
    ["Филипп Воронов", "Анна Юшина", "Иван Бочаров", "Анатолий Корсаков", "Юрий Пеньков", "Илья Сухачев",
     "Иван Маркитан", "Ринат Бибиков", "Вадим Ерошевичев", "Тимур Сейсембаев", "Максим Батырев", "Никита Шумский",
     "Алексей Степанов", "Денис Коротков", "Антон Глушков", "Сергей Индюков", "Максим Воронцов", "Евгений Грязнов",
     "Константин Виролайнен", "Сергей Сердюк", "Павел Дерендяев"],
    ["Евгений Шмаргунов", "Олег Булыгин", "Александр Бардин", "Александр Иванов", "Кирилл Табельский",
     "Александр Ульянцев", "Роман Гордиенко", "Адилет Асканжоев", "Александр Шлейко", "Алена Батицкая", "Денис Ежков",
     "Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Максим Филипенко", "Елена Никитина"],
    ["Евгений Шмаргунов", "Олег Булыгин", "Дмитрий Демидов", "Кирилл Табельский", "Александр Ульянцев",
     "Александр Бардин", "Александр Иванов", "Антон Солонилин", "Максим Филипенко", "Елена Никитина", "Азамат Искаков",
     "Роман Гордиенко"],
    ["Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Валерий Хаслер", "Татьяна Тен", "Александр Фитискин",
     "Александр Шлейко", "Алена Батицкая", "Александр Беспоясов", "Денис Ежков", "Николай Лопин", "Михаил Ларченко"]
]
durations = [14, 20, 12, 20]

def Namesakes():

    courses_list = []
    for course, mentor, duration in zip(courses, mentors, durations):
        course_dict = {"title": course, "mentors": mentor, "duration": duration}
        courses_list.append(course_dict)

    # С этого момента начинается выполнение задания 4.
    # На входе у вас есть только список курсов courses_list. Об исходных данных, на базе которых он был сделан, вы ничего не знаете

    # На каждом курсе в отдельности вам необходимо: 1) найти имена, которые встречаются более 1 раза;
    # 2) отобрать людей (Имя + Фамилия), для которых совпало Имя. Это и будут наши тёзки

    result = []
    for course_dict in courses_list:
        # print(type(course_dict))
        # Самостоятельно напишите код, который создаёт множество уникальных имён без фамилий
        # Подсказка: вам нужно вспомнить и повторить код из задания 1 по множествам
        # Результат (уникальные имена без фамилий) запишите в переменную под названием unique_names, преобразуйте в список и отсортируйте по возрастанию
        # Это необходимо, чтобы ваша программа всегда давала один и тот же результат и тренажёр смог его сверить

        unique_names = set()
        all_names = []
        same_name_list = []
        for names in course_dict["mentors"]:
            unique_names.add(names.split()[0])
            all_names.append(names.split()[0])

        for name in unique_names:
            if all_names.count(name) > 1:
                # print(name)
                for names in course_dict["mentors"]:
                    if name == names.split()[0]:
                        same_name_list.append(names)

        # print(same_name_list)
        course_dict["same_name_list"] = same_name_list.sort()
        # print(same_name_list)

        if len(same_name_list) > 0:
            result.append(f'На курсе {course_dict["title"]} есть тёзки: {", ".join(same_name_list)}')

    return result

if __name__ == '__main__':
    result = Namesakes()
    for item in result:
        print(item)

