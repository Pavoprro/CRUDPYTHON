from modelo.clientedao import ClienteDAO

def main():
    clientedao = ClienteDAO()
    clientedao.contarClientes()

if __name__ == '__main__':
    main()