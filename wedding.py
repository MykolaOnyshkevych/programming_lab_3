def wedding_graph(list_len, couple_list):

    sorted_couple_list = sorted(couple_list)
    tribes_list = []
    for people in sorted_couple_list:

        for tribe in tribes_list:

            if people[0] in tribe:
                tribe.add(people[1])
                break

            elif people[1] in tribe:
                tribe.add(people[0])
                break

        else:
            tribes_list.append(set((people[0], people[1])))

    men_in_each_tribe = [len({man for man in tribe if man % 2}) for tribe in tribes_list]
    women_in_each_tribe = [len({women for women in tribe if not women % 2}) for tribe in tribes_list]

    return sum(men_in_each_tribe) * sum(women_in_each_tribe) - sum((male * female for male, female in zip(men_in_each_tribe, women_in_each_tribe)))


