import random
from pyrogram import Client, filters
from info import COMMAND_HAND_LER
from plugins.helper_functions.cust_p_filters import f_onw_fliter


RUN_STRINGS = (
    "Ha!",
    "I invented a new word!...",
    "Can someone please shed more light on how my lamp got stolen?",
    "Will the cat eat its meal without pulling a stunt? I am not a gymnast instructor, but I know the cartwheel..",
    "Why is she called llene? She stands on equal legs.",
    "What do you call a gazelle in a lion’s territory? Denzel.",
    "Knock! Knock!",
    "Ladies looking for the fruit of the womb, even after having a man, should let that mango!",
    "Hummingbirds usually hum when speaking because they don’t know the words to use.",
    "How did the bird break into the house? It came with a crow bar!",
    "I am tired of the constant ups and downs in my life, so I got to stop using the stairs.",
    "Vegetarians don’t always need to purchase their vegetables because their boss also award them with compensatory leave",
    " Tom is the weakest in my class, everyone dared him more than letters",
    "What did 1 say to 7? Nice cap!...",
    "My sign language teacher advised me to practice frequently because her lessons may come in handy",
    "The path of a con is a difficult maze to understand.",
    "How do trees have so many friends? They branch out!.",
    "The cruelest but funniest thing I’ve ever heard is the doctor telling an amputee he needs more digits for his prosthetic fingers!",
    "It’s so romantic how I always feel a hot spot in my chest whenever I tell my wife-hi.",
    "She said she’s met me at the vegan restaurant last week but I’ve never seen herbivore.",
    "I had a change of heart on my way to get a heart transplant.",
    "My friend is so short that using him hurdle race would be an easy walk over.",
    "You will hardly find bees working under people because they’re the buzz",
    "പWhy is Danny good at all sports? He got athlete foot!",
    "Pastries are nitwits, they donut know anythingsി",
    "I feel the sadness of skeletons because they literally have no body",
    "What kind of fruit is always sorry for being a prick? Cactus.",
    "What color looks sick? Pale colors",
    "നWhat is ground beef? A cow with no legs.", 
)


@Client.on_message(
    filters.command("runs", COMMAND_HAND_LER) &
    f_onw_fliter
)
async def runs(_, message):
    """ /runs strings """
    effective_string = random.choice(RUN_STRINGS)
    if message.reply_to_message:
        await message.reply_to_message.reply_text(effective_string)
    else:
        await message.reply_text(effective_string)
