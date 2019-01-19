# -*- coding: utf-8 -*-

'''
Adding net phys/art/interp differences and total votes for each round

'''
import numpy as np
import pandas as pd



def one_if_pos_else_0(a):
  return [a > b for a, b in zip(a,0*[len(a)])]
  



SBO2018old = pd.read_csv('../Data/SBO2018Table.csv')
SBO2018 = SBO2018old

SBO2018old = SBO2018old.fillna(0)
SBO2018['Physical Difference'] = SBO2018old['Poe One Physical'] + \
                                 SBO2018old['Goku Physical'] + \
                                 SBO2018old['Storm Physical'] + \
                                 SBO2018old['Crazy Legs Physical'] + \
                                 SBO2018old['Narumi Physical'] + \
                                 SBO2018old['Skim Physical'] + \
                                 SBO2018old['Lil Cesar Physical'] + \
                                 SBO2018old['Jeskilz Physical'] + \
                                 SBO2018old['Renegade Physical']
                                 
SBO2018['Artistic Difference'] = SBO2018old['Poe One Artistic'] + \
                                 SBO2018old['Goku Artistic'] + \
                                 SBO2018old['Storm Artistic'] + \
                                 SBO2018old['Crazy Legs Artistic'] + \
                                 SBO2018old['Narumi Artistic'] + \
                                 SBO2018old['Skim Artistic'] + \
                                 SBO2018old['Lil Cesar Artistic'] + \
                                 SBO2018old['Jeskilz Artistic'] + \
                                 SBO2018old['Renegade Artistic']
                                 
SBO2018['Interpretive Difference'] = SBO2018old['Poe One Interpretive'] + \
                                 SBO2018old['Goku Interpretive'] + \
                                 SBO2018old['Storm Interpretive'] + \
                                 SBO2018old['Crazy Legs Interpretive'] + \
                                 SBO2018old['Narumi Interpretive'] + \
                                 SBO2018old['Skim Interpretive'] + \
                                 SBO2018old['Lil Cesar Interpretive'] + \
                                 SBO2018old['Jeskilz Interpretive'] + \
                                 SBO2018old['Renegade Interpretive']

SBO2018['Competitor 1 Votes'] = 1*((SBO2018old['Poe One Physical'].values + SBO2018old['Poe One Artistic'].values + SBO2018old['Poe One Interpretive'].values)>0) +\
                                1*((SBO2018old['Goku Physical'].values + SBO2018old['Goku Artistic'].values + SBO2018old['Goku Interpretive'].values)>0) +\
                                1*((SBO2018old['Storm Physical'].values + SBO2018old['Storm Artistic'].values + SBO2018old['Storm Interpretive'].values)>0) +\
                                1*((SBO2018old['Crazy Legs Physical'].values + SBO2018old['Crazy Legs Artistic'].values + SBO2018old['Crazy Legs Interpretive'].values)>0) +\
                                1*((SBO2018old['Narumi Physical'].values + SBO2018old['Narumi Artistic'].values + SBO2018old['Narumi Interpretive'].values)>0) +\
                                1*((SBO2018old['Skim Physical'].values + SBO2018old['Skim Artistic'].values + SBO2018old['Skim Interpretive'].values)>0) +\
                                1*((SBO2018old['Lil Cesar Physical'].values + SBO2018old['Lil Cesar Artistic'].values + SBO2018old['Lil Cesar Interpretive'].values)>0) +\
                                1*((SBO2018old['Jeskilz Physical'].values + SBO2018old['Jeskilz Artistic'].values + SBO2018old['Jeskilz Interpretive'].values)>0) +\
                                1*((SBO2018old['Renegade Physical'].values + SBO2018old['Renegade Artistic'].values + SBO2018old['Renegade Interpretive'].values)>0) 



SBO2018.to_csv('SBO2018MORE.csv',na_rep='NaN')
