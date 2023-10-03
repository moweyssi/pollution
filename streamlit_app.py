import streamlit as st
from PIL import Image
img=Image.open("logo.png")
st.set_page_config(page_title="Anna & Max", page_icon=img)
hide_decoration_bar_style = '''
    <style>
        header {visibility: hidden;}
    </style>
'''
st.markdown(hide_decoration_bar_style, unsafe_allow_html=True)
language = st.radio(
    "Choose your language",
    ('CZ','ENG'), horizontal=True,label_visibility="hidden")
st.image("info.png")

#with st.expander(":rewd[RSVP Form]"):
#    st.markdown(
#        """
#        <iframe src="https://docs.google.com/forms/d/e/1FAIpQLSeNEAVH0J3Fob8uPX2qJz3puVX5HhE_LTs2CqG5mkcmMSsrOg/viewform?embedded=true", width=100%, height=2200></iframe>
#        """,
#        unsafe_allow_html=True
#
#    )

if language == "ENG":
    with st.expander("**I'm driving**"):
        """
        If you're driving and using Google Maps, enter this point: https://goo.gl/maps/KJ2JbQiQmp4hMbNx5
        The contact person for parking is Františka at **+420 722 490 795**. We're sharing parking with another wedding. Please park in a way that allows other cars to fit next to you. The second wedding is taking place at the brewery. Head towards the castle marked with path  A + M.
        Please fill up the cars as much as possible. We aim to have as few cars as possible.
        """
    with st.expander("**I have space in my car**"):
        """
        Please fill in this [spreadsheet](https://docs.google.com/spreadsheets/d/18m0ynbyI23b6Ac3nsWZO7NpxU6eVmFNSXFxOKpWsWLA/edit?usp=sharing):
        """
        st.markdown("""
        <iframe width=680 height=600 src="https://docs.google.com/spreadsheets/d/18m0ynbyI23b6Ac3nsWZO7NpxU6eVmFNSXFxOKpWsWLA/edit?usp=sharing?widget=true&amp;headers=false""></iframe>
        """,unsafe_allow_html=True)
    with st.expander("**I am taking the train**"):
        """
        If you're taking the train, visit https://www.cd.cz/ and search for Kařez to find your connection. It's about a 30-minute drive from Kařez to Chříč.
        If you don't have arranged transportation from Kařez and need a ride, contact Františka at **+420 722 490 795** when you're boarding the train and let her know when you'll arrive and how many of you there are. We'll arrange for someone to pick you up.
        Please communicate with Františka through WhatsApp as there's poor signal on-site.
        """
    with st.expander("**When Should I Arrive**"):
        """
         - If you're arriving on Saturday, please come between 12:30 and 13:30. Campers, please arrive earlier. 
         - Light refreshments will be waiting for you on-site. 
         - If you want to arrive earlier or even on Friday, contact Fred at **+420 704 773 391** or Františka at **+420 722 490 795**. Please use WhatsApp or text messages. Signal is weak in Chříč.
        """
    with st.expander("**Gifts**"):
        """
        Due to our scattered possessions across various European lands and beyond, we do not wish for traditional material gifts. However, if you wish to support our newly formed unity, we would gratefully accept a financial contribution towards our journey into the world, which will take place in the winter months. Your assistance will help us explore exotic destinations and build shared memories that will fuel our peaceful marriage during times of conflict and challenge.
        """
        col1, col2, col3 = st.columns(3)
        col1.code(
            "UK bank account\nName: Maxim Oweyssi\nAccount number:\n04817931\nSort code: 04-00-75")
        col2.image("Revolut.jpg", width=220)
        col3.code(
            "EU bank account\nName: Maxim Oweyssi\nIBAN:\nGB71REVO 00997031615948\nBIC: REVOGB21")
    with st.expander("**What to Bring**"):
        """
         - If you're staying at the school or the chateau, bring a sleeping bag and sleeping mat. 
         - Don't forget headlamps, a water bottle, and a power bank.
         - Flat-soled shoes
         - Good mood 
         - If it's raining, bring an umbrella

        """
    with st.expander("**Can I Help in Any Way?**"):
        """
         - Sunday: If you have the capacity and time, we would appreciate help with cleaning on Sunday. 
         - Food: If you want to bake/cook something, it's welcome. There's no heating available on-site, nor a fridge (there's a cool room at around 15 degrees Celsius where food can be stored). 
         - On Sunday, we will need people to oversee the cleanup and handing over the local school "Pivoňka" 

        """
    with st.expander("**I will bring a tent**"):
        """
         - You can set up your tent on the meadow behind the castle.
         - You can find the sleeping meadow on Google Maps here: https://goo.gl/maps/bN56ENPyCsYYqcTh7 
         - There won't be electricity or water on the meadow, so bring power banks and water bottles.

        """
    with st.expander("**Staying at the School**"):
        """
        The local school "Pivoňka" has provided us with its premises, despite ongoing preparations for the upcoming school year that starts on Monday after the wedding. It's a lovely little community school, and we're very grateful for being able to spend the night there. While there are numerous attractions, please treat the space with respect, don't take toys from children, and clean up after yourselves.
        Bring a sleeping bag, sleeping mat, and your own cup/mug.

        """
    with st.expander("**Programme**"):
        """
         - **14:00** Ceremony 
         - **14:30** Gratulations for those who are not staying overnight
         - **15:00** First dance 
         - **15:30** Party till the morning
         - **17:00** Anna and Max have a coffee with family

        During the party, there will be speeches, throwing of the bouquet, etc. 

        It's possible, even likely, that parts of the program will be delayed, as is common at weddings.
        """
    with st.expander("**What to Wear**"):
        """
         - The party will be themed as a sparkling forest ball. What does this even mean?
         - Rule nr 1: Dress comfortably stay warm, and don't wear anything that will hinder dancing.
         - If you have the time and inclination to dress up, wear something that sparkles. It could be shoes, a piece of jewellery, a clothing item, or a hair accessory. Leave high heels at home. The terrain is not suitable.

        """
    with st.expander("**Food**"):
        """
        The selection will be diverse, and everyone who identifies as a "just-something-eater" will find something to eat, as well as thosewho identify themselves as "omnivores". Food will be served after the ceremony, i.e. Around 15.00 in a buffet format (you serve yourself whatever you want). If you feel like contributing to the food selection, we will be happy, just please keep in mind that there is no refrigerator or chance to warm the food. We can store food in a room at about 15 degrees.        """


    st.image("footer.png")
    st.subheader("Dearest Friends,")
    """
    Please allow us to share further details of our highly-anticipated wedding.
    We hope the following points will give you an idea of the festivities on that glorious day: The date to put down in your calendar is **Saturday, September 2, 2023**. Please join us at the beautiful Chříč chateau. The address is **Chříč 1**. The ceremony will commence at **2:00 PM** but we ask you to arrive between 12:30 PM and 1:30 PM. Light refreshments will be provided upon your arrival. For those camping enthusiasts, we suggest aiming for the
    start of the arrival window, so you can enjoy the rest of the party without logistical distractions.
    """
    st.image("spacer.png")

    st.subheader("Festivities")
    """
    Dear friends, on the same day, another wedding will also take place in the village. Therefore, please follow the **navigation marked with our initials A + M**. Additionally, the traditional Chříč Rally will also be happening in the village. Yes, this is not a joke. We perceive it as a positive and sincere beginning to our married life, one filled with surprises and challenges. In case the traditional automotive festivities hinder any of the many roads to Chříč, we will keep you informed.
    """
    st.image("spacer.png")

    st.subheader("Party")
    """
    The party will commence with a toast at 3:30 PM. This will also get the ball on the castle terrace rolling. To harmonise with the atmosphere, we invite you to **bring something sparkly**. It can be jewellery, a piece of clothing, shoes, or anything else. **Glitter has no limits.**
    We kindly ask all guests to **avoid clumsy footwear** that could lead to unwanted dance mishaps and incidents in the natural landscape. Instead, we recommend stylish and comfortable shoes so you can enjoy the festivities carefree.
    """
    st.image("spacer.png")

    st.subheader("Gifts")
    """

    Due to our scattered possessions across various European lands and beyond, we do not wish for traditional material gifts. However, if you wish to support our newly formed unity, we would gratefully accept a financial contribution towards our journey into the world, which will take place in the winter months. Your assistance will help us explore exotic destinations and build shared memories that will fuel our peaceful marriage during times of conflict and challenge.
    """
    col1, col2, col3 = st.columns(3)
    col1.code(
        "UK bank account\nName: Maxim Oweyssi\nAccount number:\n04817931\nSort code: 04-00-75")
    col2.image("Revolut.jpg", width=220)
    col3.code(
        "EU bank account\nName: Maxim Oweyssi\nIBAN:\nGB71REVO 00997031615948\nBIC: REVOGB21")
    st.image("spacer.png")

    st.subheader("Overnight:")
    """
    The first option is to camp. Space will be allocated for setting up tents on-site. If you prefer the comfort of a roof over your head, you can sleep in a local school, please bring a sleeping mat and a sleeping bag for this option. You will share space with other people. Just 8 minutes away by car, are two camps with cabins. There are beds and bedding. Each cabin accommodates 4 people. We have approximately 50 spots reserved, so please let us know, and we will secure a spot for you. For those who prefer the comfort of a hotel, we will
    gladly provide you with recommendations. However, this will have to be at your own expense.

    Dearest friends, your presence is the most precious gift to us on this legendary day.

    With warmth, love, and excitement,
    """
    st.image("signature.png")
    col1,col2,col3,col5,col5,col6,col7 = st.columns(7)
    with col1:
        st.button("balloon", on_click=st.balloons)
    with col7:
        st.button("snow", on_click=st.snow)
