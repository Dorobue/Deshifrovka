#Версия 1.1 от 17.02.2026
def KR(s):#Шаблон повторяющихся биграмм в слове. Например, CHurCH
    result=[]
    for a in range(0,len(s),2):
        for b in range(a+2,len(s),2):
            if s[a:a+2]==s[b:b+2]:
                result.append((a,b))
    return result
def KZ(s):#Шаблон зеркальных биграмм в слове. Например, themSElvES
    result = []
    for a in range(0, len(s), 2):
        for b in range(a+2, len(s), 2):
            if s[a] == s[b + 1] and s[a+1]==s[b]:
                result.append((a, b))
    return result
def str_cha(a):#Разбиение лингвистического слова на возможные шаблоны. Например WITHTHE дает WITHTH и ITHTHE
    if len(a) % 2:
        t = (a[:-1], a[1:])
    elif len(a) == 4:
        t = (a,)
    else:
        t = (a, a[1:-1])
    return t

class Deshifrovka:
    def __init__(self, file="r3.txt",ubiraem="Q"):
        self.ss = ["WITHTHE", 'THEMSELVES', 'FOLLOWING', 'SOMETHING', 'REMEMBER', 'THEYWERE', 'HEWAS', 'BEFORE', 'INTEREST',
              'BETWEEN', 'AGAINST', 'AGAIN', 'DIFFERENT', 'PERCENT', 'EFFECT', 'CONTINUE', 'COURSE', 'PROCESS',
              'PROVIDE', 'VOICE', 'FIGURE', 'DECIDE', 'UNDERSTAND', 'SOCIAL', 'OTHERS', 'ANDTHE', 'FORTHE', 'MIGHT',
              'PERSON', 'EXPECT', 'POSITION', 'MINUTE', 'FAMILY', 'DEVELOP', 'PROBLEM', 'BELIEVE', 'FRIEND', 'GIRL',
              'POSSIBLE', 'PUBLIC', 'INDUSTRY', 'SEVERAL', 'CONTROL', 'ITSELF', 'DESCRIBE', 'RETURN', 'VERY', 'INCLUDE',
              'GENERAL', 'PATIENT', 'EARLY', 'ACTIVITY', 'CHURCH', 'LIKELY', 'HALF', 'HAPPEN', 'LANGUAGE', 'SPECIAL',
              'DIFFICULT', 'DEPARTMENT', 'MANAGEMENT', 'MATTER', 'PRODUCT', 'COMMITTEE', 'YOUNG', 'HOUSE', 'BUILDING',
              'ITWAS', 'SYSTEM', 'YESTERDAY', 'WORK', 'EXPLAIN', 'PROJECT', 'RELATIONSHIP', 'SOMEONE', 'KUALITY',
              'ESTABLISH', 'INFORMATION', 'WHAT', 'INVOLVE', 'CHOOSE', 'BOARD', 'ACCORDING', 'KILL', 'KNOWLEDGE',
              'ARRIVE', 'ENERGY', 'DEGREE', 'HAPPY', 'ANSWER', 'FORWARD', 'HUSBAND', 'ANNOUNCE', 'MYSELF', 'LOOK',
              'OBTAIN', 'KUICKLY', 'ARGUMENT', 'SUDDENLY', 'BROTHER', 'STUDY', 'BABY', 'ADMIT', 'SUCCESSFUL', 'EXACTLY',
              'GOOD', 'MAJORITY', 'OBJECT', 'SERVE', 'LEFT', 'NGTHE', 'ANYWAY', 'HEAVY', 'TASK', 'CONTEXT', 'EXCEPT',
              'PHYSICAL', 'HIGHLY', 'SLIGHTLY', 'IAMNOT', 'SIZE', 'THROUGH', 'SPEAK', 'SUGGEST', 'OFTHE', 'ATION',
              'INTHE', 'INGTH', 'TOTHE', 'ATTHE', 'ONTHE', 'EDTHE', 'ORTHE', 'INGTO', 'THECO', 'CTION', 'ERTHE', 'SAND',
              'ETHE', 'STHE', 'MENT', 'THEP', 'TING', 'HAVEA', 'THAT', 'THIS', 'FROM', 'THEY', 'WHICH', 'WILL', 'WOULD',
              'THEIR', 'THERE', 'MAKE', 'KNOW', 'TIME', 'TAKE', 'THEM', 'SOME', 'COULD', 'YEAR', 'INTO', 'THEN', 'COME',
              'THAN', 'MORE', 'ABOUT', 'LAST', 'YOUR', 'OTHER', 'GIVE', 'JUST', 'SHOULD', 'THESE', 'WELL', 'ONLY',
              'WHEN', 'LIKE', 'SUCH', 'FIND', 'EVEN', 'THOSE', 'AFTER', 'DOWN', 'THING', 'TELL', 'STILL', 'MUST',
              'CHILD', 'HERE', 'OVER', 'MEAN', 'PART', 'LEAVE', 'LIFE', 'GREAT', 'WHERE', 'CASE', 'WOMAN', 'SEEM',
              'SAME', 'NEED', 'FEEL', 'EACH', 'MUCH', 'GROUP', 'ANOTHER', 'WORLD', 'AREA', 'SHOW', 'SHALL', 'UNDER',
              'NEVER', 'MOST', 'CALL', 'HAND', 'PARTY', 'HIGH', 'SMALL', 'PLACE', 'WHILE', 'POINT', 'HOLD', 'LARGE',
              'MEMBER', 'NEXT', 'FOLLOW', 'TURN', 'LOCAL', 'DURING', 'BRING', 'WORD', 'BEGIN', 'FACT', 'WRITE', 'STATE',
              'KUITE', 'BOTH', 'START', 'LONG', 'HELP', 'EVERY', 'HOME', 'MONTH', 'SIDE', 'NIGHT', 'HEAD', 'PLAY',
              'POWER', 'CHANGE', 'MOVE', 'ORDER', 'BOOK', 'OFTEN', 'HEAR', 'ROOM', 'WATER', 'FORM', 'MEET', 'TILL',
              'LINE', 'ALLOW', 'LATE', 'LEAD', 'STAND', 'LIVE', 'SINCE', 'NAME', 'BODY', 'LEAST', 'CARRY', 'VIEW',
              'TALK', 'FACE', 'ABLE', 'HOUR', 'RATE', 'DOOR', 'COURT', 'OFFICE', 'LESS', 'TERM', 'FULL', 'SORT', 'READ',
              'MOTHER', 'OFFER', 'ONCE', 'POLICE', 'LOSE', 'EVER', 'PRICE', 'ACTION', 'ISSUE', 'TYPE', 'FALL', 'TODAY',
              'OPEN', 'MOMENT', 'CENTRE', 'STOP', 'SEND', 'HEALTH', 'MAIN', 'WOUND', 'CLASS', 'RECEIVE', 'BUILD',
              'SPEND', 'FORCE', 'CONDITION', 'PAPER', 'MAJOR', 'AGREE', 'ECONOMIC', 'UPON', 'LEARN', 'CENTURY',
              'THEREFORE', 'FATHER', 'SECTION', 'AROUND', 'ROAD', 'TABLE', 'REACH', 'REAL', 'MIND', 'AMONG', 'TEAM',
              'DEATH', 'SOON', 'SENSE', 'STAFF', 'CERTAIN', 'STUDENT', 'INTERNATIONAL', 'MORNING', 'HOPE', 'ACROSS',
              'PLAN', 'CITY', 'GROUND', 'LETTER', 'CREATE', 'EVIDENCE', 'FOOT', 'CLEAR', 'GAME', 'FOOD', 'ROLE',
              'PRACTICE', 'BANK', 'ELSE', 'SUPPORT', 'SELL', 'EVENT', 'BEHIND', 'SURE', 'PASS', 'BLACK', 'STAGE',
              'MEETING', 'SOMETIMES', 'THUS', 'ACCEPT', 'AVAILABLE', 'TOWN', 'FURTHER', 'CLUB', 'HISTORY', 'PARENT',
              'LAND', 'TRADE', 'WATCH', 'WHITE', 'SITUATION', 'WHOSE', 'TEACHER', 'RECORD', 'MANAGER', 'RELATION',
              'COMMON', 'STRONG', 'WHOLE', 'FIELD', 'FREE', 'BREAK', 'WINDOW', 'STAY', 'WAIT', 'MATERIAL', 'WIFE',
              'COVER', 'APPLY', 'LOVE', 'RAISE', 'SALE', 'INDEED', 'PLEASE', 'LIGHT', 'CLAIM', 'BASE', 'CARE',
              'EVERYTHING', 'CERTAINLY', 'RULE', 'GROW', 'SIMILAR', 'STORY', 'WORKER', 'NATURE', 'STRUCTURE',
              'NECESSARY', 'POUND', 'METHOD', 'UNIT', 'CENTRAL', 'UNION', 'MOVEMENT', 'TRUE', 'ESPECIALLY', 'SHORT',
              'PERSONAL', 'DETAIL', 'MODEL', 'BEAR', 'SINGLE', 'JOIN', 'REDUCE', 'HERSELF', 'WALL', 'EASY', 'PRIVATE',
              'COMPUTER', 'FORMER', 'HOSPITAL', 'CHAPTER', 'SCHEME', 'CONSIDER', 'COUNCIL', 'DEVELOPMENT', 'EXPERIENCE',
              'THEORY', 'WITHIN', 'WISH', 'PROPERTY', 'ACHIEVE', 'FINANCIAL', 'POOR', 'BLOW', 'CHARGE', 'DIRECTOR',
              'DRIVE', 'APPROACH', 'CHANCE', 'APPLICATION', 'SEEK', 'COOL', 'FOREIGN', 'ALONG', 'AMOUNT', 'OPERATION',
              'FAIL', 'HUMAN', 'OPPORTUNITY', 'SIMPLE', 'LEADER', 'LEVEL', 'PRODUCTION', 'VALUE', 'FIRM', 'PICTURE',
              'SOURCE', 'SECURITY', 'BUSINESS', 'DECISION', 'CONTRACT', 'WIDE', 'AGREEMENT', 'SITE', 'EITHER',
              'VARIOUS', 'SCREW', 'TEST', 'CLOSE', 'REPRESENT', 'COLOUR', 'SHOP', 'BENEFIT', 'ANIMAL', 'HEART',
              'ELECTION', 'PURPOSE', 'SECRETARY', 'RISE', 'DATE', 'HARD', 'MUSIC', 'HAIR', 'PREPARE', 'ANYONE',
              'PATTERN', 'MANAGE', 'PIECE', 'DISCUSS', 'PROVE', 'FRONT', 'EVENING', 'ROYAL', 'TREE', 'POPULATION',
              'FINE', 'PLANT', 'PRESSURE', 'RESPONSE', 'CATCH', 'STREET', 'DESPITE', 'DESIGN', 'KIND', 'PAGE', 'ENJOY',
              'INDIVIDUAL', 'REST', 'INSTEAD', 'WEAR', 'BASIS', 'FIRE', 'SERIES', 'SUCCESS', 'NATURAL', 'WRONG', 'NEAR',
              'ROUND', 'THOUGHT', 'LIST', 'ARGUE', 'FINAL', 'FUTURE', 'INTRODUCE', 'ENTER', 'SPACE', 'ENSURE',
              'STATEMENT', 'BALCONY', 'ATTENTION', 'PRINCIPLE', 'PULL', 'DOCTOR', 'CHOICE', 'REFER', 'FEATURE',
              'COUPLE', 'STEP', 'THANK', 'MACHINE', 'INCOME', 'TRAINING', 'PRESENT', 'ASSOCIATION', 'FILM',
              'DIFFERENCE', 'REGION', 'EFFORT', 'PLAYER', 'EVERYONE', 'VILLAGE', 'ORGANISATION', 'WHATEVER', 'NEWS',
              'NICE', 'MODERN', 'CELL', 'CURRENT', 'LEGAL', 'FINALLY', 'MILE', 'MEANS', 'WHOM', 'TREATMENT', 'SOUND',
              'ABOVE', 'BEHAVIOUR', 'IDENTIFY', 'RESOURCE', 'DEFENCE', 'GARDEN', 'FLOOR', 'TECHNOLOGY', 'STYLE',
              'FEELING', 'SCIENCE', 'RELATE', 'DOUBT', 'PRODUCE', 'HORSE', 'COMPARE', 'SUFFER', 'USER', 'CHARACTER',
              'RISK', 'NORMAL', 'ARMY', 'FORGET', 'STATION', 'GLASS', 'PREVIOUS', 'RECENTLY', 'PUBLISH', 'SERIOUS',
              'VISIT', 'CAPITAL', 'SOCK', 'NOTE', 'SEASON', 'LISTEN', 'RESPONSIBILITY', 'SIGNIFICANT', 'DEAL', 'PRIME',
              'ECONOMY', 'FINISH', 'DUTY', 'FIGHT', 'TRAIN', 'MAINTAIN', 'ATTEMPT', 'SAVE', 'IMPROVE', 'AVOID',
              'TEENAGER', 'WONDER', 'TITLE', 'POST', 'HOTEL', 'ASPECT', 'INCREASE', 'SURNAME', 'INDUSTRIAL', 'EXPRESS',
              'SUMMER', 'DETERMINE', 'GENERALLY', 'DAUGHTER', 'EXIST', 'SHARE', 'NEARLY', 'SMILE', 'SORRY', 'SKILL',
              'TREAT', 'REMOVE', 'CONCERN', 'UNIVERSITY', 'DEAD', 'DISCUSSION', 'SPECIFIC', 'OUTSIDE', 'TOTAL', 'COST',
              'GIRLFRIEND', 'MARKET', 'OCCUR', 'RESEARCH', 'WONDERFUL', 'DIVISION', 'THROW', 'OFFICER', 'PROCEDURE',
              'FILL', 'KING', 'ASSUME', 'IMAGE', 'OBVIOUSLY', 'UNLESS', 'APPROPRIATE', 'MILITARY', 'PROPOSAL',
              'MENTION', 'CLIENT', 'SECTOR', 'DIRECTION', 'BASIC', 'INSTANCE', 'SIGN', 'ORIGINAL', 'REFLECT', 'AWARE',
              'PARDON', 'MEASURE', 'ATTITUDE', 'YOURSELF', 'COMMISSION', 'BEYOND', 'SEAT', 'PRESIDENT', 'ENCOURAGE',
              'ADDITION', 'GOAL', 'MISS', 'POPULAR', 'AFFAIR', 'TECHNIKUE', 'RESPECT', 'DROP', 'PROFESSIONAL',
              'VERSION', 'MAYBE', 'ABILITY', 'OPERATE', 'GOODS', 'CAMPAIGN', 'ADVICE', 'INSTITUTION', 'DISCOVER',
              'SURFACE', 'LIBRARY', 'PUPIL', 'REFUSE', 'PREVENT', 'TASTY', 'DARK', 'TEACH', 'MEMORY', 'CULTURE',
              'BLOOD', 'INSANE', 'VARIETY', 'DEPEND', 'BILL', 'COMPETITION', 'READY', 'ACCESS', 'STONE', 'USEFUL',
              'EXTENT', 'EMPLOYMENT', 'REGARD', 'APART', 'BESIDES', 'SHIT', 'TEXT', 'PARLIAMENT', 'RECENT', 'ARTICLE',
              'NOTICE', 'COMPLETE', 'DIRECT', 'IMMEDIATELY', 'COLLECTION', 'CARD', 'INTERESTING', 'CONSIDERABLE',
              'TELEVISION', 'AGENCY', 'CHECK', 'POSSIBILITY', 'SPECIES', 'SPEAKER', 'SECOND', 'LAUGH', 'WEIGHT',
              'RESPONSIBLE', 'DOCUMENT', 'SOLUTION', 'MEDICAL', 'BUDGET', 'RIVER', 'PUSH', 'TOMORROW', 'REKUIREMENT',
              'COLD', 'OPPOSITION', 'OPINION', 'DRUG', 'KUARTER', 'OPTION', 'WORTH', 'DEFINE', 'INFLUENCE', 'OCCASION',
              'SOFTWARE', 'EXCHANGE', 'LACK', 'CONCEPT', 'BLUE', 'STAR', 'RADIO', 'ARRANGEMENT', 'EXAMINE', 'BIRD',
              'BUSY', 'CHAIR', 'GREEN', 'BAND', 'FINGER', 'INDEPENDENT', 'EKUIPMENT', 'NORTH', 'MESSAGE', 'AFTERNOON',
              'FEAR', 'DRINK', 'FULLY', 'RACE', 'STRATEGY', 'EXTRA', 'SCENE', 'KITCHEN', 'ARISE', 'SPEECH', 'NETWORK',
              'PEACE', 'FAILURE', 'EMPLOYEE', 'AHEAD', 'SCALE', 'ATTEND', 'HARDLY', 'SHOULDER', 'OTHERWISE', 'RAILWAY',
              'SUPPLY', 'OWNER', 'ASSOCIATE', 'CORNER', 'PAST', 'MATCH', 'SPORT', 'BEAUTIFUL', 'HANG', 'MARRIAGE',
              'CIVIL', 'SENTENCE', 'CRIME', 'BALL', 'MARRY', 'WIND', 'TRUTH', 'PROTECT', 'DOGS', 'CATS', 'WITHOUT',
              'TOGETHER', 'SHEWAS', 'YOURENOT', 'WEARENOT', 'AMAN', 'EYES', 'SONS', 'BOYS', 'ARMS', 'IMNOT', 'YOUARE',
              'YOURE', 'YOUARENOT', 'ARENOT', 'ARENT', 'WEARE', 'WERE', 'WERENOT', 'HEIS', 'HEISNOT', 'HESNOT', 'ISNOT',
              'ISNT', 'SHEIS', 'SHES', 'SHEISNMOT', 'SHESNOT', 'ITIS', 'ITISNOT', 'ITSNOT', 'DONOT', 'DONT', 'CANNOT',
              'CANT', 'HAVENOT', 'HAVENT', 'WILLNOT', 'WONT', 'DIDNOT', 'DIDNT', 'HASNOT', 'HASNT', 'WASNOT', 'YOUWERE',
              'BECOME', 'NUMBER', 'MONEY', 'GOVERNMENT', 'HOWEVER', 'BECAUSE', 'SERVICE', 'IMPORTANT', 'ALTHOUGH',
              'REALLY', 'TIONAL', 'COUNTRY', 'THOUGH', 'ALMOST', 'KUESTION', 'SUBJECT', 'REMAIN', 'EDUCATION', 'RESULT',
              'REPORT', 'ALREADY', 'LITTLE', 'KEEP', 'TIONS', 'SCHOOL', 'IWAS', 'AUTHORITY', 'USUALLY', 'POLITICAL',
              'ANYTHING', 'WEWERE', 'NOTHING', 'TOWARDS', 'IDEA', 'ALSO', 'COMPANY', 'MANY', 'APPEAR', 'ALWAYS',
              'NATIONAL', 'HIMSELF', 'PERHAPS', 'PEOPLE', 'REASON', 'POLICY', 'RATHER', 'RIGHT', 'YEAH', 'REKUIRE',
              'PERIOD', 'WANT', 'AWAY', 'WHETHER', 'WEEK', 'INCLUDING', 'THINK', 'PROBABLY', 'EXAMPLE', 'COMMUNITY',
              'THEMIDDLE', 'ACTUALLY', 'SOCIETY', 'ENOUGH', 'EOFTHE', 'DRAW', 'BACK', 'ACCOUNT', 'WALK']
        if ubiraem!="Q":
            self.alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
            i=0
            while i<len(self.ss):
                self.ss[i]=self.ss[i].replace('KUA',"QUA").replace('KUI', "QUI").replace('KUE', "QUE").replace('KUO', "QUO").replace("J","I")
                i+=1
        else:
            self.alphabet = "ABCDEFGHIJKLMNOPRSTUVWXYZ"
        with open(file, 'r', encoding='utf-8') as file:
            self.text = file.read()
        self.slovar={}
        self.predpolozheniya={}
        self.razgadannoe=[]
        self.sss=[]#Список искомых шаблонов
        for a in self.ss:#Создаем из основного списка слов список искомых шаблонов sss
            t = str_cha(a)
            for b in t:
                if not b in self.sss:
                    self.sss.append(b)
        for a in self.alphabet:
            for b in self.alphabet:
                self.slovar[a + b] = "??"
    def razshifrovka(self):#Полная расшифровка текста найденным словарём
        retur = ""
        for a in range(0, len(self.text) - 1, 2):
            retur = retur + self.slovar[self.text[a:a + 2]]
        return retur
    def dobavit(self,d, s):#Сохраняем новую расшифрованную пару биграмм
        self.slovar[d] = s
        self.slovar[d[1] + d[0]] = s[1] + s[0]
        self.razgadannoe.append(d)
        if d[0] != d[1]:
            self.razgadannoe.append(d[1] + d[0])
        self.predpolozheniya[s] = d
        self.predpolozheniya[s[1] + s[0]] = d[1] + d[0]
    def RSP(self,l=1000):#Расшифровка со словарём предположений
        text=self.text
        text1 = self.razshifrovka()
        retur = ""
        for a in range(0, l, 2):
            if not text[a:a + 2] in self.razgadannoe and text[a:a + 2] in self.predpolozheniya:
                retur = retur + self.predpolozheniya[text[a:a + 2]]
            else:
                retur = retur + text1[a:a + 2]
        return retur
    def str_sch(self,a):  # строку в схему
        time0 = ""
        for b in range(0, len(a), 2):
            if a[b:b + 2] in self.predpolozheniya:
                time0 = time0 + a[b:b + 2]
            else:
                time0 = time0 + "??"
        return time0
    def usl(self,sch):#Предположительная дорасшифровка
        result = {}
        for a in range(0, len(sch), 2):
            if sch[a:a + 2] != "??":
                result[a] = self.predpolozheniya[sch[a:a + 2]]
        return result
    def process(self):
        usl=self.usl
        izm = True#флаг продолжения интеративного разгадывания
        text=self.text
        spisok = {}#Вспомогательный словарь для подсчёта встречаемости кандидатов
        mx = 0#Переменная для хранения максимальной встречаемости биграммы
        razg=self.razgadannoe#Уже расшифрованные биграммы
        sss = self.sss# список шаблонов слов для поиска в тексте
        str_sch=self.str_sch
        for i in range(0, len(text) - 3, 2):#Поиск самой частой двойной биграммы
            time = text[i:i + 4]
            if time in spisok:
                spisok[time] += 1
            elif time[0] == time[2] and time[1] == time[3]:
                spisok[time] = 1
        for i in spisok:
            if spisok[i] > mx:
                mx = spisok[i]
                Q = i
        self.dobavit(Q[:2], "TH")#Самой частой двойной биграмме ставим в соответствие TH
        while izm:
            izm = False # флаг ставим в False, пока не добавим новых расшифровок
            dellist = []  # список слов, расшифрованных полностью на данной итерации
            p = 0#Итератор
            while not izm and p < len(sss): #Проходим по всем шаблонам слов
                b = sss[p]#Текущий шаблон
                if not "?" in str_sch(b):#Если слово уже фактически разгадано, добавляем в разгаданное
                    dellist.append(b)
                elif "?" in str_sch(b):
                        krb = KR(b)#Узнаём, есть ли повторяющиеся или зеркальные биграммы в шаблоне
                        kzb = KZ(b)
                        time = str_sch(b)
                        if time.count("?") < len(b):#Если есть хотя бы одна расшифрованная биграмма в слове
                            yes = True
                            c = 0
                            while c < len(sss) and yes:#Проверяем, нет ли шаблонов с такой же схемой
                                scscd = sss[c]
                                time1 = str_sch(scscd)
                                if time in time1 and time1.index(time) % 2 == 0 and b != scscd[time1.index(time):time1.index(time) + len(b)] and krb == KR(scscd) and kzb == KZ(scscd):
                                    yes = False
                                c += 1
                            if yes:#Если схема уникальна, то ищем совпадения в тексте
                                spisok = {}
                                uslo = usl(time)
                                prov = list(range(0, len(b), 2))
                                for i in uslo:
                                    prov.remove(i)
                                for i in range(0, len(text) + 1 - len(b), 2):
                                    textiilenb = text[i:i + len(b)]
                                    if textiilenb in spisok:#Находим кандидатов, подходящих под схему
                                        spisok[textiilenb] += 1
                                    elif krb == KR(textiilenb) and kzb == KZ(textiilenb) and all(textiilenb[x:x + 2] == uslo[x] for x in uslo) and not any(textiilenb[x:x + 2] in razg for x in prov):
                                        spisok[textiilenb] = 1
                                if spisok:
                                    mx = 0
                                    mx2 = 0
                                    for i in spisok:
                                        if spisok[i] > mx:
                                            mx2 = mx
                                            mx = spisok[i]
                                            Q = i
                                        elif spisok[i] > mx2:
                                            mx2 = spisok[i]
                                    if mx > mx2 * 2:#Добавляем расшифровку, если найден очевидный выделяющийся кандидат
                                        izm = True
                                        for i in range(0, len(Q), 2):
                                            if not Q[i:i + 2] in razg: self.dobavit(Q[i:i + 2], b[i:i + 2])
                                        print("Добавлена расшифровка:" + Q + "->", b, ":", spisok.values())
                p += 1
            for a in dellist:#Удаляем расшифрованные шаблоны из перечня искомых шаблонов
                sss.remove(a)
        return len(self.slovar)#Возвращаем количество расшифрованных биграмм


