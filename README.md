### OB06_homework

Задание: <br>
Разработать консольную игру "Битва героев" на Python с 
использованием классов и разработать план проекта по этапам/или 
создать kanban доску для работы над данным проектом

Общее описание:<br>
Создайте простую текстовую боевую игру, где игрок и компьютер 
управляют героями с различными характеристиками. 
Игра состоит из раундов, в каждом раунде игроки по очереди наносят 
урон друг другу, пока у одного из героев не закончится здоровье.

Требования:<br>
Используйте ООП (Объектно-Ориентированное Программирование) для 
создания классов героев.

Игра должна быть реализована как консольное приложение.


Классы:<br>

Класс Hero: <br>
Атрибуты:<br>
Имя (name) <br>
Здоровье (health), начальное значение 100 <br>
Сила удара (attack_power), начальное значение 20 <br>

Методы:<br>
attack(other): атакует другого героя (other), отнимая здоровье в 
размере своей силы удара <br>
is_alive(): возвращает True, если здоровье героя больше 0, иначе False<br>

Класс Game:<br>
Атрибуты:<br>
Игрок (player), экземпляр класса Hero<br>
Компьютер (computer), экземпляр класса Hero<br>

Методы:<br>
start(): начинает игру, чередует ходы игрока и компьютера, 
пока один из героев не умрет. Выводит информацию о каждом ходе 
(кто атаковал и сколько здоровья осталось у противника) и 
объявляет победителя.