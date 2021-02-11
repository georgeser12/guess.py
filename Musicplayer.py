from tkinter import *
import pygame

pygame.mixer.init()
root = Tk()
screen = Canvas(width = 560, height= 624, bg='light blue')
screen.grid(row=0, column=0)
root.title("music player")
root.geometry("560x624")

#songs
song1 = "C:\\Users\seria\\Videos\\Song1.mp3"
song2 = "C:\\Users\\seria\\Downloads\\Song2.mp3"
song3 = "C:\\Users\\seria\\Downloads\\Song3.mp3"
song4 = "C:\\Users\\seria\\Downloads\\Song4.mp3"
song5 = "C:\\Users\\seria\\Downloads\\Song5.mp3"
song6 = "C:\\Users\\seria\\Downloads\\Song6.mp3"
song7 = "C:\\Users\\seria\\Downloads\\Song7.mp3"
song8 = "C:\\Users\\seria\\Downloads\\Song8.mp3"




global paused
paused = False

def play_music(song):
    pygame.mixer.music.load(song)
    pygame.mixer.music.play()



def pause_music(is_paused):
    global paused
    paused = is_paused
    if paused:
        pygame.mixer.music.unpause()
        pause = Button(root, text="Pause", bg="orange", height=2, width=10, font="boldFont", command=lambda: pause_music(paused))
        pause.place(x=14, y=300)
        paused = False
    else:
        pygame.mixer.music.pause()
        pause = Button(root, text="Unpause", bg="orange", height=2, width=10, font="boldFont", command=lambda: pause_music(paused))
        pause.place(x=14, y=300)
        paused = True



# background
photo = PhotoImage(file = "C:\\Users\\seria\\Pictures\\Saved Pictures\\retroback.png")
screen.create_image(0,0,image=photo, anchor=NW)

#heading
name = PhotoImage(file = "C:\\Users\\seria\\Pictures\\Saved Pictures\\logo.png")
screen.create_image(0,0,image=name, anchor=NW)

#buttons
button1 = Button(root, text="Song1", bg="green", height=2, width=10, font="boldFont", command= lambda: play_music(song1))
button1.place(x=20, y=501)

button2 = Button(root, text= "Song2", bg="light blue", height=2, width=10, font= "boldFont", command = lambda: play_music(song2))
button2.place(x=150,y=501)

button3 = Button(root, text= "Song3", bg="green", height=2, width=10, font= "boldFont", command = lambda: play_music(song3))
button3.place(x=290,y=501)

button4 = Button(root, text= "Song4", bg="light blue", height=2, width=10, font= "boldFont", command =lambda: play_music(song4))
button4.place(x=440,y=501)

button5 = Button(root, text= "Song5", bg="light blue", height=2, width=10, font= "boldFont", command =lambda: play_music(song5))
button5.place(x=20,y=555)

button6 = Button(root, text= "Song6", bg="green", height=2, width=10, font= "boldFont", command =lambda: play_music(song6))
button6.place(x=150,y=555)

button7 = Button(root, text= "Song7", bg="light blue", height=2, width=10, font= "boldFont", command =lambda: play_music(song7))
button7.place(x=290,y=555)

button8 = Button(root, text= "Song8", bg="green", height=2, width=10, font= "boldFont", command =lambda: play_music(song8))
button8.place(x=440,y=555)

pause = Button(root, text= "Pause", bg="orange", height=2, width=10, font= "boldFont", command = lambda: pause_music(paused))
pause.place(x=14,y= 300)

#music player window
screen.create_rectangle(1000, 500, 150, 200, fill="light blue")

#Song name
text_canvas = screen.create_text(170, 200, anchor = "nw")
screen.itemconfig(text_canvas, text="Song 1: Funkin Fun - Scotty Sire", font = "boldFont", fill= "blue")

text_canvas2 = screen.create_text(170, 240, anchor = "nw")
screen.itemconfig(text_canvas2, text="Song 2: HOUSTONFORNICATION - Travis Scott", font = "boldFont", fill="red")

text_canvas3 = screen.create_text(170, 280, anchor = "nw")
screen.itemconfig(text_canvas3, text="Song 3: Static Space Lover - Foster The People", font = "boldFont", fill="purple")

text_canvas4 = screen.create_text(170, 320, anchor = "nw")
screen.itemconfig(text_canvas4, text="Song 4: 505 - Arctic Monkey", font = "boldFont", fill="black")

text_canvas5 = screen.create_text(170, 360, anchor = "nw")
screen.itemconfig(text_canvas5, text="Song 5: Cigarette Daydreams - Cage The Elephant", font = "boldFont", fill="blue")

text_canvas6 = screen.create_text(170, 400, anchor = "nw")
screen.itemconfig(text_canvas6, text="Song 6: Staring - Tripling Rock", font = "boldFont", fill="red")

text_canvas7 = screen.create_text(170, 440, anchor = "nw")
screen.itemconfig(text_canvas7, text="Song 7: Can I Kick It? - A Tribe Called Quest", font = "boldFont", fill="purple")

text_canvas8 = screen.create_text(170, 480, anchor = "nw")
screen.itemconfig(text_canvas8, text="Song 8: Social Cues - Cage The Elephant", font = "boldFont", fill="black")


def change_vol(val):
    volume = int(val) / 100
    pygame.mixer.music.set_volume(volume)
#volume slider
slider = Scale(root, from_=100, to=0, command = change_vol, bg = "orange", width = 50, fg = "black")
slider.place(x=20, y = 350)



root.mainloop()
