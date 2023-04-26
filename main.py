print("""
Witamy w elektronicznym dzienniku!
Dokonaj wyboru z poniższych opcji:
1 - Wyświetl zbiór wszystkich identyfikatorów studentów
2 - Wyświetl zbiór identyfikatorów studentów, którzy oddali zadanie
3 - Wświetl zbiór identyfikatorów studentów, którzy nie wykonali zadania
4 - Dodaj do zbioru identyfikator osoby, która oddała zadanie
5 - Dodaj do zbioru identyfikator osoby, która nie oddała zadania
6 - Wyjdź z programu
""")


identity_set = {"JanTestowy", "AlicjaKowalska", "BożydarDuda", "KajetanNiewiadomski", "MagdalenaŚmigło", "ElżbietaElonorowicz"}
assigment_completed_set = {"JanTestowy", "ElżbietaElonorowicz", "AlicjaKowalska"}
assigment_uncompleted_set = identity_set.difference(assigment_completed_set)

program_active = True

while program_active:


    option = int(input("Którą z opcji wybierasz (1-6)?: "))


    if option == 1:
        print("Oto zbiór wszystkich identyfikatorów studentów: ", identity_set)

    elif option == 2:
        print("Oto zbiór identyfikatorów studentów, którzy już oddali zadanie: ", assigment_completed_set)

    elif option == 3:
        print("Oto zbiór studentów, którzy nie wykonali zadania: ", assigment_uncompleted_set)

    elif option == 4:
        identity = str(input("Podaj identyfikator osoby, która wykonała zadanie, w celu dodania do zbioru: "))

        if identity not in assigment_completed_set:
            assigment_completed_set.add(identity)
            print("Identyfikator: ", identity, "został poprawnie zapisany w bazie!")

        else:
            print("Podany identyfikator istnieje już w danej bazie!")

    elif option == 5:
        identity_notdone = str(input("Podaj identyfikator osoby, która nie oddała zadania, w celu dodania do bazy: "))

        if identity_notdone in assigment_uncompleted_set:
            print("Ten identyfikator istnieje już w danej bazie!")

        elif identity_notdone not in assigment_uncompleted_set:
            assigment_uncompleted_set.add(identity_notdone)
            print("Identyfikator: ", identity_notdone, "został prawidłowo zapisany w bazie!")

        elif identity_notdone in assigment_completed_set:
            print("Ta osoba wykonała już zadanie!")

    elif option == 6:
        print("Dziękuję za skorzystanie z programu! Do zobaczenia!")
        program_active = False

    else:
        print("Wybrałxś opcję poza zakresem możliwych opcji!")




