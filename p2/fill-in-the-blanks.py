# -*- coding: utf-8 -*-

class Sample:
    def __init__(self,difficulty):
        if difficulty == 'easy':
            self.sample = 'All heros in LOL have four skills _1_,_2_,_3_,_4_.'
        elif difficulty == 'medium':
            self.sample = 'Ezreal have four skills each named _1_,_2_,_3_,_4_.'
        else:
            self.sample = '''The intrepid young adventurer _1_ has explored some of the most remote and abandoned locations on _2_.
                     During an expedition to the buried ruins of ancient _3_, he recovered an amulet of incredible mystical power.
                     Likely constructed to be worn by one of the Ascended,the enormous talisman nonetheless fit snugly upon his arm,
                     amplifying his raw _4_ skill to such an extent that he's gained the reputation of a hero, much to his embarrassment.
                  '''

    def get_sample(self):
        return self.sample

class Key:
    def __init__(self,difficulty):
        if difficulty == 'easy':
            self.keys = ['Q', 'W', 'E', 'R']
        elif difficulty == 'medium':
            self.keys = ['Mystic Shot', 'Essence Flux', 'Arcane Shift', 'Trueshot Barrage']
        else:
            self.keys = ['Ezreal', 'Runeterra', 'Shurima', 'sorcerous']

    def get_keys(self):
        return self.keys

def welcome():
    print 'Welcome,please select the game difficulty.'
    print 'Possible choices include easy, medium, and hard.'

def set_difficulty():
    while True:
        difficulty=raw_input()
        if difficulty=='easy' or difficulty=='medium' or difficulty=='hard' :
            break
        else:
            print "Please input easy,medium or hard!"
    return difficulty

def show_difficulty(difficulty):
    print 'You choose '+difficulty+"！"+'Good luck!'

def handle_input(keys,samples):
    count=0
    while count<len(keys):
        print samples
        print "Please input your guess for "+"_"+str(count+1)+"_"+"."
        user_input=raw_input()
        if user_input==keys[count]:
            print "Correct!"
            samples=samples.replace('_'+str(count+1)+'_',keys[count])
            count += 1
        else:
            print "Wrong!Please try again."

    print "Congratulations.You win!"

def play():
    welcome()
    difficulty=set_difficulty()
    show_difficulty(difficulty)

    key = Key(difficulty)
    keys = key.get_keys()

    sample=Sample(difficulty)
    samples=sample.get_sample()

    handle_input(keys,samples)

if __name__=='__main__':
    try:
        play()
    except Exception , e:
        print e