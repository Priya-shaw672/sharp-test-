class UserInfo(forms.ModelForm):
    class Meta:
        model = Login
        fields = "__all__"