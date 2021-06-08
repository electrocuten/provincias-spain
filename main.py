import turtle
import pandas

CENTRADO = "center"
FUENTE = ("Courier", 10, "normal")

pantalla = turtle.Screen()
pantalla.title("17 comunidades de España")
imagen = "comunidades_espana.gif"
pantalla.addshape(imagen)

turtle.shape(imagen)
tab_comunidades = pandas.read_csv("19_comunidades.csv")
# dic_coordenadas_comunidades = {}
# for i in range(len(tab_comunidades)):
#     dic_coordenadas_comunidades[tab_comunidades["Comunidad"][i]] = (tab_comunidades["x"][i], tab_comunidades["y"][i])
# cont = 0
# while cont < len(dic_coordenadas_comunidades):
#     respuesta = pantalla.textinput(title=f"{cont}/19", prompt="Introduce una comunidad autonoma").title()
#     if respuesta in dic_coordenadas_comunidades.keys():
#         comunidad = turtle.Turtle()
#         comunidad.penup()
#         comunidad.hideturtle()
#         comunidad.goto(x=dic_coordenadas_comunidades[respuesta][0], y=dic_coordenadas_comunidades[respuesta][1])
#         comunidad.write(respuesta, align=CENTRADO, font=FUENTE)
#         cont +=1

cont = 0
game_on = True

#list_comunidades = tab_comunidades["Comunidad"].to_list()
while game_on:
    respuesta = pantalla.textinput(title=f"{cont}/19", prompt="Introduce una comunidad autonoma")
    if respuesta == None:
        game_on = False
    elif respuesta.lower() == "salir":
        break
    elif respuesta.title() in tab_comunidades.Comunidad.to_list():
        # Tomamos la fila que contiene los datos de la respuesta
        coordenadas = tab_comunidades[tab_comunidades.Comunidad == respuesta]
        comunidad = turtle.Turtle()
        comunidad.penup()
        comunidad.hideturtle()
        # Nos movemos a las coordenadas de dicha fila y escribimos la respuesta
        comunidad.goto(int(coordenadas["x"]),int(coordenadas["y"]))
        comunidad.write(respuesta, align=CENTRADO, font=FUENTE)
        cont +=1

    if cont == len(tab_comunidades):
        game_on = False

if cont == len(tab_comunidades):
    ganador = turtle.Turtle()
    ganador.hideturtle()
    ganador.write("HAS GANADO",align=CENTRADO,font=("Courier", 40, "normal"))
    pantalla.exitonclick()
else:
    pantalla.bye()
