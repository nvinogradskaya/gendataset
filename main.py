import random
import xlsxwriter

workbook = xlsxwriter.Workbook('Expenses02.xlsx')
worksheet = workbook.add_worksheet()

names = []
with open('first_name.txt') as f:
    for line in f:
        names.append(line)
surnames = []
with open('surname.txt') as f:
    for line in f:
        surnames.append(line)
patronymic = []
with open('second_name.txt') as f:
    for line in f:
        patronymic.append(line)
person_data = {}
snils = set()
passports = set()
def gen_random_name():
    return random.choice(surnames) + "" + random.choice(names) + "" + random.choice(patronymic)
def gen_snils():
    s = ""
    for i in range(3):
        s += str(random.randint(0, 9))
    s +='-'
    for i in range(3):
        s += str(random.randint(0, 9))
    s += '-'
    for i in range(3):
        s += str(random.randint(0, 9))
    s += ' '
    for i in range(2):
        s += str(random.randint(0, 9))
    if s not in snils:
        snils.add(s)
        return s
    else:
        new_s = gen_snils()
        return new_s
def gen_passport():
    s = ""
    for i in range(4):
        s += str(random.randint(0, 9))
    s += " "
    for i in range(6):
        s += str(random.randint(0, 9))
    # s - password
    if s not in passports:
        passports.add(s)
        return s
    else:
        new_s = gen_passport()
        return new_s


