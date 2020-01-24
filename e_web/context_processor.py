from .models import Shporta, Profile
from django.contrib.auth.models import User



def context(request):
	if request.user.is_authenticated:
		current_user = request.user
	else:
		current_user = User.objects.get(username='redi')
	numri_shportes = Profile.objects.filter(user=current_user).count()
	return {
		'numri_shportes': numri_shportes
	}