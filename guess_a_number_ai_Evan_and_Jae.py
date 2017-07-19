#Guess-A-Number AI
#
#Evan and Jae
#September 14,2016

#Imort Modules
import math





def startscreen():
    print("""
 __   __  _______  ______    _______  __   __  _______  _______    _______  __   __  _______  _______  _______ 
|  | |  ||   _   ||    _ |  |   _   ||  |_|  ||  _    ||       |  |       ||  | |  ||       ||       ||       |
|  |_|  ||  |_|  ||   | ||  |  |_|  ||       || |_|   ||    ___|  |    ___||  | |  ||    ___||  _____||  _____|
|       ||       ||   |_||_ |       ||       ||       ||   |___   |   | __ |  |_|  ||   |___ | |_____ | |_____ 
|       ||       ||    __  ||       ||       ||  _   | |    ___|  |   ||  ||       ||    ___||_____  ||_____  |
|   _   ||   _   ||   |  | ||   _   || ||_|| || |_|   ||   |___   |   |_| ||       ||   |___  _____| | _____| |
|__| |__||__| |__||___|  |_||__| |__||_|   |_||_______||_______|  |_______||_______||_______||_______||_______|""")
    print("""d+ooydmmNmds:/ydyo/++s:---+s+:::/+++oo+/:/::+///-/soo+/+:-/--:/-:/:////+o/+/+++/:/++oo/:///:+yyo+s/o
dd+/::+oymmmo:ohyhhNmNo.-:////++//-:////++/::::/-/yy++/++:::/./:::++++//+/++/++o+++:+oo/+/://+oos+:o
dddddss+o/:/--+//yyy/so----::-:/:-:::/::/+++o/---:+/:////:-----:/o+++:/+////:::/+oo+oso/ysss+/:/++oo
ddddmmmds+/ossyyssssoo:.--.-:::------:-:/+++o/:::///+////o+/:--/+o+://:::::////+o+ss+sys+:/o++////:/
ddddyy+oydmmmmNNNNNNyyh-...:/+++://+/:::--:/:-/++osssso++osy+:::/+/:+s/-/:/++o+++oososso/+-:+++o+++o
yoss:/ydmmmmmmmNNNNshNN/.--:/oso/+ydy//::+/:./sso+/////+o+++o:-:+/://+/:::/+sso++/+/++//:/o-/+-/++++
s/:shdmmmmmmmmNNNmshNNMh---:/oys/ydhoo///:../+osoosssoo+++oss+/-/::/+o+/-:++o+s+/+///:///os-.::::/oo
/ohdddddmmmmmmNNmsdNNNMm//:--/+:++o::::/:..:/ossyyhhhhhys++ooso:+++//+++:+++++oo///++/++++:--/:/://:
ydddddmmmmmmmmNNhdNNNds+:----/+/++soo/++:.-+++oo+oo+++++++///os++/+++::+//++o+///::+o:://:-:::/+/+//
mmmmmmmNmmNNmhsysyoo+/+s:---./o+oooyhyhs---//:/++++/+/+///+++sy++//+-//++/+++++++//+s/::::/o+/+++sys
mmmmmmmNmmmmho:/://s/++:----.:/:/://::--.-://+sdmmmmmmmmmmNmdhhs/:-::++///+o/::::+s//:://os++ooo++o+
hhhhhhhyyyysso/+//:::/-`````.:s+sso:-----:-+++ss++++oyyddmdddddhsss++/::++so/:-:::+++o+/ssyso+sso+o+
+//////////::::::--..`````.-:/o/+/::--://+-/o+osoo/:-//oyhyosdmhhhddho///++++///:/yhssoooyhdyo////o/
.......----------..``....-:/osssso///+oo+o:+o+/+oo/:::+ohdooshhhddddho/++/--:-:+o+++oossosys+/::////
.........-.............-:+osssosooo+ooo//+:+oso/+/:ysoy/shosshddmdddho//+//-:/+ss+oso+so+++::---:/oo
.........-----.....`.-::/osyyyssosoosoooso::+so+://:::./yyhhyhmmmmmmdy++++++//+ss+oso++:-::/:-:-/oyy
.........--.......-::::/+syyyyssossssyydy:..:+oo++++//+yyyddhdNNmmmmmdso+/+so/-:/+sso+-:::-/--::::yh
```....-:---..../+o/::/+osyhhysyyyhhdmd+.....:oossyyyyyhddmmdmmmmmmmmmo+ooosys/:/:/+///:::/o/+///oho
```````````````:soo/:/++oshhhyyhddmmds:.-------shhdmmNNNNNmmmmmmdddmmdo+ooyyhyo/o/++:/+++/+o+o+//++/
---.....-..--/oso++//oooosyhhdmmmdhs/---:::--..:ohmNNNNNNmmmmddddddmmho+ossydhy+/+++oss+/:ooos/++:+o
:--::/:/+:-/osoo+oo++ssosyyymmmho/::----:------::ohmNNNNmmmdddddhdmmdyo+syhhddhho/+oo+oo///:oo:-::+s
/::://-:/:/oooo+++++ooosyyhdmddhy/-..--:::::::::+o++dmmmmddddhhyydNmdyo+oshhddhdysossoo+oso+::--+osy
:-::::/+:+oooooooooyysyyhhddhyhdy/-``.-:::::/:://+.-+yddddhhhhyyhNNmyooo+osyhhhdds+::://::::/:--:///
------::+++oooooosymmddddhhyyoos+/:-....-::::--:/+--:/+yhyyyyyhdNMNdo/+o++ssssyyhs:/+/+/+ooo+::/++os
:+::--:++oyyyhhhhhdmmdhdhhysoooyhyyso++:--------:/-.--::/+oyyhmNMMNms++oo+oyysoyyh+/+//ossys+soosyhy
//-:--+ossyyyyyhdddmdddhyysyyyyhhyyyyyyys+/-....-:...--::/+ydNNNNMMNhs+++/osyysosyys/++oosyoss///hos
/-/:/syysyyyhyyhdhhdddhyyhyhyyyyhyyhyyyhhhyyo/--/+:-:/+oyhmmNNNNNNMNmhsosssssyyoooys/++//+o+ssoss/yy
--::shhhyssyhsyhyhyhhhhhdhyhyhddhhyhhhyyhdhhho+os+:/ohmmNNNmmmNNNNMhmdhhhssssossooyyo::+os+:+:+ysooo
--.:osyhyssyssyysssyyyhdmhhhhmmmdmmdhyyyhhddmh+//:-:/sdmmmdddmmNNNN:yhyhhyosyysoooosso/+os+:-.---:-y
-..-/oyyyssssssssso+oooyhhhdNNMMNmdhhyyydmmmmmyo+::/+oyhddhhdmmNNNy-oshhsysyddhosyyssyyosohoyssss:oo
-----+yyysssysso+:....-:--:/+osydNdhhydmmmmdmmdhy//++oosyssshmNNNh::+oddhyssyhhyohyyyhdhhssoyyhhdhhs
::----syysyysy+-``..-..```...---:+mddmmmmdhddmmdhy+//+++++++ymNmo-:::odmmhyhys+osdhsyhyyyyysooyyysso
----.-/osyhhd+.```.--```....----.:hNydmmmhhhydmmddho/+oooosshNd/..--./hNmdysyso+syhsssyyhhddhs++yss+
----...:+sys+-`````.``...-------./dMyosdhosyshhmmddyoosyysyddy:------:sNNdddhyhssshdhyysyhhyhyoshy++
---------::--..`.`.`.--------.-.:ymh+++ss+odoymmmmmdysyyhshmy::::---:/yhmNmddddhosyyyysssyhyyyooo/-+
:------:---:...--:-------.-.--../dNNmmmmmddmdmNNmmddyyhyhsdd:////:://:/smdmdhdyyyyhdhysoosysssso---/
:-::-::::-::.--:::-:--....---.-./hNMMMNMMNMNNNNNmhddhhhhddd/-::/+o//:+//+sshyhhyhdhhmddhsooosyys/-.-
-:-:-:/::-:-.--::---.``..----..-:smMMNmmNNNNNNNmmhhhhhdmNm+-.::----:::---:+syhhdhdhddmmNmdhhhhhhs/:/
:::--:/--::-.--::---....---:----:ohMNNdsyhhddmNmdddhdmNNm/-::/::+/:---..--:/ssydhddmmmmmmdddhhyyyo:.
----:-/::::-..--..-:-----::---://ohNNNmo+/o+ohdmdmddmNNmo-::/o+s+o+//:.:.-::-/syhhhdmmmddddddhhyyo:.
-::::-:--//--.:-.-::---:::--::/+osdNNNmoo/o/+yyhdhhddmdso+:-..-:-yhhy+:/::::::+oyddmmmmdhhhhhhdhhy+-
////:-::::/:--:---:---:::--:://oshmNNNmys++++oo///////::/:--.````:sys+/:::::/:/oshdmmmmmhyyhyyhddho-
::/:-----:-:--:---:::::/:::///oshdmmNmdh/::--::-::::/::/::-..`````://:--------::/ydmmmmmdysossyhddy+
::::-:::/:------:-:/:://::://+sydNNNNmdy+::-:-:://:://::::-..`````:::::::---..:/oyhddmmddhosssyhdmh+
:++://+/:::----/:///://////++oyyhdNNNmdy+::::///////::::::-...```../+oooysooooo/oyhdhdmdddhhyyyhhdmh
//o/o://:------++++/+++++osyso::-+ddmmhyo//////+/:///////---.-.-:/::so/syoyyysss/oyhydmydd+oss+odmmy
/+::::--::::::-oo+++ossyyhddhyyy.hs/+hhyyoo++/////:////:--:--:/+oss++/+oo:+-////::/-:o//::+o+////++:
:-------::/:/::+o+oosyysoosyhddm.ss-./s+ooo/+/++++//++//:/:::os/os/:-/:/-.-..---.-//+/-..-/:.:++//:-
:--::----:/+:--/:-..-ososssssyyyo.sh-.o:o/+++://///++o:/:+/+:+/::://+//:/:+:++/:-:-.-...-:/+--:+/:-:
:::+/:--:/:----:::::-/oysoo+osoos`-:---::/s/--//::/o+-:-//////:/:++:/:.:/::::/o+---:-----/--::..-///
/::-:::::::-::::----:-::----:--::.-`./o:/:/:/-:/:/:oo--/+/+/+y/oo++/:/+//:-/-::/::+-::-:+/++s+/o+++/
""")
    input("Press enter to start.")
    

