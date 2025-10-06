students_results = {
  "Harry": 85,
  "Ron": 71,
  "Hermione": 98,
  "Draco": 10
}
end_procents={
    "excelent":0,
    "well done":0,
    "fullfill":0,
    "!fullfill!":0
}

def x_funct():
        global word_score
        word_score=list(end_procents.keys())
        word_score=word_score[x]


def end_sceen():
      global majority,all_mem,fin,majority_key
      all_mem=0
      majority= int(max(end_procents.values()))
      majority_key=max(end_procents, key=end_procents.get)

      for i in end_procents:
          all_mem+=end_procents[i]

      fin=(majority/all_mem)*100
      print(f"Nejvíc bylo {majority_key} činili {fin} % ")
# Stupnice
# 91 až 100 = "Excelentní"
# 81 až 90 = "Vynikající"
# 71 až 80 = "Splněno"
# méně jak 71 = "Nesplněno"

for key in students_results:
      if students_results[key] >=90 and students_results[key]<101:
            x=0
            x_funct()
            print(f"{key}: {word_score} ")
            end_procents["excelent"]+=1
        

      elif students_results[key] >=80:
            x=1
            x_funct()
            print(f"{key}: {word_score} ")
            end_procents["well done"]+=1

      elif students_results[key] >=70:
            x=2
            x_funct()
            print(f"{key}: {word_score} ")
            end_procents["fullfill"]+=1

      else:
            x=3
            x_funct()
            print(f"{key}: {word_score} ")
            end_procents["!fullfill!"]+=1
end_sceen()


