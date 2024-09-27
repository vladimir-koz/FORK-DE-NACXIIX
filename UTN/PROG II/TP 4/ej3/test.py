from automovil import Automovil
import random
class testAutomovil():
    
    @staticmethod
    def test():
        
        auto_1 = Automovil("Ford", "Focus", 2005, 180, 100)
        
        iteraciones = int(input("Ingrese cantidad de iteraciones: "))
        
        for i in range(iteraciones):
            numero_aleatorio = random.randint(0, 3)
            parametros_aleatorios = random.randint(1, 50)
            
            if numero_aleatorio == 0:
                print (f"Velocidad = {auto_1.obtenerVelocidadActual()}, acelerar.", end = " ")
                auto_1.acelerar(parametros_aleatorios)
                print (f"Velocidad = {auto_1.obtenerVelocidadActual()}")
            if numero_aleatorio == 1:
                print (f"Velocidad = {auto_1.obtenerVelocidadActual()}, desacelerar.", end = " ")
                auto_1.desacelerar(parametros_aleatorios)
                print (f"Velocidad actual = {auto_1.obtenerVelocidadActual()}")
            if numero_aleatorio == 2:
                print (f"Velocidad = {auto_1.obtenerVelocidadActual()}, frenar.", end = " ")
                auto_1.frenarPorCompleto()
                print (f"El autó frenó.")
            if numero_aleatorio == 3:
                print (f"Falta para llegar a destino {auto_1.calcularMinutosParaLlegar(parametros_aleatorios)} minutos.")
        
if __name__ == '__main__':
    testAutomovil.test()