from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponseNotFound
from django.contrib.auth import get_user_model
import logging
from .models import SmartHealthCard, SmartHealthJWKS
from django.http import JsonResponse
from django.views.decorators.http import require_GET
from django.contrib.auth.decorators import login_required
from ..accounts.models import UserProfile
from django.conf import settings
# from django.views.decorators.cache import never_cache
from ratelimit.decorators import ratelimit

logger = logging.getLogger('healthcards.%s' % __name__)
User = get_user_model()

__author__ = "Alan Viars"


@require_GET
def jwks_json(request):
    """
    Views that returns smart health card /.well-known/jwks.json
    """
    jwks = SmartHealthJWKS.objects.all()[0]
    return JsonResponse(jwks.as_jwks)


@require_GET
@login_required
def display_user_index(request):
    smart_health_cards = SmartHealthCard.objects.filter(user=request.user)
    return render(request, "user_index.html", context={"smart_health_cards": smart_health_cards})


@ratelimit(key='ip', rate=settings.LOGIN_RATELIMIT, method='GET', block=True)
@require_GET
def shc_psi(request, sub):
    up = get_object_or_404(UserProfile, subject=sub)
    if up.public_safety_profile == "PUBLIC":
        smart_health_cards = get_list_or_404(SmartHealthCard, user=up.user)
        return render(request, "smart_health_cards.html",
                      context={"smart_health_cards": smart_health_cards,
                               "profile": up})
    return HttpResponseNotFound('Subject %s is not found or it is set to private mode.' % (sub))
