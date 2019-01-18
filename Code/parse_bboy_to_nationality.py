import re
import warnings

def parse_file_to_dict(txt_file_str):
  '''
  Parses a two column semicolon delimited file into a dictionary

  Comments in the file can be specified by using the # character
  '''
  return_dict = {}
  pattern = re.compile('(?P<name>.*);(?P<nationality>.*)')
  with open(txt_file_str) as file:
    line_number = 0
    for line in file:
      line_number = line_number+1
      line.replace("#.","") # removes comments
      match_obj = re.match(pattern,line)
      if match_obj is None:
        warnings.warn("In file "+ txt_file_str + " on line " + str(line_number) + " no match was found")
      
      else:
        return_dict[match_obj["name"]] = match_obj["nationality"]
  return return_dict 

