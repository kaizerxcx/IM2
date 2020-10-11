from django import template 

register = template.Library() 

@register.filter
def in_category(things, category):
	return things.filter(sku=category)


@register.filter
def in_filter(things, category):
	return things.filter(employee_id=category)
		