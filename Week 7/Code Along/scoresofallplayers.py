
# Compute the average scores of all players 
def average(scores):
    return sum(scores) / len(scores)




players_score_dict = {'James' :[300, 250, 350, 400],
                      'Anna' :[200, 300, 450, 150],
                      'Lou' : [250, 380, 420, 120],
                      'Thor':[100, 120, 150, 180] }
# Using an nested loop
#Construct a list of all scores from all players
#
# [300, 250, 350, 400, 200, 300, 450, 150, 250, 380, 420, 120, 100, 120, 150, 180]
#
# Recall that the values() method returns a list-like (view)
# object - an ITERABLE - that can access all the values in the dictonary 

print(f'{players_score_dict.values()}')



# Create an empty list, 

scores_list_loop = []
# append valuess from aboce dictionary
# by iterating over the list returned by the values() dictionary method
# We're looking for a structure that looks like"

# [ 300, 250, 350, 400], [200, 300, 450, 150],[250, 380, 420, 120], [100, 120, 150, 180 ]

# Note the above is a LIST OF LISTS; each element is a list of scores frome one student
#
# Iterate over the dictonary's vlaues
for players_scores in players_score_dict.values():
    # Each Iteration returns a list of scores for one player
    # Iterate over this list of scores, depending each score to our list of scores 
    for a_score in players_scores:
        scores_list_loop.append(a_score)

# All done! Print the average
print(f'Average of all scores nested loop = {average(scores_list_loop)}')

#Average of all scores nested loop = 257.5

# As a nested comprehension
# The outer loop is the first comphrension; the inner loop is the second (nested)
#We'll use the same variable/score we used in the loops above that we appended as 
# the variable/score that is the 'expression' in our nested comphrension
scores_list_comp = [ a_score
                      for players_scores in players_score_dict.values()
                             for a_score in players_scores]


print(f'Average of all scores nested comphrension = {average(scores_list_loop)}')

# Note that the average of all (16) scores is equal to the average of the average of each player
# That is, sum (16 scores)/16 = su( sum(4 scores, player 1)/4 + sum(4 scores, palter 2)/4 +... sum(4 scores, last player)/4) ) / 4 (num players)
# get (average(player 1), average(player 2), average(player 3).....)

print(f'Average of all scores average of each player: {average( [average(players_scores) for players_scores in players_score_dict.values()])}')