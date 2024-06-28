import customtkinter as ck
import tkinter as tk
ck.set_appearance_mode('dark')
ck.set_default_color_theme('dark-blue')

money = 0


root = ck.CTk()
root.title('Over or Under')
root.geometry("950x500")
root.minsize(850,450)

title_frame = ck.CTkFrame(root, fg_color='transparent')
title_frame.pack(fill='both')

title = ck.CTkLabel(title_frame, text="Over or Under", font=('Roboto', 45, 'bold'))
title.pack(pady=(10,0), padx=10)

side_frame = ck.CTkFrame(root, width=200)
side_frame.pack(side='right', pady=10, padx=(0,10), fill="both")
side_frame.pack_propagate(False)

stats_money_title = ck.CTkLabel(side_frame, text=f"Balance: ${money}", font=('Roboto', 16))
stats_money_title.pack(pady=10, padx=10)
reset_money = ck.CTkButton(side_frame, text="Reset Balance ($100)", font=('Roboto', 16))
reset_money.pack(pady=10, padx=10, side='bottom')


main_frame = ck.CTkFrame(root)
main_frame.pack(side='right', pady=10, padx=10, fill="both", expand=True)
main_frame.pack_propagate(False)

odds_frame = ck.CTkFrame(main_frame)
odds_frame.pack(padx=10, pady=10, fill='both')
main_frame.pack_propagate(False)

odds1 = ck.CTkFrame(odds_frame, height=60)
odds1.pack(side='left', padx=10, pady=10, fill='both', expand=True)
odds1.pack_propagate(False)
odds1_roll = ck.CTkLabel(odds1, text="1-6", font=('Roboto', 18))
odds1_roll.pack()
odds1_mult = ck.CTkLabel(odds1, text="2x Multiplier", font=('Roboto', 18))
odds1_mult.pack()

odds2 = ck.CTkFrame(odds_frame, height=60)
odds2.pack(side='left', padx=10, pady=10, fill='both', expand=True)
odds2.pack_propagate(False)
odds2_roll = ck.CTkLabel(odds2, text="7", font=('Roboto', 18))
odds2_roll.pack()
odds2_mult = ck.CTkLabel(odds2, text="12x Multiplier", font=('Roboto', 18))
odds2_mult.pack()

odds3 = ck.CTkFrame(odds_frame, height=60)
odds3.pack(side='left', padx=10, pady=10, fill='both')
odds3.pack_propagate(False)
odds3_roll = ck.CTkLabel(odds3, text="8-13", font=('Roboto', 18))
odds3_roll.pack()
odds3_mult = ck.CTkLabel(odds3, text="2x Multiplier", font=('Roboto', 18))
odds3_mult.pack()

bet_frame = ck.CTkFrame(main_frame, height=60, fg_color='transparent')
bet_frame.pack(padx=10, pady=10)
bet_frame.pack_propagate(False)

bet_label = ck.CTkLabel(bet_frame, text="Enter your Bet:", font=('Roboto', 18))
bet_label.grid(row=0, column=0, padx=5)

bet_entry = ck.CTkEntry(bet_frame)
bet_entry.grid(row=0, column=1)

bet_type_frame = ck.CTkFrame(main_frame, height=60, fg_color='transparent')
bet_type_frame.pack(padx=10, pady=10)






# def add_money():
#     global money
#     money += 1
#     stats_money_title.configure(text=f"Balance: ${money}")
# add_money()

root.mainloop()

