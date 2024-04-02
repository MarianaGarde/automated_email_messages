

from sql_connection import get_sql_connection

def get_all_products(connection):
    cursor = connection.cursor()
    query = ("select products.product_id, products.item, products.units, products.price from products")
    cursor.execute(query)
    response = []
    for (product_id, item, units, price) in cursor:
        response.append({
            'product_id': product_id,
            'item': item,
            'units': units,
            'price': price,
        })
    return response

def insert_new_product(connection, product):
    cursor = connection.cursor()
    query = ("INSERT INTO products "
             "(item, units, price)"
             "VALUES (%s, %s, %s)")
    data = (product['item'], product['units'], product['price'])

    cursor.execute(query, data)
    connection.commit()

    return cursor.lastrowid

def delete_product(connection, product_id):
    cursor = connection.cursor()
    query = ("DELETE FROM products where product_id=" + str(product_id))
    cursor.execute(query)
    connection.commit()

    return cursor.lastrowid

if __name__ == '__main__':
    connection = get_sql_connection()
    # print(get_all_products(connection))
    print(insert_new_product(connection, {
        'item': 'socks_puma_pink',
        'units': '1',
        'price': 4.99
    }))