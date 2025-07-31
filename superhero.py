
import random
class superhero():
    instances=[]
    def __init__(self,name,strength,dexterity,wisdom,charisma,catchphrase):
        self.name = name
        self.strength = strength
        self.dexterity = dexterity
        self.wisdom = wisdom
        self.charisma = charisma
        self.catchphrase = catchphrase
        self.average = (strength + dexterity + wisdom + charisma) / 4
        self.willcut = self.average > 80
        superhero.instances.append(self)

    def WillCut(self):
        num = random.randint(1, 3)
        if self.willcut:
            if num == 1:
               print(self.name + " is a certified superhero!")
            if num == 2:
                print("Of course "+self.name + " is a superhero!")
            if num == 3:
                print("Naturally, "+self.name+" qualifies as a superhero.")
        else:

            if num == 1:
               print("Who is "+self.name+"?" )
            if num == 2:
                print("I don't think "+self.name+" is a superhero!")
            if num == 3:
                print("I have never heard of "+self.name+".")

    def id(self):
        print(f"""
                            Name: {self.name}
                            Strength: {self.strength}
                            Dexterity: {self.dexterity}
                            Wisdom: {self.wisdom}
                            Charisma: {self.charisma}
                            Catchphrase: {self.catchphrase}
                           """)
    def power(self):
        print(f"{self.name} has a power of {self.average}.")

    def powerup(self,i=1):
        self.strength=self.strength+i
        self.dexterity=self.dexterity+i
        self.wisdom=self.wisdom+i
        self.charisma=self.charisma+i
        self.average = self.average + i
    def weaken(self,i=1):
        self.strength=self.strength-i
        self.dexterity=self.dexterity-i
        self.wisdom=self.wisdom-i
        self.charisma=self.charisma-i
        self.average = self.average - i

    def draw_attribute(self):
        attributes = {
            'strength': self.strength,
            'dexterity': self.dexterity,
            'wisdom': self.wisdom,
            'charisma': self.charisma
        }
        key = random.choice(list(attributes.keys()))
        return key, attributes[key]

Batman = superhero(
    'Batman', 93, 91, 91, 96,
    "The night is darkest just before the dawn."
)

Superman = superhero(
    'Superman', 99, 94, 89, 97,
    "Truth, justice, and a better tomorrow."
)

Flash = superhero(
    'Flash', 86, 99, 87, 98,
    "My name is Barry Allen, and I am the fastest man alive."
)

GreenLantern = superhero(
    'GreenLantern', 95, 90, 92, 97,
    "In brightest day, in blackest night, No evil shall escape my sight. Let those who worship evil's might, Beware my power—Green Lantern's light!"
)

WonderWoman = superhero(
    'WonderWoman', 97, 88, 90, 95,
    "I will fight for those who cannot fight for themselves."
)

Aquaman = superhero(
    'Aquaman', 89, 85, 84, 88,
    "The ocean is not yours to control — it answers only to me."
)

Cyborg = superhero(
    'Cyborg', 88, 87, 83, 89,
    "Booyah! Half man, half machine — all hero."
)

MartianManhunter = superhero(
    'MartianManhunter', 92, 90, 91, 94,
    "I am the last son of Mars... and Earth’s silent guardian."
)

Falconman = superhero(
    "Falconman", 41, 50, 31, 66,
    "Justice from above — swift, sharp, and unseen. I am Falconman!"
)

Glowbeam = superhero(
    "Glowbeam", 45, 43, 48, 55,
    "A spark in the shadows is all it takes to find hope."
)

Airstep = superhero(
    "Airstep", 38, 52, 40, 60,
    "Light as wind, quick as thought — I’m always one step ahead."
)

Mindweaver = superhero(
    "Mindweaver", 33, 30, 65, 45,
    "Strength is fleeting — insight lasts forever."
)

MossMaiden = superhero(
    "MossMaiden", 39, 42, 46, 50,
    "Where silence grows, so does resolve."
)


def Name():
    for hero in superhero.instances:
        print(hero.name)

def fight(hero1, hero2):
    print(f"\n{hero1.name} vs {hero2.name}!")

    attr1, val1 = hero1.draw_attribute()
    attr2, val2 = hero2.draw_attribute()

    print(f"{hero1.name} draws {attr1.upper()} = {val1}")
    print(f"{hero2.name} draws {attr2.upper()} = {val2}")

    if val1 > val2:
        print(f"\n🏆 {hero1.name} wins the battle!\n")
    elif val2 > val1:
        print(f"\n🏆 {hero2.name} wins the battle!\n")
    else:
        print("\n⚔️ It's a tie!\n")

def destroy_hero(name):
    for hero in superhero.instances:
        if hero.name.lower() == name.lower():
            superhero.instances.remove(hero)
            print(f"❌ {hero.name} has been destroyed.")
            return
    print("Hero not found.")

