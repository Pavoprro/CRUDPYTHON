from modelo.productodao import ProductoDAO

def main():
    productodao = ProductoDAO()
    productodao.listarProducto()

if __name__ == '__main__':
    main()