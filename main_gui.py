import flet as ft
import flet.canvas as cv
from logic import Hangman


def main(page: ft.Page):
    hangman = Hangman()
    white = '#FAFAFA'
    black = '#282C34'
    page.bgcolor=black
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    stroke_thin = ft.Paint(stroke_width=6, style=ft.PaintingStyle.STROKE, color=white)
    stroke_big = ft.Paint(stroke_width=15, style=ft.PaintingStyle.STROKE, color=white)
    global dlg
    
    def reset_game(e):
        global dlg
        print('Reset Game')
        dlg.open = False
        page.update()
        hangman.__init__()
        clean_hangman()
        guess.read_only = False
        button_guess.disabled = False
        guess.update()
        button_guess.update()
        verbraucht_buchstaben.value = ''
        verbraucht_buchstaben.update()
        text1.value = '  '.join(hangman.get_guessed_letters())
        text1.update()
    
    
    def clean_hangman():
        graphic.clean()
        draw_hang()
        graphic.update()
    
    
    def draw_hang():
        graphic.shapes.extend([
            cv.Line(x1=50, y1=450, x2=350, y2=450, paint=stroke_big),
            cv.Line(x1=120, y1=50, x2=120, y2=450, paint=stroke_big),
            cv.Line(x1=113, y1=50, x2=250, y2=50, paint=stroke_big),
            cv.Line(x1=243, y1=50, x2=243, y2=100, paint=stroke_big),
            cv.Line(x1=243, y1=100, x2=243, y2=140, paint=stroke_thin),
        ])
      
        
    def update_hangman(num):
        if num >= 1:
            # Kopf
            graphic.shapes.append(
                cv.Circle(x=243, y=170, radius=30, paint=stroke_thin),
            )
        if num >= 2:
            # Body
            graphic.shapes.append(
                cv.Line(x1=243, y1=200, x2=243, y2=270, paint=stroke_thin),
            )
        if num >= 3:
            # Arm rechts
            graphic.shapes.append(
                cv.Line(x1=243, y1=200, x2=210, y2=260, paint=stroke_thin),
            )
        if num >= 4:
            # Arm links
            graphic.shapes.append(
                cv.Line(x1=243, y1=200, x2=276, y2=260, paint=stroke_thin),
            )
        if num >= 5:
            # Bein rechts
            graphic.shapes.append(
                cv.Line(x1=243, y1=270, x2=210, y2=330, paint=stroke_thin),
            )
        if num >= 6: 
            # Bein links
            graphic.shapes.append(
                cv.Line(x1=243, y1=270, x2=276, y2=330, paint=stroke_thin),
            )
        graphic.update()
    
    
    def check_game_over():
        global dlg
        if hangman.check_game_over() == 'game_lost':
            guess.read_only = True
            button_guess.disabled = True
            guess.update()
            button_guess.update()
            dlg = ft.AlertDialog(
                modal=True,
                title=ft.Text('Spiel verloren!'),
                content=ft.Text(f'Das gesuchte Wort war: {hangman.get_word()}'),
                actions=[
                    ft.TextButton('OK', on_click=reset_game)
                ]
            )
            page.dialog=dlg
            dlg.open=True
            page.update()
            
        elif hangman.check_game_over() == 'game_won':
            guess.read_only = True
            button_guess.disabled = True
            guess.update()
            button_guess.update()
            dlg = ft.AlertDialog(
                modal=True,
                title=ft.Text(f'Spiel gewonnen!'),
                content=ft.Text(f'Das gesuchte Wort war: {hangman.get_word()}'),
                actions=[
                    ft.TextButton('OK', on_click=reset_game)
                ]
            )
            page.dialog=dlg
            dlg.open=True
            page.update()
    
    
    def raten(e):
        letter = guess.value
        if letter == '':
            pass
        else:
            hangman.make_guess(letter)
            # update word
            text1.value = '  '.join(hangman.get_guessed_letters())
            text1.update()
            # update used letters
            verbraucht_buchstaben.value = ', '.join(hangman.get_used_letters())
            verbraucht_buchstaben.update()
            # update graphic
            update_hangman(hangman.get_number_guesses())
            # clear input field
            guess.value = ''
            guess.update()
            guess.focus()
            check_game_over()
    
    
    # row 1 - Header
    header = ft.Text('Hangman', color=white, size=30)
    row1 = ft.Row(controls=[header], alignment=ft.MainAxisAlignment.CENTER)
    
    # row 2 - Hangman Graphics
    graphic = cv.Canvas([cv.Line(x1=0, y1=0, x2=0, y2=0, paint=stroke_big)])
    
    cont = ft.Container(
        content=graphic,
        bgcolor=black,
        width=400,
        height=460,
        padding=0,
        margin=0
    )
    
    draw_hang()

    # row 3 - Word to be guessed
    word = '  '.join(hangman.get_guessed_letters())
    text1 = ft.Text(word, color=white, size=25)
    row3 = ft.Row(controls=[text1], alignment=ft.MainAxisAlignment.CENTER)
    
    # row 4 - Letter Input
    guess = ft.TextField(
        hint_text='Buchstabe',
        hint_style=ft.TextStyle(color=white),
        border=None, 
        border_color=white, 
        bgcolor=black, 
        color=white, 
        cursor_color=white,
        cursor_width=10,
        max_length=1,
        autofocus=True,
        counter_text=' ',
        text_align=ft.TextAlign.CENTER,
        capitalization=ft.TextCapitalization.CHARACTERS,
    )
    button_guess = ft.ElevatedButton(
        'Raten', 
        on_click=raten, 
        style=ft.ButtonStyle(
            color={
                ft.MaterialState.DEFAULT: ft.colors.WHITE,
                ft.MaterialState.DISABLED: ft.colors.WHITE,
            },
            bgcolor={
                ft.MaterialState.DEFAULT: ft.colors.BLUE_900,
                ft.MaterialState.DISABLED: ft.colors.BLUE_900,
            }
        ),
    )
    row4 = ft.Row(controls=[guess, button_guess], alignment=ft.MainAxisAlignment.CENTER)
    
    # row 5 - Header Used Letters
    verbraucht_label = ft.Text('Verbrauchte Buchstaben: ', color=white)
    row5 = ft.Row(controls=[verbraucht_label], alignment=ft.MainAxisAlignment.CENTER)
    
    # row 6 - Used Letters
    verbraucht_buchstaben = ft.Text('', color=white)
    row6 = ft.Row(controls=[verbraucht_buchstaben], alignment=ft.MainAxisAlignment.CENTER)
    
    page.add(row1, cont, row3, row4, row5, row6)

ft.app(target=main)