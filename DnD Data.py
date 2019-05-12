import random
race_list = ["Elf","Halfling","Dwarf","Human","Half Elf","Half Orc","Gnome","Teifling","Dragonborn"]

class_list = ["Barbarian","Bard","Cleric","Druid","Fighter","Monk","Paladin","Ranger","Sorcerer","Rogue","Wizard"]


alignment_1 = ["Lawful","Neutral","Chaotic"]

alignment_2 = ["Good","Neutral","Evil"]

dwarf_first_names = ["Adrik", "Alberich", "Baern", "Barendd", "Brottor", "Bruenor", "Dain", "Darrak", "Delg", "Eberk", "Einkil", "Fargrim", "Flint", "Gardain", "Harbek", "Kildrak", "Morgran", "Orsik", "Oskar", "Rangrim", "Rurik","Taklinn", "Thoradin", "Thorin", "Tordek", "Traubon", "Travok", "Ulfgar", "Veit", "Vondal"]

dwarf_last_names = ["Balderk", "Battlehammer", "Brawnanvil", "Dankil", "Fireforge", "Frostbeard", "Gorunn", "Holderhek", "Ironfist", "Loderr", "Lutgehr", "Rumnaheim", "Strakeln", "Torunn", "Ungart"]

elf_first_names = ["Adran", "Aelar", "Aramil", "Arannis", "Aust", "Beiro", "Berrian", "Carric", "Enialis", "Erdan", "Erevan", "Galinndan", "Hadarai", "Heian", "Himo", "Immeral", "Ivellios", "Laucian", "Mindartis", "Paelias","Peren", "Quarion", "Riardon", "Rolen", "Soveliss", "Thamior", "Tharivol", "Theren", "Varis"]

elf_last_names = ["Amakiir", "Amastacia", "Galanodel", "Holimion", "Ilphelkiir", "Liadon", "Meliamne", "Naïlo", "Siannodel", "Xiloscient"]

halfling_first_names = ["Alton", "Ander", "Cade", "Corrin", "Eldon", "Errich", "Finnan", "Garret", "Lindal", "Lyle", "Merric", "Milo", "Osborn", "Perrin", "Reed", "Roscoe", "Wellby"]

halfling_last_names = ["Brushgather", "Goodbarrel", "Greenbottle", "Highhill", "Hilltopple", "Leagallow", "Tealeaf", "Thorngage", "Tosscobble", "Underbough"]

gnome_first_names = ["Boddynock", "Dimble", "Fonkin", "Gimble", "Glim", "Gerbo", "Jebeddo", "Namfoodle", "Roondar", "Seebo", "Zook"]

gnome_last_names = ["Beren", "Daergel", "Folkor", "Garrick", "Nackle", "Murnig", "Ningel", "Raulnor", "Scheppen", "Turen"]

orc_first_names = ["Dench", "Feng", "Gell", "Henk", "Holg", "Imsh", "Keth", "Krusk", "Ront", "Shump", "Thokk"]

human_first_names =["Adler", "Admon", "Adolph", "Ahren", "Aiden", "Aimery",
"Alain", "Alard", "Alaric", "Aldous", "Alek", "Alwyn", "Ambert", "Anlow", "Arando", "Benn",
"Bram", "Bedrich", "Bertram", "Benvolio", "Bennett", "Brandis", "Cale", "Conrad", "Dalkon",
"Daylen", "Dedric", "Del", "Derek", "Dexter", "Dian", "Dirke", "Dodd", "Donn", "Drew",
"Dungarth", "Dyrk", "Eandro", "Erik", "Falken", "Feck", "Fenton", "Gallus", "Garvin", "Gregg",
"Griswold", "Gryphero", "Hagar", "Hamlin", "Helmut", "Hew", "Jeras", "Jonn", "Kris", "Krynt",
"Lavant", "Leyten", "Madian", "Malfier", "Marc", "Markus", "Meklan", "Mikal", "Milos",
"Namen", "Navaren", "Nerle", "Nilus", "Ningyan", "Norris", "Pieter", "Quentin", "Quinn",
"Raeburn", "Raynard", "Regdar", "Ritter", "Rudolph", "Samm", "Semil", "Sevenson",
"Steveren", "Talfen", "Tamond", "Taran", "Tavon", "Tegan", "Thom", "Vanan", "Vincent",
"Wendell", "Wil", "Wolfram","Ana", "Azura", "Axelle", "Brey", "Brynna", "Carlen",
"Cassi", "Clotilda", "Druella", "Eloise", "Eliska", "Eliza", "Enye", "Giselle", "Gwenn", "Hallan",
"Jenn", "Kasaki", "Kat", "Kiera", "Lida", "Lorelei", "Luusi", "Megan", "Mika", "Millicent",
"Mirabel", "Miri", "Natalie", "Nicola", "Nydia", "Pharana", "Remora", "Rolanda", "Rosalyn",
"Rudelle", "Sachil", "Saidi", "Stasi", "Shawna", "Tanika", "Tura", "Tylsa", "Vencia",
"Veronica", "Wilhelmina", "Xandrilla", "Zanne"]

