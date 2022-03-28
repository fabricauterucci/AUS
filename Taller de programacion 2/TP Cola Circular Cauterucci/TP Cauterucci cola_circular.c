/*
Teniendo en cuenta lo descripto en el apunte de estructuras, implemente en C una cola circular
 */

#include <stdio.h>
#include <stdlib.h>
#include "ColaCircular.h"

int main(){
	ColaC primero;
	ColaC ultimo;
	
	primero = NULL;
	ultimo = NULL;
	
	// Testeamos la funcion listar,  sin elementos en la cola
	listar(primero);
	
	// Insertamos 4 elementos en la cola
	// Ademas cabe destacar que uno de los elementos ingresados, es repetido
	// Destacamos esto, porque a la hora de listar podria ser inconveniente
	//Asique para mostrar bien la lista sin problemas, directamente comparamos direcciones de memoria
	puts("--------------------------");
	insertar(&primero,&ultimo,10);
	insertar(&primero,&ultimo,20);
	insertar(&primero,&ultimo,30);
	insertar(&primero,&ultimo,10);
	puts("--------------------------");
	listar(primero);
	puts("--------------------------");
	//Como es una cola, siempre se elimina desde el primer elemento, por ser FIFO( First In First Out)
	eliminar(&primero,&ultimo);
	puts("--------------------------");
	eliminar(&primero,&ultimo);
	puts("--------------------------");
	
	listar(primero);
	puts("--------------------------");
	
	eliminar(&primero,&ultimo);
	puts("--------------------------");
	listar(primero);
	puts("--------------------------");
	insertar(&primero,&ultimo,30);
	puts("--------------------------");
	
	listar(primero);
	puts("--------------------------");
	return 0;
}

/* Devuelve 1 si la cola es vacía, 0 en caso contrario */
int cola_vacia(ColaC cola){
	if(cola == NULL) return 1;
	return 0;
}

/* Ingresa un elemento en la cola*/
void insertar(ColaC* primero, ColaC* ultimo, int dato){
	ColaC aux; //Creo un puntero auxiliar apuntando a 
	//Pido memoria para un nodo
	
	aux = (ColaC) malloc(sizeof(NodoC));
	if (cola_vacia(aux)){
		printf("\nMemoria insuficiente.\n");
		exit(1);
	}
	printf("\nAgrego al elemento %d a la cola.\n", dato);
	aux->dato = dato;
	aux->sig = NULL;
	if(cola_vacia(*primero)) (*primero) = aux;
	else (*ultimo)->sig = aux;
	
	*ultimo = aux;
	(*ultimo)->sig = *primero;
}

/* Muestra los elementos de la cola */
void listar(ColaC cola){
	if(cola_vacia(cola)) printf("\nLa cola a mostrar esta vacía.\n");
	else{
		printf("\nListo elementos:\n");
		printf("\n %d \n", cola->dato);
		ColaC aux = cola; // Nos interesa guardar la direccion de memoria del primer elemento de la cola
		// para modificiar la condicion del while, y que si ya mostro toda la lista, no repita
		cola = cola->sig;
		
		while(!(cola_vacia(cola)) && cola != aux ){
			printf("\n %d \n", cola->dato);
			cola = cola->sig;
		}	
	}
		printf("\nFin listado\n");
}

/*Elimina un elemento de la lista*/	
void eliminar(ColaC* primero,ColaC* ultimo){
	ColaC aux;
	aux = (*primero); // Apunto aux al nodo a eliminar
	(*primero) = (*primero)->sig; //cambio el primero al siguiente nodo
	(*ultimo)->sig = (*primero);
	if(cola_vacia(*primero)) (*ultimo) = NULL;
	printf("\nElimino al nodo %d\n", aux->dato);
	free(aux);
}
	

// Codigo escrito y probado por Fabrizio Alejandro Cauterucci, con ayuda de la teoria de colas vista en clase
