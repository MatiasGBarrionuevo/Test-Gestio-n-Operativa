import requests

lista = ["179571326"]

archivo = open("prueba.txt","w")

for id_seller in lista:

	datos = requests.get('https://api.mercadolibre.com/sites/MLA/search?seller_id='+id_seller).json()
	items = datos['results']

for item in items:
    id_item = item['id']
    archivo.write("ID item = "+id_item+"\n")

    title_item = item['title']
    archivo.write("title item = "+title_item+"\n")
    
    category_id_item = item['category_id']
    archivo.write("category_id item = "+category_id_item+"\n")
    
    category = requests.get('https://api.mercadolibre.com/categories/'+category_id_item).json() 
    name_category = category['name']
    
    archivo.write("name category = "+name_category+"\n\n")
    

archivo.close()


