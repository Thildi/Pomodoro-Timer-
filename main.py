import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")

all_states = data.state.to_list()

guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                    prompt="What's another state's name?").title()

    if answer_state in all_states:
        guessed_states.append(answer_state)
        state_data = data[data.state == answer_state]
        x_cor = state_data.x.iloc[0]
        y_cor = state_data.y.iloc[0]
        pen = turtle.Turtle()
        pen.hideturtle()
        pen.penup()
        pen.goto(x_cor, y_cor)
        pen.write(answer_state)


    missing_states = [state for state in all_states if answer_state == "Exit"]

    if answer_state == "Exit":
        missing_states = [state for state in all_states if state not in guessed_states]
        # missing_states = []
        # for state in all_states:
        #     if state not in guessed_states:
        #         missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break



