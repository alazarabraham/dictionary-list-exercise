boxing = [
    {"name": "Floyd Mayweather",
     "record": "50-0(27 knockouts)" ,
     "nickname: ": "Funny/Favorite sayings: 'Well point to the easy work than '",},{"name" : "Gennady Golovkin",
     "record": "39-1(35 Knockouts)",
     "nickname: ": "Funny quote: Come on guys, this is not big drama show"},{"name": "Errol Spence",
     "record": "25-0 (21 Knockouts)",
     "nickname: ": """ Funny/Favorite sayings: 'Imma knock you out tho...'-to Shawn porter 
     prior to their welterweight superfight.""",},{"name": "Deontay Wilder",
     "record": "42-0(40 Knockouts)",
     "nickname: ": "Great Wilder quote: 'I lead by faith and not by sight'"}]

ask = raw_input("Enter your favorite boxer's first name ").lower()
if ask == "floyd":
    print(boxing[0]["name"])
    asktwo = raw_input("is this the right boxer?").lower()
    yes = "yes"
    no = "no"
    if asktwo == yes:
      print("His record is: " +boxing[0]["record"] + """
      he has defeated the finest athletes in the sport, by margins 
      that are some of the highest in all sports. He has the highest 
      compubox stats in the sport of boxing, and is the highest paid 
      athlete in the world""")
      click = raw_input("Click Y for more")
      if click == "y":
        print(boxing[0]["nickname: "])
if ask == "gennady":
  print(boxing[1]["name"])
  asktwo = raw_input("is this the right boxer?").lower()
  yes = "yes"
  no = "no"
  if asktwo == yes:
    print("His record is: " +boxing[1]["record"] + """Triple G was only 9 
    when the soviet union dissolved. His brother recommended he start fighting,
    and he just happened to be extremely gifted at it. He rose through the ranks of 
    boxing's presitigious middleweight division(with the higest the knock out ration
    in division history) and is considered one of the greatest middleweight champions
    ever. He has a steel chin, a master's jab, and a right hand that can knock 
    out any champion. """)
    click = raw_input("Click Y for more")
    if click == "y":
        print(boxing[1]["nickname: "])
if ask == "errol":
    print(boxing[2]["name"])
    asktwo = raw_input("is this the right boxer?").lower()
    yes = "yes"
    no = "no"
    if asktwo == yes:
      print("His record is: " +boxing[2]["record"] + """Errol spence is currently
      boxing's golden child. His output is unmatched in boxing. He can throw up to
      a thousand punches a fight, sometimes landing half. His defense is some of the 
      finest in the division, and his power and skill is comparable to that of any 
      boxer, in any division.  """)
      click = raw_input("Click Y for more")
      if click == "y":
        print(boxing[2]["nickname: "])
if ask == "deontay":
    print(boxing[3]["name"])
    asktwo = raw_input("is this the right boxer?").lower()
    yes = "yes"
    no = "no"
    if asktwo == yes:
      print("His record is: " +boxing[3]["record"] + """ Wilder is the most devasting 
      puncher in any division. He is the fastest boxer to have qualified for the 
      olympics, qualifying only a year into boxing. His IQ is extremely high in the ring, 
      and he is capable of keeping pressure at any championship level/paced fight.He 
      intends to unify the heavyweight division by winning all five belts.""")
      click = raw_input("Click Y for more")
      if click == "y":
        print(boxing[3]["nickname: "])
        