else:
    with st.expander("**Jedu autem**"):
        """
         Pokud jedete autem a používáte Google Mapy, zadejte tenhle bod: https://goo.gl/maps/KJ2JbQiQmp4hMbNx5

        Pokud používáte mapy.cz, tak zde:
        https://en.mapy.cz/s/jegadugovu

        Kontaktní osoba pro parkování je Františka  **+ 420 722 490 795**.
        Parkování sdílíme spolu s druhou svatbou. Prosím parkujte tak, aby se vedle vás vešla i další auta. Druhá svatba se koná v pivovaru. Vy se vydejte směrem na zámek označenou cestou A + M.

        Prosím naplňte auta tak, aby vás jelo co nejvíce a aut bylo co nejméně. 

        """
    with st.expander("**Mám místo v aute**"):
        """
        Prosíme vyplňte [tabulku](https://docs.google.com/spreadsheets/d/18m0ynbyI23b6Ac3nsWZO7NpxU6eVmFNSXFxOKpWsWLA/edit?usp=sharing):
        """
        st.markdown("""
        <iframe width=680 height=600 src="https://docs.google.com/spreadsheets/d/18m0ynbyI23b6Ac3nsWZO7NpxU6eVmFNSXFxOKpWsWLA/edit?usp=sharing?widget=true&amp;headers=false""></iframe>
        """,unsafe_allow_html=True)
    with st.expander("**Jedu vlakem**"):
        """
        Pokud vyrážíte vlakem, zadejte si na https://www.cd.cz/ Kařez a najděte si spoj. Z Kařezu se jede do Chříče cca 30 minut autem. 

        Pokud nemáte domluvený odvoz z Kařezu a potřebujete svézt, ozvěte se Františce **+ 420 722 490 795** až budete nastupovat do vlaku a sdělte kdy dorazíte a kolik vás je. Zařídíme, aby vás někdo vyzvedl. 

        S Františkou prosím komunikujte přes whatsapp. Na místě je horší signál.

        """
    with st.expander("**Kdy mám přijet**"):
        """
        Pokud přijíždíte v sobotu, prosím **přijďte mezi 12.30 a 13.30**. Stanaři přijeďte dříve. Na místě vás bude čekat drobné občerstvení.
        Pokud chcete přijet dřív, případně už v pátek, ozvěte se Fredovi  **+ 420 704 773 391** nebo Františce **+ 420 722 490 795**.
        Prosím ozývejte se přes whatsapp či SMSkou.
        """
    with st.expander("**Dary**"):
        """
        Vzhledem k našim majetkovým dispozicím rozmístěným po různých evropských zemích (i za jejich hranicemi), si nepřejeme předměty. Avšak, pokud byste měli tu laskavost a chtěli nás podpořit, přijmeme s pokorou a vděkem finanční příspěvek na naší cestu do světa, která se uskuteční v zimních měsících. Tím nám pomůžete objevovat cizí kraje a budovat společné vzpomínky, které nám v období konfliktu a jiných těžkých chvil dodají energii na pohodové manželství.
        """
        
        col1, col2, col3 = st.columns(3)
        col1.code("2111945559/2700")
        col2.image("QR_code.jpg", width=220)

    with st.expander("**Co si mám vzít s sebou**"):
        """
         - Pokud spíte ve škole či na zámku, tak spacák a karimatku. Nezampomeňte čelovky, lahev na vodu a powerbanku. 
         - Boty bez podpadku
         - Dobrou náladu
         - Pokud bude pršet, tak deštník 
        """
    with st.expander("**Můžu nějak pomoci?**"):
        """
         - Neděle: Pokud budete mít kapacitu a čas, budeme rádi za pomoc s úklidem v neděli. 
         - Jídlo: Pokud chcete něco upéct/uvařit, budeme rádi. Na místě není možnost ohřívání, ani lednice (bude tam chladná místnost o cca 15 stupních, kde lze skladovat jídlo)
         - V neděli bude třeba dohlédnout na uklizení a předání místní školy Pivoňka.
        """
    with st.expander("**Beru si stan**"):
        """
         - Stan si postavíte na louce za zámkem. 
         - Tady najdete louku na spaní na Googlemaps: https://goo.gl/maps/bN56ENPyCsYYqcTh7
         - Tady je louka pro mapisty.cz  https://en.mapy.cz/s/habehesura
         - Na louku nebude dotažená elektřina, ani voda tzn powerbanky a lahve na vodu s sebou. 
        """
    with st.expander("**Spím ve škole**"):
        """
        Místní škola Pivoňka nám poskytla své prostory a to i přesto, že momentálně probíhají přípravy na další školní rok, který začíná v pondělí po svatbě. Je to milá malá komunitní školička a my jsme velice vděční za to, že tam můžeme strávit noc. Ačkoliv je tam milion atrakcí, chovejte se prosím s respektem, neberte dětem hračky a ukliďte po sobě. 

        S sebou si vemte spacák, karimatku a vlastní hrníček. 
        """
    with st.expander("**Harmonogram**"):
        """
         - **14.00** Obřad
         - **14.30** Gratulace
         - **15.00** První tanec
         - **15.30** párty
         - **17.00** Anna a Max si dají kafe s rodinou

        Během párty budou také proslovy, házení kytkou atd…
        
        Je možné až pravděpodobné, že se některá část programu zpozdí, jak už to na svatbách bývá že ano…
        """
    with st.expander("**Co na sebe**"):
        """
         - Párty se bude konat ve znamení lesního třpytivého bálu. Co s tím? 
         - Oblečte se tak, abyste se cítili dobře, aby vám bylo teplo, abyste na sobě neměli nic, co vám bude bránit v tanci
         - Pokud máte chuť a čas se vystrojit, vemte si na sebe něco co se třpytí. Mohou to být boty, kus šperku, kus oděvu či ozdoba do vlasů.
         - Podpadky nechte doma. Není na to vhodný terén
        """
    with st.expander("**Jídlo**"):
        """
        Jídlo bude různorodé a každý, kdo se identitifikuje jako „jen-něco-žravec“ si tam najde své, stejně tak jako ti, kteří na sebe pohlíží jako „vše-žravci“. Jídlo bude servírováno po obřadu tzn. Cca v 15.00 formou švédských stolů. Pokud máte chuť něčím přispět, budeme rádi, jen prosím myslete na to, že na místě není lednice ani šance ohřátí. Jídlo můžeme skladovat v místnosti o zhruba 15 stupních.
        """



    st.image("footer.png")
    st.subheader("Nejmilejší rodino a přátelé,")
    """
    Dovolte nám, abychom vás s radostí pozvali na naší avizovanou zámeckou svatbu. Doufáme, že vám následující body poskytnou představu o dění onoho slavnostního dne. Svatba se uskuteční v sobotu **2. září 2023** na krásném Chříčském zámku, který najdete na adrese **Chříč 1**. Začátek obřadu je ve **14.00**. Prosím přijeďte mezi 12.30 a 13.30. Pro stanaře doporučujeme mířit na začátek příjezdového okna.
    """
    st.image("spacer.png")

    st.subheader("Srandy kopec")
    """
    Drazí přátelé, ve stejný den se ve vesnici koná i další svatba. Proto prosím sledujte **navigační cedule** s iniciály A + M. Kromě druhé svatby se ve vesnici bude také konat tradiční chříčské rally. Ano, je to tak. Vnímáme to jako pozitivní a upřímný začátek manželského soužití, které bude jistě plné překvapení a výzev. V případě, že by tradiční automobilové slavnosti měly blokovat jednu z mnoha cest do Chříče, dáme vědět.    """
    st.image("spacer.png")

    st.subheader("Bál na zámecké terase")
    """
    Párty začíná přípitkem v 15.30. Poté vás zveme na bál na zámecké terase. Abyste se dokonale sladili s atmosférou, vyzýváme vás, abyste si přinesli **něco, co se třpytí**. Může to být šperk, kus oděvu, střevíce bez podpatku či něco jiného. Kreativitě se meze nekladou. Také prosíme všechny hosty, aby se vyhnuli **neohrabaným botám**, které by mohly způsobit nechtěné taneční eskapády. Místo toho doporučujeme stylovou a pohodlnou obuv, abyste se mohli bezstarostně bavit v exotickém chříském terénu.
    """
    st.image("spacer.png")

    st.subheader("Dary")
    """
    Vzhledem k našim majetkovým dispozicím rozmístěným po různých evropských zemích (i za jejich hranicemi), si nepřejeme předměty. Avšak, pokud byste měli tu laskavost a chtěli nás podpořit, přijmeme s pokorou a vděkem finanční příspěvek na naší cestu do světa, která se uskuteční v zimních měsících. Tím nám pomůžete objevovat cizí kraje a budovat společné vzpomínky, které nám v období konfliktu a jiných těžkých chvil dodají energii na pohodové manželství. V případě, že byste se chtěli podílet na přípravách měsíce/týdny/dny předtím, prosím ozvěte se. Pomoc bude potřeba s dekoracemi, jídlem a dalšími položkami.    """
    
    col1, col2, col3 = st.columns(3)
    col1.code("2111945559/2700")
    col2.image("QR_code.jpg", width=220)

    st.image("spacer.png")

    st.subheader("Nocleh:")
    """
    Na místě bude pro Vás a vaše blízké vyhrazeno místo pro postavení stanů. Pokud upřednostňujete střechu nad hlavou, je tu možnost spaní v hromadné místnosti místní školy Pivoňka. V tom případě vám stačí spacák a karimatka. Vzdálené pouhých 8 minut jízdy se nachází dva kempy s chatičkami. Jsou vybaveny postelemi a povlečením. Každá chatička je určena pro 4 osoby. Máme zamluveno cca 50 míst. V případě zájmu nám dejte vědět a zamluvíme vám místo. Pro ty, kteří preferují komfort hotelu, rádi poskytneme tipy, kde se ubytovat. Avšak náklady na hotel budou bohužel na vás.
    Drazí svatebčané, vaše přítomnost je pro nás tím nejcennějším darem tohoto legendárního dne.

    Těšíme se!

    S úctou, láskou a nadšením,
    """

    st.image("signature.png")

    col1,col2,col3,col5,col5,col6,col7 = st.columns(7)
    with col1:
        st.button("balónky", on_click=st.balloons)
    with col7:
        st.button("sníh", on_click=st.snow)



