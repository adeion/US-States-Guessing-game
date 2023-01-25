import turtle
import pandas
state_data = pandas.read_csv("50_states.csv")
state = state_data.state.to_list()
guessed_states = []
screen = turtle.Screen()
screen.title("U.S. States Game")
image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)
while len(guessed_states) < 50:

    answer_input = screen.textinput(title=f'{len(guessed_states)}/50 Guess the state name',
                                    prompt='What is the name of another state?').title()
    if answer_input == "Exit":
        # diff = list(set(state).difference(guessed_states))
        diff = [name for name in state if name not in guessed_states]
        Data = pandas.DataFrame(diff)
        Data.to_csv('Missed States')
        break

    elif answer_input in state:
        guessed_states.append(answer_input)
        i = state_data[state_data.state == answer_input]
        t = turtle.Turtle()
        t.penup()
        t.hideturtle()
        t.goto(int(i.x_cor), int(i.y_cor))
        t.write(f'{answer_input}', False, 'center', ('Arial', 5, 'bold'))


