import csv

def save_to_file(DATA_LIST):
  file = open("DATA.csv",  encoding='utf-8-sig', mode="w", newline="")
  writer = csv.writer(file)
  writer.writerow(["PP_ID", "DATE", "USAGE"])
  for index in DATA_LIST:
    temp = list(index.values())
    writer.writerow(temp)
  if(DATA_LIST==[]):
      print("** CSV파일 추출불가 **")
  else:
      print("** CSV파일 추출완료 **")
  return