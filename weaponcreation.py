#Program to create a villianous weapon-creation randomizer
#The program will take user input (an adjective), take the first letter of user input, output another adjective that
#shares the same letter, and a random noun ending to produce a creation a villian would probably use.
#Program type: simple, but will attempt to implement complex ideals like the Flask framework to create an html verion of the code

#for future use: wanted to implement changing images towards the end, but decided to keep it a bit simple and move on to another project.
#if looking to improve, improve on that.
import random

usable_words = ['atrocious', 'almighty', 'abominable',' accursed', 'astoundishing', 'amazing', 'beastly', 'breathtaking', 'barbaric', 'belligerent',
                'corruptive', 'cursed', 'crushing', 'calamitous', 'cancerous', 'chaotic', 'cruel', 'diabolic', 'destructive', 'dynamic', 'demonic',
                'devilish', 'devastating', 'earth-shattering', 'exalted', 'efficient', 'ethereal', 'felonious', 'fiendish', 'foul', 'fatal', 'foolish',
                'fearsome', 'formidable', 'grim', 'grievous', 'grand', 'gruesome', 'heinous', 'heartless', 'hellish', 'horrible', 'harrowing', 'hypnotic',
                'immoral', 'inhuman', 'infamous', 'impressive', 'invincible', 'jaw-dropping', 'joyous', 'justice-crushing', 'jokingly', 'killer', 'knightly',
                'killjoy', 'knowing', 'lethal', 'lost', 'lavishing', 'liberating', 'legal', 'logistical', 'lovely', 'magnificant', 'malicious', 'monstrous',
                'mortifying' 'mind-blowing', 'malevolent', 'nefarious', 'notorious', 'nightmarish', 'offensive', 'obnoxious', 'overwhelming', 'omnipotence',
                'oppressive', 'putrid', 'perverse', 'powerful', 'polluted', 'poisonous', 'questionable', 'qualified', 'quickish', 'quelling', 'rotton',
                'remarkable', 'rage-inducing', 'raging', 'ravenous', 'sinful', 'scandalous', 'supreme', 'sadistic', 'savage', 'tragic', 'terrifying',
                'treacherous', 'twisted', 'unstable', 'unholy', 'unfortunate', 'unwieldily', 'ultimate', 'unnerving', 'villianous', 'vicious', 'vile',
                'vemonous', 'wicked', 'wretched', 'wonderful', 'wild', 'warlike', 'xiphoid-damaging', 'xenophobic', 'x-terminating', 'xenobiotic-spreading',
                'yearning', 'yawling', 'yamen yelling', 'yielding', 'zombifying', 'zeal-inducing', 'zoomorphing', 'zooming', 'zero-costing']
weapon = ['mechanism', 'rocket launcher', 'shiv', 'warpinator', 'predator launcher', 'plasma striker', 'blades', 'time bomb', 'R.Y.N.O.', 'tesla spikes',
          'space cruiser', 'Battleship Goliath', 'lobotomizer', 'bomb', 'ray gun', 'katana', 'knife', 'gun', 'gaunlet', 'rifle', 'device', 'apparatus',
          'orb', 'sword', 'hammer', 'scepter', 'system', 'doomsday device' , 'operating unit' , 'flagship' , 'armada', 'cannon', 'fighting robo',
          'drill', 'lance', 'defensive unit', 'carrier assault', 'assimilation initiative', 'detonation', 'fleet', 'earth-shattering missile',
          'parasite', 'bomb', 'lazer', 'lazer beam', 'space station', 'virus', 'hypnotizing beam', 'power suit', 'homing missiles', 'robot', 'clone', 'symphony'
          'blaster pistol', 'Staff of the Arcanus', 'tank', 'bat', 'atomic bomb', 'attack helicopter', 'wand', 'magnitizer', 'exo-skeleton power suits', 'power-up', 'space marine',
          'fear gas', 'manipulator', 'ghost', 'glocks', 'rifle', 'mime-a-matic ray', 'armored fortress', 'sky citadel', 'subterranean citadel']

#this should reveal the first letter of the user input
#need to check if first letter isnt a letter
def creation_generation(word): #This was made for python originally in mind. attempting to convert to flask framework/html format
    try:
        name = word.lower()
        while True:         #important
            if name[0].isalpha() == True:
                good_input = name
                good_letter = name[0]
                break
            elif " " in name[0]:
                return("Incorrect usage of the program, you imbecile!!!\nYou must have placed a space in front of the program!\nI`ll forgive you this time, moron.\nSo do it correctly!")
                break
            else:
                return("Incorrect usage of the program, you imbecile!!!\nWhat!?!\nYou placed a number/special character in an adjective-only program!?!?\nI`ve thought i told you a thousand times what an adjective is!!!\nNow do it correctly!")   #For loop to detect usable words
                break
        my_list = []
        for item in usable_words:   #though this means i can just make 1 big list instead of 26 smaller ones
                if item[0] in good_letter:
                    selecting = set([item])     #sets the selected words from the list and turns it into a list
                    my_list.append(item)
        #the user input and first choice might still be the same. only thing to fix really
        z = random.choice(my_list) #the randonmess begins and works
        #while loop to make sure the user input and the randomly,selected adjective aren`t the same
        while True:
            if name == z:
                z = random.choice(my_list)
                continue
            else:
                break
        random_number = [1,2,3,4,5,6,7,8,9,10]
        random_output = []
        sentence = random.choice(random_number)
        random_output.append(sentence)
        fixing = random.choice(weapon) #important
        for x in list(random_output):
            if x == 1:
                return("Introducing the most %s weapon in our arsenal. One that strikes fear to those would would stand in its presence. I present to you our %s %s!" %(name,z,fixing))
            elif x == 2:
                return("While I could show off our most %s device in our catalog, my %s %s would simply atomimize you on the spot. and where`s the fun in that?" %(name,z,fixing))
            elif x == 3:
                return("Behold before you, the illustrious, the %s, the %s power that is my %s!" %(name,z,fixing))
            elif x == 4:
                return("We`ve broken around 54 federal rules to create such an %s device, but watching the %s carnage this %s creates will be well worth it." %(name,z,fixing))
            elif x == 5:
                return("You think this is some sort of game??? How dare you mock me while I`m calibrating my %s, %s %s!" %(name,z,fixing))
            elif x == 6:
                return("It took the souls of thousands to construct what might be the most %s and %s %s to have possibly ever been created by man!" %(name,z,fixing))
            elif x == 7:
                return("NO MORE GAMES! If my %s, %s %s can`t destroy you, then we`ll see if the city is as durable!" %(name,z,fixing))
            elif x == 8:
                return("When they told me I could never build the most %s contraption with a hint of %s, they were right. So I just made some %s." %(name,z,fixing))
            elif x == 9:
                return("The time has come to wipe this %s humanity from the face of this earth! Let our mighty army and the %s power of my own %s be the intrument of their demise!" %(name,z,fixing))
            else:
                return("LET MY NEW DOMINION RISE! The age of my %s might has begun! Equip those who serve with our %s %s as we take the fortress and bring death upon its doorsteps!" %(name,z,fixing))
    except IndexError:  #In case i get the greatest gift of all: NOTHING!!!!!!
        return("ENTER SOMETHING YOU MORON!")

            
                
