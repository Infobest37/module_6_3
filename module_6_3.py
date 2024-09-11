class Horse:
    def __init__(self):
        self.x_distance = 0  # Расстояние, которое пробежала лошадь
        self.sound = "Frrr"

    def run(self, dx):
        self.x_distance += dx  # Увеличиваем расстояние на dx


class Eagle:
    def __init__(self):
        self.y_distance = 0  # Высота полета
        self.sound = 'I train, eat, sleep, and repeat'

    def fly(self, dy):
        self.y_distance += dy  # Увеличиваем высоту на dy


class Pegasus(Horse, Eagle):
    def __init__(self):
        Horse.__init__(self)  # Инициализируем Horse
        Eagle.__init__(self)  # Инициализируем Eagle

    def move(self, dx, dy):
        self.run(dx)  # Вызываем метод run для изменения x_distance
        self.fly(dy)  # Вызываем метод fly для изменения y_distance

    def get_pos(self):
        return(f"{self.x_distance} {self.y_distance}")

    def voice(self):
        print(self.sound)


p1 = Pegasus()


print(p1.get_pos())
p1.move(10, 15)
print(p1.get_pos())
p1.move(-5, 20)
print(p1.get_pos())

p1.voice()