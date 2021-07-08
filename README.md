# elantris_game

The location class always keeps the previous location, in order to decide if it should print a welcome message for the new location or not.

all messages have a unique ID, which is mapped to a specific location name. two dictionaries are used for the purpose.

all available items are stored in a list.

At each iteration show the state options and the inventory options. Each option has a unique number which you can choose to continue. All of this happens in an infinite loop, which can be exited by entering the number for jumping in the Lake, or by putting "exit" or "quit".![image](https://user-images.githubusercontent.com/67368977/124869389-d03cd400-dfc9-11eb-8b6f-45065717ae47.png)


**Messages on Items**:
Begin state: empty

Food: 
Probability 50/50
	"Congratulations, there is food! Now, you can either:
		eat it (1)
		bring it back to Galladon in New Elantris, so he can distribute it among the New Elantrians (2)
		or carry it in your bag, if you need it further along your trip (3)."
	"Sorry, traveler, no food today!"
	
AonDor book:
	"Ah, the fire aon is so hard to draw. Use the book to practice aon Ehe."
	"The book is really interesting, but you don't really have time for aons practice right now. Put the book in your backpack."
	"Did Dorena write this book while drunk? What an astounding lack of scholarship. Leave the book at the library."
	
Clothes: 
	Out: "Daora thinks this old suit of Lukel's will fit you nicely."
		"Aw, I want to put on these clothes, they look so nice."
		"Ew, Lukel has a bad taste even for a dead person like me. I will leave the clothes here."
		"Unfortunately, those clothes don't fit me, but I think New Elantris will make use of them. Let me put them in my bag"
		If in elantris: "I should deliver those clothes to Katara"





**Messages on locations**:

Begin state: "Welcome Elantrian! Your flesh is gray, your hunger is growing with every hour which passes, and your body doesn't heal anymore; but if you are here, I believe you have not joined the Hoed yet. Now, may Domi give you wisdom in the choices you are to make today!

You can exit the game at any time by inputting "quit" or "exit."
Choose between your choices by inputting the number corresponding to each message. "

Elantris:
	Out: "You are in front of the gate of the cursed city of Elantris," - show only if previous state was different, same goes for each location line
	2 "Feels like the hunger is catching up on me, I'd better search for some woed newcomer's food."
	3 "I am so tired of the pain. I want to take a trip to the Perpendicularity Lake and let go."
	4 "I am able to rise above the carnal reality of a body stopped amidst its transformation, and I want to go through Raoden's secret channel into the city of Kae."
	
Perpendicularity Lake
	5 "Finally, I will give up the pain and let the lake devour me! May the Great Beyond be more merciful to me, than this world has been!" (This move will make you exit the game, since you have finally ridden yourself of the pain and died.)"
	6 "What was I thinking? I feel stronger than that, and I think I still have things to do among the living, I should head back to Elantris right now."
	
Kae:
	Out: "Welcome to the city of Kae!"
	
	8 "I feel like my aon practice needs some improvement, I will head to the library and get Dorena's new book on AonDor."
	9  "Harathen and Dillaf are back in town. They are working hard to convert the masses. I should find them!"
		70/30
		Out: "Oh, here they are! Looks like they are preparing to teleport to Teod!"
			10 "I want to join them and pay Teod a visit!"
			11 "Those Dakhori monks surrounding them look way too dangerous. I'd better remain in Kae."
		Out: "Why I didn't think of looking at the wall of Elantris on the first place? Of course they are here, preaching that all Elantrians are mindless demons."
			12 "This is scary! I'd better return to Elantris right now, or the crowd will tear me to pieces."
			13 "What an amazing opportunity to confront them and show them that we are rational beings, a lot like them! I will stay and talk to the crowds, ruining Harathen's plans. Kae is nor Duladel, your Fjorden tricks aren't going to work here!"
	14 "I miss Kii's feasts. I will head to his house."
		Out: "You have arrived to Kii's castle, and he asks you to join him for lunch."
			15 "I will join Kii for lunch, I am starving anyway."
			16 "Daora promised me that she will help me find some new clothes, I'd better see what she's got."
			17 "Ouch, I just remembered that I promised Kii to show him the Perpendicularity Lake. I should take him there."

Teod:
	Out: "Welcome to the city of Teod!"
	18 "If Harathen and Dillaf are here together, king Eventeo is in grave danger. I should go to the palace to warn him."
	19 "Unfortunately I am too late, the Dokhari have arrived here before me. I will run to the docks and take the first ship going back to Kae."





