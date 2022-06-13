"""PATRON DE DISEÑO DAO (data access object) 
    es un patron de diseño que permite acceder a los datos de una base de datos"""
    
""""CRUD: Create, Read, Update, Delete"""


from loger_base import log
from personas import Persona
from conexion import Conexion
from cursor_pool import CursorPool

class PersonaDAO:
    _SELECT = 'SELECT * FROM persona ORDER BY id_persona'
    _UPDATE = "UPDATE persona SET nombre=%s,apellido=%s,email=%s WHERE id_persona=%s"
    _INSERT = "INSERT INTO persona(nombre,apellido,email) VALUES(%s,%s,%s)"  
    _DELETE = "DELETE FROM persona WHERE id_persona=%s"  
    @classmethod
    def seleccionar(cls):
        with CursorPool() as cursor:
            cursor.execute(cls._SELECT)
            registros = cursor.fetchall()
            personas = []
            for registro in registros:
                # es una asignacion de variables
                persona = Persona(registro[0],registro[1],registro[2],registro[3])
                personas.append(persona)
            return personas
            
    @classmethod
    def insertar(cls,persona):
        with CursorPool() as cursor:
            datos = (persona.nombre,persona.apellido,persona.email)
            cursor.execute(cls._INSERT,datos)
            log.debug(f"personas {persona}") 
            return cursor.rowcount
    @classmethod
    def actualizar (cls,persona):
        with CursorPool() as cursor:
            datos = (persona.nombre,persona.apellido,persona.email,persona.id_persona)
            cursor.execute(cls._UPDATE,datos)
            log.debug(f"usuario actualizado {persona}")
            return cursor.rowcount
    @classmethod 
    def eliminar (cls,persona):
        with CursorPool() as cursor:
            datos =  (persona.id_persona,)   
            cursor.execute(cls._DELETE,datos)
            log.debug(f"ususario eliminado {persona}")
            return cursor.rowcount

if __name__ == "__main__":
    #puebas
    # #insertar
    # persona1 =Persona(nombre='Deverlan',apellido="thomsom",email="thomson@anderson.com")
    # persona_insertada = PersonaDAO.insertar(persona1)
    # log.debug(f"personas insertadas {persona_insertada}")
    
    
    # seleccionsar
    # personas=PersonaDAO.seleccionar()
    # for persona in personas:
    #     log.debug(persona)
        
        
    # actualizar
    # persona=Persona(46,"criter","us","us@criter")
    # persona_actualizada =PersonaDAO.actualizar(persona)
    # log.debug(f"personas actualizadas {persona_actualizada}")
    
    
    #eliminar
    # persona=Persona(id_persona=45)
    # persona_eliminada = PersonaDAO.eliminar(persona)
    # log.debug(f"persona eliminada {persona_eliminada}")