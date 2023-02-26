import turtle
import pandas

screen = turtle.Screen()
screen.title('U.S. States Game')
img = 'blank_states_img.gif'
screen.addshape(img)
screen.tracer(0)

states = pandas.read_csv('50_states.csv')
all_states = states.state.to_list()
print(all_states)

turtle.shape(img)

guessed_states = []
states_to_learn = []
missing_states = []

while len(guessed_states) < 50:
    screen.update()
    answer_state = screen.textinput(title=f'{len(guessed_states)}/50 States Guessed', prompt='What\'s another state\'s name?').title()

    if answer_state == 'Exit':
        break
    if (states['state'].eq(answer_state)).any():
        
        answer_state_turtle = turtle.Turtle()

        state_data = states[states['state'] == answer_state]
        answer_state_turtle.hideturtle()
        answer_state_turtle.penup()
        answer_state_turtle.goto(float(state_data.x), float(state_data.y))
        answer_state_turtle.write(answer_state, align='center', font=('Arial', 15, 'normal'))

        guessed_states.append(answer_state)
        missing_states = [state for state in all_states if state not in guessed_states]
        # [state for state in guessed_states]
        # all_states.remove(answer_state)
        # [guessed_states.append(state) for state ]
        missing_states_df = pandas.DataFrame(missing_states)
        missing_states_df.to_csv('states_to_learn.csv')

