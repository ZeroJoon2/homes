from django import forms
from supply.models import PropertyListing


class PropertyListingForm(forms.ModelForm):
    class Meta:
        model = PropertyListing
        fields = [
            "width",
            "height",
            "price",
            "owner_fee",
            "rooms",
            "bath",
            "is_park",
            "age",
            "surround",
            "etc",
        ]

        labels = {
            "width": "면적(m2)",
            "height": "층수",
            "price": "임대료",
            "owner_fee": "관리비",
            "rooms": "방 개수",
            "bath": "욕실",
            "is_park": "주차장 여부",
            "age": "연식",
            "surround": "주변환경",
            "etc": "기타 참고사항",
        }

        widgets = {
            "house_type": forms.Select(attrs={"class": "form-control"}),
            "transaction_type": forms.Select(attrs={"class": "form-control"}),
        }
