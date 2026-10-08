# -*- coding: utf-8 -*-
import json
import os
import re

def normalize(text):
    return ' '.join(re.sub(r'[^\w\s]', '', text.lower()).split())

def build_english_bank():
    items = []
    seen = set()

    def add(tier, q, opts, ans, exp):
        q = q.strip()
        ans = ans.strip()
        opts = [o.strip() for o in opts]
        exp = exp.strip()

        for forbidden in ["Warm-up", "warm-up", "Logic Riddle", "Master Trap", "پہیلی #", "#", "Level "]:
            if forbidden in q:
                raise ValueError(f"Forbidden text: {forbidden} in {q}")

        norm = normalize(q)
        if norm in seen:
            return False
        if len(opts) != 4 or len(set(opts)) != 4 or ans not in opts:
            return False
        seen.add(norm)
        items.append({
            "id": len(items) + 1,
            "difficulty": tier,
            "question": q,
            "options": opts,
            "correctAnswer": ans,
            "explanation": exp
        })
        return True

    # =========================================================================
    # TIER 1: EASY (250 distinct questions)
    # Common sense, nature, everyday physics, classic clean riddles
    # =========================================================================
    easy_data = [
        # Nature & Animals
        ("What gets wetter the more it dries?", ["A towel", "A sponge", "A cloud", "Rain"], "A towel", "A towel absorbs moisture from your body as it dries you."),
        ("What has hands but cannot clap?", ["A clock", "A glove", "A tree", "A robot"], "A clock", "A clock has hour and minute hands but no biological arms or hands."),
        ("What has to be broken before you can use it?", ["An egg", "A bottle", "A lock", "A stick"], "An egg", "You must crack an eggshell before cooking or consuming it."),
        ("I am tall when young, and short when old. What am I?", ["A candle", "A tree", "A giraffe", "A building"], "A candle", "A candle starts tall and melts down shorter as it burns."),
        ("Which month of the year has 28 days?", ["All 12 months", "Only February", "Only January", "None of them"], "All 12 months", "Every calendar month has at least 28 days in it."),
        ("What is full of holes but still holds water?", ["A sponge", "A bucket", "A net", "A colander"], "A sponge", "A sponge is filled with porous holes and absorbs water."),
        ("What question can you never answer 'yes' to honestly?", ["Are you asleep?", "Are you awake?", "Are you hungry?", "Are you ready?"], "Are you asleep?", "If you are truly asleep, you cannot consciously answer the question."),
        ("What is always in front of you but cannot be seen?", ["The future", "Air", "Your nose", "Darkness"], "The future", "The future is always ahead in time, yet invisible until it arrives."),
        ("There is a one-story pink house with pink furniture. What color are the stairs?", ["No stairs", "Pink", "White", "Brown"], "No stairs", "A one-story house has no second floor, so it has no stairs."),
        ("What can you break without ever picking it up or touching it?", ["A promise", "A window", "A twig", "A plate"], "A promise", "A promise is broken by your actions or failing to keep your word."),
        ("What goes up but never comes down?", ["Your age", "A kite", "A balloon", "Smoke"], "Your age", "Your chronological age only increases with each passing year."),
        ("A man walked outside in heavy rain with no umbrella or hat, yet didn't get a single hair wet. Why?", ["He was bald", "He was running fast", "He wore a hood", "It was mist"], "He was bald", "He had no hair on his head to get wet."),
        ("What has a neck but no head?", ["A bottle", "A guitar", "A shirt", "A snake"], "A bottle", "A bottle has a narrow neck leading to its opening, but no head."),
        ("What has a thumb and four fingers, but is not alive?", ["A glove", "A robot", "A mannequin", "A skeleton"], "A glove", "A glove is tailored with five finger slots but is an inanimate item."),
        ("What has many teeth, but cannot bite?", ["A comb", "A saw", "A zipper", "A gear"], "A comb", "A hair comb has teeth designed for styling, not chewing."),
        ("What has a head and a tail, but no body?", ["A coin", "A snake", "A pin", "A kite"], "A coin", "A standard coin has heads and tails sides but no anatomical body."),
        ("Where does today come before yesterday?", ["In a dictionary", "On a calendar", "In a dream", "In history"], "In a dictionary", "Alphabetically, the word 'Today' precedes 'Yesterday'."),
        ("What has words, but never speaks?", ["A book", "A radio", "A painting", "A smartphone"], "A book", "A book contains printed words, but cannot speak aloud on its own."),
        ("What has one eye, but cannot see anything?", ["A sewing needle", "A storm", "A potato", "A camera"], "A sewing needle", "The loop at the end of a sewing needle is called an eye."),
        ("What can travel around the entire world while staying in a single corner?", ["A postage stamp", "A compass", "A passport", "A suitcase"], "A postage stamp", "A postage stamp remains in the top corner of the envelope during international transit."),
        ("What has four legs, but cannot walk?", ["A table", "A horse", "A baby", "A lizard"], "A table", "Furniture tables have four supporting legs but cannot walk."),
        ("What has a bed but never sleeps, and a mouth but never talks?", ["A river", "A mountain", "An ocean", "A canyon"], "A river", "A river has a riverbed and river mouth, but is water."),
        ("What follows you in the sunlight but disappears in the dark?", ["Your shadow", "Your echo", "Your reflection", "Your footprints"], "Your shadow", "A shadow requires a light source to be cast against a surface."),
        ("Feed me and I live, but give me water and I die. What am I?", ["Fire", "A sponge", "A desert plant", "An engine"], "Fire", "Fire consumes fuel and oxygen, but water smothers and extinguishes it."),
        ("What runs all the way around a backyard without ever moving?", ["A fence", "A pathway", "A stream", "A dog"], "A fence", "A fence borders the perimeter of a yard while standing completely still."),
        ("What gets sharper the more you use it?", ["Your mind", "A kitchen knife", "A pencil", "A saw"], "Your mind", "Practicing mental puzzles keeps your brain sharp, whereas blades dull with use."),
        ("What has keys that cannot open any door locks?", ["A piano", "A keyboard", "A map", "A cipher"], "A piano", "A piano has musical keys that play tones rather than open doors."),
        ("What can you hold in your left hand, but never in your right hand?", ["Your right elbow", "A coin", "A pencil", "A glass of water"], "Your right elbow", "You cannot physically reach around and hold your right elbow with your right hand."),
        ("What kind of room has no doors or windows?", ["A mushroom", "A courtroom", "A basement", "An attic"], "A mushroom", "A mushroom is an edible fungus, not an architectural room."),
        ("What goes up and down, but always stays in the same place?", ["A flight of stairs", "An elevator", "An escalator", "A ladder"], "A flight of stairs", "Stairs lead up and down between floors while remaining static in position."),
        ("What has a spine, paper pages, but no skeleton?", ["A book", "A cactus", "A hedgehog", "A binder"], "A book", "The bound edge of a hardcover or paperback book is called its spine."),
        ("What flies without wings and cries without eyes?", ["A storm cloud", "The wind", "Smoke", "An airplane"], "A storm cloud", "Clouds drift across the sky and release rain without physical eyes."),
        ("What has many rings but no fingers?", ["A tree", "A telephone", "Saturn", "A circus"], "A tree", "A tree forms concentric growth rings inside its trunk each year."),
        ("What gets smaller every time it takes a bath?", ["A bar of soap", "A sponge", "A washcloth", "Ice"], "A bar of soap", "Soap dissolves into lather as it is used with water."),
        ("What can fill an entire room without taking up any physical space?", ["Light", "Air", "Sound", "Furniture"], "Light", "Light illuminates all corners of a room without occupying mass volume."),
        ("What has branches, but no fruit, trunk, or leaves?", ["A bank", "A river", "A tree", "A vine"], "A bank", "Financial banks have corporate branches, not botanical leaves."),
        ("What kind of band never plays music?", ["A rubber band", "A marching band", "A rock band", "A jazz band"], "A rubber band", "An elastic rubber band binds objects together rather than playing musical notes."),
        ("What has one head, one foot, and four legs?", ["A bed", "A table", "A horse", "A dog"], "A bed", "A standard bed has a headboard, a footboard, and four supporting legs."),
        ("What building has the most stories in the world?", ["The library", "The Burj Khalifa", "The Empire State", "The Pentagon"], "The library", "A public library contains thousands of written literary stories."),
        ("What comes once in a minute, twice in a moment, but never in a thousand years?", ["The letter M", "A second", "A heartbeat", "A breath"], "The letter M", "The letter 'M' appears once in 'Minute', twice in 'Moment', and zero times in 'Thousand years'."),
        ("What belongs entirely to you, but other people use it far more than you do?", ["Your name", "Your phone", "Your car", "Your shoes"], "Your name", "Your name is yours, but other people say it whenever they address you."),
        ("Which word becomes shorter when you add two letters to it?", ["Short", "Tiny", "Little", "Brief"], "Short", "Adding 'er' to 'Short' forms the comparative word 'Shorter'."),
        ("What can you catch, but never throw?", ["A cold", "A tennis ball", "A frisbee", "A fish"], "A cold", "You can catch a viral illness or cold, but you cannot physically toss it."),
        ("What has a heart that does not beat?", ["An artichoke", "A cabbage", "A stone", "A clock"], "An artichoke", "The tender core center of an artichoke or palm is culinary known as its heart."),
        ("What is so fragile that saying its name breaks it?", ["Silence", "A whisper", "A crystal glass", "A bubble"], "Silence", "The moment you utter any sound, the surrounding silence is broken."),
        ("What runs through cities and over hills without ever moving?", ["A paved road", "A train", "A runner", "The wind"], "A paved road", "Highways and roads traverse long terrain distances while fixed to the ground."),
        ("What has an eye in its center, but cannot see anything around it?", ["A hurricane", "A needle", "A potato", "A camera"], "A hurricane", "The calm meteorological center of a tropical cyclone is called its eye."),
        ("What kind of coat is best put on wet?", ["A coat of paint", "A raincoat", "A trenchcoat", "A winter coat"], "A coat of paint", "Paint must be applied wet so that it adheres and dries into a smooth surface."),
        ("What has eighty-eight keys, but cannot unlock a single door?", ["A grand piano", "A typewriter", "A locksmith shop", "A computer"], "A grand piano", "A standard acoustic piano has exactly 88 musical keys."),
        ("What has bark, but no bite?", ["A tree", "A seal", "A dog", "A hyena"], "A tree", "The tough protective outer layer of a tree trunk is called bark.")
    ]

    for q, opts, ans, exp in easy_data:
        add("easy", q, opts, ans, exp)

    # Animals, birds, and insects nature trivia
    animals = [
        ("Which bird can fly backwards as well as upside down?", ["Hummingbird", "Eagle", "Falcon", "Owl"], "Hummingbird", "Hummingbirds have ball-and-socket shoulder joints allowing 360-degree wing rotation."),
        ("Which mammal is the only one capable of true sustained flight?", ["Bat", "Flying squirrel", "Sugar glider", "Flying lemur"], "Bat", "Bats have modified webbed digits forming true aerodynamic wings."),
        ("Which sea creature has three hearts and blue blood?", ["Octopus", "Dolphin", "Squid", "Whale"], "Octopus", "An octopus pumps hemocyanin blue blood with two branchial hearts and one systemic heart."),
        ("Which animal sleeps for up to three years during prolonged drought?", ["Desert snail", "Brown bear", "Sloth", "Tortoise"], "Desert snail", "Certain desert snails can seal their shells with mucus and estivate for years."),
        ("Which animal can see both infrared and ultraviolet light?", ["Mantis shrimp", "Goldfish", "Honeybee", "Eagle"], "Mantis shrimp", "Mantis shrimp possess 16 color receptive cones covering infrared to ultraviolet."),
        ("Which creature never sleeps and has no lungs?", ["Bullfrog", "Ant", "Shark", "Jellyfish"], "Bullfrog", "Bullfrogs show identical alertness responsiveness whether resting or active."),
        ("Which bird lays the largest egg relative to its body weight?", ["Kiwi", "Ostrich", "Penguin", "Albatross"], "Kiwi", "A female kiwi's single egg occupies up to 20 percent of her total body volume."),
        ("Which insect can survive for weeks without its head?", ["Cockroach", "Ant", "Grasshopper", "Termite"], "Cockroach", "Cockroaches breathe through abdominal spiracles and have decentralized nerve ganglia."),
        ("Which animal produces square-shaped droppings to prevent them from rolling away?", ["Wombat", "Koala", "Beaver", "Kangaroo"], "Wombat", "Wombats produce cubic scat due to uneven elasticity in their intestinal walls."),
        ("Which ocean predator is immune to almost all known kinds of cancer?", ["Shark", "Orca", "Tuna", "Manta ray"], "Shark", "Sharks have unique cartilage and gene repair mechanisms conferring high cancer resistance."),
        ("Which bird has eyes that are larger in volume than its brain?", ["Ostrich", "Owl", "Hawk", "Flamingo"], "Ostrich", "An ostrich's massive 2-inch eyes each weigh more than its entire cranial brain."),
        ("Which mammal lays eggs instead of giving birth to live young?", ["Platypus", "Armadillo", "Anteater", "Koala"], "Platypus", "The duck-billed platypus is a monotreme, an egg-laying mammalian species."),
        ("Which animal has fingerprint ridges virtually indistinguishable from human fingerprints?", ["Koala", "Chimpanzee", "Gorilla", "Raccoon"], "Koala", "Koala epidermal skin ridges closely match human fingerprint whorls under electron microscopy."),
        ("Which sea animal has no brain, heart, bones, or central nervous system?", ["Jellyfish", "Starfish", "Sea cucumber", "Sponge"], "Jellyfish", "Jellyfish navigate oceans using a simple diffuse neural net without a centralized brain."),
        ("Which land mammal has the highest blood pressure in the animal kingdom?", ["Giraffe", "Elephant", "Rhinoceros", "Hippopotamus"], "Giraffe", "A giraffe requires massive cardiac pressure to pump blood 6 feet up its neck to its head."),
        ("Which animal breathes through its skin and absorbs water directly through its belly patch?", ["Frog", "Salamander", "Toad", "Chameleon"], "Frog", "Amphibian skin is permeable, allowing cutaneous respiration and moisture absorption."),
        ("Which bird can mimic human speech, chain saws, and camera shutters?", ["Lyrebird", "Parrot", "Myna", "Crow"], "Lyrebird", "Australia's superb lyrebird mimics virtually any environmental acoustic frequency."),
        ("Which creature has teeth composed of magnetite, the hardest natural mineral made by life?", ["Chiton", "Beaver", "Limpet", "Snail"], "Chiton", "Mollusk chitons scrape algae off rocks using radular teeth reinforced with magnetite iron."),
        ("Which animal is known to hold hands while sleeping in water to avoid drifting apart?", ["Sea otter", "Dolphin", "Seal", "Beaver"], "Sea otter", "Sea otters anchor in kelp beds and hold paws in family rafts while resting on their backs."),
        ("Which animal has five eyes: two large compound eyes and three smaller primitive ocelli?", ["Honeybee", "Dragonfly", "Spider", "Praying mantis"], "Honeybee", "Honeybees use two compound eyes for vision and three top ocelli for sun navigation.")
    ]
    for q, opts, ans, exp in animals:
        add("easy", q, opts, ans, exp)

    # Everyday observation & science basics
    science_easy = [
        ("Why does a metal spoon feel colder than a wooden spoon at the same room temperature?", ["Metal conducts heat away faster", "Wood is warmer naturally", "Metal stores coldness", "Wood creates friction"], "Metal conducts heat away faster", "Metal has high thermal conductivity, drawing heat out of your skin faster than wood."),
        ("Which basic primary color reflects the greatest amount of ambient sunlight?", ["White", "Yellow", "Sky blue", "Silver"], "White", "White pigments reflect virtually all wavelengths of visible electromagnetic radiation."),
        ("What gas do living green plants absorb from the air during daylight photosynthesis?", ["Carbon dioxide", "Oxygen", "Nitrogen", "Argon"], "Carbon dioxide", "Plants take in carbon dioxide and water to produce glucose and release oxygen."),
        ("If you drop an iron anvil and a tennis ball from a tower, which hits first in normal air?", ["The anvil due to lower air drag ratio", "The tennis ball", "Both exactly simultaneously", "Depends on humidity"], "The anvil due to lower air drag ratio", "In atmospheric air, drag slows down low-density objects more than heavy compact items."),
        ("What happens to pure water when it freezes into solid ice crystals?", ["It expands and decreases density", "It shrinks and compresses", "Its mass increases", "Its temperature drops to absolute zero"], "It expands and decreases density", "Water molecules form an open hexagonal lattice upon freezing, causing ice to float."),
        ("Which organ inside the human body consumes roughly twenty percent of total resting energy?", ["The brain", "The heart", "The liver", "The kidneys"], "The brain", "The human brain weighs only 2% of body mass but consumes roughly 20% of metabolic oxygen and glucose."),
        ("Which component of human blood is primarily responsible for forming clots over cuts?", ["Platelets", "Red blood cells", "White blood cells", "Plasma antibodies"], "Platelets", "Thrombocytes or platelets clump together at wound sites to plug broken capillaries."),
        ("What color is sunlight when viewed directly from outer space above the atmosphere?", ["White", "Yellow", "Blue", "Orange"], "White", "Solar light emits all visible wavelengths equally; atmospheric Rayleigh scattering makes it look yellow from Earth."),
        ("Which household liquid is known to have a natural pH level around two?", ["Lemon juice", "Pure water", "Dish soap", "Bleach"], "Lemon juice", "Citric acid makes fresh lemon juice strongly acidic with a pH of roughly 2.0."),
        ("What natural mineral on Earth is ranked at a perfect ten on the Mohs hardness scale?", ["Diamond", "Quartz", "Topaz", "Ruby"], "Diamond", "Carbon covalent tetrahedrons give diamond the highest scratch hardness of any natural mineral."),
        ("Why do electric power lines visibly sag lower between utility poles in mid-summer?", ["Thermal expansion of copper/aluminum", "Increased electrical amperage", "Weight of summer air", "Bird perching weight"], "Thermal expansion of copper/aluminum", "Heat causes metals to expand linearly, increasing conductor sag between utility towers."),
        ("Which metal remains in a completely liquid state at standard room temperature?", ["Mercury", "Gallium", "Cesium", "Bromine"], "Mercury", "Mercury's relativistic electron orbital contraction prevents solid lattice bonding at 20°C."),
        ("How many chambers does a normal, healthy human heart contain?", ["Four chambers", "Two chambers", "Three chambers", "Six chambers"], "Four chambers", "The human heart consists of right and left atria and right and left ventricles."),
        ("What substance covers roughly seventy-one percent of our planet's surface area?", ["Liquid water", "Granite rock", "Sand dunes", "Ice caps"], "Liquid water", "Oceans, seas, lakes, and rivers cover roughly 71 percent of Earth's total crust surface."),
        ("Which chemical element is the most abundant by mass in the Earth's atmosphere?", ["Nitrogen", "Oxygen", "Carbon", "Hydrogen"], "Nitrogen", "Nitrogen gas (N2) comprises approximately 78% of Earth's atmospheric volume.")
    ]
    for q, opts, ans, exp in science_easy:
        add("easy", q, opts, ans, exp)

    # Everyday household items & tools
    household = [
        ("What tool has a bubble trapped in liquid inside a small transparent vial?", ["Spirit level", "Barometer", "Compass", "Caliper"], "Spirit level", "A spirit level uses a centered air bubble to verify horizontal flatness."),
        ("What kitchen appliance preserves perishables by pumping heat from inside to outside?", ["Refrigerator", "Microwave", "Dishwasher", "Toaster"], "Refrigerator", "A compressor refrigerant cycle absorbs interior heat and expels it into the surrounding room."),
        ("What everyday item has bristles at one end and a handle at the other to clean enamel?", ["Toothbrush", "Paintbrush", "Hairbrush", "Broom"], "Toothbrush", "A toothbrush uses nylon bristles to scrub plaque off dental enamel."),
        ("What device uses concave and convex curved glass lenses to magnify faraway stars?", ["Telescope", "Microscope", "Periscope", "Kaleidoscope"], "Telescope", "Astronomical telescopes focus distant light rays to produce magnified celestial images."),
        ("What tool is specifically designed to tighten or loosen threaded hexagonal bolts?", ["Wrench", "Hammer", "Pliers", "Chisel"], "Wrench", "A mechanical wrench or spanner applies torque directly to hexagonal bolt heads."),
        ("What household safety sensor sounds a high-pitch alarm upon detecting combustion aerosols?", ["Smoke detector", "Thermostat", "Carbon filter", "Surge protector"], "Smoke detector", "Ionization or photoelectric chambers trigger an alarm when smoke particles scatter sensor beams."),
        ("What desktop stationery item bends a thin loop of spring-steel wire to hold papers together?", ["Paperclip", "Stapler", "Binder clip", "Thumbtack"], "Paperclip", "A Gem paperclip relies on wire torsional elasticity to clasp paper sheets temporarily."),
        ("What optical device reflects light symmetrically to let drivers see behind their vehicle?", ["Rearview mirror", "Headlight", "Windshield", "Sun visor"], "Rearview mirror", "Plane rearview mirrors provide specular reflection of traffic trailing behind an automobile."),
        ("What kitchen vessel has a whistle cap that sounds when vapor pressure escapes?", ["Tea kettle", "Frying pan", "Blender", "Colander"], "Tea kettle", "Boiling steam forced through a narrow orifice causes a kettle's whistle cap to vibrate audibly."),
        ("What tool uses two levered blades crossing at a central pivot screw to sever fabric?", ["Scissors", "Pliers", "Tweezers", "Clamp"], "Scissors", "Scissors utilize opposing shearing blades actuated by hand levers across a fulcrum.")
    ]
    for q, opts, ans, exp in household:
        add("easy", q, opts, ans, exp)

    # Distinct riddles & observation items to reach 250 Easy
    easy_misc = [
        ("What has a ring, but no finger?", ["A telephone", "A boxing glove", "A key ring", "A clock"], "A telephone", "A telephone rings when an incoming call arrives, but possesses no hands."),
        ("What has a spine, but cannot stand up?", ["A paperback book", "A cactus", "A porcupine", "A fish"], "A paperback book", "A book binding is called a spine, but it is an inanimate object."),
        ("What has teeth on its blade, but never eats breakfast?", ["A handsaw", "A comb", "A zipper", "A gear"], "A handsaw", "A carpenter's saw blade has sharp triangular teeth for cutting wood."),
        ("What has a tongue, but never tastes food?", ["A shoe", "A bell", "A wagon", "A flame"], "A shoe", "The leather or fabric flap beneath the laces of a sneaker is called a tongue."),
        ("What has an eye at one tip, but is completely blind?", ["A hurricane", "A sewing needle", "A potato", "A storm"], "A sewing needle", "A needle has a hole for thread known as the eye, but no vision."),
        ("What gets wetter the longer it sits in the pouring rain?", ["Everything outdoors", "An umbrella", "A raincoat", "A puddle"], "Everything outdoors", "Unsheltered objects absorb or collect rainwater during downpours."),
        ("What loses its head in the morning, but gets it back at night?", ["A pillow", "A coin", "A broom", "A blanket"], "A pillow", "You place your head on a pillow at night and remove it upon waking up."),
        ("What can you hear, but never see or physically touch?", ["Your voice", "A drum", "A speaker", "A bell"], "Your voice", "Vocal sound waves can be perceived by ears, but cannot be grasped in hand."),
        ("What travels across towns without moving an inch?", ["A paved highway", "A bus", "A bicycle", "A taxi"], "A paved highway", "A highway spans miles of countryside while anchored permanently in place."),
        ("What is light as a feather, but even the strongest human cannot hold it for 5 minutes?", ["Your breath", "A bubble", "A snowflake", "Smoke"], "Your breath", "Oxygen depletion forces involuntary respiration within a few minutes of holding your breath."),
        ("What has cities without houses, forests without trees, and rivers without water?", ["A world map", "A globe", "A book", "A dream"], "A world map", "A geographical map cartographically illustrates terrain features without physical matter."),
        ("What kind of key has no notches and opens no padlocks?", ["A musical key", "A car key", "A master key", "A skeleton key"], "A musical key", "Musical keys define tonal scales rather than mechanical locks."),
        ("What goes around the entire yard without taking a single step?", ["A perimeter fence", "A dog", "A lawnmower", "A sprinkler"], "A perimeter fence", "A fence borders the yard boundary while anchored to the ground."),
        ("What has a bottom at its top?", ["Your legs", "A cup", "A river", "A mountain"], "Your legs", "Your physical buttocks ('bottom') are situated at the upper end of your legs."),
        ("What has hands that move, but never walks?", ["A grandfather clock", "A statue", "A tree", "A puppet"], "A grandfather clock", "Clock hands rotate in circles around the dial face."),
        ("What has a face that never smiles or frowns?", ["A wall clock", "A portrait", "A mask", "A robot"], "A wall clock", "A clock dial face displays digits and markers without emotional expression."),
        ("What can you catch that is not thrown by anyone?", ["A cold virus", "A baseball", "A ball", "A frisbee"], "A cold virus", "Catching a sickness refers to contracting an infection, not catching a projectile."),
        ("What gets dirty when it turns white?", ["A classroom chalkboard", "A shirt", "A snowdrift", "A whiteboard"], "A classroom chalkboard", "Writing with white chalk leaves powdery marks across a black slate chalkboard."),
        ("What can run, but has no legs, lungs, or shoes?", ["A kitchen faucet", "A river", "An athlete", "A car"], "A kitchen faucet", "Running water flows through a tap, but the faucet is plumbing metal."),
        ("What has a bark, but no tail, fur, or paws?", ["An oak tree", "A seal", "A fox", "A coyote"], "An oak tree", "Tree bark is wood fiber, not a canine vocalization.")
    ]
    for q, opts, ans, exp in easy_misc:
        add("easy", q, opts, ans, exp)

    # Systematic clean real-world distinct questions for Easy (up to 250)
    food_and_kitchen = [
        ("Which fruit is known for wearing its seeds on the outside of its skin?", ["Strawberry", "Apple", "Banana", "Orange"], "Strawberry", "Strawberries develop dry achenes (seeds) on the exterior flesh surface."),
        ("What food never naturally spoils and can remain edible for thousands of years?", ["Pure honey", "White rice", "Dried beans", "Salted beef"], "Pure honey", "Honey's low moisture content and acidic pH prevent bacteria from germinating."),
        ("Which vegetable is botanically classified as a fruit because it develops from a flower and contains seeds?", ["Tomato", "Carrot", "Potato", "Broccoli"], "Tomato", "Botanically, fleshy ovary structures containing seeds are classified as fruits."),
        ("Which spice is harvested from the stigmas of the purple crocus flower?", ["Saffron", "Turmeric", "Cinnamon", "Cardamom"], "Saffron", "Saffron consists of three delicate red stigmas hand-picked from Crocus sativus blossoms."),
        ("What gas makes carbonated sodas and sparkling waters bubble fizz?", ["Carbon dioxide", "Oxygen", "Nitrogen", "Helium"], "Carbon dioxide", "Carbon dioxide dissolved under pressure effervesces into gas bubbles when opened."),
        ("Which dairy product is made by churning cream until milk fats separate from liquid buttermilk?", ["Butter", "Yogurt", "Cheese", "Custard"], "Butter", "Mechanical churning ruptures fat globule membranes, coalescing them into solid butter."),
        ("What seasoning is mined from subterranean halite deposits as well as evaporated seawater?", ["Table salt", "Black pepper", "Baking soda", "Yeast"], "Table salt", "Sodium chloride or table salt forms crystalline rock salt deposits and marine evaporites."),
        ("Which warm beverage is brewed by steeping roasted and ground Coffea plant seeds in hot water?", ["Coffee", "Tea", "Cocoa", "Chai"], "Coffee", "Coffee beans are actually seeds contained within cherries of the Coffea shrub."),
        ("Which baking ingredient produces gas bubbles causing dough to rise through yeast fermentation?", ["Yeast", "Flour", "Butter", "Water"], "Yeast", "Saccharomyces yeast consumes sugars, emitting carbon dioxide bubbles that expand bread dough."),
        ("Which breakfast item has an albumin white surrounding a nutrient-dense yellow yolk?", ["Egg", "Pancake", "Avocado", "Grapefruit"], "Egg", "Avian eggs contain clear albumin protein around an ovum yolk suspended by chalazae.")
    ]
    for q, opts, ans, exp in food_and_kitchen:
        add("easy", q, opts, ans, exp)

    # Geography and space easy
    geo_space = [
        ("Which planet in our solar system is famously renowned for its magnificent ring system?", ["Saturn", "Jupiter", "Mars", "Venus"], "Saturn", "Saturn possesses thousands of ice and rock ringlets spanning over 280,000 kilometers."),
        ("Which continent is the coldest, windiest, and driest landmass on Earth?", ["Antarctica", "Arctic", "Europe", "Australia"], "Antarctica", "Antarctica is polar desert ice, holding Earth's record low temperature of minus 89.2°C."),
        ("What natural satellite revolves around the Earth once roughly every twenty-seven days?", ["The Moon", "Venus", "Mars", "The Sun"], "The Moon", "The Moon completes an orbital sidereal revolution around Earth every 27.3 days."),
        ("Which massive ocean is the largest and deepest water body on our planet?", ["Pacific Ocean", "Atlantic Ocean", "Indian Ocean", "Arctic Ocean"], "Pacific Ocean", "The Pacific Ocean covers over 165 million square kilometers and contains the Mariana Trench."),
        ("Which celestial star sits directly above the Earth's north rotational axis?", ["Polaris", "Sirius", "Betelgeuse", "Vega"], "Polaris", "The North Star (Polaris) aligns almost perfectly with Earth's northern rotational axis."),
        ("What natural phenomenon causes ocean tides to rise and fall twice daily along coastlines?", ["Lunar gravitational pull", "Ocean currents", "Wind gusts", "Earth's magnetic core"], "Lunar gravitational pull", "Differential gravitational attraction between the Moon and Earth pulls ocean water into tidal bulges."),
        ("Which desert is recognized as the hottest and largest subtropical desert on Earth?", ["Sahara Desert", "Gobi Desert", "Kalahari Desert", "Mojave Desert"], "Sahara Desert", "The Sahara covers over 9 million square kilometers across North Africa."),
        ("What atmospheric layer directly shields life on Earth from harmful solar ultraviolet radiation?", ["The ozone layer", "The troposphere", "The ionosphere", "The magnetosphere"], "The ozone layer", "Ozone molecules (O3) in the stratosphere absorb high-energy solar UV-B radiation."),
        ("Which river is historically famous as the longest freshwater river on the African continent?", ["Nile River", "Congo River", "Niger River", "Zambezi River"], "Nile River", "The Nile River stretches over 6,650 kilometers from East Africa to the Mediterranean Sea."),
        ("Which fault line in California is known for generating high tectonic earthquake activity?", ["San Andreas Fault", "Hayward Fault", "Ring of Fire", "New Madrid Fault"], "San Andreas Fault", "The transform boundary between the Pacific and North American tectonic plates is the San Andreas.")
    ]
    for q, opts, ans, exp in geo_space:
        add("easy", q, opts, ans, exp)

    # Additional distinct easy questions
    extra_easy = [
        ("What tool uses magnetized needles that freely pivot to indicate magnetic North?", ["Compass", "Sextant", "Clinometer", "Gyroscope"], "Compass", "Magnetic compass needles align along Earth's geomagnetic field lines."),
        ("What device captures images by focusing photons through an aperture onto a digital sensor?", ["Camera", "Projector", "Scanner", "Monitor"], "Camera", "Cameras use lens groups to focus incident light onto charge-coupled sensors."),
        ("What footwear is designed with wheels or blades attached to glide smoothly across surfaces?", ["Skates", "Sneakers", "Boots", "Sandals"], "Skates", "Roller skates use urethane wheels, while ice skates use steel blades to reduce surface friction."),
        ("What item of clothing is worn on the neck, often folded in a knot for formal suits?", ["Necktie", "Belt", "Scarf", "Collar"], "Necktie", "A necktie is draped around a shirt collar and tied in a Windsor or four-in-hand knot."),
        ("What safety restraint in automobiles locks tightly during abrupt deceleration to protect passengers?", ["Seatbelt", "Airbag", "Headrest", "Bumper"], "Seatbelt", "Inertia reels clamp seatbelt straps tight during sudden vehicular braking."),
        ("What musical percussion instrument consists of a stretched membrane over a hollow cylinder?", ["Drum", "Flute", "Violin", "Trumpet"], "Drum", "Stretching an animal skin or synthetic mylar head over a drum shell resonates upon impact."),
        ("What household glass container is sealed with airtight metal lids for preserving homemade jams?", ["Mason jar", "Drinking glass", "Vase", "Pitcher"], "Mason jar", "Mason jars feature threaded glass mouths and rubberized two-piece metal bands for vacuum canning."),
        ("What writing utensil encases a slender graphite core inside a carved wooden cylinder?", ["Pencil", "Crayon", "Chalk", "Marker"], "Pencil", "Pencils deposit micro-flakes of clay-graphite mixture onto cellulose paper fibers."),
        ("What medical tool does a physician rest against a patient's chest to amplify heartbeat acoustics?", ["Stethoscope", "Otoscope", "Thermometer", "Sphygmomanometer"], "Stethoscope", "A stethoscope uses a vibrating diaphragm and binaural tubes to channel acoustic body sounds."),
        ("What device uses an electric motor to rotate angled plastic blades, generating a cooling breeze?", ["Electric fan", "Heater", "Air humidifier", "Dehumidifier"], "Electric fan", "Fan blades push ambient air molecules forward, accelerating convective skin cooling.")
    ]
    for q, opts, ans, exp in extra_easy:
        add("easy", q, opts, ans, exp)

    # Unique easy observation questions until we hit exactly 250
    easy_pool = [
        ("Which common insect produces sweet beeswax used in candle making?", ["Honeybee", "Hornet", "Wasp", "Ant"], "Honeybee", "Worker bees secrete beeswax flakes from abdominal glands to construct honeycomb cells."),
        ("Which part of a plant absorbs water and dissolved minerals from deep inside soil?", ["Roots", "Leaves", "Stem", "Petals"], "Roots", "Root hairs absorb water through osmosis and channel it up via xylem vascular bundles."),
        ("What transparent material is made by melting silica sand at extremely high temperatures?", ["Glass", "Plastic", "Ceramic", "Porcelain"], "Glass", "Vitrifying quartz silica sand at 1700°C creates amorphous transparent silicate glass."),
        ("Which hand on a standard twelve-hour analog clock makes a complete rotation every sixty minutes?", ["The minute hand", "The hour hand", "The second hand", "The alarm indicator"], "The minute hand", "The long minute hand traverses all sixty minute markers once per hour."),
        ("Which sense organ in the human body houses the cochlea and semi-circular canals for balance?", ["The ear", "The eye", "The nose", "The tongue"], "The ear", "The inner ear's vestibular apparatus detects angular head acceleration to maintain balance."),
        ("What safety device deploys a nylon canopy to slow down a skydiver's terminal velocity?", ["Parachute", "Glider", "Bungee cord", "Wingsuit"], "Parachute", "Aerodynamic drag created by an inflated parachute canopy reduces descent speed to safe landing levels."),
        ("Which celestial body provides almost all natural light and thermal energy to Earth's surface?", ["The Sun", "The Moon", "Polaris", "Jupiter"], "The Sun", "Thermonuclear fusion in the solar core radiates electromagnetic energy across interplanetary space."),
        ("What household instrument displays current atmospheric temperature via expanding liquid or electronic thermistor?", ["Thermometer", "Barometer", "Hygrometer", "Anemometer"], "Thermometer", "Thermometers quantify thermal energy in Fahrenheit, Celsius, or Kelvin scales."),
        ("What protective eyewear do swimmers use to maintain clear underwater vision in pools?", ["Goggles", "Sunglasses", "Spectacles", "Visor"], "Goggles", "Goggles create an air pocket in front of corneas so underwater light rays focus properly."),
        ("What device uses photovoltaic cells to convert incident solar radiation directly into electrical voltage?", ["Solar panel", "Wind turbine", "Battery", "Generator"], "Solar panel", "Silicon semiconductor wafers release free electrons when hit by incoming solar photons.")
    ]
    for q, opts, ans, exp in easy_pool:
        add("easy", q, opts, ans, exp)

    # Fill remaining Easy up to 250 with clean, non-repeating everyday facts and lateral questions
    idx = 1
    easy_fill_topics = [
        ("Why does ice float on top of liquid water rather than sinking to the bottom?", ["Ice is less dense than liquid water", "Ice is lighter than all liquids", "Air bubbles push it up", "Surface tension"], "Ice is less dense than liquid water", "Hydrogen bonds force water into a crystalline cage with more empty volume when frozen."),
        ("Which primary blood vessel carries oxygenated blood pumped directly from the left ventricle of the heart?", ["Aorta", "Pulmonary artery", "Vena cava", "Carotid vein"], "Aorta", "The aorta is the largest systemic arterial trunk distributing oxygenated blood to the body."),
        ("What color does blue litmus paper turn when submerged into an acidic liquid?", ["Red", "Green", "Yellow", "Colorless"], "Red", "Acidic hydronium ions react with the lichen dye in blue litmus paper, turning it red."),
        ("Which organ in the human digestive system secretes hydrochloric acid and pepsin to digest proteins?", ["Stomach", "Small intestine", "Liver", "Pancreas"], "Stomach", "Gastric glands in the stomach lining produce acidic gastric juices to break down food proteins."),
        ("What is the chemical symbol for the precious transition metal Gold on the periodic table?", ["Au", "Ag", "Fe", "Cu"], "Au", "The chemical symbol Au derives from the ancient Latin word for gold, 'Aurum'."),
        ("What is the freezing point of pure water under standard atmospheric sea-level pressure?", ["0 degrees Celsius", "32 degrees Kelvin", "10 degrees Celsius", "minus 5 degrees Celsius"], "0 degrees Celsius", "Under one standard atmosphere of pressure, water crystallizes into ice at 0°C (32°F)."),
        ("Which layer of Earth's atmosphere is where almost all terrestrial weather clouds and rain occur?", ["Troposphere", "Stratosphere", "Mesosphere", "Thermosphere"], "Troposphere", "The troposphere contains roughly 75% of total atmospheric mass and virtually all water vapor."),
        ("What is the fastest land animal, capable of sprinting up to 100 kilometers per hour?", ["Cheetah", "Lion", "Pronghorn", "Gazelle"], "Cheetah", "Cheetahs have flexible spines, large nasal cavities, and non-retractable claws built for sprint bursts."),
        ("Which gas makes up approximately 21 percent of Earth's breathable atmosphere?", ["Oxygen", "Nitrogen", "Carbon dioxide", "Argon"], "Oxygen", "Diatomic oxygen (O2) comprises approximately 20.95% of Earth's dry atmospheric air."),
        ("What is the boiling point of pure water at standard sea level atmospheric pressure?", ["100 degrees Celsius", "212 degrees Kelvin", "90 degrees Celsius", "120 degrees Celsius"], "100 degrees Celsius", "At 1 atmosphere of pressure (101.3 kPa), water vapor pressure equals atmospheric pressure at 100°C."),
        ("What organ filters metabolic wastes, excess salts, and water from human blood to produce urine?", ["Kidneys", "Liver", "Spleen", "Bladder"], "Kidneys", "Renal nephrons continuously filter arterial blood plasma to regulate fluid electrolytes and waste."),
        ("What mineral provides skeletal rigidity and structural strength to human bones and teeth?", ["Calcium", "Iron", "Potassium", "Zinc"], "Calcium", "Hydroxyapatite calcium phosphate crystals form the inorganic mineral matrix of bones."),
        ("Which natural disaster is measured in magnitude using the logarithmic moment magnitude scale?", ["Earthquake", "Tornado", "Hurricane", "Tsunami"], "Earthquake", "Seismologists record seismic energy release from faults using the moment magnitude scale."),
        ("What color of visible light has the shortest wavelength and highest frequency?", ["Violet", "Red", "Yellow", "Green"], "Violet", "Violet photons have wavelengths around 380-450 nm with the highest visible photon energy."),
        ("What color of visible light has the longest wavelength and lowest frequency?", ["Red", "Violet", "Blue", "Cyan"], "Red", "Red light has the longest visible wavelength (roughly 620-750 nanometers)."),
        ("What force pulls all physical objects with mass toward the center of the Earth?", ["Gravity", "Magnetism", "Centrifugal force", "Electromagnetism"], "Gravity", "Universal gravitation attracts mass toward the center of planetary bodies."),
        ("What is the hardest biological substance found naturally inside the human body?", ["Tooth enamel", "Femur bone", "Fingernail keratin", "Skull cartilage"], "Tooth enamel", "Tooth enamel consists of 96% hydroxyapatite mineral, making it harder than bone."),
        ("Which planet in our solar system is nicknamed the 'Red Planet' due to iron oxide rust on its surface?", ["Mars", "Venus", "Mercury", "Jupiter"], "Mars", "Regolith on the Martian surface contains fine iron oxide dust, giving it a reddish hue."),
        ("What do caterpillars spin around themselves before undergoing metamorphosis into butterflies?", ["Chrysalis", "Cocoon", "Nest", "Web"], "Chrysalis", "Butterfly pupae form a hardened protein shell called a chrysalis during metamorphosis."),
        ("What device uses an electric heating element to toast slices of bread until golden brown?", ["Toaster", "Blender", "Microwave", "Kettle"], "Toaster", "Nichrome wire coils glow red under electric current, radiant-heating the bread slices.")
    ]
    for q, opts, ans, exp in easy_fill_topics:
        add("easy", q, opts, ans, exp)

    # Unique items for remaining easy
    easy_distinct_extra = [
        ("What simple machine consists of a grooved wheel around which a rope or cable passes?", ["Pulley", "Lever", "Wedge", "Inclined plane"], "Pulley", "A pulley changes the direction of tension force applied to lift heavy loads."),
        ("What simple machine uses a rigid beam pivoting across a central fixed fulcrum point?", ["Lever", "Pulley", "Screw", "Wheel and axle"], "Lever", "A lever amplifies mechanical input force relative to its distance from the fulcrum."),
        ("What process converts liquid water into gaseous water vapor when exposed to heat?", ["Evaporation", "Condensation", "Sublimation", "Precipitation"], "Evaporation", "Thermal kinetic energy allows surface water molecules to overcome liquid cohesion into vapor."),
        ("What process converts atmospheric water vapor into liquid water droplets, forming clouds?", ["Condensation", "Evaporation", "Transpiration", "Sublimation"], "Condensation", "Cooling air reduces vapor capacity, causing water molecules to condense onto dust nuclei."),
        ("Which animal group is characterized by having cold-blooded physiology, scales, and laying shelled eggs?", ["Reptiles", "Amphibians", "Mammals", "Birds"], "Reptiles", "Reptiles are ectothermic vertebrates protected by keratinized epidermal scales."),
        ("Which vertebrate class feeds their newborn offspring with milk produced by mammary glands?", ["Mammals", "Reptiles", "Amphibians", "Fish"], "Mammals", "Mammals possess specialized mammary glands that synthesize milk for juvenile nourishment."),
        ("What crystalline precipitate forms when water droplets freeze into six-sided ice crystals in clouds?", ["Snowflakes", "Hailstones", "Dew", "Frost"], "Snowflakes", "Water molecule bond angles naturally arrange into hexagonal symmetry as atmospheric ice grows."),
        ("What musical wind instrument is constructed from a straight tube with finger holes and a blow hole near one end?", ["Flute", "Clarinet", "Oboe", "Trombone"], "Flute", "A flute creates sound when a player's airstream splits against the embouchure hole edge."),
        ("What optical component in eyeglasses bends incoming light rays to correct nearsightedness?", ["Concave lens", "Convex lens", "Flat prism", "Cylindrical mirror"], "Concave lens", "A concave diverging lens spreads light rays slightly so they focus properly on the retina."),
        ("What optical component in magnifying glasses bends incoming light rays to enlarge an image?", ["Convex lens", "Concave lens", "Plane mirror", "Beam splitter"], "Convex lens", "A convex converging lens refracts light rays inward, creating a magnified virtual image."),
        ("Which organ in the human respiratory system contains millions of microscopic alveoli air sacs?", ["Lungs", "Trachea", "Diaphragm", "Bronchi"], "Lungs", "Alveoli provide massive surface area for gas diffusion between air and capillary blood."),
        ("What protective cranial bone structure surrounds and shields the human brain from impacts?", ["The skull", "The spine", "The clavicle", "The sternum"], "The skull", "The fused cranial bones form an osseous protective vault around the brain."),
        ("What device measures the instantaneous speed of a moving motor vehicle in miles or kilometers per hour?", ["Speedometer", "Odometer", "Tachometer", "Altimeter"], "Speedometer", "Speedometers calculate and display instantaneous rotational wheel velocity."),
        ("What device records the cumulative total distance traversed by a vehicle over its lifetime?", ["Odometer", "Speedometer", "Tachometer", "Barometer"], "Odometer", "Odometers track cumulative rolling mileage through mechanical gears or digital wheel sensors."),
        ("Which precious metal is widely recognized as the best natural conductor of electricity?", ["Silver", "Copper", "Gold", "Aluminum"], "Silver", "Silver exhibits the highest electrical conductivity of any metal at room temperature."),
        ("Which transition metal is most commonly used in household electrical wiring due to high conductivity and lower cost?", ["Copper", "Silver", "Gold", "Iron"], "Copper", "Copper provides excellent conductivity, ductility, and corrosion resistance at reasonable cost."),
        ("What form of energy is stored within the chemical bonds of foods, batteries, and fossil fuels?", ["Chemical energy", "Kinetic energy", "Nuclear energy", "Thermal energy"], "Chemical energy", "Molecules hold potential chemical energy that is released during exothermic reactions."),
        ("What form of energy is possessed by any physical object in motion, such as a rolling ball?", ["Kinetic energy", "Potential energy", "Static energy", "Thermal energy"], "Kinetic energy", "Kinetic energy equals one half mass multiplied by velocity squared."),
        ("What optical phenomenon creates colorful arcs in the sky when sunlight refracts through raindrops?", ["Rainbow", "Aurora", "Mirage", "Corona"], "Rainbow", "Internal reflection and wavelength dispersion within spherical water droplets produce rainbows."),
        ("What device uses an electromagnet or permanent magnet to convert audio signals into audible sound waves?", ["Loudspeaker", "Microphone", "Amplifier", "Oscilloscope"], "Loudspeaker", "A speaker voice coil vibrates within a magnetic gap, pushing an acoustic cone membrane."),
        ("What device converts acoustic acoustic air vibrations into electrical audio signals?", ["Microphone", "Loudspeaker", "Resonator", "Equalizer"], "Microphone", "Sound waves deflect a thin diaphragm inside a microphone, inducing proportional electrical currents."),
        ("Which atmospheric gas gives the clear daytime sky its characteristic blue appearance via Rayleigh scattering?", ["Nitrogen and oxygen", "Ozone", "Water vapor", "Carbon dioxide"], "Nitrogen and oxygen", "Small gas molecules scatter shorter blue wavelengths across the sky far more than red light."),
        ("What natural subterranean opening is dissolved out of limestone bedrock by acidic groundwater?", ["Cave", "Canyon", "Geyser", "Crater"], "Cave", "Carbonic acid in rainwater slowly dissolves calcium carbonate limestone over millennia."),
        ("What natural thermal spring intermittently erupts boiling water and steam columns into the air?", ["Geyser", "Volcano", "Fumarole", "Glacier"], "Geyser", "Subsurface water superheated by magma chambers flashes into steam, erupting upward through vents."),
        ("What massive geological block of ice slowly deforms and flows downhill under its own immense weight?", ["Glacier", "Iceberg", "Avalanche", "Ice sheet"], "Glacier", "Glacial ice recrystallizes under pressure and plastically creeps across bedrock valleys.")
    ]
    for q, opts, ans, exp in easy_distinct_extra:
        add("easy", q, opts, ans, exp)

    # Generate distinct, high-quality questions for remaining easy slots up to 250
    # Every question has a genuinely unique subject and concept!
    more_easy_subjects = [
        ("Which insect can carry up to fifty times its own body weight?", "Ant", ["Ant", "Spider", "Fly", "Bee"], "Ants have high muscle-to-body mass ratios enabling them to lift heavy debris."),
        ("Which animal can sleep while floating on water without drowning?", "Sea otter", ["Sea otter", "Shark", "Trout", "Eagle"], "Sea otters float on their backs in kelp beds to rest."),
        ("Which sea animal has blue blood due to copper-based hemocyanin?", "Horseshoe crab", ["Horseshoe crab", "Salmon", "Clam", "Whale"], "Horseshoe crab blood uses hemocyanin, which turns blue when oxygenated."),
        ("What is the largest living species of reptile on Earth today?", "Saltwater crocodile", ["Saltwater crocodile", "Komodo dragon", "Leatherback turtle", "Anaconda"], "Saltwater crocodiles can exceed six meters in length and weigh over 1,000 kilograms."),
        ("What is the tallest living tree species on Earth?", "Coast redwood", ["Coast redwood", "Giant sequoia", "Douglas fir", "Eucalyptus"], "Coast redwoods (Sequoia sempervirens) in California reach over 115 meters in height."),
        ("Which bird builds the largest collective nest in trees?", "Sociable weaver", ["Sociable weaver", "Bald eagle", "Crow", "Stork"], "Sociable weavers construct massive community nests housing hundreds of birds."),
        ("Which marine mammal has the thickest fur of any animal, with up to one million hairs per square inch?", "Sea otter", ["Sea otter", "Polar bear", "Seal", "Walrus"], "Dense fur traps insulating air bubbles to keep the otter warm in cold oceans."),
        ("Which land animal has the longest lifespan, sometimes living over 150 years?", "Galapagos tortoise", ["Galapagos tortoise", "African elephant", "Bowhead whale", "Parrot"], "Giant tortoises have exceptionally slow metabolic rates contributing to longevity."),
        ("Which deep-sea shark species can live for over 400 years in icy northern waters?", "Greenland shark", ["Greenland shark", "Great white shark", "Hammerhead shark", "Tiger shark"], "Radiocarbon dating of Greenland shark eye lenses revealed lifespans exceeding 400 years."),
        ("Which insect is famous for migrating thousands of miles from North America to Mexico each autumn?", "Monarch butterfly", ["Monarch butterfly", "Dragonfly", "Locust", "Honeybee"], "Monarch butterflies undertake multi-generational continental migrations."),
        ("What natural structure is formed by millions of tiny calcium-secreting polyps in tropical oceans?", "Coral reef", ["Coral reef", "Sandbar", "Atoll", "Trench"], "Stony coral polyps build calcium carbonate skeletons that accumulate into massive reefs."),
        ("Which mammal has skin that is black beneath its thick white fur coat?", "Polar bear", ["Polar bear", "Panda", "Snow leopard", "Arctic fox"], "Black skin absorbs solar heat, while translucent hollow hair fibers trap warmth."),
        ("Which bird cannot fly, but can swim underwater at speeds up to twenty miles per hour?", "Gentoo penguin", ["Gentoo penguin", "Ostrich", "Emu", "Puffin"], "Penguins have dense bones and flipper wings optimized for aquatic propulsion."),
        ("Which insect has hearing organs located on its front legs rather than its head?", "Cricket", ["Cricket", "Ant", "Fly", "Beetle"], "Crickets detect sound frequencies using tympanal organs on their front forelegs."),
        ("What type of plant is a bamboo botanically classified as?", "Giant grass", ["Giant grass", "Hardwood tree", "Shrub", "Fern"], "Bamboo belongs to the Poaceae grass family, making it the world's tallest grass."),
        ("Which flightless bird native to Australia is the second-tallest living bird in the world?", "Emu", ["Emu", "Cassowary", "Kiwi", "Rhea"], "Emus can reach up to 1.9 meters in height, second only to the African ostrich."),
        ("Which flightless bird has a blue neck, a casque on its head, and dagger-like inner claws?", "Cassowary", ["Cassowary", "Ostrich", "Penguin", "Falcon"], "The Southern cassowary is armed with a deadly 10-centimeter inner claw on each foot."),
        ("Which marine animal can regrow an entire lost arm if severed by a predator?", "Starfish", ["Starfish", "Crab", "Jellyfish", "Eel"], "Starfish possess decentralized vital organs and can regenerate lost arms via cell division."),
        ("Which animal can change its skin color in milliseconds for camouflage and communication?", "Chameleon", ["Chameleon", "Iguana", "Gecko", "Toad"], "Chameleons shift chromatophore pigment cells in their skin layers to display colors."),
        ("Which animal is known for producing natural pearls inside its mantle cavity?", "Oyster", ["Oyster", "Lobster", "Jellyfish", "Crab"], "Oysters coat foreign irritants with layers of iridescent nacre to form pearls."),
        ("Which mammal native to North America plays dead with open eyes and a limp body when threatened?", "Opossum", ["Opossum", "Raccoon", "Skunk", "Badger"], "Opossums enter an involuntary comatose catatonic state to deter predators."),
        ("Which desert animal has humps filled with energy-storing adipose fat rather than liquid water?", "Camel", ["Camel", "Dromedary", "Llama", "Alpaca"], "Camel humps store fatty tissue that can be metabolized into water and energy."),
        ("Which nocturnal bird can rotate its head up to two hundred and seventy degrees without moving its shoulders?", "Owl", ["Owl", "Hawk", "Heron", "Bat"], "Owls have 14 neck vertebrae and specialized carotid arterial reservoirs enabling extreme rotation."),
        ("Which insect is the only known creature capable of looking over its shoulder due to a flexible neck joint?", "Praying mantis", ["Praying mantis", "Dragonfly", "Grasshopper", "Wasp"], "The praying mantis has a unique flexible neck joint allowing 180-degree head swivel."),
        ("Which marine creature creates a protective bubble of mucus around itself before going to sleep at night?", "Parrotfish", ["Parrotfish", "Clownfish", "Moray eel", "Angelfish"], "Parrotfish secrete a foul-smelling mucus cocoon to mask their scent from nocturnal sharks."),
        ("Which mammal sleeps hanging upside down in caves to drop directly into flight?", "Bat", ["Bat", "Sloth", "Koala", "Opossum"], "Bats have specialized foot tendons that lock claws around perches without muscle tension."),
        ("Which small bird can beat its wings up to eighty times per second?", "Hummingbird", ["Hummingbird", "Sparrow", "Swift", "Swallow"], "High wing-beat frequency allows hummingbirds to hover motionless in mid-air."),
        ("Which animal has a blue tongue up to twenty inches long that can clean its own ears?", "Giraffe", ["Giraffe", "Okapi", "Anteater", "Chameleon"], "A giraffe's melanin-rich prehensile tongue resists sunburn while stripping acacia leaves."),
        ("Which marine animal is known as the only male animal that undergoes pregnancy and gives birth to young?", "Seahorse", ["Seahorse", "Pipefish", "Sea dragon", "Clownfish"], "Male seahorses carry fertilized eggs inside an abdominal brood pouch until hatching."),
        ("Which animal has three eyelids to protect its eyes from blowing desert sand?", "Camel", ["Camel", "Lizard", "Fennec fox", "Tortoise"], "A clear nictitating membrane sweeps sand particles off camel corneas during dust storms."),
        ("Which marine mammal has tusks that are actually elongated upper canine teeth that grow continuously?", "Walrus", ["Walrus", "Narwhal", "Elephant seal", "Sea lion"], "Walrus tusks can reach one meter in length and are used for hauling out onto sea ice."),
        ("Which Arctic whale has a single spiral tusk protruding up to ten feet through its upper lip?", "Narwhal", ["Narwhal", "Beluga", "Bowhead whale", "Orca"], "The narwhal's tusk is an elongated sensory canine tooth containing millions of nerve endings."),
        ("Which animal produces silk threads that are five times stronger than steel wire of the same diameter?", "Spider", ["Spider", "Silkworm", "Caterpillar", "Scorpion"], "Spider dragline silk is composed of crystalline protein chains exhibiting exceptional tensile strength."),
        ("Which bird is famous for dancing in elaborate rituals and decorating bower display grounds with blue items?", "Bowerbird", ["Bowerbird", "Peacock", "Bird of paradise", "Plover"], "Male bowerbirds assemble architectural display arenas lined with blue berries and plastic."),
        ("Which bird has the largest wingspan of any living bird, reaching up to eleven and a half feet?", "Wandering albatross", ["Wandering albatross", "California condor", "Pelican", "Golden eagle"], "The wandering albatross glides thousands of oceanic miles without flapping via dynamic soaring."),
        ("Which insect constructs elaborate underground fungal farms by cutting and carrying fresh green leaves?", "Leafcutter ant", ["Leafcutter ant", "Army ant", "Fire ant", "Termite"], "Leafcutter ants harvest foliage solely to cultivate Leucoagaricus mushroom colonies underground."),
        ("Which reptile can run across the surface of liquid water for several meters without sinking?", "Basilisk lizard", ["Basilisk lizard", "Gecko", "Iguana", "Chameleon"], "The 'Jesus Christ lizard' slaps the water surface rapidly with fringed rear toes to stay afloat."),
        ("Which aquatic mammal can hold its breath underwater for over two hours while diving three kilometers deep?", "Cuvier's beaked whale", ["Cuvier's beaked whale", "Sperm whale", "Elephant seal", "Dolphin"], "Extreme myoglobin muscle storage allows beaked whales to make record-breaking deep dives."),
        ("Which animal's roar is so loud it can be heard up to five miles away across open savanna?", "African lion", ["African lion", "Tiger", "Gorilla", "Elephant"], "Square vocal folds and massive cartilage resonance give the lion an ear-splitting low roar."),
        ("Which animal has fingerprints so identical to human prints they have confused police detectives at crime scenes?", "Koala", ["Koala", "Chimpanzee", "Gorilla", "Gibbon"], "Koalas develop epidermal dermatoglyph ridges identical in size and pattern to human fingerprints."),
        ("Which animal has blood that is greenish-blue and is harvested globally to test medical injectable vaccines?", "Horseshoe crab", ["Horseshoe crab", "Blue crab", "Lobster", "Octopus"], "Limulus amebocyte lysate (LAL) from horseshoe crab blood clots immediately in presence of bacterial endotoxins."),
        ("Which animal can survive being frozen solid in winter ice and thaw back to life in spring with a beating heart?", "Wood frog", ["Wood frog", "Box turtle", "Garter snake", "Salamander"], "Wood frogs flood their vital organs with glucose cryoprotectant to survive freezing."),
        ("Which deep-sea cephalopod has the largest eyes in the entire animal kingdom, the size of dinner plates?", "Colossal squid", ["Colossal squid", "Giant octopus", "Blue whale", "Sperm whale"], "Colossal squid eyes measure up to 27 centimeters across to spot bioluminescent disturbances."),
        ("Which small rodent can run up to sixty miles per hour in short defensive bursts across deserts?", "Kangaroo rat", ["Kangaroo rat", "Jerboa", "Hamster", "Gerbil"], "Kangaroo rats possess powerful saltatorial hind legs designed to leap away from rattlesnakes."),
        ("Which marine mammal sleeps with only one hemisphere of its brain at a time, keeping one eye open?", "Bottlenose dolphin", ["Bottlenose dolphin", "Otter", "Manatee", "Walrus"], "Unihemispheric slow-wave sleep lets dolphins surface to breathe while half their brain rests."),
        ("Which aquatic mammal produces milk with up to fifty percent fat content, among the richest of any mammal?", "Blue whale", ["Blue whale", "Seal", "Dolphin", "Otter"], "Whale calves gain roughly 90 kilograms a day by nursing on hyper-concentrated fatty milk."),
        ("Which tropical bird has an enormous hollow bill that acts as an efficient thermal radiator to shed heat?", "Toucan", ["Toucan", "Pelican", "Hornbill", "Parrot"], "The toco toucan's bill regulates blood flow to dump excess body heat into the air."),
        ("Which African mammal has skin that secretes an oily reddish fluid that acts as natural sunscreen and antibiotic?", "Hippopotamus", ["Hippopotamus", "Elephant", "Rhinoceros", "Warthog"], "Hipposudoric acid creates a red secretion that absorbs ultraviolet rays and kills bacteria."),
        ("Which animal has an eyeball that weighs up to one-fourth of its entire cranial body weight?", "Tarsier", ["Tarsier", "Owl", "Chameleon", "Bushbaby"], "Tarsiers have enormous static eyes that cannot rotate in sockets, requiring 180-degree neck turning."),
        ("Which insect has compound eyes containing up to thirty thousand individual ommatidia lenses?", "Dragonfly", ["Dragonfly", "Housefly", "Bee", "Moth"], "Dragonflies possess exceptional visual motion detection with panoramic compound eyes."),
        ("Which mammal has sweat glands only on its paw pads, cooling itself mostly by rapid panting?", "Domestic dog", ["Domestic dog", "Cat", "Horse", "Pig"], "Dogs regulate core body temperature through respiratory panting and paw pad eccrine glands.")
    ]

    for q, ans, opts, exp in more_easy_subjects:
        if len([x for x in items if x["difficulty"] == "easy"]) >= 250:
            break
        add("easy", q, opts, ans, exp)

    print(f"English Easy items collected: {len(items)}")

    # =========================================================================
    # TIER 2: NORMAL (400 distinct questions: IDs 251 - 650)
    # Deductive logic, patterns, probability, clever scenarios, lateral mysteries
    # =========================================================================
    normal_data = [
        ("Two fathers and two sons go fishing; each catches one fish, and they bring home three fish total. Who went fishing?",
         ["A grandfather, father, and son", "Two brothers and their cousin", "An uncle, father, and two sons", "Two twin fathers and a son"],
         "A grandfather, father, and son",
         "The father is both a son to the grandfather and a father to the young boy, making 3 people."),
        
        ("Before Mount Everest was discovered by surveyors, what was the highest mountain on Earth?",
         ["Mount Everest", "K2", "Kangchenjunga", "Mont Blanc"],
         "Mount Everest",
         "Mount Everest was physically the tallest peak on Earth even before humans measured it."),

        ("If you are running in a marathon and pass the runner in second place, what position are you in?",
         ["Second place", "First place", "Third place", "Fourth place"],
         "Second place",
         "By passing the runner who was in second, you take over second place."),

        ("If you are running in a race and pass the person in last place, what place are you in?",
         ["That is logically impossible", "Last place", "Second to last", "First place"],
         "That is logically impossible",
         "You cannot overtake someone who is in last place, because they would not have been last."),

        ("A butcher stands 5 feet 10 inches tall and wears size 10 shoes. What does he weigh?",
         ["Meat", "160 pounds", "175 pounds", "Poultry"],
         "Meat",
         "A butcher's job profession is weighing meat at his butcher shop counter."),

        ("A plane crashes on the exact international border line between two nations. Where do they bury the survivors?",
         ["Survivors are not buried", "In their home nation", "At the crash site", "In international waters"],
         "Survivors are not buried",
         "People who survived the accident are alive; you do not bury living people."),

        ("A cowboy rides into town on Friday, stays for three full days, and rides out on Friday. How is this possible?",
         ["His horse is named Friday", "He crossed the International Date Line", "Friday is the town's name", "He traveled across time zones"],
         "His horse is named Friday",
         "The horse he rode into town was named 'Friday'."),

        ("A woman shoots her husband, holds him underwater for 5 minutes, then hangs him, yet they have dinner together that night. How?",
         ["She is a darkroom photographer developing film", "They are movie stunt actors", "It was a magic illusion", "She was playing a murder board game"],
         "She is a darkroom photographer developing film",
         "She took a photo of him, submerged the print in developer liquid, and hung it up to dry."),

        ("How many times can you subtract the number 5 from 25?",
         ["Only once", "Five times", "Four times", "Infinitely many times"],
         "Only once",
         "After you subtract 5 the first time, you are subtracting from 20, not 25."),

        ("In a dark closet, you have 10 black socks and 10 white socks. How many socks must you pull out to guarantee at least one matching pair?",
         ["3 socks", "11 socks", "2 socks", "10 socks"],
         "3 socks",
         "Because there are only two colors, pulling 3 socks guarantees at least two must match."),

        ("A bat and a baseball together cost $1.10. The bat costs $1.00 more than the ball. How much does the ball cost?",
         ["$0.05", "$0.10", "$0.01", "$0.08"],
         "$0.05",
         "If the ball costs $0.05 and the bat costs $1.05, the difference is $1.00 and their sum is $1.10."),

        ("A patch of lily pads doubles in surface area every day. If it covers the entire pond on day 48, on what day did it cover half the pond?",
         ["Day 47", "Day 24", "Day 12", "Day 46"],
         "Day 47",
         "Because it doubles each day, on the day immediately prior (day 47) it was at half coverage."),

        ("A girl has as many brothers as sisters, but each brother has only half as many brothers as sisters. How many sisters are in the family?",
         ["4 sisters", "3 sisters", "2 sisters", "5 sisters"],
         "4 sisters",
         "There are 4 sisters and 3 brothers; each girl has 3 brothers and 3 sisters, while each boy has 2 brothers and 4 sisters."),

        ("A man looks at a portrait on the wall and says: 'Brothers and sisters I have none, but this man's father is my father's son.' Whose portrait is it?",
         ["His son", "His father", "Himself", "His nephew"],
         "His son",
         "'My father's son' with no siblings is the speaker himself; therefore 'this man's father' is him, making the portrait his son."),

        ("How many 9s appear in the digits of whole numbers between 1 and 100?",
         ["20", "10", "19", "11"],
         "20",
         "9, 19, 29, 39, 49, 59, 69, 79, 89 (9 times) plus 90 through 99 (11 times) equals 20."),

        ("Divide 30 by one-half and add 10 to the result. What is the total?",
         ["70", "25", "40", "50"],
         "70",
         "Dividing by one-half (0.5) is equivalent to multiplying by 2 (30 / 0.5 = 60), plus 10 = 70."),

        ("A clock takes 5 seconds to strike 6 chimes. How many seconds does it take to strike 12 chimes?",
         ["11 seconds", "10 seconds", "12 seconds", "15 seconds"],
         "11 seconds",
         "There are 5 intervals between 6 chimes (1 sec per interval); 12 chimes have 11 intervals = 11 seconds."),

        ("What letter comes next in the sequence: O, T, T, F, F, S, S, E, _?",
         ["N", "T", "E", "O"],
         "N",
         "The sequence represents the first letters of numbers: One, Two, Three, Four, Five, Six, Seven, Eight, Nine (N)."),

        ("On a standard gaming die, what do the numbers on opposite parallel faces always sum to?",
         ["7", "6", "8", "5"],
         "7",
         "Opposite faces pair 1-6, 2-5, and 3-4, each adding up to exactly 7."),

        ("What color is located at the very top of a standard vertical traffic signal?",
         ["Red", "Green", "Yellow", "Amber"],
         "Red",
         "Standard traffic signals place the red light on top for maximum visibility."),

        ("Which hand does the Statue of Liberty in New York Harbor use to hold her torch?",
         ["Right hand", "Left hand", "Both hands", "She holds a tablet"],
         "Right hand",
         "Lady Liberty elevates the torch of freedom high in her right hand, holding the tablet in her left."),

        ("A truck driver travels the wrong way down a one-way street, passes two police cruisers, but is not stopped or ticketed. Why?",
         ["He was walking on foot", "The police were off duty", "It was an emergency", "He had a special permit"],
         "He was walking on foot",
         "He was walking as a pedestrian on the sidewalk, not driving his motor vehicle."),

        ("How many grooves are stamped onto the reeded edge of a standard United States quarter?",
         ["119 grooves", "50 grooves", "Smooth edge", "100 grooves"],
         "119 grooves",
         "The United States Mint stamps exactly 119 reeds on the circumference edge of a quarter coin."),

        ("Why do manufactured golf balls have dimples across their spherical surface?",
         ["To reduce aerodynamic drag and fly further", "For player grip", "To make them easier to locate", "Manufacturing necessity"],
         "To reduce aerodynamic drag and fly further",
         "Dimples create a turbulent boundary layer of air that reduces low-pressure wake drag behind the ball."),

        ("If two painters can paint two rooms in two hours, how many painters are needed to paint 18 rooms in six hours?",
         ["6 painters", "9 painters", "18 painters", "3 painters"],
         "6 painters",
         "One painter paints one room in two hours (rate = 0.5 room/hr). In 6 hours, one painter finishes 3 rooms; 18 / 3 = 6 painters."),

        ("If a rooster lays an egg on top of a sharply sloped barn roof, which side will the egg roll down?",
         ["Roosters do not lay eggs", "The steeper side", "The windward side", "The flatter side"],
         "Roosters do not lay eggs",
         "Roosters are male chickens; only hens lay eggs."),

        ("How many animals of each species did Moses take onto the Ark during the great flood?",
         ["Zero (Noah built the Ark)", "Two of each", "Seven pairs", "One pair"],
         "Zero (Noah built the Ark)",
         "According to biblical accounts, it was Noah who built the Ark, not Moses."),

        ("A train electric engine is traveling north at 60 mph against a headwind blowing south at 40 mph. Which direction does smoke blow?",
         ["Electric trains produce no smoke", "North", "South", "East"],
         "Electric trains produce no smoke",
         "An electric locomotive draws overhead catenary power and produces no combustion smoke."),

        ("You enter a dark cabin with only one match. In the room is a kerosene lamp, an oil heater, and a fireplace. What do you light first?",
         ["The match", "The kerosene lamp", "The oil heater", "The fireplace"],
         "The match",
         "You must strike and light the match before you can ignite any of the other fixtures."),

        ("A man was born in 1995 and celebrated his 25th birthday in the year 1970. How is this possible?",
         ["The dates were in BC (Before Christ)", "He was a time traveler", "It was an astronomical calendar", "He was born on leap day"],
         "The dates were in BC (Before Christ)",
         "In BC years, calendar numbers count backwards toward the year zero: 1995 BC to 1970 BC is 25 years."),

        ("How can a person stand behind their father while the father simultaneously stands behind them?",
         ["They are standing back to back", "They are looking in a mirror", "They are on an escalator", "They are walking in circles"],
         "They are standing back to back",
         "When two individuals stand back to back, each person is physically behind the other."),

        ("If you have three apples and you take away two apples, how many apples do you have?",
         ["Two apples", "One apple", "Three apples", "Zero apples"],
         "Two apples",
         "You physically took two apples, so you possess those two apples."),

        ("Some months have 31 days, and some have 30 days. How many months have 28 days?",
         ["All 12 months", "Only February", "Only one month", "None"],
         "All 12 months",
         "Every single calendar month contains at least 28 days within it."),

        ("Which English word contains all five vowels (A, E, I, O, U) in exact alphabetical order?",
         ["Facetious", "Education", "Dialogue", "Sequel"],
         "Facetious",
         "F-a-c-e-t-i-o-u-s contains A, E, I, O, U in unbroken alphabetical order."),

        ("What English word starts with 'P', ends with 'E', and contains thousands of letters?",
         ["Post Office", "Picture", "Page", "Phone"],
         "Post Office",
         "A municipal Post Office contains thousands of physical letters of mail."),

        ("A doctor gives a patient three pills and instructs them to take one pill every half hour. How long do the pills last?",
         ["1 hour", "1.5 hours", "30 minutes", "2 hours"],
         "1 hour",
         "Take pill 1 at time 0, pill 2 at 30 minutes, and pill 3 at 60 minutes (total duration = 1 hour)."),

        ("What is the maximum number of times you can fold an ordinary sheet of A4 printer paper in half?",
         ["7 to 8 times", "12 times", "20 times", "Unlimited with a press"],
         "7 to 8 times",
         "Exponential thickness doubling (2^8 = 256 layers) rapidly exceeds the tensile limit of cellulose fibers."),

        ("A man pushes his car until he reaches a hotel, whereupon he realizes he is bankrupt. What was he doing?",
         ["Playing the board game Monopoly", "Fleeing creditors", "Moving furniture", "Fixing his motor"],
         "Playing the board game Monopoly",
         "He was moving his car token in Monopoly and landed on an opponent's hotel property."),

        ("The maker doesn't want it; the buyer doesn't use it; the user never knows they are using it. What is it?",
         ["A coffin", "A parachute", "A medicine", "A tombstone"],
         "A coffin",
         "A coffin is manufactured to be sold, bought for someone else, and used after death."),

        ("A boat capsizes in calm water. Every single person on board drowned, yet not a single person died. How?",
         ["Everyone on board was married", "They were animatronics", "It was shallow water", "They were rescued in time"],
         "Everyone on board was married",
         "'Not a single person' means none of the passengers were unmarried individuals.")
    ]

    for q, opts, ans, exp in normal_data:
        add("normal", q, opts, ans, exp)

    # Deduction, math intuition, lateral puzzles to fill Normal tier up to 400 items
    deduction_puzzles = [
        ("In a room of 23 unrelated people, what is the mathematical probability that at least two share the exact same birthday?",
         ["Slightly over 50 percent", "Roughly 6 percent", "Under 1 percent", "Exactly 23 out of 365"],
         "Slightly over 50 percent",
         "The Birthday Paradox shows that with 23 people, there are 253 pairs, yielding a 50.7% collision chance."),
        
        ("A coin is flipped nine consecutive times and lands on heads every single time. What is the probability of heads on flip ten?",
         ["50 percent", "Less than 1 percent", "Over 99 percent", "10 percent"],
         "50 percent",
         "Previous flips have no memory; each fair coin toss is an independent 50% probability event."),

        ("If an analog clock displays 3:15, what is the exact angle in degrees between the hour hand and the minute hand?",
         ["7.5 degrees", "0 degrees", "15 degrees", "5 degrees"],
         "7.5 degrees",
         "At 15 minutes, the hour hand has moved 1/4 of the way toward 4 o'clock (0.25 * 30 degrees = 7.5 degrees)."),

        ("You have twelve identical-looking balls, but one is counterfeit and has a different weight. How many balance-scale weighings are needed to guarantee finding it?",
         ["3 weighings", "2 weighings", "4 weighings", "6 weighings"],
         "3 weighings",
         "A 3-outcome pan balance (left, right, balanced) provides 3^3 = 27 states, sufficient to resolve 24 possibilities."),

        ("A farmer needs to cross a river with a wolf, a goat, and a cabbage, but the boat can only carry him and one item. How many trips minimum across the river are required?",
         ["7 trips", "5 trips", "9 trips", "6 trips"],
         "7 trips",
         "The classic riddle requires 7 crossings, taking the goat first, returning, taking the cabbage, returning with the goat, etc."),

        ("A rope ladder hangs over the side of a ship with rungs spaced 1 foot apart. If the ocean tide rises 3 feet, how many rungs will be underwater?",
         ["The same number as before", "3 more rungs", "2 more rungs", "All rungs"],
         "The same number as before",
         "The ship and its attached ladder float on top of the water and rise along with the rising tide."),

        ("What is the total number of black squares on a standard tournament chess board?",
         ["32 squares", "64 squares", "30 squares", "36 squares"],
         "32 squares",
         "A chess board has an 8x8 grid of 64 alternating squares: exactly 32 white and 32 black."),

        ("A bridge can support a maximum weight of exactly 5,000 kilograms. A truck weighing exactly 5,000 kg drives onto it. A bird lands on the truck. Does the bridge collapse?",
         ["No, because the truck consumed fuel driving across", "Yes immediately", "Only if the bird flaps", "Depends on bird weight"],
         "No, because the truck consumed fuel driving across",
         "Combustion of diesel fuel reduced the vehicle's total mass by more than the tiny mass of the bird."),

        ("A blindfolded player is handed a deck of cards containing 10 cards face up and 42 face down. How can he divide them into two piles with equal face-up cards?",
         ["Take any 10 cards and flip them all upside down", "Count card edges", "Feel the weight", "Cut the deck evenly"],
         "Take any 10 cards and flip them all upside down",
         "If the 10-card pile had k face-up cards, flipping them produces 10-k face-up cards, matching the remaining deck."),

        ("If three cats can catch three mice in three minutes, how many cats are needed to catch 100 mice in 100 minutes?",
         ["3 cats", "100 cats", "30 cats", "1 cat"],
         "3 cats",
         "Three cats catch 1 mouse per minute. Over 100 minutes, those same 3 cats catch 100 mice."),

        ("A barrel of water weighs 60 pounds. What can you add to the barrel to make it weigh 40 pounds?",
         ["A hole", "Dry ice", "Helium", "Sponges"],
         "A hole",
         "Drilling a hole in the barrel allows water to drain out, reducing the total weight."),

        ("Which word in the English language is spelled incorrectly in every single dictionary?",
         ["Incorrectly", "Misspell", "Pharaoh", "Rhythm"],
         "Incorrectly",
         "The word 'Incorrectly' is literally spelled I-N-C-O-R-R-E-C-T-L-Y in all dictionaries."),

        ("How many birthdays does an average human celebrate in their lifetime?",
         ["One (the day of their birth)", "As many years as they live", "None", "Two"],
         "One (the day of their birth)",
         "A person is only born on one single calendar day; subsequent anniversaries are birthday celebrations."),

        ("A light bulb is inside a closed upstairs room. Downstairs are three switches. How can you determine which switch turns on the bulb with only one trip upstairs?",
         ["Turn switch 1 on for 10 minutes, turn it off, turn switch 2 on, and go upstairs", "Flip all switches quickly", "Look under the door", "Toggle the fuse box"],
         "Turn switch 1 on for 10 minutes, turn it off, turn switch 2 on, and go upstairs",
         "The on switch lights the bulb; the warmed off switch feels hot; the untouched switch is cold and dark."),

        ("A prisoner is given two doors: one to freedom, one to execution. One guard always lies, one always tells truth. What single question reveals the door to freedom?",
         ["Which door would the other guard say leads to freedom?", "Are you a liar?", "Which door do you like?", "Does 2 plus 2 equal 4?"],
         "Which door would the other guard say leads to freedom?",
         "Both guards will indicate the execution door, so taking the opposite door guarantees freedom."),

        ("A man pushed his car to a hotel and had to pay the owner $200. Why?",
         ["He was playing Monopoly and landed on a hotel", "He hit the hotel wall", "Valet parking fee", "He rented a room"],
         "He was playing Monopoly and landed on a hotel",
         "Landing on an opponent's hotel property in Monopoly incurs rent penalty."),

        ("What English word has three consecutive double letters in a row?",
         ["Bookkeeper", "Mississippi", "Committee", "Subcommittee"],
         "Bookkeeper",
         "B-O-O-K-K-E-E-P-E-R has oo, kk, and ee consecutively."),

        ("If yesterday was tomorrow, today would be Saturday. What day is today actually?",
         ["Sunday", "Friday", "Thursday", "Monday"],
         "Sunday",
         "If today were Sunday, yesterday was Saturday. If that Saturday were 'tomorrow', today would be Friday, or conversely Sunday."),

        ("A window washer falls from a 40-foot scaffold onto a concrete sidewalk without a harness, but suffers no injuries. How?",
         ["He fell from the bottom rung, 1 foot high", "He landed on an awning", "He was wearing a parachute", "He caught a rope"],
         "He fell from the bottom rung, 1 foot high",
         "He was on the bottom step of the scaffold just above ground level."),

        ("A grandfather, two fathers, and two sons went to a movie theater and bought three tickets total. Did everyone get a ticket?",
         ["Yes, because there are only three people", "No, one was turned away", "They shared a seat", "Children were free"],
         "Yes, because there are only three people",
         "The group consists of a grandfather, his son (a father and son), and his grandson (a son).")
    ]

    for q, opts, ans, exp in deduction_puzzles:
        add("normal", q, opts, ans, exp)

    # Expand Normal tier systematically up to 650 total items with distinct puzzles
    normal_extra_catalog = [
        ("What occurs once in every minute, twice in every moment, but never in a hundred thousand years?", "The letter M", ["The letter M", "A leap second", "A heartbeat", "An eclipse"], "The letter 'm' appears once in 'minute', twice in 'moment', and zero times in 'a hundred thousand years'."),
        ("What 4-letter word can be written forward, backward, or upside down, and can still be read from left to right?", "NOON", ["NOON", "DEED", "RACE", "LEVEL"], "The word 'NOON' is vertically and horizontally symmetrical."),
        ("A man drives down a country road with headlights off, no moon in the sky, and no streetlights, yet stops in time to avoid hitting a black dog. How?", "It was broad daylight", ["It was broad daylight", "He had night vision goggles", "The dog wore reflective tape", "The dog barked"], "The driver was traveling during daytime hours when the sun was shining."),
        ("What English word becomes an entirely different word when capitalized?", "polish to Polish", ["polish to Polish", "book to Book", "chair to Chair", "stone to Stone"], "Uncapitalized 'polish' means making something shine; capitalized 'Polish' refers to Poland."),
        ("You throw a small ball as hard as you can. It stops without touching any wall, barrier, or net, reverses direction, and returns to your hand. How?", "You threw it straight up into the air", ["You threw it straight up into the air", "It was attached to a string", "A strong headwind blew it back", "It was a magnetic ball"], "Gravity decelerates the ball thrown upward until it halts and falls back down."),
        ("A woman has 7 daughters, and each daughter has exactly one brother. How many children does the mother have in total?", "8 children", ["8 children", "14 children", "7 children", "9 children"], "All 7 sisters share the exact same single brother."),
        ("What five-letter English word retains the same pronunciation even when you remove four of its five letters?", "Queue", ["Queue", "Stone", "Light", "Right"], "Removing 'u-e-u-e' from 'Queue' leaves the single letter 'Q', pronounced identically."),
        ("How many seconds are there in a single calendar year?", "12 (January 2nd, February 2nd, etc.)", ["12 (January 2nd, February 2nd, etc.)", "31,536,000 seconds", "86,400 seconds", "365 seconds"], "In wordplay, each of the 12 months has a 'second' day."),
        ("What can run for hours without legs, has a face that never frowns, and strikes without hurting anyone?", "A grandfather clock", ["A grandfather clock", "A river", "The wind", "A boxing referee"], "A clock runs continuously, has a dial face, and chimes its hourly strikes."),
        ("If you have a 3-gallon jug and a 5-gallon jug, how can you measure out exactly 4 gallons of water at a tap?", "Fill 5-gallon, pour into 3-gallon until full; empty 3-gallon; transfer 2 gallons to 3-gallon; fill 5-gallon; top off 3-gallon leaving 4", ["Fill 5-gallon, pour into 3-gallon until full; empty 3-gallon; transfer 2 gallons to 3-gallon; fill 5-gallon; top off 3-gallon leaving 4", "Fill both halfway", "Guess the midpoint", "Weigh them on a scale"], "This classic water-pouring algorithm yields exactly 4 gallons."),
        ("A man is looking at an old photograph. Someone asks who it is. He replies: 'I have no brothers or sisters, but this man's father is my father's son.' Who is in the photo?", "His son", ["His son", "Himself", "His father", "His uncle"], "'My father's son' is the man himself; thus 'this man's father' is him, meaning the photo depicts his son."),
        ("Why can a person living in New York not be legally buried west of the Mississippi River?", "Because living people cannot be buried", ["Because living people cannot be buried", "State burial jurisdiction laws", "Interstate transport restrictions", "Tax penalties"], "The prompt describes a living person, and living people are not buried."),
        ("A red house is made of red bricks, and a blue house is made of blue bricks. What is a green house made of?", "Glass", ["Glass", "Green bricks", "Wood and leaves", "Green plastic"], "A greenhouse is an agricultural glass enclosure used to grow plants."),
        ("What travels around the entire world while remaining stationed in one corner?", "A postage stamp", ["A postage stamp", "A compass", "A radar dish", "A passport"], "A postage stamp stays adhered to the corner of an envelope as it travels globally."),
        ("What has 13 hearts, but no lungs, brain, or other biological organs?", "A deck of playing cards", ["A deck of playing cards", "An octopus", "A hospital ward", "A rose bush"], "A standard deck contains 13 playing cards in the suit of Hearts."),
        ("A man gives his son 10 cents and another son 15 cents. What time is it?", "A quarter to two", ["A quarter to two", "Half past three", "Ten after one", "Midnight"], "He gave a quarter (25 cents) to two sons: 'A quarter to two'."),
        ("How many sides does a circular coin have?", "Two (inside and outside, or heads and tails)", ["Two (inside and outside, or heads and tails)", "Zero", "One", "Infinite"], "In riddle terms, a coin or circle has an inside and outside, or two sides."),
        ("What English word starts with 'E', ends with 'E', but contains only a single letter inside it?", "An envelope", ["An envelope", "Eye", "Ewe", "Edge"], "A postal envelope contains a single written letter inside it."),
        ("If you drop an empty glass bottle onto a plush carpeted floor, it does not break. Why?", "The carpet absorbs the kinetic impact energy", ["The carpet absorbs the kinetic impact energy", "The bottle was plastic", "Glass never breaks", "Carpet is magnetic"], "Plush carpet fibers compress over time, reducing peak deceleration shock."),
        ("Which weighs more: a ton of dry bricks or a ton of wet cotton?", "They weigh the exact same (one ton)", ["They weigh the exact same (one ton)", "The bricks", "The wet cotton", "Depends on humidity"], "One ton is a standardized unit of mass; both weigh exactly one ton.")
    ]

    for q, ans, opts, exp in normal_extra_catalog:
        add("normal", q, opts, ans, exp)

    # Continue generating unique Normal questions until items reach 650
    # Create varied, engaging deduction and logic scenarios
    unique_scenarios = [
        ("A heavy wooden chest is locked with three padlocks. Alice has key A, Bob has key B, Charlie has key C. How can they ensure the chest opens only if all three are present?", "Lock the chest with all three padlocks linked together in series", ["Lock the chest with all three padlocks linked together in series", "Make copies of all keys", "Use a combination lock", "Give Alice all keys"], "Linking three padlocks in series requires unlocking all three to open the latch."),
        ("In a single-elimination tennis tournament with 64 players, how many total matches must be played to determine the champion?", "63 matches", ["63 matches", "64 matches", "32 matches", "128 matches"], "Each match eliminates exactly one player; to eliminate 63 losers requires 63 matches."),
        ("If an analog clock is running 10 minutes slow, but loses an additional 2 minutes every hour, how many hours until it displays the correct time again?", "355 hours", ["355 hours", "12 hours", "24 hours", "720 hours"], "It must lose 11 hours and 50 minutes (710 minutes); at 2 min/hr, that requires 355 hours."),
        ("You have two hourglass sand timers: one measures 7 minutes, and the other measures 4 minutes. How can you time exactly 9 minutes to boil an egg?", "Start both; when 4-min ends, invert it; when 7-min ends, invert 4-min (1 min left); wait 1 min to reach 9", ["Start both; when 4-min ends, invert it; when 7-min ends, invert 4-min (1 min left); wait 1 min to reach 9", "Run 7-minute twice", "Guess the middle", "Run 4-minute twice"], "Coordinating both sand timers allows measuring precisely 9 minutes."),
        ("A farmer has 17 sheep, and all but 9 run away during a storm. How many sheep are left on the farm?", "9 sheep", ["9 sheep", "8 sheep", "0 sheep", "17 sheep"], "'All but 9' means exactly 9 sheep remained on the farm."),
        ("A man was born in 1955 and celebrated his 30th birthday in 1985. In what hospital room was he born?", "Room number has no correlation with calendar years", ["Room number has no correlation with calendar years", "Room 1955", "Room 30", "Room 85"], "The question presents a standard calendar fact, making the room number irrelevant trickery."),
        ("How many two-cent stamps are there in a standard dozen of stamps?", "12 stamps", ["12 stamps", "24 stamps", "6 stamps", "2 stamps"], "A dozen always equals twelve items, regardless of their denomination."),
        ("A baseball team has won 6 games and lost 4. What percentage of their games have they won?", "60 percent", ["60 percent", "40 percent", "50 percent", "66 percent"], "6 wins out of 10 total games played equals 60%."),
        ("If a digital clock displays time in 24-hour format (00:00 to 23:59), how many times per day do all four digits match identical numbers?", "3 times (00:00, 11:11, 22:22)", ["3 times (00:00, 11:11, 22:22)", "4 times", "2 times", "1 time"], "Only 00:00, 11:11, and 22:22 have four identical digits in 24-hour time."),
        ("If five machines take five minutes to make five widgets, how many minutes would one hundred machines take to make one hundred widgets?", "5 minutes", ["5 minutes", "100 minutes", "1 minute", "20 minutes"], "Each machine takes 5 minutes to produce one widget; 100 machines produce 100 widgets in parallel in 5 minutes.")
    ]

    for q, ans, opts, exp in unique_scenarios:
        add("normal", q, opts, ans, exp)

    # Populate remainder of normal up to 650 with unique reasoning items
    word_deductions = [
        ("Which five-letter word contains only one vowel and four consonants, yet describes someone who is bold and confident?", "Brash", ["Brash", "Brave", "Proud", "Smart"], "'Brash' contains only the vowel 'a' and means audaciously self-assertive."),
        ("What six-letter word contains four consonants in a row, describing someone very strong?", "Brawny", ["Brawny", "Mighty", "Tough", "Hardy"], "'Brawny' has four consonants (b-r-w-n-y) and signifies muscular strength."),
        ("Which word becomes plural when you add the letter 'S', but becomes singular again if you add another 'S'?", "Princess", ["Princess", "Prince", "Care", "Need"], "'Prince' + 's' = 'Princes' (plural); + 's' = 'Princess' (singular female royalty)."),
        ("What four-letter word can be placed after 'rain', 'bow', and 'fire' to create three new compound words?", "Fly", ["Fly", "Bow", "Man", "Dog"], "Rainfly, bowfly, and firefly form valid English words or terms."),
        ("What three-letter word can precede 'hole', 'fall', and 'proof' to create three common words?", "Water", ["Water", "Down", "Fire", "Wind"], "Waterhole, waterfall, and waterproof are valid compound words."),
        ("What four-letter word can follow 'sun', 'moon', and 'star' to describe cosmic illumination?", "Light", ["Light", "Shine", "Beam", "Glow"], "Sunlight, moonlight, and starlight form recognized words for natural illumination."),
        ("What word is pronounced as a single syllable, but when two letters are added, it is pronounced as three syllables?", "Came to Cameo", ["Came to Cameo", "Go to Gone", "See to Seen", "Do to Done"], "'Came' has one syllable; adding 'o' forms 'cameo' with three distinct syllables (cam-e-o)."),
        ("What 7-letter word contains ten words within it without rearranging any letters?", "Therein", ["Therein", "Somehow", "Because", "Another"], "'Therein' contains: the, there, he, in, rein, her, here, ere, herein, and I."),
        ("What word begins with 'under' and ends with 'ground', yet is not beneath the earth?", "Underground", ["Underground", "Underpass", "Undercurrent", "Undercover"], "'Underground' starts with 'under' and ends with 'ground'."),
        ("What seven-letter word has three vowels that are all the exact same letter 'E'?", "Element", ["Element", "Evening", "Extreme", "Elevate"], "'Element' contains three vowels, all of which are the letter 'E'.")
    ]
    for q, ans, opts, exp in word_deductions:
        add("normal", q, opts, ans, exp)

    import puzzle_families as pf
    for family in pf.NORMAL:
        if len([x for x in items if x["difficulty"] == "normal"]) >= 400:
            break
        for p in family('en'):
            if len([x for x in items if x["difficulty"] == "normal"]) >= 400:
                break
            add("normal", p["question"], p["options"], p["correctAnswer"], p["explanation"])

    print(f"English Normal items collected: {len(items)}")

    # =========================================================================
    # TIER 3: TRICKY (350 distinct questions: IDs 651 - 1000)
    # Deep lateral traps, counter-intuitive physics, paradoxes, mind benders
    # =========================================================================
    tricky_data = [
        ("A heavy metal washer with a round hole in its exact center is heated uniformly in an oven. What happens to the diameter of the central hole?",
         ["It expands and becomes larger", "It shrinks and becomes smaller", "It remains exactly identical", "It distorts into an oval"],
         "It expands and becomes larger",
         "Thermal expansion causes all dimensions of a solid object to expand outward, just like photographic enlargement."),

        ("A stone is thrown out of a small rowboat floating in a swimming pool and sinks to the bottom. Does the water level in the pool rise, fall, or stay the same?",
         ["It falls slightly", "It rises slightly", "It remains exactly the same", "It overflows"],
         "It falls slightly",
         "In the boat, the stone displaced its weight in water. At the bottom, it displaces only its physical volume, which is less."),

        ("Why does a helium-filled balloon inside a closed car move forward toward the windshield when the driver steps on the accelerator?",
         ["Denser air moves backward, creating a forward pressure gradient that pushes the light helium forward", "Air conditioning pulls it", "Centrifugal force acts on helium", "Static electricity on the glass"],
         "Denser air moves backward, creating a forward pressure gradient that pushes the light helium forward",
         "Inertia pushes denser cabin air toward the rear, creating higher air pressure at the back that buoys light helium forward."),

        ("You spin a raw egg and a hard-boiled egg on a tabletop, briefly stop each with your finger for a fraction of a second, and let go. Which egg resumes spinning?",
         ["The raw egg resumes spinning", "The hard-boiled egg resumes spinning", "Both resume spinning equally", "Neither resumes spinning"],
         "The raw egg resumes spinning",
         "The raw egg's liquid yolk continues rotating inside due to inertia, and its momentum restarts the shell spinning upon release."),

        ("In the Monty Hall game show with three doors, you pick Door 1. The host opens Door 3 to reveal a goat. Should you switch to Door 2 to maximize your chance of winning the car?",
         ["Yes, switching doubles your winning probability to 2 out of 3", "No, your probability remains exactly 50/50", "It makes absolutely no mathematical difference", "Only if you originally guessed Door 2"],
         "Yes, switching doubles your winning probability to 2 out of 3",
         "Your initial pick had a 1/3 chance of being correct; the unpicked door retains the remaining 2/3 probability."),

        ("In a small isolated village, the town barber shaves all men, and only those men, who do not shave themselves. Who shaves the barber?",
         ["The scenario is an impossible logical paradox (Russell's paradox)", "The barber shaves himself", "The barber's apprentice shaves him", "A visiting physician shaves him"],
         "The scenario is an impossible logical paradox (Russell's paradox)",
         "If he shaves himself, he violates the rule; if he doesn't shave himself, he must shave himself. The barber cannot logically exist."),

        ("An elevator cable snaps at the 50th floor and plunges toward the ground. Can a passenger survive the impact by jumping upward right before the cab hits the ground?",
         ["No, the upward jump speed barely reduces the massive downward terminal velocity", "Yes, it cancels out the downward momentum completely", "Only if the elevator has carpet", "Yes, if the passenger jumps backwards"],
         "No, the upward jump speed barely reduces the massive downward terminal velocity",
         "A human can only jump upward at roughly 2-3 m/s, which barely counters a catastrophic downward fall speed of 40+ m/s."),

        ("Under certain specific laboratory conditions, can a container of hot water freeze into ice faster than an identical container of cold water?",
         ["Yes, known scientifically as the Mpemba effect", "No, it violates the laws of thermodynamics", "Only when salt is dissolved in it", "Only under zero gravity"],
         "Yes, known scientifically as the Mpemba effect",
         "The Mpemba effect occurs due to faster evaporation, convection currents, and dissolved gas reduction in hot water."),

        ("If a tree falls deep in an uninhabited forest with no living ears present to detect it, does it make a sound?",
         ["Physical acoustic compression waves exist, but perceived auditory sound requires an ear and brain", "No acoustic waves exist", "Yes, identical to when people listen", "Sound is an illusion"],
         "Physical acoustic compression waves exist, but perceived auditory sound requires an ear and brain",
         "Acoustics distinguishes between mechanical pressure vibrations in air and the biological auditory perception of sound."),

        ("A man stands on a scale in an elevator. When does the scale read the lowest weight?",
         ["When the elevator accelerates downward", "When the elevator moves upward at constant speed", "When the elevator moves downward at constant speed", "When the elevator is stationary"],
         "When the elevator accelerates downward",
         "Downward acceleration reduces the upward normal reaction force exerted by the scale on his feet."),

        ("A submarine is submerged in fresh water. It moves into salt water ocean at the exact same depth. Does the water pressure on its hull increase, decrease, or remain identical?",
         ["It increases slightly due to higher salt water density", "It decreases", "It remains exactly identical", "It drops to zero"],
         "It increases slightly due to higher salt water density",
         "Hydrostatic pressure equals density * gravity * depth (P = rho * g * h); salt water has higher density than fresh water."),

        ("Why do passenger airplanes fly at high cruising altitudes of 30,000 to 40,000 feet?",
         ["Thinner atmospheric air creates less aerodynamic drag, saving jet fuel", "Gravity is lower at high altitude", "To fly above clouds and stay warm", "Jet engines need more oxygen"],
         "Thinner atmospheric air creates less aerodynamic drag, saving jet fuel",
         "Lower air density at high altitudes drastically minimizes drag, allowing high cruise velocities with minimal fuel consumption."),

        ("What happens to the temperature of an insulated room if an ordinary household refrigerator is left running with its door wide open?",
         ["The room temperature increases overall", "The room temperature decreases overall", "The room temperature stays exactly the same", "The room turns into a freezer"],
         "The room temperature increases overall",
         "The refrigerator compressor's electrical motor inefficiency expels more heat into the room than it can absorb from interior air."),

        ("If Earth's rotational speed suddenly doubled instantly, what would happen to a human's apparent weight measured on a scale at the equator?",
         ["Apparent weight would decrease slightly due to higher centrifugal force", "Apparent weight would double", "Apparent weight would stay identical", "Apparent weight would drop to zero"],
         "Apparent weight would decrease slightly due to higher centrifugal force",
         "Higher tangential velocity increases outward centrifugal acceleration, reducing the downward net force against the scale."),

        ("Why does hot tea cool down faster when you blow air gently across the top surface of the mug?",
         ["It removes saturated vapor, accelerating evaporative cooling", "Your breath is freezing cold", "It pushes cold air into the bottom", "It oxidizes the tea leaves"],
         "It removes saturated vapor, accelerating evaporative cooling",
         "Blowing air sweeps away the humid boundary layer above the liquid, allowing high-energy water molecules to evaporate rapidly."),

        ("If you drop an iron cannonball and a wooden ball of identical diameter from a cliff in a vacuum chamber, which hits first?",
         ["Both hit the ground at the exact same instant", "The iron cannonball hits first", "The wooden ball hits first", "The one dropped from higher"],
         "Both hit the ground at the exact same instant",
         "In a vacuum with zero air resistance, gravitational acceleration (g = 9.8 m/s^2) is entirely independent of mass."),

        ("Why does asphalt pavement look like a shimmering pool of water on a hot sunny day?",
         ["Light rays refract upward through hot, low-density air near the ground (inferior mirage)", "Water condenses out of the asphalt", "Reflection from car glass", "Heat waves vibrate the eyes"],
         "Light rays refract upward through hot, low-density air near the ground (inferior mirage)",
         "A hot air boundary layer bends light rays from the sky upward into the driver's eyes, mimicking a reflective water puddle."),

        ("Why is a diamond transparent to visible light, while graphite (pure carbon of the same element) is completely black and opaque?",
         ["Diamond's wide electron band gap prevents visible photon absorption, while graphite has free delocalized electrons", "Diamond is made of glass", "Graphite absorbs light because it is heavy", "Diamond reflects 100 percent of light"],
         "Diamond's wide electron band gap prevents visible photon absorption, while graphite has free delocalized electrons",
         "Carbon hybridization in diamond locks electrons into rigid sp3 bonds with a 5.5 eV band gap, allowing visible light to pass."),

        ("When light enters a glass prism from air, its speed decreases by about 33 percent. Does the light's frequency change?",
         ["No, the frequency remains constant while wavelength shortens", "Yes, frequency decreases", "Yes, frequency increases", "Frequency drops to zero"],
         "No, the frequency remains constant while wavelength shortens",
         "The frequency of electromagnetic radiation is determined by the source wave oscillation and never changes across media."),

        ("If you shine a flashlight forward from the front bumper of a spaceship traveling at 99 percent the speed of light, at what speed does the beam travel?",
         ["At the speed of light (c) in all reference frames", "At 1.99 times the speed of light", "At 0.99 times the speed of light", "At double the speed of sound"],
         "At the speed of light (c) in all reference frames",
         "Einstein's Special Relativity dictates that the speed of light in vacuum is invariant across all inertial frames of reference.")
    ]

    for q, opts, ans, exp in tricky_data:
        add("tricky", q, opts, ans, exp)

    for family in pf.TRICKY:
        if len([x for x in items if x["difficulty"] == "tricky"]) >= 350:
            break
        for p in family('en'):
            if len([x for x in items if x["difficulty"] == "tricky"]) >= 350:
                break
            add("tricky", p["question"], p["options"], p["correctAnswer"], p["explanation"])

    print(f"Total English items generated: {len(items)}")
    return items[:1000]

print("English bank builder ready.")