human_last_names =["Arkalis", "Armanci", "Baldric", "Ballard", "Bilger",
"Blackstrand", "Brightwater", "Carnavon", "Caskajaro", "Coldshore", "Coyle", "Cresthill",
"Cuttlescar", "Daargen", "Dalicarlia", "Danamark", "Donoghan", "Drumwind", "Dunhall",
"Ereghast", "Falck", "Fallenbridge", "Faringray", "Fletcher", "Fryft", "Goldrudder",
"Grantham", "Graylock", "Gullscream", "Hardy", "Hartman", "Hayward", "Hindergrass",
"Iscalon", "Kreel", "Kroft", "Lamoth", "Leerstrom", "Lynchfield", "Moonridge",
"Netheridge", "Oakenheart", "Pyncion", "Ratley", "Redraven", "Revenmar", "Roxley",
"Rowland", "Sell", "Seratolva", "Shanks", "Shattermast", "Shaulfer", "Silvergraft",
"Stavenger", "Stormchapel", "Strong", "Swiller", "Talandro", "Targana", "Towerfall",
"Umbermoor", "Van Devries", "Van Gandt", "Van Hyden", "Varcona", "Varzand",
"Voortham", "Vrye", "Webb", "Welfer", "Wilxes", "Wintermere", "Wygarthe", "Zatchet",
"Zethergyll"]

tiefling_first_names = ["Akta","Bryseis","Damaia","Kallistra","Lerissa","Makaria","Nemela","Orianna","Phelaia","Rieta","Akemenos","Amonon","Barakas","Damakos","Ekemon","Lados","Kairon","Leucis","Melech","Morthos","Pelaios","Skamos","Therai"]

tiefling_last_names = ["Angelbane","Babausong","Balorfist","Blackbard","Coilbone","Demoneye","Dretchsticker","Fiendline","Hezroustrike","Incubore","Lemureslayer","Vicelord"]

dragonborn_first_names = ["Arjhan", "Balasar", "Bharash", "Donaar", "Ghesh", "Heskan", "Kriv", "Medrash", "Mehen", "Nadarr", "Pandjed", "Patrin", "Rhogar", "Shamash", "Shedinn", "Tarhun", "Torinn","Akra", "Biri", "Daar", "Farideh", "Harann", "Havilar", "Jheri", "Kava", "Korinn", "Mishann", "Nala", "Perra", "Raiann", "Sora", "Surina", "Thava", "Uadjit"]

dragonborn_last_names = ["Clethtinthiallor", "Daardendrian", "Delmirev", "Drachedandion", "Fenkenkabradon", "Kepeshkmolik", "Kerrhylon", "Kimbatuul", "Linxakasendalor", "Myastan", "Nemmonis", "Norixius", "Ophinshtalajiir", "Prexijandilin", "Shestendeliath", "Turnuroth", "Verthisathurgiesh", "Yarjerit"]

#Pick a Race
Race_choice = random.choice(race_list)
#Pick a Class
Class_choice = random.choice(class_list)
#Pick an Alignment
Alignment = random.choice(alignment_1) + " " + random.choice(alignment_2)

#Code to choose names
if Race_choice == 'Elf':
    First_name = random.choice(elf_first_names)
    Last_name = random.choice(elf_last_names)
elif Race_choice == 'Halfling':
    First_name = random.choice(halfling_first_names)
    Last_name = random.choice(halfling_last_names)
elif Race_choice == 'Dwarf':
    First_name = random.choice(dwarf_first_names)
    Last_name = random.choice(dwarf_last_names)
elif Race_choice == 'Human':
    First_name = random.choice(human_first_names)
    Last_name = random.choice(human_last_names)
elif Race_choice == 'Half Elf':
    Name_choice = random.randint(0,1)
    if Name_choice == 0:
        First_name = random.choice(human_first_names)
        Last_name = random.choice(human_last_names)
    else:
        First_name = random.choice(elf_first_names)
        Last_name = random.choice(elf_last_names)