def credit_screen():
    print()
    print("This game was coded by Evan B. and Jae C.")
    print()
    print("It was completed on 9/14/2016")
  
def play():
    print()
    low=int(input("What is the lowest number in the range, " + name + "?"))
    print()
    high=int(input("What is the highest number in the range, " + name + "?"))
    tries = 1

    print()
    print("Please think of a number between " + str(low) + " and " + str(high) + " and I will try to guess it, " + name + ".")
    print()
    print("Press enter you have thought of a number, " + name + ".")
    input()
    next_guess = False
    got_it = False
    while got_it == False:
        guess=math.floor((high + low)/2)
        print("Is the number " + str(guess) + ", " + name + "?")
        print()
        value=input("Did I guess it, or is the number higher or lower, " + name + "?")
        value = value.lower()
        if high == low:
            print('You are a dirty cheater! I win!')
            got_it = True
        if value== "higher" or value == "h":
            low = guess + 1
            tries = tries + 1
            next_guess = True
        elif value == "lower" or value == "l":
            high = guess - 1
            tries = tries + 1
            next_guess = True
        elif value == "yes" or value == "y":
            print()
            print("Yay! I got it in " + str(tries) + " tries, " + name + "!")
            got_it = True
        else:
            print()
            print("Please just say higher, lower, or yes, " + name + ".")
            print()
            got_it = False

            
def play_again():
    repeat = True
    restart = False
    while repeat == True:
        again=input("Would you like to play again, " + name + "?")
        again = again.lower()
        if again == "yes" or again == "y":
            restart = True
            print()
            print("Ok! Restarting, " + name + "!")
            play()
        elif again == "no" or again == "n":
            restart = False
            repeat = False
            print()
            print("GAME OVER!")
            credit_screen()
        else:
            print()
            print("I don't understand! Please type yes or no, " + name + "!")
            print()
            repeat = True

    
startscreen()
print()
name = input("What is your name?")
play()

play_again()
