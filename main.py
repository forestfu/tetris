from renderer import Renderer
from turtle import Screen
from time import sleep
# from sys import exit

screen = Screen()
screen.setup(410, 625)
screen.title("tetris")
screen.tracer(0)

renderer = Renderer()

screen.listen()
screen.onkeypress(renderer.right_pressed, "Right")
screen.onkeyrelease(renderer.right_release, "Right")
screen.onkeypress(renderer.left_pressed, "Left")
screen.onkeyrelease(renderer.left_release, "Left")
screen.onkeypress(renderer.up_pressed, "Up")
screen.onkeyrelease(renderer.up_release, "Up")
screen.onkeypress(renderer.down_pressed, "Down")
screen.onkeyrelease(renderer.down_release, "Down")
screen.onkeypress(renderer.space_pressed, "space")
screen.onkeyrelease(renderer.space_release, "space")
screen.onkeypress(renderer.s_pressed, "s")
screen.onkeyrelease(renderer.s_release, "s")

renderer.generate_piece()
while not renderer.game_over:
    renderer.render_grid()
    renderer.update_key_frames()
    renderer.update_falling_piece()
    screen.update()
    sleep(0.033)

screen.exitonclick()
