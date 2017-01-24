# -*- coding: utf-8 -*-

class Sample:
    '''
    The class Sample store the sample data.
    '''
    def __init__(self,difficulty):
        '''
        Init the class.
        :param difficulty:
        '''
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
        '''
        return: sample data
        '''
        return self.sample

class Key:
    '''
    The class Key store the key data.
    '''
    def __init__(self,difficulty):
        '''
        Init the class.
        :param difficulty:
        '''
        if difficulty == 'easy':
            self.keys = ['Q', 'W', 'E', 'R']
        elif difficulty == 'medium':
            self.keys = ['Mystic Shot', 'Essence Flux', 'Arcane Shift', 'Trueshot Barrage']
        else:
            self.keys = ['Ezreal', 'Runeterra', 'Shurima', 'sorcerous']

    def get_keys(self):
        '''
        :return: key data
        '''
        return self.keys

def welcome():
    '''
    print welcome words.
    '''
    print 'Welcome,please select the game difficulty.'
    print 'Possible choices include easy, medium, and hard.'

def set_difficulty():
    '''
    Set difficulty of the game.
    '''
    while True:
        difficulty=raw_input()
        if difficulty in ['easy','medium' ,'hard'] :
            break
        else:
            print "Please input easy,medium or hard!"
    return difficulty

def show_difficulty(difficulty):
    '''
    Show the difficulty user choose.
    :param difficulty:
    '''
    print 'You choose '+difficulty+"！"+'Good luck!'

def handle_input(keys,samples):
    '''
    Handle user's input.
    :param keys:
    :param samples:
    :return:
    '''
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
    print samples
    print "Congratulations.You win!"

def main_func():
    '''
    The main function is building a fill-in-the-blanks quiz.
    Argument:None
    return:None
    '''

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
        main_func()
    except Exception , e:
        print e
