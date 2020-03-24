from django import forms


class TracklistForm(forms.Form):
    url = forms.URLField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',  # specify CSS class
            'placeholder': 'Podcast URL'  # default text
        }
    ))


class SpotifyForm(forms.Form):
    playlist_name = forms.CharField(initial='', widget=forms.TextInput(
        attrs={
            'class': 'form-control',  # specify CSS class
            'placeholder': 'Playlist name',  # default text
        }
    ))
    existing_playlists = forms.ChoiceField(choices=[], widget=forms.Select(
        attrs={
            'id': 'opt-param',
            'class': 'form-control',

        }
    ))
