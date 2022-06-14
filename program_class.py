class Minum:

	def __init__(self,typeMinuman,harga):

		self.typeMinuman = typeMinuman

		self.harga = harga

		

	def chekIn(self):

		print('Anda mau beli minuman',self.typeMinuman,'dengan harga :',self.harga)

		

class pesan(Minum):

	pass

costumer1 = Minum('Lee mineral','2000')

costumer1.chekIn()

    

	

	

		
