# Это программный код на языке Python, который реализует функции 
# добавления контакта в базу данных, 
# поиска контакта и редактирования контакта. 
# Функции используются в главном меню программы, где пользователь может выбрать нужное действие.-

import sqlite3
import easygui

# Подключение к базе данных
def connect_db():
    conn = sqlite3.connect('contacts.db')
    c = conn.cursor()
    # Cоздание базы данных в случае её отсутствия
    c.execute('''
        CREATE TABLE IF NOT EXISTS contacts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name VARCHAR(16) NOT NULL,
            last_name VARCHAR(16),
            phone VARCHAR(14) NOT NULL,
            comment TEXT)
        ''')
    conn.commit()
    return conn, c

# Модуль добавление контакта к базе данных
def contact_add(conn, c):
    c.execute('SELECT MAX(id) FROM contacts')
    max_id = c.fetchone()[0]
    if max_id is None:
        new_id = 1
    else:
        new_id = max_id + 1
    # Поверка поля "Имя"
    while True:
        name = easygui.enterbox('Введите имя (не более 16 символов):')
        if len(name) <= 16:
            break
        else:
            easygui.msgbox('Поле заполнено не верно')
    # "Фамилия" без проверки, но с предупреждением пользователя
    last_name = easygui.enterbox('Введите фамилию (не более 16 символов):')
    # Поверка поля "телефон" на ввод только числовых значений
    while True:
        phone = easygui.enterbox('Введите телефон (не более 14 цифр):')
        if len(phone) <= 14 and phone.isdigit():
            break
        else:
            easygui.msgbox('Поле заполнено не верно')
    # Ввод комментария
    comment = easygui.enterbox('Введите комментарий (не более 265 символов):')
    
    c.execute('SELECT id FROM contacts WHERE phone=?', (phone,))
    existing_contact = c.fetchone()
    # Проверка контакто в БД на дубли
    if existing_contact:
        result = easygui.buttonbox('Контакт с таким номером существует. Добавить повторно контакт?', choices=['Да', 'Нет'])
        if result == 'Да':
            name += ' (Второй)'
        else:
            return

    c.execute('INSERT INTO contacts VALUES (?, ?, ?, ?, ?)', (new_id, name, last_name, phone, comment))
    conn.commit()

    easygui.msgbox(f'Контакт "{name} {last_name} {phone}" успешно записан.')

# Модуль поиска контакта в базе данных
def contact_search(c):
    search_term = easygui.enterbox('Кого ищем?')
    c.execute('SELECT * FROM contacts WHERE first_name LIKE ? OR last_name LIKE ? OR phone LIKE ?', (f'%{search_term}%', f'%{search_term}%', f'%{search_term}%'))
    results = c.fetchall()
    # В случае, если контактов несколько - выводится список всех контактов.
    if len(results) == 0:
        easygui.msgbox('Контакты не найдены')
    elif len(results) == 1:
        contact = results[0]
        contact_menu(contact)
    else:
        choices = []
        for contact in results:
            choices.append(f'{contact[0]} - {contact[1]} {contact[2]} {contact[3]}')
        choice = easygui.buttonbox('Найдены несколько контактов, выберите контакт:', choices=choices)
        index = choices.index(choice)
        contact = results[index]
        contact_menu(contact)

# Модуль изменения контакта в базе данных
def contact_edit(contact, c):
    while True:
        field = easygui.buttonbox('Какое поле редактируем?', choices=['Имя', 'Фамилия', 'Телефон', 'Комментарий'])
        # Перезапись имени, с проверкой
        if field == 'Имя':
            while True:
                name = easygui.enterbox('Введите новое имя (не более 16 символов):')
                if len(name) <= 16:
                    break
                else:
                    easygui.msgbox('Поле заполнено не верно')
            c.execute('UPDATE contacts SET first_name=? WHERE id=?', (name, contact[0]))
        # Перезапись Фамилии
        elif field == 'Фамилия':
            last_name = easygui.enterbox('Введите новую фамилию (не более 16 символов):')
            c.execute('UPDATE contacts SET last_name=? WHERE id=?', (last_name, contact[0]))
        # Перезапись телефона, с проверкой
        elif field == 'Телефон':
            while True:
                phone = easygui.enterbox('Введите новый телефон (не более 14 цифр):')
                if len(phone) <= 14 and phone.isdigit():
                    break
                else:
                    easygui.msgbox('Поле заполнено не верно')
                    c.execute('UPDATE contacts SET phone=? WHERE id=?', (phone, contact[0]))
                    conn.commit()

# Модуль удаления контакта в базе данных
def contact_delete(contact, c, conn):
    result = easygui.buttonbox(f'Удалить контакт "{contact[1]} {contact[2]} {contact[3]}"?', choices=['Да', 'Нет'])
    if result == 'Да':
        c.execute('DELETE FROM contacts WHERE id=?', (contact[0],))
        conn.commit()
        easygui.msgbox('Контакт успешно удален.')
 
# Модуль основного меню       
def contact_menu(contact):
    choices = ['Просмотреть', 'Редактировать', 'Удалить']
    choice = easygui.buttonbox(f'Выбран контакт "{contact[1]} {contact[2]} {contact[3]}", выберите действие:', choices=choices)
    if choice == 'Просмотреть':
        easygui.msgbox(f'Имя: {contact[1]}\nФамилия: {contact[2]}\nТелефон: {contact[3]}\nКомментарий: {contact[4]}')
    elif choice == 'Редактировать':
        contact_edit(contact, connect_db())
    elif choice == 'Удалить':
        contact_delete(contact, 'DELETE FROM contacts WHERE id=?', (contact[0],))

# Запуск программы основного меню
def main():
    conn, c = connect_db()
    while True:
        action = easygui.buttonbox('Выберите действие:',
        choices=['Добавить контакт', 'Поиск контакта', 'Редактировать контакт', 'Выход'])
        if action == 'Добавить контакт':
            contact_add(conn, c)
        elif action == 'Поиск контакта':
            contact_search(c)
        elif action == 'Редактировать контакт':
            contact_id = easygui.enterbox('Введите ID контакта для редактирования:')
            c.execute('SELECT * FROM contacts WHERE id=?', (contact_id,))
            contact = c.fetchone()
            if contact:
                contact_edit(conn, c)
            else:
                easygui.msgbox('Контакт с таким ID не найден.')
        elif action == 'Удалить':
            contact_delete(contact, c, conn)
        elif action == 'Выход':
            break
    conn.close()

# Cобственно - Main
main()