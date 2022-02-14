# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")
define guy = Character("Guy", color="#990000")
image eileen = "Characters/Eileen.png"
image john = "Characters/John.png"
image libraryBackground = "Backgrounds/library.jpg"
image pecanCourtBackground = "Backgrounds/p.jpg"
#

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it. aklsdjflkjsdkjlf
    show screen gameUI
    scene p

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen

    # These display lines of dialogue.
    e "Press once to get option to quit."

    menu:
        "Do you want to go to quit?"
        "Yes":
            jump quit
        "No":
            jump start

    return

label library:

    hide eileen with dissolve

    scene libraryBackground
    # Renpy checks images in images folder for image with name same as used. Do not have to make variables!
    # Need to make sure images are in correct aspect ratio. Currently 1920X1080

    show john at right with dissolve
    guy "My name is a different color because of a secondary argument from my definition."

    # This ends the game.

    jump start

label sltc:
    scene ANOTHER PLACEHOLDER
    show eileen
    e "This is where you can find tons of helpful student recources, some great food, and a nice place to hang out!"
    jump start

label welcomecenter:
    hide eileen
    hide pecanCourtBackground
    scene PLACEHOLDER
    "I should see whats around here, being new and all..."
    jump start

label quit:
    return
