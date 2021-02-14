/*
 * sgrep.c - searches input files (or standard input if no files provided) for
 * lines containing the give string pattern. Then prints the matching lines on
 * standard output
 *
 * Author: Kelly Schombert
 * Usage: ./sgrep.c [OPTION] ... STRING [FILE] ...
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

void main(int argc, char *argv[]) {
	int iflag = 1;	/* if case-sensitive */
	int vflag = 0;	/* if inverting the matches */
	int cflag = 0;	/* if counting the lines */
	int i = 1;

	for(; i < argc; i++) {
		if (argv[i][0] == '-') {
			for (int j = 1; argv[i][j] != '\0'; j++) {
				if (argv[i][j] == 'i')
					iflag = 0;
				else if (argv[i][j] == 'v')
					vflag = 1;
				else if (argv[i][j] == 'c')
					cflag = 1;
				else {
					fprintf(stderr, "%s: unknown option -- %c\n", argv[0], argv[i][j]);
					exit(1);
				}
			}
		}else
			break;
	}

	if (i >= argc){
		fprintf(stderr, "Invoked without the required STRING parameter\n");
		exit(1);
	}
	
	char string[10];
	if (iflag){
		strcpy(string, argv[i]);
	}
	else {
		strcpy(string, argv[i]);
		for (int k = 0; k < 10; k++){
			string[k] = tolower(string[k]);
		}
	
	}
	fprintf(stdout, "%s\n", string);
       	i += 1;

	fprintf(stdout, "%i %i %i\n", iflag, vflag, cflag);
	fprintf(stdout, "%i\n", i);

	char *files[argc];
	int n = i; 
	fprintf(stdout, "%i\n", n);
	for (; i < argc; i++) {
		FILE *fp = fopen(argv[i], "r");
		if (fp == NULL) {
			fprintf(stderr, "%s: no such file or directory %s\n", argv[0], argv[i]);
			exit(1);
		}
		else {
			files[i-n] = argv[i];	
		}
	}
	fprintf(stdout, "%s\n", files);
	fprintf(stdout, "%i\n", i);
	
	exit(0);
}
