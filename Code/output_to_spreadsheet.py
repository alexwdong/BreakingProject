
import xml.etree.ElementTree as ET
import parse_bboy_to_nationality
tree = ET.parse('../Data/SilverbackOpen2018.xml')
root = tree.getroot()
bboy_results_dict = {}
nationality_dict = parse_bboy_to_nationality.parse_file_to_dict('../Data/BBoyToNationality.txt')

out_file = open('jank.txt','w')
for battle in root:
    competitors = battle.find("Competitors")
    competitor_1 = competitors.find("Competitor_1").text
    competitor_2 = competitors.find("Competitor_2").text
    nationality_1 = nationality_dict[competitor_1]
    nationality_2 = nationality_dict[competitor_2]
    #If competitors arent in already, create a Judge Vote Tracker for them
   
    judge_list = []
    judges = battle.find("Judges")
    judge_list.append(judges.find("Judge_1").text)
    judge_list.append(judges.find("Judge_2").text)
    judge_list.append(judges.find("Judge_3").text)
    judge_list.append(judges.find("Judge_4").text)
    judge_list.append(judges.find("Judge_5").text)
    judge_list.append(judges.find("Judge_6").text)
    judge_list.append(judges.find("Judge_7").text)
    out_file.write('Competitor 1'+'\t'+'Competitor 2'+'\t''Nationality 1'+'\t'+'Nationality 2'+'\t'+'Round'+'\t'
                   +judge_list[0]+' Physical'+'\t'+judge_list[0]+' Artistic'+'\t'+judge_list[0]+' Interpretive'+'\t'
                   +judge_list[1]+' Physical'+'\t'+judge_list[1]+' Artistic'+'\t'+judge_list[1]+' Interpretive'+'\t'
                   +judge_list[2]+' Physical'+'\t'+judge_list[2]+' Artistic'+'\t'+judge_list[2]+' Interpretive'+'\t'
                   +judge_list[3]+' Physical'+'\t'+judge_list[3]+' Artistic'+'\t'+judge_list[3]+' Interpretive'+'\t'
                   +judge_list[4]+' Physical'+'\t'+judge_list[4]+' Artistic'+'\t'+judge_list[4]+' Interpretive'+'\t'
                   +judge_list[5]+' Physical'+'\t'+judge_list[5]+' Artistic'+'\t'+judge_list[5]+' Interpretive'+'\t'
                   +judge_list[6]+' Physical'+'\t'+judge_list[6]+' Artistic'+'\t'+judge_list[6]+' Interpretive'+'\n')
    
    round_list = battle.findall("Round")
    round_number = 0
    for round in round_list:
        round_number = round_number+1
       
        
        physical_1 = float(round.find("Judge_1_Scores").find("Physical").text)
        artistic_1 = float(round.find("Judge_1_Scores").find("Artistic").text)
        interpretive_1 = float(round.find("Judge_1_Scores").find("Interpretive").text)
        
        physical_2 = float(round.find("Judge_2_Scores").find("Physical").text)
        artistic_2 = float(round.find("Judge_2_Scores").find("Artistic").text)
        interpretive_2 = float(round.find("Judge_2_Scores").find("Interpretive").text)
        
        physical_3 = float(round.find("Judge_3_Scores").find("Physical").text)
        artistic_3 = float(round.find("Judge_3_Scores").find("Artistic").text)
        interpretive_3 = float(round.find("Judge_3_Scores").find("Interpretive").text)

        
        physical_4 = float(round.find("Judge_4_Scores").find("Physical").text)
        artistic_4 = float(round.find("Judge_4_Scores").find("Artistic").text)
        interpretive_4 = float(round.find("Judge_4_Scores").find("Interpretive").text)
        
        
        physical_5 = float(round.find("Judge_5_Scores").find("Physical").text)
        artistic_5 = float(round.find("Judge_5_Scores").find("Artistic").text)
        interpretive_5 = float(round.find("Judge_5_Scores").find("Interpretive").text)
        
        
        physical_6 = float(round.find("Judge_6_Scores").find("Physical").text)
        artistic_6 = float(round.find("Judge_6_Scores").find("Artistic").text)
        interpretive_6 = float(round.find("Judge_6_Scores").find("Interpretive").text)
        
        
        physical_7 = float(round.find("Judge_7_Scores").find("Physical").text)
        artistic_7 = float(round.find("Judge_7_Scores").find("Artistic").text)
        interpretive_7 = float(round.find("Judge_7_Scores").find("Interpretive").text)
        
        out_file.write(competitor_1 + "\t" + competitor_2 +  "\t" +
              nationality_1 +'\t' + nationality_2 + '\t' + 'Round ' + str(round_number) + '\t' + 
              str(physical_1) + "\t" + str(artistic_1) + "\t" + str(interpretive_1) + "\t" +
              str(physical_2) + "\t" + str(artistic_2) + "\t" + str(interpretive_2) + "\t" +
              str(physical_3) + "\t" + str(artistic_3) + "\t" + str(interpretive_3) + "\t" +
              str(physical_4) + "\t" + str(artistic_4) + "\t" + str(interpretive_4) + "\t" +
              str(physical_5) + "\t" + str(artistic_5) + "\t" + str(interpretive_5) + "\t" +
              str(physical_6) + "\t" + str(artistic_6) + "\t" + str(interpretive_6) + "\t" +
              str(physical_7) + "\t" + str(artistic_7) + "\t" + str(interpretive_7)+ "\n")
    out_file.close
        
