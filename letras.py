from time import sleep
import os
def limpar_tela():
    if os.name == "nt":

        comando = "cls"

    else:
        comando = "clear"

    os.system(comando)
def soletrar(texto: str):
    palavra_separada = []

    for letra in texto:
        palavra_separada.append(letra)

        if letra == ",":
            sleep(0.3)

        elif letra =="\n":
            sleep(0.8)

        else:
            sleep(0.1)
            
        limpar_tela()
        print("".join(palavra_separada))



musica = """Don't ask me why
We couldn't make it happen
We've just got nothing to go on for
I waste my time
Drinking all of your wine
And staying sober in the meantime
While I listened
You relisted
All the reasons
That you had for leaving
I insisted
You resisted
It didn't go down very well
You say it's me
I say I'm your reflection
You smash the mirror
But we've had that
Before
You're so confused
Don't know what you require
Won't be the puppet on your wire
No more
While you listened
I relisted
All the reasons
That I had for leaving
You insisted
But I resisted
And it didn't go down very well
At all to say the least (It didn't go down very well)
At all to say the least (It didn't go down very well)
Remember when the sun was shining down
It felt so magical
And you were there with me
I never thought it too incredible
Why did you have to go?
What did I say?
Where are you going?
And I don't know
What I'd have done
If you had done
What I'm going to do
At all to say the least
It didn't go down very well
At all to say the least
It didn't go down very well
And again and again
It didn't go down very well
And again and again
"""


soletrar(musica)