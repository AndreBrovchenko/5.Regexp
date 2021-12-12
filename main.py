from pprint import pprint
# читаем адресную книгу в формате CSV в список contacts_list
import csv
import re

contacts_list = []
fix_contacts_list = []


def read_files(name):
    global contacts_list
    # with open(name, encoding="utf-8") as f:
    with open(name) as f:
        rows = csv.reader(f, delimiter=",")
        contacts_list = list(rows)
    pprint(contacts_list)


def fix_phone_book():
    # TODO 1: выполните пункты 1-3 ДЗ
    # ваш код
    temp_contacts_list = {}
    pattern = r"(\+7|8)?\s?\(?(\d{3})\)?[-\s]?\s*(\d{3})[-\s]?(\d{2})[-\s]?(\d{2})(\s)?\(?(доб.)?\s?(\d+)?\)?"
    for contact in contacts_list:
        text = contact[5]
        res = re.sub(pattern, r"+7(\2)\3-\4-\5\6\7\8", text)
        contact[5] = res
        lastname, firstname, surname, organization, position, phone, email = contact
        temp_name = (lastname + ' ' + firstname + ' ' + surname).strip()
        temp_list = temp_name.split(' ')
        i = 0
        lastname, firstname, surname = '', '', ''
        for name in temp_list:
            if i == 0:
                lastname = name
            elif i == 1:
                firstname = name
            elif i == 2:
                surname = name
            i += 1
        contact = [lastname, firstname, surname, organization, position, phone, email]
        key = contact[0] + ' ' + contact[1]
        if temp_contacts_list.get(key, None):
            # print('такой элемент есть')
            k = 2
            for field in temp_contacts_list[key]:
                if len(field) != len(contact[k]):
                    contact[k] = field + contact[k]
                k += 1
        temp_contacts_list[key] = [contact[2], contact[3], contact[4], contact[5], contact[6]]
    global fix_contacts_list
    for key, value in temp_contacts_list.items():
        key_list = key.split()
        contact_list = key_list + value
        fix_contacts_list.append(contact_list)
    pprint(fix_contacts_list)


def write_files(name):
    # TODO 2: сохраните получившиеся данные в другой файл
    # код для записи файла в формате CSV
    with open(name, "w") as f:
        datawriter = csv.writer(f, delimiter=',')
        # Вместо contacts_list подставьте свой список
        # datawriter.writerows(contacts_list)
        datawriter.writerows(fix_contacts_list)


if __name__ == '__main__':
    read_files("phonebook.csv")
    fix_phone_book()
    write_files("phonebook_fix.csv")
