/* Kelly Schombert
 * Project 3-1
 * CIS 314
 */

#include <stdio.h>
#include <stdlib.h>

struct IntArray {
	/* Defines the structure for all IntArrays called and created*/
	 
	int length;
	int *dataPtr;
};

struct IntArray* mallocIntArray(int length) {
	/* Allocates, initializes and returns a pointer to a new struct IntArray
	 *
	 * int length: length of desired IntArray
	 */

	struct IntArray *arrayPtr = (struct IntArray *)malloc(sizeof(struct IntArray));
	if(arrayPtr != NULL){
		int *array = (int *)malloc(2 * sizeof(int));
		if (array != NULL){
			arrayPtr->length = length;
			arrayPtr->dataPtr = array;
		} else {
			free(arrayPtr);
		}
	}
	return arrayPtr;
}

void freeIntArray(struct IntArray *arrayPtr){
	/*frees the IntArray instance dataPtr and the instance itself*/

	free(arrayPtr->dataPtr);
	free(arrayPtr);
}

void readIntArray(struct IntArray *array){
	/* Prompts and reads positive(>0) integers from the user to fill IntArray instance
	 * If a valid input is not given, user will be prompted until a valid input is given
	 *
	 * struct IntArray *arrayPtr: pointer to the IntArray instance
	 *
	 *
	 * Information on strtol and fgets obtained from lab and tutorialspoint.com
	 */

	int i = 0;
	int len = array->length/4;
	char line[20];
	int count = 0;
	char *endptr = NULL;

	for(; i<len; i++){
		printf("Enter int:");
		fgets(line, 20, stdin);
		count = strtol(line, &endptr, 10);
		while(count <= 0){
			printf("Invalid Input\n");
			printf("Enter int:");
			fgets(line, 20, stdin);
			count = strtol(line, &endptr, 10);
		}

		array->dataPtr[i] = count;	
	}
}

void swap(int *xp, int *yp){
	/* Swaps the int values stored at the xp and yp pointers*/

	long ent1 = *xp;
	long ent2 = *yp;
	*xp = ent2;
	*yp = ent1;
}

void sortIntArray(struct IntArray *array){
	/* Sort the IntArray instance in ascending order using Bubblesort method and the swap function
	 *
	 * struct IntArray *array: pointer to the IntArray instance
	 *
	 * Code for Bubblesort method obtained from geeksforgeeks.org/bubblesort/
	 */
	
	int i, j;
	int len = array->length/4;

	for(i = 0; i < len-1; i++){
		for(j = 0; j < len-i-1; j++){
			if(array->dataPtr[j] > array->dataPtr[j+1]){
				swap(&array->dataPtr[j], &array->dataPtr[j+1]);
			}
		}
	}
}

void printIntArray(struct IntArray *array){
	/* Prints the contents of the IntArray instance's array
	 *
	 * struct IntArray *array: pointer to the IntArray instance
	 */

	int i = 0;
	int len = array->length/4;

	printf("[ ");
	for(; i<len; i++){
		printf("%d, ", array->dataPtr[i]);
	}
	printf("]\n");
}

int main(){
	/* Prompts the user to input a length for an array then calls the functions to fill, sort and print the array
	 * Frees the IntArray instance at the end of the function
	 *
	 * Returns 0
	 */

	char line[20];
	int entry;
	char *endptr = NULL;

	printf("Enter length:");
	fgets(line, 20, stdin);
	entry = strtol(line, &endptr, 10);
	while(entry <= 0){
		printf("Invalid Input\n");
		printf("Enter length:");
		fgets(line, 20, stdin);
		entry = strtol(line, &endptr, 10);
		}

	struct IntArray *array = NULL;
	array = mallocIntArray(sizeof(int)*entry);
	if(array != NULL){	
		readIntArray(array);

		sortIntArray(array);

		printIntArray(array);
		
		freeIntArray(array);
	}

	return 0;
}
