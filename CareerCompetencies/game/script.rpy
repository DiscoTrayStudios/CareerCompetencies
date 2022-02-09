# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")
define guy = Character("Guy", color="#990000")

#

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene p

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.

    e "You've created a new Ren'Py game."

    e "Once you add a story, pictures, and music, you can release it to the world!"

    menu:
        "Do you want to go to the library?"
        "Yes":
            jump library
        "No":
            jump noLibrary
        "Three?":
            jump three
        "Quit Game":
            jump quit
        


    return

label library:


    scene library
    hide eileen happy with dissolve
    # Renpy checks images in images folder for image with name same as used. Do not have to make variables!
    # Need to make sure images are in correct aspect ratio. Currently 1920X1080

    show NEW CHARACTER at right with dissolve
    guy "My name is a different color because of a secondary argument from my definition."

    # This ends the game.

    jump start

label noLibrary:

    e "Okay we won't go then"
    jump start

label three:
    hide eileen happy with dissolve
    scene p
    show THREE at left
    guy "THREE WORKS!"
    jump start

label quit:
    return
