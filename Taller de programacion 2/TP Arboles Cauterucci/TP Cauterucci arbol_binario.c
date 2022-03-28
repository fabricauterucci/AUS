/*
Para la realización de este TP puede utilizar la implentación del apunte de árbol binario. Modifíquela para que los datos guardados sean una cadena de strings.
El programa debe poder leer los datos desde un archivo 'entrada.txt'. También debe permitir almacenar cada una de las formas de recorer un árbol en sus respectivos archivos de salida.

Un posible formato de entrada, 'entrada.txt':

N1: "H" | N2: "E" | N3: "O" | N4: "A" | N5: "F" | N6: "G" 
N1:L=N2 | N1:R=N3 | N2:L=N4 | N2:R=N5 | N5:R=N6

Las salidas serian:

inorden.txt
A E F G H O

preorden.txt
H E A F G O

postorden:
A G F E O H
*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "ArbolBinario.h"

int main(){
	
	char* cadena = malloc(sizeof(char)*7);
	int* posicion = malloc(sizeof(int));
	ArbolB raiz;
	raiz = NULL;
	*posicion = 0;
	archivo_a_cadena(cadena);
	char  a_aux[2];
	for(int i = 0 ; cadena[i]; i++){
		a_aux[0] = cadena[i];
		a_aux[1] = '\0';
		insertar(&raiz, a_aux);
	}

	//Opcion 1 hace el que archivo tenga el nombre inorden.txt
	//Opcion 2 hace el que archivo tenga el nombre postorden.txt
	//Opcion 3 hace el que archivo tenga el nombre preorden.txt
	//Con cualquier otra opcion, el archivo imprime el orden de la funcion que se llame pero con otro nombre
	listar_in_orden(&raiz, cadena, posicion);
	cadena_a_archivo(cadena,1);
	
	*posicion = 0;
	listar_post_orden(&raiz, cadena, posicion);
	cadena_a_archivo(cadena,2);
	
	*posicion = 0;
	listar_pre_orden(&raiz, cadena, posicion);
	cadena_a_archivo(cadena,3);
	
	eliminar_arbol(raiz);
	free(posicion);
	free(cadena);
	
	return 0;
}

/* Devuelve 1 si la cola es vacía, 0 en caso contrario */
int arbol_vacio(ArbolB arbol){
	return(arbol == NULL) ;
}

/* Ingresa un elemento en el arbol*/
void insertar(ArbolB* arbol, char* dato){
	if(arbol_vacio(*arbol)){
		*arbol = (ArbolB) malloc(sizeof(Nodos));
		(*arbol)->dato = malloc(sizeof(char)*2); //El char, mas el terminador nulo o \0
		strcpy((*arbol)->dato, dato);
		(*arbol)->h_izq = (*arbol)->h_der = NULL;
	} else {	
		if(dato[0] < (*arbol)->dato[0]){
			insertar(&((*arbol)->h_izq), dato);
		}
		else if(dato[0] > (*arbol)->dato[0]){
			insertar(&((*arbol)->h_der), dato);
		}
	}
}


//Funcion auxiliar para suprimir un nodo y acomoda el arbol para no quedar inconexo
char* suprime_minimo(ArbolB* arbol){
	char* v_ref = malloc(sizeof(char)*2);
	
	if(arbol_vacio((*arbol)->h_izq)){
		strcpy(v_ref, (*arbol)->dato);
		ArbolB tmp = *arbol;
		*arbol = (*arbol)->h_der;
		free(tmp);
		
		return v_ref;
	}
	
	return suprime_minimo(&((*arbol)->h_izq));
}
//Toma un arbol, un dato y elimina el dato del arbol
void suprime(ArbolB* arbol, char* dato){
	if( ! (arbol_vacio(*arbol)) ){
		if(dato[0] < (*arbol)->dato[0])
			suprime(&((*arbol)->h_izq), dato);
		else if ( dato[0] > (*arbol)->dato[0])
			suprime(&((*arbol)->h_der), dato);
		else if( arbol_vacio((*arbol)->h_izq) && arbol_vacio((*arbol)->h_der)){
			ArbolB temp = *arbol;
			*arbol = NULL;
			free(temp);
		} else if (arbol_vacio((*arbol)->h_izq)){
			ArbolB temp = *arbol;
			*arbol = (*arbol)->h_der;
			free(temp);
		} else if (arbol_vacio((*arbol)->h_der)){
			ArbolB temp = *arbol;
			*arbol = (*arbol)->h_izq;
			free(temp);
		} else{
		//Este es el caso en que ambos hijos estan presentes:
			(*arbol)->dato = suprime_minimo(&((*arbol)->h_der));
		}
	}
}

// Toma un arbol y borra todos sus nodos
void eliminar_arbol(ArbolB raiz){
    if(arbol_vacio(raiz)) return;
    eliminar_arbol(raiz->h_izq);
    eliminar_arbol(raiz->h_der);
    free(raiz->dato);
    free(raiz);
}


/* Lista un arbol en forma pre orden, a diferencia de la teoria, se agrego una cadena donde
 * vaya almacenando los nodos, y un puntero a int que aumente en uno la posicion de la cadena
 */
void listar_pre_orden(ArbolB* arbol,char* cadena, int* posicion){
	if( ! arbol_vacio((*arbol)) ){
		printf("%s ", (*arbol)->dato); 
		cadena[(*posicion)] = (*arbol)->dato[0];
		(*posicion)++;
		listar_pre_orden((&(*arbol)->h_izq), cadena, posicion);
		listar_pre_orden(&((*arbol)->h_der), cadena, posicion);
	 }	
}

