﻿define she = Character("Вона", image="she")
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
image she robe disappointed = "lady/disappointed 2"
image she robe sad = "lady/sad 2.png"
image she robe smiling = "lady/smiling 2.png"
image she robe surprised = "lady/surprised 2.png"
image she robe neutral = "lady/neutral 2.png"
image side me neutral = "tmp.png"
image side me smiling = "tmp.png"
image side me serious = "tmp.png"

default itsOkToEscape = False
label start:

    scene bg black
    with fade
    play music romantic
    "Замок впізнав ключ-карту і радісно пропищав. Двері в номер відкрилися"
    play sound door
    "Номер був в суцільній темряві. Я намацав вимикач."
    scene bg room
    with fade

    "Швиденько оглянув номер - чи все прибрано і охайно, поки є ще час щоб покликати покоївку."
    "Люкс був в ідеальному стані"

    me neutral "Час прийняти душ. Я добре знаю що вона це любить. Вона постійний клієнт."
    play sound shower
    scene bg room
    with fade

    "Застібаючи свіжу сорочку я відсунув скляні двері на балкон."
    play sound sliding_door
    scene bg balcony
    with fade
    "Зорі на небі, приглушені ліхтарями міста, ледь мерехтіли."
    me neutral "Огорожа за низька для мого комфорту, особливо якщо врахувати що це дев'ятий поверх!"
    "Пропищав замок і відкрилися вхідні двері."
    play sound door
    scene bg room
    with fade

    show she dress neutral
    with moveinleft

    me neutral "Добрий вечір!"
    she "Добрий, добрий"
    "Вона причепила табличку не турбувати на ручку і закрила двері"
    "Вона одягнена в сукню, прикраси і з макіяжем - вона з вечірки"
    she "Як справи?"
    me neutral "Чудово. Як вечірка?"
    she "Світлана передавала привіт."
    me "Давно з нею не зустрічався, сподіваюся в неї все добре?"
    she "О так, вона була на вечірці з новим бойфрендом, то твої послуги їй найближчим часом не знадобляться!"
    me "Та невже"
    she "Геймер, постійно у віар зависає."
    me "Її завжди тягнуло на пригоди."
    she "Це точно. Вона розповіла що в них навіть було побачення в віарі!"
    menu:
        "Я вважаю що:"
        "Це їхні проблеми. Якщо вони нікому не заважають, нехай собі що хочуть то і роблять":
            $ itsOkToEscape = True
            me smiling "Ха ха. Треба з цією темою познайомитися по ближче."
            me "Може мені не треба буди нікуди їздити?"
            she dress sceptical "Мені ніяково стає поруч з людьми що сидять у віарі. Що вони роблять і що від них чекати не зрозуміло, начебто вони якісь навіжені."
            me neutral "Якщо вони нікому не заважають, нехай собі що хочуть то і роблять"
            she dress sad "Напевно ти правий..."
        "Йому потрібна допомога. Він хворий, навіть якщо сам цього не усвідомлює":
            $ itsOkToEscape = False
            me neutral "Світлана як завжди. Знайшла чегову жертву яка потребує допомоги!" 
            me "Хоч би не довелося потім її саму рятувати."
            she dress sceptical "Ти перебільшуєш, то лише ігри."
            me  neutral "Бігти від реальності не має сенсу. Вона тебе наздожене. Навіть у віарі."
            me "Люди які цього не розуміють, вони як діти, і потребують допомоги."
            she dress sad "Напевно ти правий..."
    play music sad fadeout 2.0 fadein 2.0
    "Вона зітхає."
    she "Є вино?"
    play sound [bottle, pour]
    me neutral "Що тебе гризе?"
    she dress neutral """
    Робота задовбала. Раніше... Раніше я любила свою роботу.

    В нас був малий коллектив. Ми працювали зарди ідеї, не зважаючи чи принесе ця ідея гроші чи ні.

    А тепер я лише сиджу на мітингах і папірці перекладаю... Спочатку успіх приніс нам гроші. 

    Не встигла і блимнути - все стало обертатися лише навколо них.
        
    Ти напевно не знаєш, але в мене був чоловік ми разом створили цю компанію. Але він загинув.
    """
    me "Він був, напевно дуже гарною людиною"
    she dress smiling"О так! Він був найкращім!"
    she "Звідки ти знаєш?"
    me "Бо я тепер розумію чтому ти відмовляєшь усім чоловікам! Вони не дотягують до його рівня!"
    she dress sceptical "Не знаю. Я вже не дівчинка. Відносини то складно, на це потрібно багато часу... Я не бачу чоловіків на яких його варто витрачати."
    me "Ну на мене ти витрачаєшь не тільки час, та ще й гроші!"
    she "То я навпаки бережу свій час."

    "Вона ініціює секс"
    scene bg black
    with fade
    scene bg room after
    with fade
    play sound shower
    "Вона повертаэться з душу"
    show she robe neutral
    with moveinleft

    "Ви сидите в обіймах на дивані"
    me "Можна задати особисте питання?"
    she robe surprised "Ти якийсь дивний. Ну питай"
    me "Нащо я тобі?"
    she "Ти часом не захворів? З такими питанями ти багато грошей не заробиш!"
    me """До біса гроші. На зовні ти завжди веслеа, впевнена і вправна. Все можеш. Алеж я знаю що ти насправді нещасна.
        І я лише тимчасова розвага. """
    she robe sad "До чого ти ведеш"
    me "Я не зможу замінити твого чоловіка"
    she "Твоя справа бути зручним"
    hide she
    with moveoutright
    "Вона вийшла на балкон"
    play sound sliding_door
    "Раптово задзеленчав її телефон"
    play sound message
    "Я взяв його і пішов з ним на балкон"
    play sound sliding_door
    scene bg balcony
    with fade
    show she robe neutral
    "Телефон був старий, навіть без сенсорногу єкрану"
    me "Вибач"
    "Я віддав їй телефон."
    she "Пробачений."
    "Вона мовчки переглянула повідомлення на телефоні"
    me "Чому ти не придбаєшь новий?"
    "Вона поклала телефон на долонь і болісно посміхнулась."
    show she robe sad
    she """
    Цей телефон його подарунок.

    На ньму багато фото і відео де ми разом...

    Треба їх скачати, десь має бути кабель...

    В його кімнаті...
    """

    she robe crying "Бо зазвичай він цим займався..."

    "Ти її обійняв"

    play music tragic fadeout 2.0 fadein 2.0
    she robe sad "Правду ти казав... Я біжу від реальності..."
    "Вона підішла до краю балкона"
    she "Можна покінчити з цим тут і зараз..."
    "Вона перехилилася через огорожу"
    "Схопивши її сзаду ти відягнув її від огорожі. Вона не чинила опіру."

    menu:
        "Ти кажеш:"
        "Я не хочу сісти в тюрму, це не входить в мій бізнес план":
            me "Я не хочу сісти в тюрму, це не входить в мій бізнес план"
            if itsOkToEscape:
                she "Будь ласка. Дозволь мені це зробити."
                "Ти її відпускаєш."
                show she robe smiling
                jump free
            else:
                stop music fadeout 2.0
                she robe disappointed "Тиж казав що бігати від реальності не має сенсу!"
                she "Хоча, що я кажу. Вибач, то був жарт. На сьгодні досить."
                jump fail
        "Не треба здаватися!":
            me "Так, що ти таке кажешь! Я не дозволю тобі це зробити!"
            if itsOkToEscape:
                stop music fadeout 2.0
                she robe disappointed "Тиж казав що кожна людина має право жити я хоче?"
                she "Хоча, що я кажу. Вибач, то був жарт. На сьгодні досить."
                jump fail
            else:
                she robe smiling "Дякую... Будьласка залишься зі мною до ранку"
                me "Звичайно"
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
    "Ти був підозрюванним у вбивстві, але зясувалося що вона ввімкнула запис на телефоні, і твоє алібі було підтверджено."
    return

label sleep:
    scene bg black
    with fade
    "Вона й далі продовжувала користуватися твоїми послугами."
    "Ви білше не поверталися до цієї теми."
    return
   


