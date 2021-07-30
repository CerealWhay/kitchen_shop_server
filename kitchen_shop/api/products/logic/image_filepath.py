

def product_image_path(obj, filename):
    return f'products_images/{obj.category.slug}/{obj.slug}/{filename}'
