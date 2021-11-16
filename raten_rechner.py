#Jeldrik Hemmme
#ETS 2021
#15.11.2021

#Hardware: wird nicht benötigt

#Version:0.2

#Aufgabe: Sie bauen ein Haus und wollen wissen wieviel Geld Sie bei einer bestimmten Summe und einem bestimmten Zinssatz 
#monatlich zahlen müssen, wenn Sie in 10 Jahren schuldenfrei sein wollen.

#Quelle: https://kredit.bildungsbibel.de/kreditzinsen-berechnen-abzinsungsfaktor-formel-beispiel-vorlage

#Aufforderung zu Eingabe von Werten
zinssatz = input('Bitte Zinssatz in % angeben: ')
laufzeit = input('Bitte Laufzeit in Monaten angeben: ')
kapital = input('Bitte Kapital in Euro angeben: ')

#Änderen des Variabelntypes
zinssatz = int(zinssatz)
laufzeit= int(laufzeit)
kapital = int(kapital)

#Errechnen des Zinsfaktors
zinsfaktor_0 = (zinssatz/100)+1
zinsfaktor_1 = zinsfaktor_0**(1/12)         #zinzsfator_0**(1/12) --> zieht die zwölfte Wurzel

#Ausgabe des zinsfaktors
print("Der Zinfaktor beträgt:", zinsfaktor_1)

#Errechnen der monatlichen Rate
zwischenergebnis_mntl_rate_1 = zinsfaktor_1**laufzeit           #zinsfktor**laufzeit -->bedeute das die Laufzeit der Exponent ist 
zwischenergebnis_mntl_rate_2 = (zinsfaktor_1**laufzeit) -1

monatliche_rate = kapital*(zwischenergebnis_mntl_rate_1/zwischenergebnis_mntl_rate_2)*(zinsfaktor_1-1)
monatliche_rate_1 = round(monatliche_rate, 2)

#Ausgabe der monatlichen Rate 
print("Monatliche Rate in Euro =", monatliche_rate_1)


