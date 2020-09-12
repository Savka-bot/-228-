class Critter:
    total = 0

    @staticmethod
    def status():
        print("Общее число зверушек", Critter.total)
        
    def __init__(self,name, hunger = 0, boredom = 0):
        self.name = name
        self.hunger= hunger
        self.boredom = boredom
        Critter.total += 1

    ...
    def __str__(self):
        ans = 'Обьект класса Critter\n'
        ans += 'имя: ' + self.name + '\n'
        return ans 
    def __init__(self, name , hunger = 0, boredom = 0):
        self.name = name 
        self.hunger = hunger
        self.boredom = boredom 
    def talk(self):
        print("Меня зовут", self.name)

def main():
    crit1 = Critter('Бобик')
    crit1.talk()
    crit2 = Critter('Мурзик')
    crit2.talk()
    print('Доступ к атрибуту -', crit1.name)
    crit1 = Critter('Бобик')
    crit2 = Critter('Мурзик')
    print(crit2)
main()

        
    