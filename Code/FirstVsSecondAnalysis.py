#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 19 20:20:04 2019

@author: adong
"""

import pandas as pd
import numpy as np
import math

class _BBoyOrderTracker:
    def __init__(self,name):
        self.name = name
        self.battles_going_first = 0
        self.battles_going_second = 0
        self.wins_going_first = 0
        self.wins_going_second = 0
        
    def add_entry(self,went_first,won_battle):
        if type(went_first) is not bool:
            raise RuntimeError('went_first must be bool')
        if type(won_battle) is not bool:
            raise RuntimeError('won_battle must be bool')
        
        if went_first is True:
            self.battles_going_first = self.battles_going_first + 1
            if won_battle is True:
                self.wins_going_first = self.wins_going_first + 1
        else:
            self.battles_going_second = self.battles_going_second + 1
            if won_battle is True:
                self.wins_going_second = self.wins_going_second + 1
    
class _JudgeOrderTracker:
     def __init__(self,name):
        self.name = name
        self.voted_first = 0
        self.voted_second = 0
        self.voted_tie = 0
     def add_entry(self,vote_enum):
        if vote_enum == -1:
            self.voted_first = self.voted_first + 1
        elif vote_enum == 1:
            self.voted_second = self.voted_second + 1
        elif vote_enum == 0:
            self.voted_tie = self.voted_tie + 1
        else:
            raise RuntimeError('vote_enum must be -1, 0, or 1')
        
            
        
# Initializations
sbo2018_judges = ['Poe One','Goku','Narumi', 'Skim', 'Storm', 'Jeskilz', 'Renegade', 'Crazy Legs', 'Lil Cesar']
green_panda2018_judges= ['Ken Swift', 'Poe One' ,'Reveal' ,'Kid David', 'Kowloon']
ibe2018_judges = ['El Nino','Taisuke','Renegade','Moy','Reveal']
outbreak2018_judges = ['Poe One','Hatsolo','Renegade','Max','Wing','Felix']
unbreakable2018_judges = ['Renegade','Extremo','Kleju','Niek','Admiracles']
data_file_judge_list = [green_panda2018_judges,
                        ibe2018_judges,
                        outbreak2018_judges,
                        sbo2018_judges,
                        unbreakable2018_judges]

all_judge_list =  green_panda2018_judges + \
                  ibe2018_judges + \
                  outbreak2018_judges + \
                  sbo2018_judges + \
                  unbreakable2018_judges


data_file_path_list = ['../Data/GP2018Table_Votes.csv',
                       '../Data/IBE2018Table_Votes.csv',
                       '../Data/Outbreak2018Table_Votes.csv',
                       '../Data/SBO2018Table_Votes.csv',
                       '../Data/Unbreakable2018Table_Votes.csv',]

# Main
judge_result_dict = {} # end dictionary to be analyzed
bboy_result_dict = {} # end dictionary to be analyzed
                    

for judge in all_judge_list:
    if judge not in judge_result_dict:
       judge_result_dict[judge] = _JudgeOrderTracker(judge)

path_and_judge = zip(data_file_path_list,data_file_judge_list)

for file_path,jam_judge_list in path_and_judge:
    data_frame = pd.read_csv(file_path,index_col=None,header=0)
    
    # Winrate by round
    num_rounds = data_frame['Round Winner Order'].size
    first_wins = data_frame['Round Winner Order'] == 'First'
    second_wins = data_frame['Round Winner Order'] == 'Second'
    ties = data_frame['Round Winner Order'] == 'Tie'
    
    first_percentage_round = first_wins.tolist().count(True)/num_rounds
    second_percentage_round = second_wins.tolist().count(True)/num_rounds
    tie_percentage_round = ties.tolist().count(True)/num_rounds
    # Winrate by battle
    first_wins_count = 0
    second_wins_count = 0
    battle_seen_set = set()
    num_battles = len(np.unique(data_frame['Battle Number']))
    for index, row in data_frame.iterrows():
        if row.isnull().all():
            continue
        if row['Battle Number'] in battle_seen_set:
            continue
        else:
            battle_seen_set.add(row['Battle Number'])
            if row['Battle Winner'] == row['First']:
                first_wins_count = first_wins_count+ 1
            elif row['Battle Winner'] == row['Second']:
                second_wins_count = second_wins_count + 1
            else: 
                raise RuntimeError("Error, seems like there was an entry in Battle Winner that was not 'First' bboy/bgirl or 'Second' bboy/bgirl")
                        
    print('First person wins battle: ' + str(first_wins_count/num_battles))
    print('Second person wins battle: ' + str(second_wins_count/num_battles))

    # Judge Stats
    battle_seen_set = set()
    for index, row in data_frame.iterrows():
        if row['Battle Number'] in battle_seen_set:
            continue
        else:
            battle_seen_set.add(row['Battle Number'])
            competitor_1 = row['Competitor 1']
            competitor_2 = row['Competitor 2']
            battle_winner = row['Battle Winner']
            competitor_1_won = battle_winner is competitor_1
            for judge in jam_judge_list:
                if math.isnan(row[judge]):
                    continue
                else:
                    judge_result_dict[judge].add_entry(row[judge])
    
    # BBoy Stats
    
    battle_seen_set = set()
    for index, row in data_frame.iterrows():
        if row['Battle Number'] in battle_seen_set:
            continue
        else:
            battle_seen_set.add(row['Battle Number'])
            competitor_1 = row['Competitor 1']
            competitor_2 = row['Competitor 2']
            
            if competitor_1 not in bboy_result_dict:
                bboy_result_dict[competitor_1] = _BBoyOrderTracker(competitor_1)
            if competitor_2 not in bboy_result_dict:
                bboy_result_dict[competitor_2] = _BBoyOrderTracker(competitor_2)
            
            battle_winner = row['Battle Winner']
            first_person = row['First']
            competitor_1_won = battle_winner is competitor_1
            competitor_1_first = first_person is competitor_1
            bboy_result_dict[competitor_1].add_entry(competitor_1_first,competitor_1_won)
            bboy_result_dict[competitor_2].add_entry(not competitor_1_first,not competitor_1_won)

                
    



