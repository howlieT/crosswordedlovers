from Rooms import Room
from Items import Item
from time import sleep

# Kitchen
kitchen = Room("kitchen")
kitchen.set_description("""
The Kitchen
-----------------------------
A small bright room, there is a cooker beside the door, 
and a sink under one window, opposite the door a second window overlooks the garden.
Everything is bright and light, the linoleum is yellow, the cupboards are cream,
the trims are blue""")


# Things in the Kitchen

# White Goods, sort of
kettle = Item("kettle")
kettle.set_description("A cream coloured electric kettle, useful for boiling water")

cooker = Item("cooker")
cooker.set_description("A white gas cooker with 4 rings on the hob and a grill at the top. Good for cooking on.")

# Cutlery, plates etc
mug = Item("mug")
mug.set_description("A mug for drinking out of, it commemorates the death of Princess Diana")

plate = Item("plate")
plate.set_description("A white ceramic plate with a blue rim, slightly chipped")

knife = Item("Knife")
knife.set_description("A table knife, good for spreading, less good for stabbing")

fork = Item("fork")
fork.set_description("An ordinary fork, for eating with, or in a pinch for whisking")

tea_spoon = Item("tea spoon")
tea_spoon.set_description("A spoon for small jobs, like fishing tea bags out of a mug")

spoon = Item("spoon")
spoon.set_description("A regular desert spoon, the sort you might eat cereal with.")

# Pen and Paper
newspaper = Item("newspaper")
newspaper.set_description("""
A newspaper, headlines on the front, sports on the back, mostly news in the middle,
the crossword is near the end""")

biro = Item("biro")
biro.set_description("A useful pen for making notes, or doing the crossword with. Mightier than a sword?")

# Fridge and Contents
fridge = Item("fridge")
fridge.set_description("""
A cold storage for the kind of things you keep in a kitchen. Milk, some orange juice, some cheese, 
half a jar of strawberry jam of unknown origin, some mustard that might possible predate decimal currency.""")

milk = Item("milk")
milk.set_description("A bottle of milk, half full. Or half empty, depending on how you think")

jam = Item("jam")
jam.set_description("Half a jar of strawberry jam, provenance unknown")

mustard = Item("mustard")
mustard.set_description("""
The remains of some very old mustard, a very lurid shade of yellow. 
Smells firey, like it might take your nose hairs""")

cheese = Item("cheese")
cheese.set_description("Some regular yellow cheese, a small bit. The kind mice are supposed to like. A good snack.")

# Furniture
kitchen_table = Item("kitchen table")
kitchen_table.set_description("A small wooden table with painted white legs and top")

kitchen_chair = Item("kitchen chair")
kitchen_chair.set_description(" A painted white chair with a yellow seat cushion. One of a pair.")

kitchen_window = Item("kitchen window")
kitchen_window.set_description("A window, you can see the garden out of it.")

# Bedroom
bedroom = Room("bedroom")
bedroom.set_description("""
The Bedroom 
----------------------------
The walls are blue, there is a table with a lamp on it on either side of
the bed on the east wall. On one side, there is a small stack of books and an alarm clock. 
The furniture is pine, the curtains are darker blue and match the carpet.
There is a pine chest  of drawers against the west wall.
""")

# Things in the Bedroom
# Furniture
bed = Item("bed")
bed.set_description("An orange pine frame double bed, the coverlet and pillows are blue")

side_table_books = Item("side table with books on")
side_table_books.set_description("A side table with a small stack of books on")

side_table_empty = Item("side table without books on")
side_table_empty.set_description("A side table with nothing on it, no one uses this side of the bed regularly")

chest_of_drawers = Item("chest of drawers")
chest_of_drawers.set_description("A chest of five drawers, orange pine. For storing clothes in. A hairbrush is on top.")

curtains = Item("curtains")
curtains.set_description("Dark blue curtains to keep the daylight out")

bedroom_window = Item("bedroom window")
bedroom_window.set_description("A window, you can see the garden out of it.")
# Small Objects
alarm_clock = Item("alarm clock")
alarm_clock.set_description("""
A small battery powered alarmclock, silver, with what looks like glow in the dark paint on the hands.""")

table_lamp = Item("lamp")
table_lamp.set_description("A side lamp for reading by in bed")

top_book = Item("top book")
top_book.set_description("The top book in the stack, its not written in a recognisable language")

second_book = Item("second book")
second_book.set_description("""
A copy of Charles Dickens Great Expectations, there's a bookmark two thirds of the way through""")

bottom_book = Item("bottom_book")
bottom_book.set_description("A copy of War and Peace, but it doesn't look like it's ever been opened.")

hairbrush = Item("hairbrush")
hairbrush.set_description("A black plastic hairbrush with white spikes. For brushing hair.")

# Clothes
pyjamas = Item("pyjamas")
pyjamas.set_description("Pyjamas, for sleeping in.")

underwear = Item("underwear")
underwear.set_description("""
It's what you wear under your clothes. You could go without it, but that sort of thing tends to be frowned upon.""")

shirt = Item("shirt")
shirt.set_description("A clean shirt to wear, it's pale blue, that's nice")

trousers = Item("trousers")
trousers.set_description("Clean trousers to wear, they're dark green")

jumper = Item("jumper")
jumper.set_description("A nice navy blue jumper that someone knitted, it smells very faintly of lemons.")

# Hall
hall = Room("hall")
hall.set_description("""
The Hall
------------------------------
There is not much natural light in here. Some comes through the glass panels
in the front door. There is a coat stand on the east wall, there is a key hook 
on the west wall. At the southern end you can see the kitchen. A door on the east wall leads to the bedroom,
a door on the west wall leads to the bathroom.
""")

