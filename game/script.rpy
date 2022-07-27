define she = Character("Вона", image="she")
define me = Character("Я", image="me")

define audio.romantic = audio.mixkit_a_love_affair_1050
define audio.sad = audio.pixabay_lofi_study_112191
define audio.tragic = audio.mixkit_silent_descent_614

define audio.door = audio.pixabay_dorm_door_opening_6038
define audio.sliding_door = audio.mixkit_lightweight_sliding_door_close_182
define audio.shower = audio.pixabay_shower_14461
define audio.bottle = audio.pixabay_bottle_open_14895
define audio.pour = audio.pixabay_pouring_coffee_6743
define audio.message = audio.mixkit_page_forward_single_chime_1107

image bg black = "#000"
image bg room = "rooms/bedroom 1.png"
image bg room after = "rooms/bedroom 2.png"
image bg balcony = "rooms/balcony.png"

image she dress sad = "lady/sad.png"
image she dress sceptical = "lady/sceptical.png"
image she dress smiling = "lady/smiling.png"
image she dress neutral = "lady/neutral.png"

image she robe crying = "lady/crying 2.png"
image she robe disappointed = "lady/disappointed 2.png"
image she robe sad = "lady/sad 2.png"
image she robe smiling = "lady/smiling 2.png"
image she robe surprised = "lady/surprised 2.png"
image she robe neutral = "lady/neutral 2.png"
image she robe sceptical = "lady/sceptical 2.png"
image side me neutral = "man/neutral.png"
image side me smiling = "man/smiling.png"
image side me serious = "man/serious.png"
image side me disturbed = "man/disturbed.png"