elif Race_choice == 'Half Orc':
    Name_choice = random.randint(0,1)
    if Name_choice == 0:
        First_name = random.choice(human_first_names)
        Last_name = random.choice(human_last_names)
    else:
        First_name = random.choice(orc_first_names)
        Last_name = random.choice(orc_first_names)
elif Race_choice == 'Gnome':
    First_name = random.choice(gnome_first_names)
    Last_name = random.choice(gnome_last_names)
elif Race_choice == 'Teifling':
    First_name = random.choice(tiefling_first_names)
    Last_name = random.choice(tiefling_last_names)
elif Race_choice == 'Dragonborn':
    First_name = random.choice(dragonborn_first_names)
    Last_name = random.choice(dragonborn_last_names)

print("Your are a: " + Race_choice)
print("Your class is: " + Class_choice)
print("Your name is: " + First_name,Last_name)
print("Your alignment is: " + Alignment)

#Generate random stat values
Strength = str(random.randint(3,18))
Dexterity = str(random.randint(3,18))
Wisdom = str(random.randint(3,18))
Intelligence = str(random.randint(3,18))
Constitution = str(random.randint(3,18))
Charisma = str(random.randint(3,18))

#Generate Ability Scores with Race Bonuses
print('--------Ability Scores--------')
if Race_choice == 'Human':
    Strength_bonus = str(1)
    Dex_b = str(1)
    Wis_b = str(1)
    Int_b = str(1)
    Con_b = str(1)
    Char_b = str(1)
    Total_Strength = str(int(Strength) + int(Strength_bonus))
    Dex_total = str(int(Dexterity) + int(Dex_b))
    Int_total = str(int(Intelligence) + int(Int_b))
    Wis_total = str(int(Wisdom) + int(Wis_b))
    Con_total = str(int(Constitution) + int(Con_b))
    Char_total = str(int(Charisma) + int(Char_b))
elif Race_choice == 'Half Orc':
    Strength_bonus = str(2)
    Con_b = str(1)
    Total_Strength = str(int(Strength) + int(Strength_bonus))
    Dex_total = Dexterity
    Int_total = Intelligence
    Wis_total = Wisdom
    Con_total = str(int(Constitution) + int(Con_b))
    Char_total = Charisma
elif Race_choice == 'Dragonborn':
    Strength_bonus = str(2)
    Char_b = str(1)
    Total_Strength = str(int(Strength) + int(Strength_bonus))
    Dex_total = Dexterity
    Wis_total = Wisdom
    Int_total = Intelligence
    Con_total = Constitution
    Char_total = str(int(Charisma) + int(Char_b))
elif Race_choice == 'Dwarf':
    Con_b = str(2)
    Total_Strength = Strength
    Dex_total = Dexterity
    Int_total = Intelligence
    Wis_total = Wisdom
    Con_total = str(int(Constitution) + int(Con_b))
    Char_total = Charisma
elif Race_choice == 'Half Elf':
    Dex_b = str(2)
    Char_b = str(2)
    Total_Strength = Strength
    Dex_total = str(int(Dexterity) + int(Dex_b))
    Int_total = Intelligence
    Wis_total = Wisdom
    Con_total = Constitution
    Char_total = str(int(Charisma) + int(Char_b))
elif Race_choice == 'Elf':
    Dex_b = str(2)
    Total_Strength = Strength
    Dex_total = str(int(Dexterity) + int(Dex_b))
    Int_total = Intelligence
    Wis_total = Wisdom
    Con_total = Constitution
    Char_total = Charisma
elif Race_choice == 'Teifling':
    Int_b = str(1)
    Total_Strength = Strength
    Dex_total = Dexterity
    Int_total = str(int(Intelligence) + int(Int_b))
    Wis_total = Wisdom
    Con_total = Constitution
    Char_total = Charisma
elif Race_choice == 'Gnome':
    Int_b = str(2)
    Total_Strength = Strength
    Dex_total = Dexterity
    Int_total = str(int(Intelligence) + int(Int_b))
    Wis_total = Wisdom
    Con_total = Constitution
    Char_total = Charisma
elif Race_choice == 'Halfling':
    Dex_b = str(2)
    Total_Strength = Strength
    Dex_total = str(int(Dexterity) + int(Dex_b))
    Int_total = Intelligence
    Wis_total = Wisdom
    Con_total = Constitution
    Char_total = Charisma

print("You have the Strength stat of " + Total_Strength)
print("You have the Dexterity stat of " + Dex_total)
print("You have the Intelligence stat of " + Int_total)
print("You have the Wisdom stat of " + Wis_total)
print("You have the Constitution stat of " + Con_total)
print("You have the Charisma stat of " + Char_total)





