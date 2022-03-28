/*
 */
#include "kruskal.h"
#include <stdlib.h>

int main (){
	int M_Costos[VERTICES][VERTICES];
	Rama* arbol ;
	for ( int i = 0; i <= VERTICES -1; i ++){
		for ( int j = i +1; j <= VERTICES -1; j ++){
			printf("Ingrese el costo de lado entre vertices %d y %d: ", i, j);
			scanf("%d", &M_Costos[i][j]);
			}
	}
	
	for(int i = 0; i <= VERTICES-1; i++){ //La mitad inferior de diagonal de matriz
		for(int j = i+1; j <= VERTICES-1; j++){
			if(M_Costos[i][j] != 0)  inserta(i,j,M_Costos[i][j], &arbol); //Inserto en cola de prioridad
		}
	}
	
	
	
	kruskal(arbol);
	
	return 0;
}

// Toma una etiqueta Nombre, que es int, un vertice entero v, e inicializa el conjunto_CE (Conjunto de componentes)
void inicial(tipo_nombre A, tipo_elemento x, conjunto_CE* C){
	C->nombres[x].nombre_conjunto = A;
	C->nombres[x].siguiente_elemento = 0; //Puntero nulo al siguiente elemento
	C->encabezamientos_conjunto[A].cuenta = 1;
	C->encabezamientos_conjunto[A].primer_elemento = x;
}

//Suponiendo que los conjuntos A y B son conjuntos disjuntos
//Hace la union de los conjuntos A y B en el conjunto C
void combina(tipo_nombre A, tipo_nombre B, conjunto_CE* C){
	int i;
	if (C->encabezamientos_conjunto[A].cuenta > C->encabezamientos_conjunto[B].cuenta){
		// A es el conjunto mas grande, combina B dentro de A
		// encuentra el final de B, cambiando los nombres de los connjuntos por
		// A conforme se avanza
		i = C->encabezamientos_conjunto[B].primer_elemento;
		while(C->nombres[i].siguiente_elemento != 0){
			C->nombres[i].nombre_conjunto = A;
			i = C->nombres[i].siguiente_elemento;
		} //Agrega a la lista A al final de la B y llama A al resultado
		// Ahora i es el indice del ultimo elemento de B
		C->nombres[i].nombre_conjunto = A;
		C->nombres[i].siguiente_elemento = C->encabezamientos_conjunto[A].primer_elemento;
		C->encabezamientos_conjunto[A].primer_elemento = C->encabezamientos_conjunto[B].primer_elemento;
		C->encabezamientos_conjunto[A].cuenta = C->encabezamientos_conjunto[A].cuenta + C->encabezamientos_conjunto[B].cuenta;
	}else {// B es al menos tan grande como A
		i = C->encabezamientos_conjunto[A].primer_elemento; //Analogo al if anterior, reemplazando A por B
		while(C->nombres[i].siguiente_elemento != 0){
			C->nombres[i].nombre_conjunto = B;
			i = C->nombres[i].siguiente_elemento;
		} //Agrega a la lista A al final de la B y llama A al resultado
		// Ahora i es el indice del ultimo elemento de B
		C->nombres[i].nombre_conjunto = B;
		C->nombres[i].siguiente_elemento = C->encabezamientos_conjunto[B].primer_elemento;
		C->encabezamientos_conjunto[B].primer_elemento = C->encabezamientos_conjunto[A].primer_elemento;
		C->encabezamientos_conjunto[B].cuenta = C->encabezamientos_conjunto[B].cuenta + C->encabezamientos_conjunto[A].cuenta;
	}
}

tipo_nombre encuentra(int x, conjunto_CE* C){
	//Devuelve el nombre de aquel conjunto que tiene al vertice x como miembro
	return C->nombres[x].nombre_conjunto;
}

//Toma dos vertices y el costo de su arista para devolver
//un puntero a una rama, compuesta por esa arista
Rama* crear_rama(int u, int v, int costo){
	Rama* nuevaRama = malloc(sizeof(Rama));
	nuevaRama->a.u = u;
	nuevaRama->a.v = v;
	nuevaRama->a.costo = costo;
	return nuevaRama;
}

//Encola una arista en la cola de prioridad
void encolar(int u, int v, int costo, Rama** T){
	Rama* aux = crear_rama(u,v,costo);
	aux->sig = NULL;
	
	if((*T) == NULL) *T = aux; //Encola el primer elemento
	else{
		Rama* temp = (*T);
		while(temp->sig != NULL) temp = temp->sig; //sale cuando el siguiente es null
		temp->sig = aux;
	}
}

//Toma una Rama y muestra todas sus aristas
void lista(Rama* T){
	while( T != NULL){
		puts("--------------------------");
		printf("Arista de costo: %d\n Vertice u: %d\n Vertice v: %d ", T->a.costo, T->a.u, T->a.v );
		puts("--------------------------");	
		T = T->sig;
	}
}

//Ordenamos por prioridad, las de costo minimo primero
void ordenar_prioridad(Rama** T){
	Rama* aux1,* aux2;
	//int costo_aux;
	Arista* arista_aux = malloc(sizeof(Arista));
	
	aux1 = (*T);
	while( aux1->sig != NULL){
		aux2 = aux1->sig;
		while(aux2 != NULL){
			if(aux1->a.costo > aux2->a.costo){
			arista_aux->costo = aux1->a.costo;
			arista_aux->u = aux1->a.u;
			arista_aux->v = aux1->a.v;
			aux1->a.costo = aux2->a.costo;
			aux1->a.u = aux2->a.u;
			aux1->a.v = aux2->a.v;
			aux2->a.costo = arista_aux->costo;
			aux2->a.u = arista_aux->u;
			aux2->a.v = arista_aux->v;
			}
			aux2 = aux2->sig;
		}
	aux1 = aux1->sig;
	}
	free(arista_aux);
}

//Inserta llama primero a la funcion encolar, y luego ordena la rama por prioridad
void inserta(int u, int v, int costo, Rama** T){
	//Encola una arista en la cola de prioridad
	encolar(u, v, costo, T); //encola solo el ultimo elemento
	//Ordenamos por prioridad
	
	ordenar_prioridad(T); 
}

//Toma una direccion de memoria de un puntero
//a una rama, y devuelve la arista de costo minimo
Arista* sacar_min(Rama** T){
	return &((*T)->a);
}

//Aplica el algoritmo de kruskal a una cola de prioridad
// en este caso es un puntero a una rama, que contiene
//una arista, y un puntero a la arista siguiente

void kruskal(Rama* Top){
	int comp_n = VERTICES;
	Rama* aux = Top;
	Rama* T = NULL;
	conjunto_CE* componentes = (conjunto_CE*) malloc(sizeof(conjunto_CE));
	Arista*  a;
	tipo_nombre comp_siguiente = 0, comp_u, comp_v ;
	
	for(int i = 0; i <= VERTICES -1; i++){
		comp_siguiente++;
		inicial(comp_siguiente, i, componentes);
	}
	
	while(comp_n > 1){
		a = sacar_min(&aux);
		aux = aux->sig;
		comp_u = encuentra(a->u, componentes);
		comp_v = encuentra(a->v, componentes);
		if( comp_u != comp_v){
			combina(comp_v, comp_u, componentes);
			comp_n = comp_n-1;
			inserta(a->v, a->u, a->costo, &T);
			}
	}
	lista(T);
}


// Codigo escrito y probado por Fabrizio Alejandro Cauterucci