doctor_symp = {}
sympt = [["задержка менструации", "токсикоз", "повышение базальной температуры", "болезненные ощущения в молочных железах", "пятна", "задержка развития плода", "кровотечение"],
         ["слезотечение", "насморк", "чихание", "кашель",  "покраснение", "зуд", "отечность"],
         ["нарушения эрекции", "проблемы с зачатием", "изменение формы", "изменение плотности половых органов", "боли в области половых органов" , "дискомфорт в области половых органов", "пятна в области половых органов"],
         ["зуд", "покраснением", "жжением в половых органах", "импотенция", "боль половых органов", "жжение в половых органах", "боль рядом с половыми органами"],
         ["острая боль в животе", "ноющая боль", "изжога", "рвота", "понос", "боли после приема пищи", "диарея"],
         ["повышения температуры", "онемении кончиков пальцев", "бледности кожи", "ухудшения аппетита", "появлению синяков", "слабость", "усталость"],
         ["боли в правом подреберье", "тяжесть в области печени", "чувство дискомфорта в области печени", "изменение цвета кожи", "бронзовый оттенок кожи", "желтые бляшки на веках", "газообразование"],
         ["зуд половых органов", "жжение в половых органах", "выделения", "боли в области придатков", "боли при мочеиспускании", "нарушение менструального цикла", "сбой менструального цикла"],
         ["неврозы", "бессонница", "головные боли", "мигрень", "гипертония", "заболевания желудочно-кишечного тракта","боли в спине"],
         ["зуд", "сыпь", "покраснение", "шелушение", "пигментация", "появление новообразований"],
         ["избыточный вес", "недостаточный вес", "нарушения аппетита", "пониженный иммунитет", "сахарный диабет", "гормональные нарушения"],
         ["хроническая усталость", "головные боли", "сонливость", "ломота в мышцах и суставах", "частые простудные заболевания", "частые обострения герпеса", "неполадки в работе желудочно-кишечного тракта"],
         ["сильные головные боли", "бессонница", "сонливость", "быстрая утомляемость", "нарушение в работе желудочно-кишечного тракта", "чувство ломоты в суставах", "чувство ломоты в мышцах"],
         ["боли в груди", "боли в области сердца", "нарушение пульса", "нарушение биения сердца", "повышение давления", "понижение давления", "одышка", "вялость"],
         ["дефекты внешности человека"],
         ["задержка речевого развития", "неправильное произношение отдельных звуков", "заикание", "медленная речь", "быстрая речь", "нарушения ритмики речи", "нарушение способа произношения", "проблемы с чтением", "проблемы с восприятием речи на слух"],
         ["боли в груди", "уплотнения в молочной железе", "специфические выделения из сосков", "изменение пигментации", "втянутость сосков или изменение формы", "явная несимметричность грудей", "нарушения менструального цикла"],
         ["боли в позвоночнике", "боли в суставах", "скованность позвоночника", "головные боли", "головокружения"],
         ["боли в спине и пояснице", "нарушение осанки", "боли в суставах"],
         ["курение", "алкоголизм", "наркозависимость", "компьютерная зависимость"],
         ["нарушением сна", "головная боль при изменении погоды", "головокружением", "шум в ушах", "боль в шее", "боль в спине"],
         ["наличие крови или белка в моче", "прекращение или сокращение мочеиспускания", "боли в поясничном отделе"],
         ["частые необъяснимые кровотечения из внутренних органов", "необъяснимые кровотечения из носа", "беспричинная потеря волос", "кожные новообразования", "уплотнения в любой из частей тела"],
         ["боль в спине", "боль или хруст в суставах", "опухание суставов", "нарушение осанки", "недуги связанные с работой костей или мышц", "недуги связанные с работой суставов или связок"],
         ["нарушение дыхания", "заложенность носа", "выделение из носа и ушей", "шум в ушах", "боль в горле или области лица", "воспаление миндалин", "болезненность языка"],
         ["нарушение зрения", "дискомфортные ощущения в глазах", "изменения формы или цвета глазных тканей", "рябь в глазах", "выпадение ресниц"],
         ["боль в животе","нарушение работы желудочно-кишечного тракта", "понос", "запор", "рвота", "появление кожных реакций", "дерматиты"],
         ["ожоги", "облысение", "заячья губа", "глубокие морщины", "лишний вес"],
         ["дискомфорт в области прямой кишки или ануса", "запоры или диарея", "кровотечение или боли при дефекации", "геморрой", "недержание кала", "прианальные боли"],
         ["постоянное чувство тревоги", "чувство страха (вообще или боязни конкретных объектов или ситуаций)", "постоянная сонливость", "нарушения работы памяти", "вспышки агрессии"],
         ["постоянная подавленность", "неспособность справляться с проблемами", "неспособность найти общий язык с окружающими", "проблемы в семье"],
         ["тревога", "паника", "плохой сон", "неспособность нормально осознавать себя и окружающих", "неспособность нормально функционировать"],
         ["заболеваний дыхательных путей", "сухой или влажный кашель", "кровь в мокроте", "приступы удушья", "затрудненность дыхания", "боли в области груди"],
         ["ощущение скованности", "боли и отек в суставах", "подкожные узлы", "набухание и отечность височных артерий", "ограничение движений", "дискомфорт и боли в пояснице", "боли в коленях", "боли в суставах"],
         ["не удается забеременеть в течение длительного времени"],
         ["отсутствие сексуального влечения", "отсутствие удовольствия во время полового акта", "отсутствие оргазма", "боли во время полового акта", "боли при мастурбации"],
         ["боль в зубах", "кровоточивость десен", "реакция на кислое-сладкое/холодное-горячее", "пигментация эмали", "язвочки на внутренней поверхности щек"],
         ["повышение температуры", "кашель", "боль в животе", "боль в грудной клетке"],
         ["зуд", "сыпь", "покраснение", "шелушение кожи головы", "выпадение волос", "сухость или жирность волос"],
         ["боли в районе малого таза", "в почках", "признаки патологии сердца"],
         ["боли в области мочевого пузыря и поясницы", "рези при мочеиспускании", "частые позывы", "кровь или гной в моче", "недержание"],
         ["боль в ногах", "отечность к вечеру", "судороги", "сосудистые звездочки", "расширение вен"],
         ["последствиями травм (болезней)", "долго не заживающие раны", "гнойники", "порезы", "ожоги", "изменение цвета кожи", "кровотечения"],
         ["избыточный или недостаточный вес", "нарушения аппетита", "повышенная утомляемость", "непереносимость жары или холода", "нарушения физического или умственного развития", "бесплодие невыясненной этимологии"],
         ["выраженные симптомы интоксикации","резкий подъем температуры до высоких цифр","поза легавой собаки","геморрагическая сыпь с характерной локализацией"],
         ["болевой синдром","подготовка к беременности и ЭКО","желудочно-кишечные патологии","болезни опорно-двигательной системы","заболевания нервной системы","нарушения менструального цикла"],
         ["Повышенная потливость(ночная)","Похудание","Одышка","Боль в груди","Боль в пояснице","Кровохарканье"],
         ["необычная родинка","развитие злокачественной опухоли"],
         ["регулярные запоры и диарея","появление красноты, боли и зуда в заднем проходе","наличие слизистых, гнойных и кровянистых выделений из ануса","метеоризм","недержание кала","образование геморроидальных узлов и их выход наружу"],
         ["забывчивость","рассеянность","трудности с контролированием эмоций","суетливость","неуклюжесть движений","навязчивые состояния"]]
doctor = []
analys = []
with open('doc.txt') as f:
    for line in f:
        doctor.append(line)
