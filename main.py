import csv
import re


def read_file(file):
    with open(file, 'r', encoding='utf-8') as f:
        rows = csv.reader(f, delimiter=",")
        contacts_list = list(rows)
    return contacts_list


def format_name(contacts_list):
    pattern_raw = r"^([А-ЯЁа-яё]+)(\s*)(\,?)([А-ЯЁа-яё]+)(\s*)(\,?)([А-ЯЁа-яё]*)(\,?)(\,?)(\,?)"
    pattern_new = r"\1\3\10\4\6\9\7\8"
    updated_contacts_list = []
    for entry in contacts_list:
        entry_string = ','.join(entry)
        edited_entry = re.sub(pattern_raw, pattern_new, entry_string)
        entry_list = edited_entry.split(",")
        updated_contacts_list.append(entry_list)
    return updated_contacts_list


def format_phone_number(contacts_list):
    pattern_raw = r"(\+7|8)(\s*)(\(*)(\d{3})(\)*)(\s*)(\-*)(\d{3})(\s*)(\-*)(\d{2})(\s*)(\-*)(\d{2})(\s*)(\(*)" \
                  r"(доб)*(\.*)(\s*)(\d+)*(\)*)"
    pattern_new = r"+7(\4)\8-\11-\14\15\17\18\20"
    updated_contacts_list = []
    for entry in contacts_list:
        entry_string = ','.join(entry)
        edited_entry = re.sub(pattern_raw, pattern_new, entry_string)
        entry_list = edited_entry.split(",")
        updated_contacts_list.append(entry_list)
    return updated_contacts_list


def duplicate_entries(contacts_list):
    for ent in contacts_list:
        if len(ent) > 7:
            del ent[-1]
    for i in contacts_list:
        for j in contacts_list:
            if i[0] == j[0] and i[1] == j[1] and i is not j:
                if i[2] == "":
                    i[2] = j[2]
                if i[3] == "":
                    i[3] = j[3]
                if i[4] == "":
                    i[4] = j[4]
                if i[5] == "":
                    i[5] = j[5]
                if i[6] == "":
                    i[6] = j[6]
    updated_contacts_list = []
    for entry in contacts_list:
        if entry not in updated_contacts_list:
            updated_contacts_list.append(entry)
    return updated_contacts_list


def write_file(contacts_list):
    with open("phonebook.csv", "w", encoding='utf-8') as f:
        datawriter = csv.writer(f, delimiter=',')
        datawriter.writerows(contacts_list)


if __name__ == '__main__':
    phonebook = read_file('phonebook_raw.csv')
    phonebook = format_name(phonebook)
    phonebook = format_phone_number(phonebook)
    phonebook = duplicate_entries(phonebook)
    write_file(phonebook)