# Things in the Hall
coat_stand_dict = {"look": """
A wooden stand for hanging coats on, maybe hats and scarves too. You can put umbrellas in the base
""", "use" : " You hang your jacket on the coat stand"}

coat_stand = Item("coat stand", coat_stand_dict)
# coat_stand.set_description({"look": """
# A wooden stand for hanging coats on, maybe hats and scarves too. You can put umbrellas in the base
# """, "use" : " You hang your jacket on the coat stand"})


key_hook = Item("key hook")
key_hook.set_description("Hooks for hanging keys on, there's a spare set here for the front door.")

door_mat = Item("door mat")
door_mat.set_description("A scratchy brown mat for getting the dirt off your shoes when you come in")

# Bathroom
bathroom = Room("bathroom")
bathroom.set_description("""
The Bathroom
--------------------------
This room is white. There is a toilet and a sink and a bathtub with a shower. 
The shower curtain is also white, and is slightly mouldy at the base. The glass 
in the window is frosted. There is a mirrored cabinet above the sink. There is
a towel on the radiator.
""")

# Things in the Bathroom
# Fixtures and Fittings
bathtub = Item("bathtub")
bathtub.set_description("A regular white ceramic bathtub, the sort with silver handles in the sides to help you stand")

shower_curtain = Item("shower curtain")
shower_curtain.set_description("A white shower curtain to keep the water inside the tub, slightly mouldy.")

sink = Item("sink")
sink.set_description("A white ceramic sink for washing your hands and brushing your teeth, that sort of thing.")

toilet = Item("toilet")
toilet.set_description("A toilet, white with a plastic seat. Could probably use a scrub.")

mirrored_cabinet = Item("mirrored cabinet")
mirrored_cabinet.set_description("A mirrored cabinet for storing things in, look into it and see your reflection")

bathroom_window = Item("bathroom window")
bathroom_window.set_description("A frosted window, you can't see out of it.")

# In the Cabinet
tooth_mug = Item("tooth mug")
tooth_mug.set_description("""
A slightly chipped tooth mug, white ceramic with a blue rim, looks like it matches the kitchen plate""")

toothbrush = Item("toothbrush")
toothbrush.set_description("A nice green toothbrush, to brush yur teeth with")

toothpaste = Item("toothpaste")
toothpaste.set_description("Mint flavoured toothpaste, the kind with coloured stripes in")

floss = Item("floss")
floss.set_description("A tub of floss, for flossing your teeth")

hair_gel = Item("hair gel")
hair_gel.set_description("A tub of hair gel, slightly sticky, for styling")

deodorant = Item("deodorant")
deodorant.set_description("A stick of roll on deodorant, for making yourself smell less")

# Garden
garden = Room("garden")
garden.set_description("""
The Garden
-----------------------
A smallish, squarish sort of a garden on the southern side of the house but only accessible from the front. 
There is a tree at the end,
the lawn looks to be in need of mowing. There are beds of flowers up both sides which buzz lazily
with bees and other insects. There is a small set of bistro furniture just beside the house.
On the wall behind the tree, a cat snoozes in the sun.
""")

# Garden Items
# Furniture etc
garden_table = Item("garden table")
garden_table.set_description("A metal table in the garden, dark grey, slightly rusty in places, warm from the sun.")

garden_chair = Item("garden chair")
garden_chair.set_description("A metal chair in the garden, one of two, matches the table.")

cat = Item("cat")
cat.set_description("A small black cat, snoozing")

# Plants
tree = Item("tree")
tree.set_description("""
A deciduous tree with lots of bright green foliage, tall and somewhat wizened, 
it appears to be a fruit tree, maybe an apple tree?""")

left_flowers = Item("left hand flower bed")
left_flowers.set_description("""
The left hand flowerbed, a vibrant range of flowers, buzzing with life. Primulas and pansies, some tulips,
there a peach coloured rose brush right at the end""")

right_flowers = Item("right hand flower bed")
right_flowers.set_description("""
The right hand flowerbed, a vibrant range of flowers, buzzing with life. Marigolds and nasturtiums, irises, anemones,
a lobelia explodes onto the grass.""")

# Linking Rooms
hall.link_room(garden, "north")
hall.link_room(kitchen, "south")
hall.link_room(bathroom, "west")
hall.link_room(bedroom, "east")
kitchen.link_room(hall, "north")
bedroom.link_room(hall, "west")
bathroom.link_room(hall, "east")
garden.link_room(hall, "south")

# Linking Items to Rooms
# Kitchen Links
kitchen_table.link_item(kitchen, "use")

# Hall Links
coat_stand.link_item(hall, "use")
key_hook.link_item(hall, "use")

# Movement and Interaction Commands
current_room = hall
current_item = coat_stand

# Command Finder

def command_finder(old_string):
    new_string = ''
    for x in old_string:
        if x == ' ':
            return new_string
        else:
            new_string += x


while True:
    sleep(1)
    print("\n")
    current_room.get_description()
    current_room.get_details()
    command = input("> ")
    command_finder(command)
    if command in ["north", "south", "east", "west"]:
        current_room = current_room.move(command)
    else:
        if command in ["use", "look", "read", "wear", "open", "break", "sit", "spread"]:
            current_item = current_item.use(commamd)

    #    else:
    #       if command == ["talk"]:
    #            if inhabitant is not None:
    #                inhabitant.talk()
    #        else:
    #            print("Who are you talking to?")

# TODO: Convert all item descriptions to dicts
# TODO: Can Item dicts become sub dicts of one big dict?
# TODO: Work out how to iterate time in the game, maybe a for loop? Maybe counting on by one?
# TODO: Have interactable items/objects in the description text be a colour? Ask Ivan about that?
# TODO: Convert cat from Item to Char
# TODO: Figure out the mechanics for the cross word...
