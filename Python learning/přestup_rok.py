def main():
  global year,Q_month
  year = int(input("Jaký rok chcete zkontrolovat? "))
  Q_month=input("A kolik dnů bude mít měsíc v tom roce? ").lower()
  year_evaluation(year=year)
  if year_evaluation(year):
     print("Je to přestupný rok.")
     days_in_month[1]+=1
  else:
     print("Není to přestupný rok.")
  month_evaluation(month=Q_month)
  print(f"Měsíc:{month_evaluation(month=Q_month)}")
def year_evaluation(year):
  if year % 4 == 0:
      if year % 100 == 0:
          if year % 400 == 0:
            return True
          return False
      return True
  return False
def month_evaluation(month):
  index=months.index(month)
  return days_in_month[index]
days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
months=["leden","unor","brezen","duben","kveten","cerven","cervenec","srpen","zari","rijen","listopad","prosinec"]
main()
