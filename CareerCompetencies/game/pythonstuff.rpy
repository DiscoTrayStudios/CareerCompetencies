init python:


    #string stuff
    txtdict = {}
    chapters = []
    chapters.append(1)
    chapters.append(2)

    txtdict[1] = ["This is information 1!", "This is two!", "Now 3!", "Ttttttttttttttttttttttttttttttttthhhhhhhhhhhhhhhhhhiiiiiiiiiiiiissssssssssssssssssssssss is a long message test"]
    txtdict[2] = ["chp2 test", "see chp1 for better data", "Moderatley long passage I suppose just in case"]
    def gettxt(chapter, i):
        return txtdict[chapter][i]
