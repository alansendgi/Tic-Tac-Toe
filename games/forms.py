HUMAN = 0
COMPUTER = 1
PLAYER_CHOICES = (
    (HUMAN, 'X'),
    (COMPUTER, 'O'),
)

class PlayerForm(forms.Form):
    game_square = forms.ChoiceField(choices=PLAYER_CHOICES, 
                                    widget=forms.RadioSelect())
    
