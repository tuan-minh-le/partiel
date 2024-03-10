# -*- coding: utf-8 -*-

"""
 * @author : maxime
 * @email : maxime.barthomeuf@cpe.fr
 * @date : 18/12/2023, lundi
 * TODO : Implémenter le support des accents "ê" pour l'Entry
"""

import random


class GameController:
    def __init__(self, app_controller):
        self.app_controller = app_controller

        self.attemps = 0
        
        self.word_list = []
        self.load_text_file()

        self.current_word = self.get_random_word()
        self.current_enter = []

        self.display_word = ""

    def load_text_file(self):
        # ouvrir le fichier txt et le transforme en liste
        with open('assets/MotsDeSixLettres.txt', encoding='utf-8') as f:
            contents = f.readlines()

            for element in contents:
                self.word_list.append(element.rstrip("\n"))
        

    def get_random_word(self):
        # récupère un mot au hasard dans la liste
        n = random.randint(0, len(self.word_list) - 1)
        return self.word_list[n]
    

    def verify_letter(self, entry_letter):
        # vérifie le mot et renvoie une chaine de caractère avec les lettres vides : "_"
        if entry_letter in self.current_enter:
            print("Lettre déjà entrée")
            return self.display_word
        else:
            self.display_word = ""
            self.current_enter.append(entry_letter)

        if entry_letter not in self.current_word:
            self.attemps += 1
            print("Lettre pas dans le mot")

        if self.attemps == 6:
            # game over
            return "Game Over"
        
        temp = ["" for i in range(len(self.current_word))]

        for i, letter in enumerate(self.current_word):
            for entered_letter in self.current_enter:
                if letter == entered_letter:
                    temp[i] = letter

        
        count = 0
        for element in temp:
            if element == '':
                self.display_word += "_ "
            else:
                self.display_word += element + " "
                count += 1

        if count == 6:
            return "Vous avez gagné"

        return self.display_word

        
        
