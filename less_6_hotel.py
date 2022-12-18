response = '''Привіт! Відвідала курорт «Морська зірка».
Дуже сподобалося обслуговування, вищий клас!
Щодо меню також залишилися найкращі враження ,
 спортзал має сучасні велотренажени'''

counter_service = response.count("обслуговування")
counter_menu = response.count("меню")
counter_sport = response.count("спортзал")

discount = 5           # 5% знижка
sum_discount = 0       # остаточна знижка
sum_pay = 100          # сума без знижок

if len(response) > 60:       #додаткова знижка 15%
    sum_discount += 15

sum_discount += discount * (counter_service + counter_menu + counter_sport)
sum_money = (sum_pay * sum_discount)/100
sum_result = sum_pay - sum_money

print("Вам нараховано знижку %d" % sum_discount + "%")

print("Сума зі знижкою %d грн" % sum_result)

