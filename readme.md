Тестовый пример

Предполагаем, что валидация правильных ответов ( в случае выбора) делается во фронтенде.

API опросов

Пути:

/polls - вывод ВСЕХ (в том числе просроченных опросов)

/active-polls - вывод активных опросов

/person/<int:pk> - вывод прошедших опросов по юзеру

/poll/<int:pk> - по номеру опроса выводит его инфу для формирования фронтэнда ответа на опрос

/answer/<int:poll>/<int:id> - по id юзера (если не было такого id, создается новый юзер) создается ответ на опрос
предполагается, что фронтенд объединил ответы с множественным вариантом выбора в одну строку

Развертывание в контейнерах докер. Рабочий порт - 84. Сделать git clone, если надо, установить права на исполнение файла pools_init.sh
далее в каталоге pools запустить docker-compose up, и все должно заработать.

Если не хочется в контейнерах, то можно с использованием venv. 

Вход в админку sdmin, пароль 1234

