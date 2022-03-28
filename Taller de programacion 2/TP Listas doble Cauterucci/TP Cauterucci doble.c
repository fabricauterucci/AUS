/*
Implemente en C una lista doblemente enlazada.
*  El dato a guardar puede ser el que elija.
*  Debe poseer todas las operaciones correspondientes.
 */

#include <stdio.h>
#include <stdlib.h>
#include "ListaDoble.h"

int main(){
	// Casos de prueba
	ListaD lista;
	lista = NULL; // Creamos la lista y la inicializamos en Null
	
	//Primer elemento
	lista = insertar(1,  &lista); // Primero vamos a probar las funciones con un solo elemento, luego dos, luego 3 y luego con 4
	lista = insertar(1,  &lista); // Como vemos, la lista no admite elementos duplicados
	puts("--------------------------");
	listar(lista);
	puts("--------------------------");
	lista = eliminar(1, &lista);
	puts("--------------------------");
	listar(lista);
	puts("--------------------------");
	
	//Segundo elemento
	lista = insertar(1,  &lista);	lista = insertar(1,  &lista);
	lista = insertar(3,  &lista);  lista = insertar(3,  &lista); 
	puts("--------------------------");
	listar(lista);
	puts("--------------------------");
	lista = eliminar(3, &lista);
	lista = eliminar(1, &lista);
	puts("--------------------------");
	listar(lista);
	puts("--------------------------");
	
	//Tercer elemento
	lista = insertar(1,  &lista); //Ingresamos los elementos en este orden, para mostrar que ingresan por orden
	lista = insertar(3,  &lista);
	lista = insertar(2,  &lista); 
	
	puts("--------------------------");
	listar(lista);
	puts("--------------------------");
	lista = eliminar(3, &lista);
	lista = eliminar(1, &lista);
	lista = eliminar(2, &lista);
	puts("--------------------------");
	listar(lista);
	puts("--------------------------");
	
	
	//Cuarto elemento
	lista = insertar(1,  &lista); 	lista = insertar(-1,  &lista);
	lista = insertar(3,  &lista);	lista = insertar(2,  &lista); 
	puts("--------------------------");
	listar(lista);
	puts("--------------------------");
	lista = eliminar(3, &lista);
	lista = eliminar(-1, &lista);
	lista = eliminar(1, &lista);
	lista = eliminar(2, &lista);
	puts("--------------------------");
	listar(lista);
	puts("--------------------------");
	
	//Fin de casos de prueba
	
	return 0;
}

int lista_vacia(ListaD lista){
	if(lista == NULL) return 1;
	return 0;
}

/* Ingresa un elemento en la lista*/
ListaD insertar ( int elemento , ListaD* lista ){

	if ( lista_vacia(*lista) ){ //Primer elemento
		printf("Insertando %d en la lista\n", elemento);
		(*lista) = (ListaD) malloc(sizeof(NodoD));
		(*lista)->dato = elemento;
		(*lista)->sig = (*lista)->ant = NULL; 
		
		return (*lista);  //Los returns son para que la funcion no siga ejecutandose
	}
	
	if((*lista)->dato > elemento){ // Cuando va al inicio
		printf("Insertando %d en la lista\n", elemento);
		ListaD nuevo = (ListaD) malloc(sizeof(NodoD));
		nuevo->dato = elemento;
		nuevo->sig = (*lista);
		nuevo->ant = NULL;
		(*lista) = nuevo;

		return (*lista);
	}
		
		
	ListaD temp = (*lista); //Creamos una variable temporal para recorrer la lista sin perder el inicio
	for( ; temp->sig != NULL ; temp = temp->sig){
		if (temp->dato == elemento){
			printf("Ya existe el elemento %d en lista\n", elemento);
			return (*lista);
		}
		
		if((temp->dato < elemento) && (temp->sig->dato > elemento)){ //  Cuando esta entre dos
			printf("Insertando %d en la lista\n", elemento);
			ListaD nuevo = (ListaD) malloc(sizeof(NodoD));
			nuevo->dato = elemento;
			nuevo->sig = temp->sig;
			nuevo->ant = temp;
			temp->sig = nuevo;
			return (*lista);
		}
	}
	
	//temp apunta al ultimo
	if (temp->dato == elemento){
			printf("Ya existe el elemento %d en lista\n", elemento);
			return (*lista);
	}
	
	printf("Insertando %d en la lista\n", elemento);
	ListaD ultimo = (ListaD) malloc(sizeof(NodoD));
	ultimo->dato = elemento;
	ultimo->ant = temp;
	ultimo->sig = NULL;
	temp->sig = ultimo;
	
	return (*lista);
}

/* Muestra los elementos de la lista */
void listar ( ListaD lista){
	if(lista_vacia(lista)) printf("\nLa lista a mostrar esta vacia.\n");
	else{
		printf("Listo elementos\n\n");	
		ListaD temp = lista;
		for( ; temp != NULL ; temp = temp->sig){
			printf("Elemento := %d \n", temp->dato);
		}
		printf("\nFin listado\n");
	}
}

/*Elimina un elemento de la lista*/
ListaD eliminar (int elemento, ListaD* lista){
	if (lista_vacia(*lista)){  
		printf("No existe el elemento a eliminar\n");

		return (*lista);
	}
		
	if((*lista)->dato == elemento){
	printf("Elimino a %d\n", (*lista)->dato);
	ListaD aux = (*lista);
	if(!(lista_vacia((*lista)->sig))){ //Este es el caso de que la lista no tenga un unico elemento
		(*lista) = (*lista)->sig;
		(*lista)->ant = NULL;
		free(aux);
	
		return (*lista);
	} // Si la lista tiene un solo elemento, libero la memoria y devuelvo Null
		free(aux);
	
		return NULL;	
	}
		
	ListaD temp = (*lista)->sig;
	if(temp->dato == elemento && temp->sig == NULL){ // la lista solo tiene dos elementos, y estamos en el segundo
		printf("Elimino a %d\n", temp->dato);
		(*lista)->sig = NULL;
		free(temp);
	
		return (*lista);
	}
	
	temp = (*lista)->sig->sig; // Empezamos en el tercer elemento
	//Empezamos por ese debido a que al momento de la ejecución, no se me ocurria
	//otra forma de hacerlo andar, mas que separarlos por casos de listas de uno, dos y tres o mas elementos
	
	for( ; temp->sig != NULL; temp = temp->sig){
		if(temp->dato == elemento){
			printf("Elimino a %d\n", temp->dato);
			//Reordenacion de punteros, con liberacion de memoria del nodo a eliminar
			ListaD aux = temp;
			temp->ant->sig = temp->sig;
			temp->sig->ant = temp->ant;
			free(aux);
		} 
	}
	
	//temp apunta al ultimo elemento
	
	if(temp->dato == elemento){
		printf("\nElimino a %d\n", temp->dato); //ver aqui
		(temp->ant)->sig->sig = NULL;
		free(temp);
	}
	
	return (*lista); // En caso de que el elemento no este, se devuelve la misma lista
}

 // Codigo escrito y probado por Fabrizio Alejandro Cauterucci, con ayuda de la teoria de listas vista en clase
