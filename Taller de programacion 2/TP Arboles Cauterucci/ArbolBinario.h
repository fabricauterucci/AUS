#ifndef __ARBOLBINARIO_H__
#define __ARBOLBINARIO_H__

#define long_max 25;

//Deficion de los tipos de datos
typedef struct nodo{
	char* dato ;
	struct nodo *h_izq, *h_der;
} Nodos;

typedef Nodos* ArbolB;

/* Devuelve 1 si la cola es vacía, 0 en caso contrario */
int arbol_vacio(ArbolB);

/* Ingresa un elemento en el arbol*/
void insertar(ArbolB*, char*);

/* Toma un arbol y borra todos sus nodos*/
void eliminar_arbol(ArbolB );

 /* Lista un arbol en forma pre orden, de izquierda a derecha, mostrando la raiz primero. A diferencia de la teoria, se agrego una cadena donde
  vaya almacenando los nodos, y un puntero a int que aumente en uno la posicion de la cadena
 */
void listar_pre_orden(ArbolB*, char* , int* );


/* Lista un arbol en forma In orden, de izquierda a derecha, mostrando el arbol en orden. A diferencia de la teoria, se agrego una cadena donde
  vaya almacenando los nodos, y un puntero a int que aumente en uno la posicion de la cadena
 */
void listar_in_orden(ArbolB*, char* , int* );

/* Lista un arbol en forma post orden, de izquierda a derecha, mostrando la raiz por ultimo. A diferencia de la teoria, se agrego una cadena donde
  vaya almacenando los nodos, y un puntero a int que aumente en uno la posicion de la cadena
 */
void listar_post_orden(ArbolB*, char* , int* );

/*Elimina un elemento de la lista*/
void suprime(ArbolB*, char*);

/* Toma un elemento y un arbol, y devuelve 1 si el elemento
 * se encuentra en el arbol, 0 en caso contrario*/
int es_miembro(ArbolB, char*);

/* ver que hace*/
char* suprime_minimo(ArbolB*);


//Toma la cadena que contiene los nodos(primer linea de entrada.txt) y devuelve la cantidad de ellos
int contador_de_nodos(char* );

//Toma la cadena que contiene la primer linea del archivo de  entrada
// devuelve una cadena con los nodos
char* cadena_a_nodos(char* );

/*
 Toma la primer cadena del archivo de texto, y llama a cadena_a_nodos para extraer los nodos
 de la primer cadena 
 */
void archivo_a_cadena(char* );

/* Toma la cadena de nodos, a la cual previamente se le aplico el algoritmo de ordenacion,
 *  que componen al arbol, y una opcion para luego escribir un archivo nuevo,
 * con el nombre del orden sea in, pre o post
 */
void cadena_a_archivo(char*, int );

//Toma una cadena y la muestra
void mostrar(char* );

#endif
