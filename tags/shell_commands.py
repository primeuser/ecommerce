python manage.py shell
Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>> from tags.models import Tag
>>> Tags.objects.all()
Traceback (most recent call last):
  File "<console>", line 1, in <module>
NameError: name 'Tags' is not defined
>>> Tag.objects.all()
<QuerySet [<Tag: cube>, <Tag: t-shirt>, <Tag: camera>, <Tag: red>, <Tag: black>]>
>>> Tag.objects.last()
<Tag: black>
>>> black=Tag.objects.last()
>>> black.title
'black'
>>> black.slug
'black-34'
>>> black.active
True
>>> black.products
<django.db.models.fields.related_descriptors.create_forward_many_to_many_manager.<locals>.ManyRelatedManager object at 0x000002D4FA2FBB70>
>>> black.products.all()
<ProductQuerySet [<Product: t-shirt>, <Product: hat>, <Product: cap>, <Product: Camera Canon>, <Product: Camera Nikon>, <Product: Panasonic Camera>, <Product: camera Sony>, <Product: Fujifilm Camera>]>
>>> black.products.all().first()
<Product: t-shirt>
>>> exit()

C:\Users\Anand\Desktop\djangohaha\ecommerce>python manage.py shell
Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>> from products.model import Product
Traceback (most recent call last):
  File "<console>", line 1, in <module>
ModuleNotFoundError: No module named 'products.model'
>>> from products.models import Product
>>> qs=Product.objects.all()
>>> qs
<ProductQuerySet [<Product: t-shirt>, <Product: hat>, <Product: cap>, <Product: Supercomputer>, <Product: Camera Canon>, <Product: Camera Nikon>, <Product: Panasonic Camera>, <Product: camera Sony>, <Product: Fujifilm Camera>, <Product: cube>]>
>>> cube=qs.last()
>>> cube
<Product: cube>
>>> cube.title
'cube'
>>> cube.description
'In marketing, a product is anything that can be offered to a market that might satisfy a want or need.[1] In retailing, products are called merchandise. In manufacturing, products ar bought as raw materials and sold as finished goods. A service is another common product type. Commodities are usually raw materials such as metals and agricultural products, but a commodity can also be anything widely available in the open market. In project management, products are the formal definition of the project deliverables that make up or contribute to delivering the objectives of the project. In insurance, the policies are considered products offered for sale by the insurance company that created the contract. In economics and commerce, products belong to a broader category of goods. The economic meaning of product was first used by political economist Adam Smith.[citation needed] A related concept is that of a sub-product, a secondary but useful result of a production process. Dangerous products, particularly physical ones, that cause injuries to consumers or bystanders may be subject to product liability.\r\nIn marketing, a product is anything that can be offered to a market that might satisfy a want or need.[1] In retailing, products are called merchandise. In manufacturing, products ar bought as raw materials and sold as finished goods. A service is another common product type. Commodities are usually raw materials such as metals and agricultural products, but a commodity can also be anything widely available in the open market. In project management, products are the formal definition of the project deliverables that make up or contribute to delivering the objectives of the project. In insurance, the policies are considered products offered for sale by the insurance company that created the contract. In economics and commerce, products belong to a broader category of goods. The economic meaning of product was first used by political economist Adam Smith.[citation needed] A related concept is that of a sub-product, a secondary but useful result of a production process. Dangerous products, particularly physical ones, that cause injuries to consumers or bystanders may be subject to product liability.'
>>> cube.tag
Traceback (most recent call last):
  File "<console>", line 1, in <module>
AttributeError: 'Product' object has no attribute 'tag'
>>> cube.tags
Traceback (most recent call last):
  File "<console>", line 1, in <module>
AttributeError: 'Product' object has no attribute 'tags'
>>> cube.tag_set
<django.db.models.fields.related_descriptors.create_forward_many_to_many_manager.<locals>.ManyRelatedManager object at 0x00000216211A8978>
>>> cube.tag_set.all()
<QuerySet [<Tag: cube>]>
>>> cube.tag_set.filter(title__exact='cube')
<QuerySet [<Tag: cube>]>