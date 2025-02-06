import arcade

arcade.open_window(800, 600, "Drawing Example")

arcade.set_background_color(arcade.color.WHITE)

arcade.start_render()

x = 300 ; y = 300 ; radius = 200
arcade.draw_circle_filled(x,y,radius,arcade.color.YELLOW)


x = 370 ; y = 350 ; radius = 40
arcade.draw_circle_filled(x,y,radius,arcade.color.BLACK)


x = 230 ; y = 350 ; radius = 15
arcade.draw_circle_filled(x,y,radius,arcade.color.BLACK)


x = 300 ; y = 280 ; width = 60 ; height = 50
start_angle= 180; end_angle = 360; line_width = 50
arcade.draw_arc_outline(x,y,width,height,arcade.color.BLACK,start_angle,end_angle,line_width)

x = 300 ; y = 200 ; width = 60 ; height = 50
start_angle= 190; end_angle = 380; line_width = 100
arcade.draw_arc_outline(x,y,width,height,arcade.color.BLACK,start_angle,end_angle,line_width)

arcade.finish_render()

arcade.run()