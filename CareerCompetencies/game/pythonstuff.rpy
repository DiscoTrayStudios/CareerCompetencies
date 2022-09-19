init python in mystore:


    #string stuff
    txtdict = {}
    chapters = []
    chapters.append(1)
    chapters.append(2)

    txtdict[1] = [["Welcome Center", "Come by the Welcome Center to get an overview of the Hendrix experience!"], ["Library", "Meet and Greet for new students! Come meet some new friends!"], ["SLTC", "No events planned for today"], ["Resume Tip #1","Get new experiences!", "Always be on the lookout for new opportunities you would enjoy!"], ["Good Vibe of the Day", "'Thinking: the talking of the soul with itself.'", "           -Plato"]]
    txtdict[2] = [["Library", "Come study for finals with others with Peer Learning!"], ["SLTC", "Information Panel for STEM Majors in the Burrow!"], ["Mills", "Interested in the Humanities? Come by for an overview of our program!"], ["Resume Tip #2", "Use Reverse Chronological Order!", "List most recent experiences and work backward"], ["Good Vibe of the Day", "'Love and desire are the spirit's wings to great deeds.'", "              -Johann Wolfgang von Goethe"]]
    txtdict[3] = [["Library", "Learn about studying abroad!"], ["SLTC", "Ice cream social! Come meet some people!"], ["Mills", "Club meeting if you are in one!"], ["Resume Tip #3", "Let the job post be your guide! Job descriptions can help you", "decide which skills/experiences to highlight on your resume"], ["Good Vibe of the Day", "'If life were predictable it would cease to be life,", "and be without flavor'", "          -Eleanor Roosevelt"]]
    txtdict[4] = [["Library", "Student Study Session! Come learn with peers!"], ["SLTC", "Clubs are meeting today!", "If you are interested in summer research in Biology, come by the Burrow!"], ["Mills", "Wanting summer research in the social sciences? If so, come by Mills!"], ["Resume Tip #5", "Perfect your descriptions!","Read a lot of good resumes and work with a Career Services professional"], ["Good Vibe of the Day", "Today is a good day to try", "         -Quasimodo"]]
    txtdict[5] = [["Library", "NEED TO FILL OUT"], ["SLTC", "NEED TO FILL OUT!!!!"], ["Mills", "NEED TO FILL OUT!!!!"], ["Resume Tip #5", "NEED TO FILL OUT!!!!"], ["Good Vibe of the Day", "NEED TO FILL OUT!!!!"]]

    def gettxt(chapter, i):
        return txtdict[chapter][i]

    def gettxtblock(chapter):
        return txtdict[chapter]
