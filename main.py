import tkinter as tk
import random

countdown = 60
text = ""
window = tk.Tk()
window.geometry("700x700")
window.configure(background="gray")
next_l = 1


def main():
    global countdown
    countdown = 60
    global text
    texts = [
            "The European languages are members of the same family. Their separate existence is a myth. For science, music, sport, etc, Europe uses the same vocabulary. The languages only differ in their grammar, their pronunciation and their most common words. Everyone realizes why a new common language would be desirable: one could refuse to pay expensive translators. To achieve this, it would be necessary to have uniform grammar, pronunciation and more common words. If several languages coalesce, the grammar of the resulting language is more simple and regular than that of the individual languages. The new common language will be more simple and regular than the existing European languages. It will be as simple as Occidental; in fact, it will be Occidental. To an English person, it will seem like simplified English, as a skeptical Cambridge friend of mine told me what Occidental is.The European languages are members of the same family. Their separate existence is a myth. For science, music, sport, etc, Europe uses the same vocabulary. The languages only differ in their grammar, their pronunciation and their most common words. Everyone realizes why a new common language would be desirable: one could refuse to pay expensive translators. To",
            "Far far away, behind the word mountains, far from the countries Vokalia and Consonantia, there live the blind texts. Separated they live in Bookmarksgrove right at the coast of the Semantics, a large language ocean. A small river named Duden flows by their place and supplies it with the necessary regelialia. It is a paradisematic country, in which roasted parts of sentences fly into your mouth. Even the all-powerful Pointing has no control about the blind texts it is an almost unorthographic life One day however a small line of blind text by the name of Lorem Ipsum decided to leave for the far World of Grammar. The Big Oxmox advised her not to do so, because there were thousands of bad Commas, wild Question Marks and devious Semikoli, but the Little Blind Text didn’t listen. She packed her seven versalia, put her initial into the belt and made herself on the way. When she reached the first hills of the Italic Mountains, she had a last view back on the skyline of her hometown Bookmarksgrove, the headline of Alphabet Village and the subline of her own road, the Line Lane. Pityful a rethoric question ran over her cheek, then",
            "A wonderful serenity has taken possession of my entire soul, like these sweet mornings of spring which I enjoy with my whole heart. I am alone, and feel the charm of existence in this spot, which was created for the bliss of souls like mine. I am so happy, my dear friend, so absorbed in the exquisite sense of mere tranquil existence, that I neglect my talents. I should be incapable of drawing a single stroke at the present moment; and yet I feel that I never was a greater artist than now. When, while the lovely valley teems with vapour around me, and the meridian sun strikes the upper surface of the impenetrable foliage of my trees, and but a few stray gleams steal into the inner sanctuary, I throw myself down among the tall grass by the trickling stream; and, as I lie close to the earth, a thousand unknown plants are noticed by me: when I hear the buzz of the little world among the stalks, and grow familiar with the countless indescribable forms of the insects and flies, then I feel the presence of the Almighty, who formed us in his own image, and the breath",
            "One morning, when Gregor Samsa woke from troubled dreams, he found himself transformed in his bed into a horrible vermin. He lay on his armour-like back, and if he lifted his head a little he could see his brown belly, slightly domed and divided by arches into stiff sections. The bedding was hardly able to cover it and seemed ready to slide off any moment. His many legs, pitifully thin compared with the size of the rest of him, waved about helplessly as he looked. 'What's happened to me?' he thought. It wasn't a dream. His room, a proper human room although a little too small, lay peacefully between its four familiar walls. A collection of textile samples lay spread out on the table - Samsa was a travelling salesman - and above it there hung a picture that he had recently cut out of an illustrated magazine and housed in a nice, gilded frame. It showed a lady fitted out with a fur hat and fur boa who sat upright, raising a heavy fur muff that covered the whole of her lower arm towards the viewer. Gregor then turned to look out the window at the dull weather. Drops",
            "One of the best ways to practice touch typing and to become a keyboard typing master is by typing exercises of entire fragments of text. This approach provides a real-world context for applying your touch typing skills. You familiarize yourself with common word combinations and sentence structures as you type complete sentences and paragraphs. This helps you to not only improve your speed but also your overall typing efficiency, which also includes accuracy.Before starting to type full texts, you should take the typing lessons to learn to type faster. It is recommended first to do all the lessons connected with typing characters. You may leave the lessons about special characters or numbers for later. You do not need to type without looking at the keyboard to practice entire text fragment typing, but pressing given keys with the correct fingers is always required - it is a general rule for learning touch typing and a characteristic of a typing master. The ability to type faster comes as a consequence of accurate typing.",
            "Learning to type faster revolves around mastering touch typing, a technique that allows you to type without looking at the keyboard. The process begins with typing only a few particular characters repeatedly. Gradually, you expand your reach to the other keys, developing muscle memory and improving your accuracy, and you start to type faster.Initially, it might feel counterintuitive or even slow as you consciously focus on placing your fingers correctly. However, with consistent practice, your fingers start to move effortlessly across the keyboard, and your typing becomes faster and more precise. Hopefully, when you are satisfied with your typing skills, you can call yourself a typing master.As you are reading this, you know well that the AgileFingers assist the typing learning process. The platform provides structured lessons and exercises designed to improve touch typing skills and help you to type faster. You can track progress and identify improvement areas with interactive exercises and real-time feedback.Remember, speed and accuracy in typing come not from rushing but from developing muscle memory through regular practice and repetition. Be patient with yourself; gradually, you'll become a master capable of typing effortlessly and accurately.",
            "The spot was perfect for camouflage. At least that's what she thought when she picked the spot. She couldn't imagine that anyone would ever be able to see her in these surroundings. So there she sat, confident that she was hidden from the world and safe from danger. Unfortunately, she had not anticipated that others may be looking upon her from other angles, and now they were stealthily descending toward her hiding spot.No matter how hard he tried, he couldn't give her a good explanation about what had happened. It didn't even really make sense to him. All he knew was that he froze at the moment and no matter how hard he tried to react, nothing in his body allowed him to move. It was as if he had instantly become a statue and although he could see what was taking place, he couldn't move to intervene. He knew that wasn't a satisfactory explanation even though it was the truth.The irony of the situation hadn't escaped her. She had taken years to sculpt the perfect persona with the perfect look that she shared on Instagram. She knew her hundreds of thousands of followers envied that life she showed and stayed engaged with her because they wanted that life too. The truth was that she wanted the perfect life she portrayed more than any of her fans. The fact was that despite all the perfection she shared on social media, her life was actually more of a mess than most."
        ]

    chosen_text = random.choice(texts).lower()

    text = chosen_text

    global right_label
    right_label = tk.Label(text=text[0:], bg="gray", fg="white", font=("Arial", 30))
    right_label.place(relx=0.5, rely=0.5, anchor="w")

    global left_label
    left_label = tk.Label(text=text[0:0], bg="gray", fg="cyan", font=("Arial", 30, "bold"))
    left_label.place(relx=0.5, rely=0.5, anchor="e")

    global current_letter
    current_letter = tk.Label(text=text[0], bg="gray", fg="cyan", font=("Arial", 30, "bold"))
    current_letter.place(relx=0.5, rely=0.6, anchor='n')

    global counter
    counter = tk.Label(text=f"{countdown} Seconds", bg="gray", fg="white", font=("Arial", 30, "bold"))
    counter.place(relx=0.5, rely=0.4, anchor='n')

    window.bind("<Key>", next_letter)

    # global writeable # it was defined because needed one more step to counter to work
    # writeable = True

    counter.configure(text=f"{countdown} Seconds")
    # window.after(60000, result)  # after 60 secs game gets closed.
    window.after(1000, subtract_sec)  # every 1 sec counter goes 1 sec down.


