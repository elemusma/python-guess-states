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

# print(states[states['state'] == 'Colorado'].x)

turtle.shape(img)

# keep_guessing = True
# guessed_right = 0

guessed_states = []

while len(guessed_states) < 50:
    screen.update()
    answer_state = screen.textinput(title=f'{len(guessed_states)}/50 States Guessed', prompt='What\'s another state\'s name?').title()

    if answer_state == 'Exit':
        break
    if (states['state'].eq(answer_state)).any():
        # guessed_right += 1
        guessed_states.append(answer_state)
        all_states.remove(answer_state)
        answer_state_turtle = turtle.Turtle()
        # print(answer_state)
        state_data = states[states['state'] == answer_state]
        # x_coor = states[states['state'] == answer_state].x
        # y_coor = states[states['state'] == answer_state].y
        # print(float(x_coor))
        # print(float(y_coor))
        answer_state_turtle.hideturtle()
        answer_state_turtle.penup()
        answer_state_turtle.goto(float(state_data.x), float(state_data.y))
        answer_state_turtle.write(answer_state, align='center', font=('Arial', 15, 'normal'))
        # print('hello')
    
    # if guessed_right > 51:
    #     keep_guessing = False
    # print(answer_state)

# states to learn.csv
# create list of all states
# when guessed right, remove current state from all states list
all_states_df = pandas.DataFrame(all_states)
all_states_df.to_csv('states_to_learn.csv')

# turtle.mainloop()
# screen.exitonclick()