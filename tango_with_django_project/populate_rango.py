import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE' , 'tango_with_django_project.settings')

import django
django.setup()

from rango.models import Category, Page

def populate() :
	python_cat = add_category('Python')
	add_page(category = python_cat,title="Python",url="http://docs.python.org/2/tutorial")
	add_page(category = python_cat,title="Think Python",url="http://www.greenteapress.com/thinkpython/")
	add_page(category = python_cat,title="Learn Python",url="http://www.korokithakis.net/tutorials/python/")	

	for category in Category.objects.all():
		for page in Page.objects.filter(category = category):
			print ("- {0} - {1}".format(str(category),str(page)))

def add_category(name) :
	new_category = Category.objects.get_or_create(name=name)[0]
	return new_category

def add_page(category,title,url,views=0) :
	new_page = Page.objects.get_or_create(category = category,title = title)[0]
	new_page.url = url
	new_page.views = views
	new_page.save()
	return new_page

if __name__ == '__main__' :
	print ("Starting Rango population script..")
	populate()