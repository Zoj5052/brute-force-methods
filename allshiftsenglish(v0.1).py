import string
import re
import sys
import time
import pprint

class force_decrypt():
    
    def __init__(self, message):
        self.message = message.upper()
        self.final_output = []
        self.list_of_values = []
        self.list_of_combinations = []
        self.alpha = list(string.ascii_uppercase)
        self.words_file = open('words.txt', 'r')
        
        self.words = []

    def get_words(self):
        self.words = self.words_file.readlines()
        self.words = ''.join(self.words).split()
        self.words = [i.upper() for i in self.words]
        self.words_file.close()
    
    def decode(self, amount_to_shift):
        new_message = []
        for word in self.message.split(' '):
            try:
                new_message.append("".join([self.alpha[(self.alpha.index(i)+amount_to_shift)%26] for i in word]))
            except:
                indexes_of_period = [i for i in enumerate(word) if i[1] == '.']
                indexes_of_exclamation = [i for i in enumerate(word) if i[1] == '!']
                indexes_of_question = [i for i in enumerate(word) if i[1] == '?']
                indexes_of_comma = [i for i in enumerate(word) if i[1] == ',']
                
                word = word.replace('.', '')
                word = word.replace('!', '')
                word = word.replace('?', '')
                word = word.replace(',', '')
                word = word.replace("'", '')
                
                new_message.append("".join([self.alpha[(self.alpha.index(i)+amount_to_shift)%26] for i in word]))
        new_message = ' '.join(new_message)
        return new_message
        
    def assign_points(self, message_to_assign):
            num_of_points = 0
            num_of_points += len([i for i in message_to_assign if i == 'E'])*12.49
            num_of_points += len([i for i in message_to_assign if i == 'T'])*9.28
            num_of_points += len([i for i in message_to_assign if i == 'A'])*8.04
            num_of_points += len([i for i in message_to_assign if i == 'O'])*7.64
            num_of_points += len([i for i in message_to_assign if i == 'I'])*7.57
            num_of_points += len([i for i in message_to_assign if i == 'N'])*7.23
            num_of_points += len([i for i in message_to_assign if i == 'S'])*6.51
            num_of_points += len([i for i in message_to_assign if i == 'R'])*6.28
            num_of_points += len([i for i in message_to_assign if i == 'H'])*5.05
            num_of_points += len([i for i in message_to_assign if i == 'L'])*4.07
            num_of_points += len([i for i in message_to_assign if i == 'D'])*3.82
            num_of_points += len([i for i in message_to_assign if i == 'C'])*3.34
            num_of_points += len([i for i in message_to_assign if i == 'U'])*2.73
            num_of_points += len([i for i in message_to_assign if i == 'M'])*2.51
            num_of_points += len([i for i in message_to_assign if i == 'F'])*2.40
            num_of_points += len([i for i in message_to_assign if i == 'P'])*2.14
            num_of_points += len([i for i in message_to_assign if i == 'G'])*1.87
            num_of_points += len([i for i in message_to_assign if i == 'W'])*1.68
            num_of_points += len([i for i in message_to_assign if i == 'Y'])*1.66
            num_of_points += len([i for i in message_to_assign if i == 'B'])*1.48
            num_of_points += len([i for i in message_to_assign if i == 'V'])*1.05
            num_of_points += len([i for i in message_to_assign if i == 'K'])*0.54
            num_of_points += len([i for i in message_to_assign if i == 'X'])*0.23
            num_of_points += len([i for i in message_to_assign if i == 'J'])*0.16
            num_of_points += len([i for i in message_to_assign if i == 'Q'])*0.12
            num_of_points += len([i for i in message_to_assign if i == 'Z'])*0.09
            num_of_points += len(re.findall(r'(TH)|(CH)|(PH)|(OR)|(AN)|(IN)|(HE)|(IE)|(CK)|(ER)|(RD)|([A-Z]{2})', message_to_assign))*676          
            num_of_points += len(re.findall(r'(ING)|(OST)|(ACE)|(ORD)', message_to_assign))*17576
            message_split = message_to_assign.split(' ')
            for i in message_split:
                if i in self.words:
                    word_length = len(i)
                    num_of_points += (26**word_length)

                
            num_of_points *= (1/len(message_to_assign))
            return num_of_points
            # common three letter occurances

    def calculate_everything(self):
        for i in range(1,27):
            self.list_of_combinations.append(self.decode(i))
            self.list_of_values.append(self.assign_points(self.decode(i)))
        the_max = max(self.list_of_values)
        print(the_max, 'this is the max here')
        index_of_max = self.list_of_values.index(the_max)
        the_max = self.list_of_combinations[index_of_max]
        self.final_output = the_max
        return self.final_output

    def printing(self):
        print('The input that was entered is: ', self.message)
        print('The different combinations are the following: ')
        for i in enumerate(self.list_of_combinations):
            print('\t%s   %s'%(i[1],self.list_of_values[i[0]]))
        print('\nOur suspected output is the following: ', self.final_output)
            
decrypt = force_decrypt(input('Message to decrypt: '))
start_time = time.time()
decrypt.get_words()
decrypt.calculate_everything()
decrypt.printing()
#decrypt.decode(-2)
#decrypt.assign_points()

end_time = time.time()
runtime = str(round(end_time-start_time, 2))
print(runtime + 's')
