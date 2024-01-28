# My first game

Simple version af (Pygame Zero Introduction)[https://pygame-zero.readthedocs.io/en/stable/introduction.html]

1. Start MU (mere [her](https://github.com/casperghst42/codingpirates/tree/main/mu-editor))
2. Click [+] New for at lave en ny fil
3. Indsæt følgende:
```py
"""
Mit allerførste Pygame Zero spil
"""

WIDTH = 300
HEIGHT = 300
```

![code-1](code-1.png)


4. Tryk på [Save] for at gemme.<br/>
4.1. Opret en folder (direktory): codingpirates/first-game<br/>
4.2. Gem filen: first-game.py<br/>
5. Kør filen ved at trykke på [Run], og du skulle gerne se:<br/>
![first-graphics](first-graphics.png)
6. Download følgende filer:<br/>
- [eep.wav](https://pygame-zero.readthedocs.io/en/stable/_static/eep.wav)
- [Platformer Art Deluxe](https://www.kenney.nl/assets/sci-fi-sounds)<br/><br/>
6.1. Unzip filerne Platform Art Delux<br/>
6.2. I dit codingpirates/first-game opret følgende directories:<br/>
6.2.1. sounds<br/>
6.2.2. images<br/>
6.2. Fra "Platform Art Deleux" "Extra animations and enemies/Alien sprites/alienGreen.png" til dit images directory. Og kopiere eep.wav til dit sounds directory."

6. Tilføj følgende:
```py
alien = Actor('alien')
alien.pos = 100, 56

WIDTH = 500
HEIGHT = alien.height + 20

def draw():
    screen.clear()
    alien.draw()
```
![code-2](code-2.png)

7. Test ....

8. Tilføj følgende:
8.1 Efter "alien.pos...":
```py
alien.topright = 0, 10
```
8.2 Efter "draw()" funktionen, tilføj følgende funktion:
```py
def update():
    alien.left += 2
    if alien.left > WIDTH:
        alien.right = 0
```
Der skulle nu være lidt bevægelse!!! (ya!)

Hvad med at kunnen klikke på noget.

9. Efter "update()" funktionen, tilføj dette:
```py
def on_mouse_down(pos):
    if alien.collidepoint(pos):
        print("Eek!")
    else:
        print("You missed me!")
```
<strong>Prøv at klikke på vores alien.</strong> Og kig på status vinduet:

```
Eek!
Eek!
You missed me!
You missed me!
```
)

10. Ændre vores on_mouse_down(pos) til dette:
```py
def on_mouse_down(pos):
    if alien.collidepoint(pos):
        sounds.eep.play()
        alien.image = 'alien_hurt'
```

Nu kan vi da se at vi rammer vores alien. 