with open('analyzes.txt') as f:
    for line in f:
        analys.append(line)
for j in range(len(doctor)):
    doctor_symp[doctor[j]] = [sympt[j]]
def gen_symp(j):
    s = ""
    for p in doctor_symp[j][0]:
        a = random.randint(0, 1)
        u = 0
        if a == 0:
            u = 5
        s += p * a + " " * a + "," * a
    if u == 5:
        s += doctor_symp[j][0][len(doctor_symp[j][0]) - 1]
    return(s)
date = []
def gen_date():
    s1 = ""
    month1 = ""
    month = random.randint(1,12)
    if month < 10:
        month1 = "0" + str(month)
    else:
        month1 = str(month)
    day = 0
    if month == 2:
        day = random.randint(1,28)
    elif month == 4 or month == 6 or month == 9 or month == 11 or month == 12:
        day = random.randint(1,30)
    else:
        day = random.randint(1,31)
    day1 = " "
    if day < 10:
        day1 = "0" + str(day)
    else:
        day1 = str(day)
    hours1 = " "
    hours = random.randint(8,20)
    if hours < 10:
        hours1 = "0"+ str(hours)
    else:
        hours1 = str(hours)

    year = random.randint(2015, 2018)
    min = str(random.randint(0,3) * 15)
    if min == 0:
        min = "00"
    s1 = str(year) + "-" + month1 + "-" + day1 + "T" + hours1 + ":" + min + "+03:00"
    if (day == 28 and month == 2) or (day==30 and (month ==4 or month ==6 or month == 9 or month == 11)) or (day==31 and (month == 1 or month == 3 or month == 5 or month == 7 or month ==8 or month==10)):
        day = 1
        month +=1
    else:
        day += 1
    if month < 10:
        month1 = "0" + str(month)
    else:
        month1 = str(month)
    if day < 10:
        day1 = "0" + str(day)
    else:
        day1 = str(day)

    s2 = str(year) + "-" + month1 + "-" + day1 + "T" + hours1 + ":" + min + "+03:00"
    year+=1
    s3 = str(year) + "-" + month1 + "-" + day1 + "T" + hours1 + ":" + min + "+03:00"
    if (day == 28 and month == 2) or (day==30 and (month ==4 or month ==6 or month == 9 or month == 11)) or (day==31 and (month == 1 or month == 3 or month == 5 or month == 7 or month ==8 or month==10)):
        day = 1
        month +=1
    else:
        day += 1
    if month < 10:
        month1 = "0" + str(month)
    else:
        month1 = str(month)
    if day < 10:
        day1 = "0" + str(day)
    else:
        day1 = str(day)

    s4 = str(year) + "-" + month1 + "-" + day1 + "T" + hours1 + ":" + min + "+03:00"
    year += 1
    s5 = str(year) + "-" + month1 + "-" + day1 + "T" + hours1 + ":" + min + "+03:00"
    if (day == 28 and month == 2) or (day==30 and (month ==4 or month ==6 or month == 9 or month == 11)) or (day==31 and (month == 1 or month == 3 or month == 5 or month == 7 or month ==8 or month==10)):
        day = 1
        month +=1
    else:
        day += 1
    if month < 10:
        month1 = "0" + str(month)
    else:
        month1 = str(month)
    if day < 10:
        day1 = "0" + str(day)
    else:
        day1 = str(day)

    s6 = str(year) + "-" + month1 + "-" + day1 + "T" + hours1 + ":" + min + "+03:00"
    year += 1
    s7 = str(year) + "-" + month1 + "-" + day1 + "T" + hours1 + ":" + min + "+03:00"
    if (day == 28 and month == 2) or (day==30 and (month ==4 or month ==6 or month == 9 or month == 11)) or (day==31 and (month == 1 or month == 3 or month == 5 or month == 7 or month ==8 or month==10)):
        day = 1
        month +=1
    else:
        day += 1
    if month < 10:
        month1 = "0" + str(month)
    else:
        month1 = str(month)
    if day < 10:
        day1 = "0" + str(day)
    else:
        day1 = str(day)

    s8 = str(year) + "-" + month1 + "-" + day1 + "T" + hours1 + ":" + min + "+03:00"
    year += 1
    s9 = str(year) + "-" + month1 + "-" + day1 + "T" + hours1 + ":" + min + "+03:00"
    if (day == 28 and month == 2) or (day == 30 and (month == 4 or month == 6 or month == 9 or month == 11)) or (
            day == 31 and (month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10)):
        day = 1
        month += 1
    else:
        day += 1
    if month < 10:
        month1 = "0" + str(month)
    else:
        month1 = str(month)
    if day < 10:
        day1 = "0" + str(day)
    else:
        day1 = str(day)

    s10 = str(year) + "-" + month1 + "-" + day1 + "T" + hours1 + ":" + min + "+03:00"
    return[s1,s2,s3,s4,s5,s6,s7,s8,s9,s10]
