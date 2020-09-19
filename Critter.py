class Critter:

    ...
    @property
    def mood(self):
        unhappiness = self.hunger + self.boredom
        if unhappiness < 5:
            m = "прекрасно"
        elif 5 <= unhappiness <= 10:
            m = "неплохо"
        elif 11 <= unhappiness <= 15:
            m = "не сказать чтобы хорошо"
        else:
            m = "ужастно"
        return m 
    
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
def __init__(self, name, hunger = 0, boredom = 0):
        self.__name = name
        self.hunger = hunger
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
    print("Создание зверушек")
    crit1 = Critter("Зверушка1")
    crit2 = Critter("Зверушка2")
    crit3 = Critter("Зверушка3")

    Critter.status()

    print("Доступ к свойству объекта:", crit1.mood)
main()

        
    