from rest_framework import serializers
from ...models import CustomUser
from django.contrib.auth import authenticate
from django.utils.translation import ugettext_lazy as _


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=255)
    password = serializers.CharField(
        label=_("Password"),
        style={"input_type": "password"},
        trim_whitespace=False,
        max_length=128,
        write_only=True,
    )

    def validate(self, data):
        email = data.get("email")
        password = data.get("password")

        if email and password:
            user = authenticate(
                request=self.context.get("request"),
                email=email,
                password=password,
            )
            if not user:
                msg = _("Unable to log in with provided credentials.")
                raise serializers.ValidationError(msg, code="authorization")
        else:
            msg = _('Must include "email" and "password".')
            raise serializers.ValidationError(msg, code="authorization")
        data["user"] = user
        return data


class RegisterSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=255)
    password1 = serializers.CharField(
        label=_("Password1"),
        style={"input_type": "password"},
        trim_whitespace=False,
        max_length=128,
        write_only=True,
    )
    password2 = serializers.CharField(
        label=_("Password2"),
        style={"input_type": "password2"},
        trim_whitespace=False,
        max_length=128,
        write_only=True,
    )

    def validate(self, data):
        email = data.get("email")
        password1 = data.get("password1")
        password2 = data.get("password2")

        if not password1 == password2:
            msg = _("Passwords must be equal")
            raise serializers.ValidationError(msg, code="authorization")
        if CustomUser.objects.filter(email=email).exists():
            msg = _("User already exists pick another email")
            raise serializers.ValidationError(msg, code="authorization")

        return data


class EmptySerializer(serializers.Serializer):
    pass