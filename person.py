from random import random

class Person:
        def __init__(self, firstname, lastname, health, status):
            """initialize attributes to be used in/available for all class methods in this class, and for class
            objects created by this class"""

            self.firstname = firstname
            self.lastname = lastname
            self.health = health
            self.status = status

        def introduce(self):
                #All people introduce themselves
                print("Helo, my name is {} {}".format(self.firstname, self.lastname))

        def emote(self):
                emotion = random.randrange(1,3)

                if emotion ==1 :
                    print("{} is happy".format(self.firstname))
                elif emotion == 2 :
                    print("{} is sad".format(self.firstname))

        def status_change(self):

                if self.health == 100:
                    print("{} healthy".format(self.firstname))
                elif self.health >= 76:
                    print("{} little tired".format(self.firstname))
                elif self.health >= 51:
                    print("{} unwell".format(self.firstname))
                else :
                    print("{} unconscious".format(self.firstname))

Maria = Person("Maria", "Reeves", 90, status=True)
Rey = Person("Rey", "Reeves", 50, status=False)
Lee = Person("Lee", "Reeves", 20, status=True)

print("{} is my friend ? {}".format(Maria.firstname, Maria.status))
print("{} is my friend ? {}".format(Rey.firstname, Rey.status))

Maria.introduce()

Maria.status_change()

#inherit person class attributes to enemy class
class Enemy(Person) :

    def __init__(self, weapon, firstname, lastname, health, status):
        super().__init__(firstname, lastname, health, status) #same attributes in super class
        self.weapon = weapon

    def introduce(self):
        #All people introduce themselves
        print("Helo, my name is {} {}".format(self.firstname, self.lastname))

    def hurt(self, other):
        if self.weapon== 'rock':
            other.health-=10
        elif self.weapon== 'stick':
            other.weapon -=5
        print(other.health)

    def insult(self, other):
        if other.health <=80:
            print("{}, you are tired and weak".format(other.firstname))

    def steal(self, other):
        print("ha ha ha, {}, I have your stuff!", format(other.firstname))
        if other.status == True:
            other.status == False


Alex = Enemy('rock', 'Alex', 'Wayne', 65, status='Fales')

Alex.hurt(Maria)
Alex.insult(Rey)
Alex.steal(Lee)

#we cannot use sub class methods in superclass
Rey.steal(Alex)

