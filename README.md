# Django_Home_Works
Kichulkin Denis Homeworks_Django

В соответствии с условиями Homework-No.-19.2:
 1) Настроено виртуальное окружение.
 2) Создан новый Django-проект.
 3) Создано приложение с названием catalog.
 4) Внесены начальные настройки проекта. 
 5) Настроены URL-файлы для нового приложения.
 6) Подготовлены два шаблона для домашней страницы 
    и страницы с контактной информацией.
 7) В приложении в контроллере реализованы два контроллера:
    - Контроллер, который отвечает за отображение домашней страницы.
    - Контроллер, который отвечает за отображение контактной информации.
 8) Реализована обработка сбора обратной связи от пользователя, который 
    зашел на страницу контактов и отправил свои данные для обратной связи.

В соответствии с условиями Homework-No.-20.1:
1) Подключенва СУБД PostgreSQL для работы в проекте, для этого:
1.1) Создана база данных в ручном режиме.
1.2) Внесены изменения в настройки подключения.
2) В приложении каталога созданы модели: Product, Category. Описаны для них начальные настройки.
3) Для каждой модели описаны поля
4) Перенесены отображения моделей в базу данных с помощью инструмента миграций.
5) Для моделей категории и продукта настроено отображение в административной панели. 
Для категорий выведен id и наименование в список отображения, а для продуктов выведен
в список id, название, цену и категорию.
При этом интерфейс вывода продуктов настроен так, чтобы можно было результат отображения фильтровать по категории, 
а также осуществлять поиск по названию и полю описания.
6) Через инструмент shell заполните список категорий, а также выберите список категорий, 
применив произвольные рассмотренные фильтры. Сформированы фикстуры для заполнения базы данных.
Напишсана кастомная команда, которая умеет заполнять данные в базу данных, 
при этом предварительно ее зачищать от старых данных.
   * Скрипт для заполнения базы данных из фикстур находится в catalog\management\commands\fix_command.py.
   Сами фикстуры находятся в catalog_data\


В соответствии с условиями Homework-No.-20.2:
1)Создайн новый контроллер и шаблон, которые будут отвечают за отображение отдельной страницы с товаром, 
на которой выведена всю информация о самом товаре.
2) В созданный ранее шаблон для главной страницы выведен список товаров в цикле
3) Выделен общий (базовый) шаблон, а также подшаблон с главным меню
4) Для выводимого изображения на странице реализован шаблонный фильтр или шаблонный тег, 
который преобразует переданный путь в полный путь для доступа к медиафайлу.

В соответствии с условиями Homework-No.-21.1:

1) Переведены имеющиеся контроллеры с FBV на CBV.
2) Создана новуя модель блоговой записи (CRUD)
3) Модифицированы вывод и обработка запросов