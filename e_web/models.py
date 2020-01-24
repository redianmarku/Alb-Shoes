from django.db import models
from django.contrib.auth.models import User


class Produkt(models.Model):
	titulli = models.CharField(max_length=200)
	cmimi = models.CharField(max_length=10)
	foto = models.ImageField(upload_to='images/')

	def __str__(self):
		return self.titulli	


class ProdukteReja(models.Model):
	produkt = models.OneToOneField(Produkt, on_delete=models.CASCADE)

	def __str__(self):
		return self.produkt.titulli	


class Shporta(models.Model):
	produkt = models.OneToOneField(Produkt, on_delete=models.CASCADE, primary_key=True)

	def __str__(self):
		return self.produkt.titulli


class Profile(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	produkt = models.OneToOneField(Produkt, on_delete=models.CASCADE, primary_key=True)

	
