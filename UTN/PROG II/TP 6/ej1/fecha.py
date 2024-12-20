class Fecha:
    
    def __init__(self, dia:int, mes:int, anio:int):
        if isinstance(dia, int) and 0 < dia <= 31:
            self.__dia = dia
        else:
            raise TypeError("El valor del parametro dia debe ser un numero entero positivo entre 0 y 31 inclusive.")
        
        if isinstance(mes, int) and 0 < mes <= 12:
            self.__mes = mes
        else:
            raise TypeError("El valor del parametro mes debe ser un numero entero positivo entre 0 y 12 inclusive.")
        
        if isinstance(anio, int) and 0 < anio <= 2024:
            self.__anio = anio
        else:
            raise TypeError("El valor del parametro anio debe ser un numero entero positivo entre 0 y 2024 inclusive.")
    
    def establecerDia(self, dia:int):
        if isinstance(dia, int) and 0 < dia <= 31:
            self.__dia = dia
        else:
            raise TypeError("El valor del parametro dia debe ser un numero entero positivo entre 0 y 31 inclusive.")
        
    
    def establecerMes(self, mes:int):
        if isinstance(mes, int) and 0 < mes <= 12:
            self.__mes = mes
        else:
            raise TypeError("El valor del parametro mes debe ser un numero entero positivo entre 0 y 12 inclusive.")
    
    def establecerAnio(self, anio:int):
        if isinstance(anio, int) and 0 < anio <= 2024:
            self.__anio = anio
        else:
            raise TypeError("El valor del parametro anio debe ser un numero entero positivo entre 0 y 2024 inclusive.")
    
    def obtenerDia(self)->int:
        return self.__dia
    
    def obtenerMes(self)->int:
        return self.__mes
    
    def obtenerAnio(self)->int:
        return self.__anio
    
    def esAnterior(self, otraFecha:'Fecha')->bool:
        self_esAnterior = False
        if isinstance(otraFecha, object):
            if self.obtenerAnio() < otraFecha.obtenerAnio():
                self_esAnterior = True
                return self_esAnterior
            elif (self.obtenerAnio() == otraFecha.obtenerAnio()):
                if self.obtenerMes() < otraFecha.obtenerMes():
                    self_esAnterior = True
                    return self_esAnterior
                elif self.obtenerMes() == otraFecha.obtenerMes():
                    if self.obtenerDia() < otraFecha.obtenerDia():
                        self_esAnterior = True
                        return self_esAnterior
        else:
            raise TypeError("El parametro ingresado debe ser un objeto de tipo Fecha.")
        
    def sumaDias(self, cantDias:int)->'Fecha':
        sumar_dia = self.obtenerDia() + cantDias
        
        dia = self.__dia
        mes = self.__mes
        anio = self.__anio
        
        while sumar_dia > 31:
            sumar_dia -= 31
            mes += 1
            
            if mes > 12:
                mes = 1
                anio += 1
                
        dia = sumar_dia
        
        return Fecha(dia, mes, anio)
    
    def diaSiguiente(self)->'Fecha':
        lista_datos_fecha = [self.__dia, self.__mes, self.__anio]
        
        if lista_datos_fecha[0] < 31:
            lista_datos_fecha[0] += 1
        else:
            if lista_datos_fecha[1] < 12:
                lista_datos_fecha[1] += 1 
                lista_datos_fecha[0] = 1
            else:
                lista_datos_fecha[2] += 1
                lista_datos_fecha[1] = 1
                lista_datos_fecha[0] = 1
                
        return Fecha(lista_datos_fecha[0], lista_datos_fecha[1],lista_datos_fecha[2])
    
    def esIgualQue(self, otraFecha:'Fecha')->bool:
        return self.obtenerDia() == otraFecha.obtenerDia() and self.obtenerMes() == otraFecha.obtenerMes() and self.obtenerAnio() == otraFecha.obtenerAnio()
    
    def __str__(self):
        return f'{self.__dia}/{self.__mes}/{self.__anio}'
    