def subtract_sec():
    global countdown
    countdown -= 1
    try:
        counter.configure(text=f"{countdown} Seconds")
        if countdown != 0:
            window.after(1000, subtract_sec)
        else:
            result()
    except tk.TclError:
        pass


def next_letter(pressed_letter=None):
    global next_l
    try:
        if pressed_letter.char.lower() == current_letter.cget("text"):  # if event letter equal to current letter then
            right_label.configure(text=text[next_l:])   # delete the right label first letter then
            left_label.configure(text=text[0:next_l])   # add the deleted letter to right label
            current_letter.configure(text=right_label.cget("text")[0])  # re-adjust the current letter next letter
            next_l += 1
    except tk.TclError:
        pass


def result():

    # counting the words typed
    amount_of_words = len(left_label.cget('text').split(' '))

    # Destroy all unwanted widgets.
    counter.destroy()
    current_letter.destroy()
    right_label.destroy()
    left_label.destroy()

    # show the result
    global result_label
    result_label = tk.Label(text=f'Words per Minute: {amount_of_words}', fg='black',bg="grey", font=("Arial", 30, "bold"))
    result_label.place(relx=0.5, rely=0.5, anchor="center")
    # restart button
    global restart_button
    restart_button = tk.Button(text="RESTART", command=restart, bg="white", fg="black", )
    restart_button.place(relx=0.5, rely=0.6, anchor="center")


# Restarting the game
def restart():
    global next_l
    result_label.destroy()
    restart_button.destroy()
    next_l = 1  # it must be reset to 1 otherwise after restart it gives bug

    # re-run the main()
    main()


main()

window.mainloop()
