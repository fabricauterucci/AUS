#ifndef __KRUSKAL_H__
#define __KRUSKAL_H__
/*Kruskal.h*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef int tipo_nombre;
typedef int tipo_elemento;
typedef int vertice;

#define VERTICES 5

typedef struct _ARISTA{
	vertice u;
	vertice v;
	int costo;
}Arista;

typedef struct _RAMA{
	Arista a;
	struct _RAMA* sig;
} Rama;

typedef struct _ENCABEZADO{
	int cuenta;
	int primer_elemento;
}Encabezado;

typedef struct _NOMBRE{
	tipo_nombre nombre_conjunto;
	int siguiente_elemento;
}Nombre;

typedef struct _CONJUNTO_CE{
	Nombre nombres[VERTICES];
	Encabezado encabezamientos_conjunto[VERTICES];
}conjunto_CE;

// Toma una etiqueta Nombre, que es int, un vertice entero v, e inicializa el conjunto_CE (Conjunto de componentes)
void inicial(tipo_nombre, tipo_elemento, conjunto_CE*);
//Hace la union de los conjuntos A y B en el conjunto C
void combina(tipo_nombre, tipo_nombre, conjunto_CE*);

// encuentra devuelve el nombre del componente de C, del cual el vértice v es miembro.
tipo_nombre encuentra(int, conjunto_CE*);

//Aplica el algoritmo de kruskal a una cola de prioridad
// en este caso es un puntero a una rama, que contiene
//una arista, y un puntero a la arista siguiente
void kruskal(Rama*);

//Toma una direccion de memoria de un puntero
//a una rama, y devuelve la arista de costo minimo
Arista* sacar_min(Rama**);

//Toma una Rama y muestra todas sus aristas
void lista(Rama*);

//Toma dos vertices y el costo de su arista para devolver
//un puntero a una rama, compuesta por esa arista
Rama* crear_rama(int u, int v, int costo);

//Encola una arista en la cola de prioridad
void encolar(int u, int v, int costo, Rama** T);

//Ordenamos por prioridad, las de costo minimo primero
void ordenar_prioridad(Rama** T);
//Inserta llama primero a la funcion encolar, y luego ordena la rama por prioridad
void inserta(int, int, int, Rama**);
#endif