default itsOkToEscape = False
label start:

    scene bg black
    with fade
    play music romantic
    "Замок впізнав ключ-карту і радісно пропищав. Двері в номер відкрилися."
    play sound door
    "Номер був в суцільній темряві. Я намацав вимикач."
    scene bg room
    with fade

    "Швиденько оглянув номер - чи все прибрано і охайно, поки є ще час щоб покликати покоївку."
    "Люкс був в ідеальному стані."

    me neutral """
    Час прийняти душ.

    Я добре знаю, що вона це любить.

    Вона постійний клієнт.
    """
    play sound shower
    scene bg room
    with fade

    "Застібаючи свіжу сорочку, я відсунув скляні двері на балкон."
    play sound sliding_door
    scene bg balcony
    with fade
    "Зорі на небі, приглушені ліхтарями міста, ледь мерехтіли."
    
    me neutral "Огорожа занизька для мого комфорту."
    me serious "Oсобливо якщо врахувати, що це дев'ятий поверх!"
    
    "Пропищав замок і відкрилися вхідні двері."
    play sound door
    scene bg room
    with fade

    show she dress neutral
    with moveinleft

    me smiling "Добрий вечір!"
    she dress smiling "Добрий, добрий."
    "Вона причепила табличку не турбувати на ручку і закрила двері."
    hide she dress neutral
    with moveoutleft
    show she dress neutral
    with moveinleft

    "Вона одягнена в сукню, прикраси і з макіяжем - вона з вечірки."
    she dress smiling "Як справи?"
    me smiling "Чудово. Як вечірка?"
    she dress smiling "Світлана передавала привіт."
    me neutral "Давно з нею не зустрічався, сподіваюся в неї все добре?"
    she dress smiling "О так, вона була на вечірці з новим бойфрендом, тож твої послуги їй найближчим часом не знадобляться!"
    me smiling "Та невже?"
    she dress sceptical  "Геймер, постійно у віарі зависає."
    me serious "Її завжди тягнуло на пригоди."
    she dress neutral """
    Це точно.
    
    Вона розповіла, що в них навіть було побачення в віарі!
    """

    menu:
        "Я вважаю що:"
        "Нехай собі що хочуть то і роблять.":
            $ itsOkToEscape = True
            me neutral "Це їхні проблеми. Якщо вони нікому не заважають, нехай собі що хочуть то і роблять."
            me smiling """
            Ха ха. Треба з цією темою познайомитися ближче.

            Може мені не треба буди нікуди їздити?
            """
            she dress sceptical """
            Мені ніяково стає поруч з людьми, що сидять у віарі.
            
            Що вони роблять і що від них чекати не зрозуміло, начебто вони якісь навіжені.
            """
            me neutral "Якщо вони нікому не заважають, нехай собі що хочуть то і роблять."
            she dress sad "Напевно ти правий..."
        "Йому потрібна допомога.":
            $ itsOkToEscape = False
            me neutral """
            Світлана - як завжди. 
            
            Знайшла чегову жертву, яка потребує допомоги!
            """ 
            me serious "Хоч би не довелося потім її саму рятувати."
            she dress sceptical "Ти перебільшуєш, то лише ігри."
            me serious """
            Бігти від реальності не має сенсу. 
            
            Вона тебе наздожене. 
            
            Навіть у віарі.
            
            Люди, які цього не розуміють, вони як діти і потребують допомоги.
            """
            she dress sad "Напевно ти правий..."
    play music sad fadeout 2.0 fadein 2.0
    "Вона зітхає."
    she dress sad "Є вино?"
    play sound [bottle, pour]
    me neutral "Що тебе гризе?"
    she dress sad "Робота задовбала."
    she dress smiling """
    Раніше...

    Раніше я любила свою роботу.
    
    В нас був малий коллектив. Ми працювали зарди ідеї, не зважаючи чи принесе ця ідея гроші чи ні.
    """
    she dress sad "А тепер я лише сиджу на мітингах і папірці перекладаю..."
    she dress neutral "Спочатку успіх приніс нам гроші."
    she dress sad """
    Не встигла і блимнути - все стало обертатися лише навколо них.

    Ти напевно не знаєш, але в мене був чоловік. Ми разом створили цю компанію.
    
    Але він загинув.
    """
    me disturbed "Він був, напевно, дуже гарною людиною."
    she dress smiling "О так! Він був найкращім!"
    she dress neutral "Звідки ти знаєш?"
    me neutral "Бо я тепер розумію, чтому ти відмовляєш усім чоловікам!"
    me smiling "Вони не дотягують до його рівня!"
    she dress sceptical """
    Не знаю.
    
    Я вже не дівчинка.
    
    Відносини то складно, на це потрібно багато часу...
    """
    she dress sad "Я не бачу чоловіків, на яких його варто витрачати."
    me neutral "Ну на мене ти витрачаєш не тільки час, та ще й гроші!"
    she dress sceptical "То я, навпаки, бережу свій час."

    "Вона ініціює секс"
    hide she dress neutral
    with moveoutright

    scene bg black
    with fade
    scene bg room after
    with fade
    play sound shower
    "Вона повертається з душу."
    show she robe neutral
    with moveinleft

    "Ви сидите в обіймах на дивані."
    me neutral "Можна задати особисте питання?"
    she robe surprised """
    Ти якийсь дивний. 
    
    Ну питай...
    """
    me serious "Навіщо я тобі?"
    she sceptical """
    Ти, часом, не захворів? 
    
    З такими питанями ти багато грошей не заробиш!
    """
    me serious """
    До біса гроші. 

    Ззовні ти завжди весела, впевнена і вправна. 
    
    Все можеш. 
    """
    
    she robe disappointed "..."

    me neutral """
    Алеж я знаю що ти насправді нещасна.
    
    І я лише тимчасова розвага. 
    """
    she robe sad "До чого ти ведеш?"
    me neutral "Я не зможу замінити твого чоловіка."
    she robe disappointed "Твоя справа бути зручним."
    hide she
    with moveoutright
    "Вона вийшла на балкон."
    play sound sliding_door
    "Раптово задзеленчав її телефон."
    play sound message
    "Я взяв його і пішов з ним на балкон."
    play sound sliding_door
    scene bg balcony
    with fade
    show she robe disappointed
    "Телефон був старий, навіть без сенсорногу екрану."
    me neutral "Вибач..."
    "Я віддав їй телефон."
    she robe sad "Пробачений."
    "Вона мовчки переглянула повідомлення на телефоні."
    show she robe disappointed
    me neutral "Чому ти не придбаєш новий?"
    "Вона поклала телефон на долоні і болісно посміхнулась."
    she robe smiling "Цей телефон - його подарунок."
    she robe sad """
    На ньму багато фото і відео де ми разом...

    Треба їх скачати, десь має бути кабель...

    В його кімнаті...
    """

    she robe crying "Бо зазвичай він цим займався..."

    "Я її обійняв."

    play music tragic fadeout 2.0 fadein 2.0
    she robe sad """
    Правду ти казав... 
    
    Я біжу від реальності...
    """
    
    "Вона підішла до краю балкона"
    she robe disappointed "Можна покінчити з цим тут і зараз..."
    "Вона перехилилася через огорожу"
    "Схопивши її сзаду ти відягнув її від огорожі."
    "Вона не чинила опору."

    menu:
        "Ти кажеш:"
        "Я не хочу сісти в тюрму":
            me serious "Я не хочу сісти в тюрму, це не входить в мій бізнес план!"
            if itsOkToEscape:
                she disappointed "Будь ласка. Дозволь мені це зробити."
                "Ти її відпускаєш."
                show she robe smiling
                jump free
            else:
                stop music fadeout 2.0
                she robe disappointed "Ти ж казав, що бігати від реальності не має сенсу!"
                she robe sad "Хоча, що я кажу."
                she robe neutral """
                Вибач, то був жарт. 
                
                На сьгодні досить."""
                jump fail
        "Не треба здаватися!":
            me disturbed """
            Так, що ти таке кажеш?! 
            
            Я не дозволю тобі це зробити!
            """
            if itsOkToEscape:
                stop music fadeout 2.0
                she robe disappointed "Тиж казав що кожна людина має право жити як хоче!"
                she robe sad "Хоча, що я кажу."
                she robe neutral """
                Вибач, то був жарт. 
                
                На сьгодні досить."""
                jump fail
            else:
                she robe disappointed "Дякую..."
                she robe smiling "Будь ласка, залишся зі мною до ранку."
                me smiling "Звичайно."
                jump sleep

    return

label fail:
    scene bg black
    with fade
    "З тобою вона більше не зв'язувалася." 
    "Через декілька років вона таки вчинила самогубство."
    return

label free:
    scene bg black
    with fade
    "Ти одразу викликав поліцю і швидку."
    "Вона померла."
    "Ти був підозрюванним у вбивстві, але зясувалося, що вона ввімкнула запис на телефоні, і твоє алібі було підтверджено."
    return

label sleep:
    scene bg black
    with fade
    "Вона й далі продовжувала користуватися твоїми послугами."
    "Ви білше не поверталися до цієї теми."
    return