void listar_post_orden(ArbolB* arbol, char* cadena, int* posicion){
	if( ! arbol_vacio(*arbol) ){
		listar_post_orden((&(*arbol)->h_izq), cadena, posicion);
		listar_post_orden(&((*arbol)->h_der), cadena, posicion);
		printf("%s ", (*arbol)->dato); 
		cadena[(*posicion)] = (*arbol)->dato[0];
		(*posicion)++;
	 }	
}

void listar_in_orden(ArbolB* arbol, char* cadena, int* posicion){
	if( ! arbol_vacio(*arbol) ){
		listar_in_orden((&(*arbol)->h_izq), cadena, posicion);
		printf("%s ", (*arbol)->dato); 
		cadena[(*posicion)] = (*arbol)->dato[0];
		(*posicion)++;
		listar_in_orden(&((*arbol)->h_der), cadena, posicion);
	 }	
}

//Toma la cadena que contiene los nodos y devuelve la cantidad de ellos
int contador_de_nodos(char* cadena){
	int contador_Comillas = 0;
	int contador_Nodos = 0;
	
	for(int i = 0 ; cadena[i]; i++){
		if( cadena[i] == '"') contador_Comillas++;
	}
	contador_Nodos = contador_Comillas/2;
	
	return contador_Nodos;
}


//Toma la cadena que contiene la primer linea del archivo de  entrada
// devuelve una cadena con los nodos
char* cadena_a_nodos(char* cadena){
	int contador_Nodos = 0;
	int i = 0, j = 0;
	int tope_iteracion = 0;      //La distancia entre nodo y nodo son 10 caracteres, a excepcion del primero
								// el -5 es porque el primer nodo aparece en el caracter 5
	
	contador_Nodos = contador_de_nodos(cadena);							
	char* conjunto_Nodos = malloc(sizeof(char)* contador_Nodos+1); //El +1 es por el \0
		
	if( contador_Nodos <= 9) tope_iteracion = (contador_Nodos * 10) - 5;
	else tope_iteracion = ((contador_Nodos - 3) * 10) - 5 + ((contador_Nodos - 9) * 11);
	
	// En el caso del else, son 8 nodos con distancia de 10 caracteres ( del N2 al N9)
	// A partir del N10, la distancia entre caracteres es de 11 numeros
	//PD el programa funcionaria hasta los 99 nodos, en caso de querer mas
	// se deberia tener en cuenta un caracter mas ya que seria del N100 en adelante 
	// que no lo tuve en cuenta ya que no crei que se utilizarian mas de 100 nodos
	
	for( i = 5 ; i <= tope_iteracion ; i += 10){	
		conjunto_Nodos[j] = cadena[i];
		j++;
		if( i >= 85) i++; //cuando pasa de ser N9 a N10 continuamos, pero en el iterador sumamos un caracter
	}
	conjunto_Nodos[j] = '\0';
	
	return conjunto_Nodos;
}

//Se uso para mostrar la cadena de nodos y poder encontrar errores. 
void mostrar(char* cadena){
	for(int i = 0 ; cadena[i]; i++){
		printf("\n %c \n", cadena[i]);
	}	
}

/*
 Toma la primer cadena del archivo de texto, y llama a cadena_a_nodos para extraer los nodos
 de la primer cadena 
 */
void archivo_a_cadena(char* cadena){
	FILE *pArchivo;
	
	char* primer_cadena = malloc(sizeof(char)*200);

	pArchivo = fopen("./entrada.txt", "rt");
	
	//valida que el archivo este creado bien
	if (pArchivo != NULL){
		fscanf(pArchivo, "%[^\n]%*c", primer_cadena);// Guardamos la primer cadena completa
		
		printf("Cadena leida: %s \n" , primer_cadena);
	
		if (!fclose(pArchivo)) printf("El archivo ha sido cerrado.\n");
		else printf("Error al cerrar el archivo. \n");
	 }else {
		printf("Error al cerrar el archivo.\n");
	}
	
	char* cadena_nodos;
	cadena_nodos = cadena_a_nodos(primer_cadena);
	strcpy(cadena, cadena_nodos);
	free(primer_cadena);
	free(cadena_nodos);
}

/* Toma la cadena de nodos, a la cual previamente se le aplico el algoritmo de ordenacion,
 *  que componen al arbol, y una opcion para luego escribir un archivo nuevo,
 * con el nombre del orden sea in, pre o post
 */
void cadena_a_archivo(char* cadena,int opcion){
	FILE *pArchivo;
	char* salida = malloc(sizeof(char)*10); // el maximo de caracteres es el de post_orden que contiene 9 caracteres mas el barra 0
	
	strcpy(salida, "./salida_incorrecta.txt"); //Por defecto el nombre de archivo es salida incorrecta, a excepcion que se indique la opcion del orden
	
	if(opcion == 1) strcpy(salida, "./inorden.txt");
	else if(opcion == 2) strcpy(salida, "./postorden.txt");
	else if(opcion == 3) strcpy(salida, "./preorden.txt");
	else printf("Las opcion ingresada es incorrecta\n");
	
	pArchivo = fopen(salida, "w");
	//valida que el archivo este creado bien
	if (pArchivo != NULL){
		//Escribimos los nodos con un espacio de separacion
		for(int i = 0 ; cadena[i]; i++){
			fprintf(pArchivo,"%c ",cadena[i]);
		}		
		if (!fclose(pArchivo)) printf("El archivo ha sido cerrado.\n");
		else printf("Error al cerrar el archivo. \n");
	} else {
		printf("Error al cerrar el archivo.\n");
	}
	free(salida);	
}	

// Codigo escrito y probado por Fabrizio Alejandro Cauterucci, con ayuda de la teoria de arboles vista en clase
