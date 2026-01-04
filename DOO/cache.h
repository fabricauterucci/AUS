//cache.h

#ifndef CACHE_H
#define CACHE_H

#include <iostream>
#include <fstream>
#include <map>
#include <utility>
#include <string>
#include <list>
#include <fstream>
#include <set>
#include <vector>
#include <algorithm>   // Incluir para usar sort

using namespace std;

template<class T>
class CacheManager {
	//members (private)
	private:
	    int usageIndex;
		int capacity;
		map <string, pair<T, int>> cache_data;	// <Clave, <Obj, Indice de Uso>>
		bool write_file(string, T);
	
	public:
		CacheManager(int); //recibe la capacidad en el int
		~CacheManager();

		void insert(string key, T obj);
		T get(string key);
		void clear_cache();

		//agregar funciones
		void show_cache() ;
		void save_cache_to_file(const char* filename) ; // Método para guardar en archivo
		
		void load_cache_from_file(const char* filename); // Carga desde el archivo
		int getCapacity() ;
		set<string> all_keys; //// Mantiene un registro de todas las claves insertadas
		void removeLeastUsed();
		list<string> usage_order; // Mantiene el orden de uso
	};
	
	template <class T>
	CacheManager<T>:: CacheManager(int cap){
		capacity = cap;
		usageIndex = 0;
		load_cache_from_file("cache.txt"); // Carga los datos desde el archivo al inicializar
	}
	
	//template <class T>
	//CacheManager<T>::~CacheManager(){}
	
	
	template <class T>
	CacheManager<T>::~CacheManager() {clear_cache();}

	
	//INSERT
	template <class T>
	void CacheManager<T>:: insert(string key, T obj){
		usageIndex++;
		
		// Si la clave ya existe, actualiza el objeto y el índice de uso
		auto it = cache_data.find(key);
		if (it != cache_data.end()) {
			it->second = make_pair(obj, usageIndex);
			usage_order.remove(key);
			usage_order.push_back(key);
		} else {
			// Si la caché está llena, elimina el menos usado
			if (static_cast<int>(cache_data.size()) >= capacity) {
				//removeLeastUsed();
			}
			cache_data[key] = make_pair(obj, usageIndex);
			usage_order.push_back(key);
			all_keys.insert(key); // Añadir la clave al conjunto de todas las claves
		}
		// Guarda la caché en el archivo
		save_cache_to_file("cache.txt");
	}

	template <class T>
	T CacheManager<T>::get(string key) {
		auto it = cache_data.find(key);
		
		if (it != cache_data.end()) {
		   // Si el elemento está en la caché en memoria, actualiza el índice de uso
			it->second.second = ++usageIndex;
			// Mover la clave al final de la lista de uso
			usage_order.remove(key); 
			usage_order.push_back(key);
			return it->second.first;
		} else {
			// Si el elemento no está en la caché, buscar en el archivo
			ifstream file("cache.txt");
			if (!file.is_open()) {
				throw runtime_error("Failed to open file");
			}

			string file_key;
			int file_index;
			char buffer[256];

			while (file >> file_key >> file_index) {
				file.ignore();
				file.getline(buffer, sizeof(buffer));
				if (file_key == key) {
					 // Si se encuentra en el archivo, crear el objeto y añadir a la caché
					T obj(file_index, file_index, buffer); 
					if (static_cast<int>(cache_data.size()) >= getCapacity()) {
						removeLeastUsed();
					}
					cache_data[key] = make_pair(obj, ++usageIndex);
					usage_order.push_back(key);
					// También podrías actualizar el archivo si lo necesitas
					file.close();
					return obj;
				}
			}
			file.close();
			throw runtime_error("Key not found in cache or file");
		}
	}

	// Elimina el elemento menos usado
	template <class T>
	void CacheManager<T>::removeLeastUsed() {
		if (cache_data.empty()) return; // No hacer nada si la caché está vacía

		// La primera clave en la lista de uso es la menos usada
		string leastUsedKey = usage_order.front();
		cache_data.erase(leastUsedKey);
		usage_order.pop_front();
	}

	// Muestra el contenido de la caché, ordenado por MRU y mostrando sólo los más recientes
	template <class T>
	void CacheManager<T>::show_cache() {
		// Crea una lista de pares para almacenar los elementos y sus índices de uso
		vector<pair<string, pair<T, int>>> cache_list(cache_data.begin(), cache_data.end());

		// Ordena la lista en función del índice de uso en orden descendente
		sort(cache_list.begin(), cache_list.end(), [](const pair<string, pair<T, int>>& a, const pair<string, pair<T, int>>& b) {
			return a.second.second > b.second.second;
		});

		// Muestra los últimos `capacity` elementos con más MRU
		cout << "   <<<<<<<<<<<< Show Cache <<<<<<<<<<<<<<<<< " << endl;
		cout << "   Key \t\t\t Dato \t\t\t\t MRU/LRU" << endl;
		int count = 0;
		for (const auto& entry : cache_list) {
			if (count >= capacity) break; // Muestra sólo hasta `capacity` elementos
			cout << " --------------------------- - --------------------------------- " << endl;
			cout << "   " << entry.first << ", \t\t";
			entry.second.first.print();
			cout << " \t\t\t\t \t\t\t     " << entry.second.second << endl;
			cout << " --------------------------- - ---------------------------------" << endl;
			count++;
		}
		cout << "   <<<<<<<<<<<<< Fin de Show Cache <<<<<<<<< " << endl;
	}

	// Devuelve la capacidad de la caché
	template <class T>
	int CacheManager<T>::getCapacity() {
		return capacity;
	}

	template <typename T>
	void CacheManager<T>::save_cache_to_file(const char* filename) {
	  // Primero leer todo el archivo existente para mantener los elementos antiguos
		map<string, pair<T, int>> all_data;

		ifstream infile(filename);
		if (infile.is_open()) {
			string file_key;
			int file_index;
			char buffer[256];

			while (infile >> file_key >> file_index) {
				infile.ignore();
				infile.getline(buffer, sizeof(buffer));
				T obj(file_index, file_index, buffer);
				all_data[file_key] = make_pair(obj, file_index);
			}
			infile.close();
		}

		// Actualizar all_data con los elementos actuales en cache_data
		for (const auto& entry : cache_data) {
			all_data[entry.first] = entry.second;
		}

		// Escribir todo en el archivo
		ofstream outfile(filename, ios::trunc); // Usa trunc para sobrescribir el archivo
		if (!outfile.is_open()) {
			throw runtime_error("Failed to open file for writing");
		}

		for (const auto& entry : all_data) {
			// Escribir clave, índice de uso y datos del objeto
			outfile << entry.first << ' '  << ' ' << entry.second.first << endl;
		}
		outfile.close();
	}

	// Método para cargar la caché desde un archivo
	template <class T>
	void CacheManager<T>::load_cache_from_file(const char* filename) {
		ifstream file(filename);
		if (!file.is_open()) {
			// Si el archivo no existe, créalo
			ofstream outfile(filename);
			if (!outfile.is_open()) {
				throw runtime_error("Failed to create file");
			}
			outfile.close();
			return; // Salir de la función después de crear el archivo
		}

		string file_key;
		int file_index;
		char buffer[256];

		while (file >> file_key >> file_index) {
			file.ignore();
			file.getline(buffer, sizeof(buffer));

			T obj(file_index, file_index, buffer);
			if (static_cast<int>(cache_data.size()) >= capacity) {
				removeLeastUsed();
			}
			cache_data[file_key] = make_pair(obj, ++usageIndex);
			usage_order.push_back(file_key);
			all_keys.insert(file_key); // Añadir la clave al conjunto de todas las claves
		}
		file.close();
	}

	// Método para escribir un objeto en un archivo
	template <class T>
	bool CacheManager<T>::write_file(string filename, T obj) {
		ofstream file(filename);
		if (!file.is_open()) {
			return false; // No pudo abrir el archivo
		}
		file << obj;
		file.close();
		return true;
	}

	template <class T>
	void CacheManager<T>::clear_cache() {
		cache_data.clear();      // Limpia la caché en memoria
		usage_order.clear();     // Limpia el orden de uso en memoria
	}
	
#endif
