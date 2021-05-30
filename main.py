import  turtle
import pandas

screen=turtle.Screen()
screen.title("U.S states Game")
image="blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# def got_mouse_click_coor(x,y):
#     print(x,y)
#
# turtle.onscreenclick(got_mouse_click_coor)
data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()


score=0
guess_states=[]

FONT=("Arial", 15, "normal")
while len(guess_states) < 50:
    answer = screen.textinput(title=f"{len(guess_states)}/50 states correct",
                              prompt="what's another states").title()

    if answer == "Exit":
        ##using list comprehenssion

        missing_states = [state for state in all_states if state not in guess_states]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states.csv")
        break

    if answer in all_states:
        guess_states.append(answer)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer]
        t.goto(float(state_data.x), float(state_data.y))
        t.write(answer,font=FONT)  ##answer==state_data.state.item()