while True:
    print("Press'i' if you are here for first time")
    action = input(": ").strip()

    if action.lower() == 'i':
        print("""
               NAVIGATOR   
            - Type 'name' to view all heroes' names.

            - Type '<hero_name>' to view that hero's full profile.

            - Type '<hero_name> s/d/w/c/p' to view:
                  s → strength
                  d → dexterity
                  w → wisdom
                  c → charisma
                  p → power (average of rest of stats)

            - Type 'rank' to view superhero rankings by power.
            
            - Type 'mystery' to add a mystery hero.
      
            - Type 'create' to create a new superhero.
           
            - Type 'fight' to fight a superhero. 
            
            - Type 'willcut <hero>' to see if a hero qualifies as a certified superhero.

            - Type 'powerup <hero> <amount>' to increase all attributes (default: 1).

            - Type 'weaken <hero> <amount>' to decrease all attributes (default: 1).

            
            - Type 'destroy' to remove a superhero from existence.

            
            - Type 'q' to quit.
               
          """)

    elif action.lower() == "name":
        Name()

    elif action.lower() == "q":
        break

    elif action.lower() == "create":
        print("\n--- Create a New Superhero ---")
        name = input("Name: ").replace(" ", "")
        if name.lower() == "exit":
            break
        try:
            strength = int(input("Strength: "))
            dexterity = int(input("Dexterity: "))
            wisdom = int(input("Wisdom: "))
            charisma = int(input("Charisma: "))
        except ValueError:
            print("Please enter valid numbers for attributes.")
            continue
        catchphrase = input("Catchphrase: ")

        new_hero = superhero(name, strength, dexterity, wisdom, charisma, catchphrase)
        print(f"{new_hero.name} has been created!\n")
        new_hero.id()
    elif action.lower() == "mystery":
        import random
        import string

        def generate_random_name(max_len=10):
            name = ''.join(random.choices(string.ascii_uppercase, k=1)) + \
                   ''.join(random.choices(string.ascii_lowercase, k=random.randint(2, max_len - 1)))
            return name

        catchphrases = [
            "Justice doesn't need an invitation.",
            "From the shadows, I strike.",
            "Power lies within purpose.",
            "Silence is louder than fear.",
            "Hope is my secret weapon.",
            "Unknown but unstoppable.",
            "Born to rise, built to last.",
            "Destiny forged in mystery.",
            "My story is just beginning.",
            "The mask is only the start."
        ]

        name = generate_random_name()
        strength = random.randint(0, 100)
        dexterity = random.randint(0, 100)
        wisdom = random.randint(0, 100)
        charisma = random.randint(0, 100)
        catchphrase = random.choice(catchphrases)

        mystery_hero = superhero(name, strength, dexterity, wisdom, charisma, catchphrase)
        print(f"\n🎭 A new mystery hero has emerged: {name}!\n")
        mystery_hero.id()



    elif action.lower() == "rank":
        print("\n🏆 Superhero Power Rankings:")
        ranked = sorted(superhero.instances, key=lambda h: h.average, reverse=True)
        for i, hero in enumerate(ranked, 1):
            print(f"{i}. {hero.name} - Power: {hero.average:.2f}")

    elif action.lower() == "fight":
        Name()
        h1_name = input("Enter first hero's name: ").lower()
        h2_name = input("Enter second hero's name: ").lower()
        hero1 = next((h for h in superhero.instances if h.name.lower() == h1_name), None)
        hero2 = next((h for h in superhero.instances if h.name.lower() == h2_name), None)
        if hero1 and hero2:
            fight(hero1, hero2)
        else:
            print("One or both hero names were not found.")

    elif action.lower() == "destroy":
        Name()
        name = input("Enter the name of the hero to destroy: ")
        destroy_hero(name)

    if action.lower().startswith("willcut "):
        name = action[8:].strip()
        for hero in superhero.instances:
            if hero.name.lower() == name.lower():
                hero.WillCut()
                break
        else:
            print("Hero not found.")

    elif action.lower().startswith("powerup "):
        parts = action.split()
        if len(parts) >= 2:
            name = parts[1]
            amt = int(parts[2]) if len(parts) > 2 else 1
            for hero in superhero.instances:
                if hero.name.lower() == name.lower():
                    hero.powerup(amt)
                    print(f"{hero.name} has been powered up by {amt} points!")
                    break
            else:
                print("Hero not found.")
        else:
            print("Usage: powerup <hero name> [amount]")

    elif action.lower().startswith("weaken "):
        parts = action.split()
        if len(parts) >= 2:
            name = parts[1]
            amt = int(parts[2]) if len(parts) > 2 else 1
            for hero in superhero.instances:
                if hero.name.lower() == name.lower():
                    hero.weaken(amt)
                    print(f"{hero.name} has been weakened by {amt} points!")
                    break
            else:
                print("Hero not found.")
        else:
            print("Usage: weaken <hero name> [amount]")


    else:
        parts = action.split()
        if len(parts) == 2:
            name_input, cmd = parts[0].lower(), parts[1].lower()
            found = False
            for hero in superhero.instances:
                if hero.name.lower() == name_input:
                    found = True
                    if cmd == 's':
                        print(f"{hero.name}'s strength is {hero.strength}")
                    elif cmd == 'd':
                        print(f"{hero.name}'s dexterity is {hero.dexterity}")
                    elif cmd == 'w':
                        print(f"{hero.name}'s wisdom is {hero.wisdom}")
                    elif cmd == 'c':
                        print(f"{hero.name}'s charisma is {hero.charisma}")
                    elif cmd == 'p':
                        print(f"{hero.name}'s average power is {hero.average:.2f}")
                    else:
                        print("Invalid command. Use s, d, w, c, or p.")
                    break
            if not found:
                print("Hero not found.")

        elif len(parts) == 1:
            name_input = parts[0].lower()
            found = False
            for hero in superhero.instances:
                if hero.name.lower() == name_input:
                    hero.id()
                    found = True
                    break
            if not found:
                print("Hero not found.")

        else:
            print("Invalid input. Type 'i' for instructions.")
