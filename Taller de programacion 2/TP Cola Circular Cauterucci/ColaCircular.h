#ifndef __COLACIRCULAR_H__
#define __COLACIRCULAR_H__

//Deficion de los tipos de datos
typedef struct nodo{
	int dato ;
	struct nodo *sig;
} NodoC;

typedef NodoC* ColaC;

/* Devuelve 1 si la cola es vacía, 0 en caso contrario */
int cola_vacia(ColaC);

/* Ingresa un elemento en la cola*/
void insertar(ColaC*, ColaC*, int);

/* Muestra los elementos de la cola */
void listar(ColaC);

/*Elimina un elemento de la lista*/
void eliminar(ColaC*, ColaC*);


#endif




