
#Crear una subrutina llamada "Login", que recibe un nombre de usuario y una 
#contraseña y te devuelve Verdadero si el nombre de usuario es "usuario1" y la 
#contraseña es "asdasd". Además recibe el número de intentos que se ha intentado 
#hacer login y si no se ha podido hacer login incremente este valor.
#Crear un programa principal donde se pida un nombre de usuario y una contraseña 
#y se intente hacer login, solamente tenemos tres oportunidades para intentarlo.
    def Login (nombre, password, intentos_dict):
                if nombre == "usuario1" and password == "asdasd":
        return True
    else:
        intentos_dict['valor'] += 1
        return False

def entrar_en_el_sistema():
    
    intentos = {'valor': 0}
    entrar = False
    
    while not entrar and intentos['valor'] < 3:
        usuario = input("Usuario: ")
        clave = input("Password: ")
        
        entrar = login(usuario, clave, intentos)
        
        if not entrar:
            intentos_restantes = 3 - intentos['valor']
            print(f"Error. Usuario o contraseña incorrectos. Te quedan {intentos_restantes} intentos.")
            print("-" * 20)

    if entrar:
        print("\n¡Bienvenidos al sistema!")
    else:
        print("\nAcceso denegado. Has agotado los 3 intentos.")
