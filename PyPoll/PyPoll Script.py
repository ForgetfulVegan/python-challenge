
import pandas as pd
import numpy as np

csvfile = pd.read_csv('election_data.csv')
df = pd.DataFrame(csvfile)

#drop unnecessary columns
df = df.drop('County', axis=1)

#group by cand
group_df = df.groupby(['Candidate']).count()

#total vote counts
total_votes = group_df['Voter ID'].sum()

def summary():

    #line break
    print('------------------------')

    #total votes print
    print(f'Total Votes: {total_votes}')

    #line break
    print('------------------------')

    group_df['%'] = (group_df['Voter ID'] / total_votes) * 100
    print(group_df.sort_values(['Voter ID'], ascending = False))

    #winner func
    def winner():
        return group_df['Voter ID'].idxmax()

    #line break
    print('------------------------')

    #print winner
    print(f'Winner: {winner()}')

    #line break
    print('------------------------')

#run function
summary()

# exportable format
group_df.sort_values(['Voter ID'], ascending = False).to_csv('PyPoll.csv',index=True)
