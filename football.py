smallest_difference_in_for_and_against_goals = 10000
line_number = 0
for i in open('football.dat').readlines():
    line = i.strip().split()
    length_of_row = len(line)
    if (line_number > 0) and (length_of_row > 1):
        goals_scored_for = int(line[length_of_row-4])
        goals_scored_against = int(line[length_of_row-2])

        difference_in_for_and_against_goals = abs(goals_scored_for - goals_scored_against)
        if difference_in_for_and_against_goals < smallest_difference_in_for_and_against_goals:
            smallest_difference_in_for_and_against_goals = difference_in_for_and_against_goals
            line_number_for_smallest_difference_in_for_and_against_goals = line_number
            name_of_the_team = line[length_of_row-9]

    line_number += 1

print('The name of the team with the smallest difference in ‘for’ and ‘against’ goals is: ', name_of_the_team)
