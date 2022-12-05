from rest_framework import serializers


class ForbiddenDomain:
    """Проверка домена"""

    def __init__(self, forbidden_domain: tuple):
        self.forbidden_domain = forbidden_domain

    def __call__(self, value):
        domain = value.split("@")[1]
        if domain in self.forbidden_domain:
            raise serializers.ValidationError(f"домен {domain} запрещен")
