import add_event, remove_event, os
from database_py import Database
from show_reminders import Show_Reminders

def deletar():
    remove_date = remove_event.Rm_Date()
    remove_date.delete_reminder()

def adicionar():
    add_reminder = add_event.Add_Reminder()
    add_reminder.add_reminder_execute()

def show():
    show = Show_Reminders()
    show.show()

def recive_action():
    while True:
        acao = input('''
Enter "a" to add a new reminder.
Enter "d" to delete an existent reminder.
Enter "s" to show reminders.
Enter "e" to end the app.

>>> ''').lower()
        possible_actions = ('a', 'd', 's', 'e')
        if not acao in possible_actions:
            print('\nYou must enter just "a", "d" or "s" or "e"')
        else:
            return acao

def execute():
    Database.cria_json('json_calendary.json')
    while True:
        os.system('cls')
        action = recive_action()
        if action == 'a':
            adicionar()
        elif action == 'd':
            deletar()
        elif action == 's':
            show()
        elif action == 'e':
            break


execute()