def gen_analys():
    num = random.randint(0, len(analys)-1)
    s = analys[num]
    num = random.randint(0, len(analys)-1)
    for i in range(4):
       if analys[num] not in s:
           r = random.randint(0, 1)
           s += r * analys[num] + r*" "
           num = random.randint(0, len(analys)-1)
    return(s)

cards = []
def gen_cards(system, percent1, bank, percent2,count):
    n = count
    p1 = percent1/100
    p2 = percent2/100
    card = ""
    if system == 1:
        #for i in range(int(n * p1)):  #30
        card += "4"
        if bank == 1:
            for j in range(int(n * p1 * p2)):
                card += "27924"
                for k in range(10):
                    card += str(random.randint(0, 9))
                cards.append(card)
                card = "4"
            for j in range(int(int(n * p1) - int(n * p1 * p2))):
                card += "00812"
                for k in range(10):
                    card += str(random.randint(0, 9))
                cards.append(card)
                card = "4"
        if bank == 2:
            for j in range(int(n * p1 * p2)):
                card += "00812"
                for k in range(10):
                    card += str(random.randint(0, 9))
                cards.append(card)
                card = "4"
            for j in range(int(int(n * p1) - int(n * p1 * p2))):
                card += "27924"
                for k in range(10):
                    card += str(random.randint(0, 9))
                cards.append(card)
                card = "4"
        card = ""
        for i in range(n - int(n * p1)):  # 30
            card += "5"
            for j in range(15):
                card += str(random.randint(0, 9))
            cards.append(card)
            card = ""
    if system == 2:
        #for i in range(int(n * p1)):  #30
        card += "5"
        if bank == 1:
            for j in range(int(n * p1 * p2)):
                card += "54781"
                for k in range(10):
                    card += str(random.randint(0, 9))
                cards.append(card)
                card = "5"
            for j in range(int(int(n * p1) - int(n * p1 * p2))):
                card += "52574"
                for k in range(10):
                    card += str(random.randint(0, 9))
                cards.append(card)
                card = "5"
        if bank == 2:
            for j in range(int(n * p1 * p2)):
                card += "52574"
                for k in range(10):
                    card += str(random.randint(0, 9))
                cards.append(card)
                card = "5"
            for j in range(int(int(n * p1) - int(n * p1 * p2))):
                card += "54781"
                for k in range(10):
                    card += str(random.randint(0, 9))
                cards.append(card)
                card = "5"
        card = ""
        for i in range(n - int(n * p1)):  # 30
            card += "4"
            for j in range(15):
                card += str(random.randint(0, 9))
            cards.append(card)
            card = ""
    return(cards)
print("Введите количество различных людей")
count = int(input())
count = count//5
print("Выберите банковскую систему: Visa(1) или Mastercard(2)")
system = int(input())
print("Введите ее вероятность в датасете в процентах")
percent1 = int(input())
print("Выберите банк: для Visa - Сбербанк(1) или Росбанк(2); для Mastercard - Промсвязьбанк(1) или Ситибанк(2)")
bank = int(input())
print("Введите его вероятность в датасете в процентах")
percent2 = int(input())
cards_for_people = gen_cards(system, percent1, bank, percent2, count)
m = 0

for l in range(count):
    passport = gen_passport()
    name = gen_random_name()
    snil = gen_snils()
    date = gen_date()
    for t in range(5):
        j = random.choice(doctor)
        s = ' '
        worksheet.write(t+l*5, 0, name)
        worksheet.write(t+l*5, 1, passport)
        worksheet.write(t+l*5, 2, snil)
        worksheet.write(t + l * 5, 4, j)
        worksheet.write(t + l * 5, 3, gen_symp(j))
        worksheet.write(t+l*5, 5, date[2*t])
        worksheet.write(t+l*5, 6, gen_analys())
        worksheet.write(t+l*5, 7, date[2*t+1])
        worksheet.write(t+l*5, 8, str(random.randint(10, 100)*50) + " руб.")
        worksheet.write(t+l*5, 9, cards_for_people[m])
    m +=1
workbook.close()




