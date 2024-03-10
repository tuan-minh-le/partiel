# -*- coding: utf-8 -*-

"""
 * @author : maxime
 * @email : maxime.barthomeuf@cpe.fr
 * @date : 18/12/2023, lundi
 * TODO :
"""

import tkinter as tk


class GameView(tk.Frame):
    def __init__(self, master, app_controller, game_controller):
        super().__init__(master)

        self.app_controller = app_controller
        self.game_controller = game_controller

        self.game_frame = tk.Frame(self, height=575, width=800)
        self.game_frame.pack(expand=True)

        self.nav_bar = tk.Frame(self)
        self.nav_bar.pack()

        self.quit_button = tk.Button(self.nav_bar, text ="Quitter", command=self.quit_game)
        self.quit_button.pack(side='left')

        self.word_view = tk.Label(self.game_frame, font=("Arial", 25))
        self.word_view.pack()

        self.entry = tk.Entry(self.game_frame)
        self.entry.pack()

        self.validate_button = tk.Button(self.game_frame, text ="Valider", command=self.on_validate_press)
        self.validate_button.pack()

        self.info_label = tk.Label(self.game_frame)
        self.info_label.pack()


        self.init_game()
        


    def on_validate_press(self):
        entry_text = self.entry.get()
        self.word_view.config(text=self.game_controller.verify_letter(entry_text))
        self.entry.delete(0, 'end')
        



    def init_game(self):
        first_letter = self.game_controller.current_word[0]
        self.word_view.config(text=self.game_controller.verify_letter(first_letter))


    
    def quit_game(self):
        # permet de quitter le jeu proprement
        self.app_controller.quit()