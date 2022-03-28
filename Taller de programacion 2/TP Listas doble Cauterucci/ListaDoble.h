/* 
 * 
 */

#ifndef __LISTADOBLE_H__
#define __LISTADOBLE_H__

typedef struct nodo {
	int dato ;
	struct nodo* sig ;
	struct nodo* ant ;
} NodoD;

typedef NodoD* ListaD;


/* Devuelve 1 si la lista es vacía, 0 en caso contrario */
int lista_vacia(ListaD);

/* Ingresa un elemento en la lista*/
ListaD insertar (int , ListaD* );

/* Muestra los elementos de la lista */
 void listar ( ListaD );

/*Elimina un elemento de la lista*/
ListaD eliminar (int , ListaD* );


#endif




