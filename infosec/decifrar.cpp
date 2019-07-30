#include <iostream>
#include <sstream>
#include <fstream>
#include "stdlib.h"
#include "string.h"

int main(int argc,char * argv[]) {
	
	if(argc != 4) {
		std::cerr << "Wrong amount of arguments" << std::endl;
		exit(-1);
	}	
	
	int sizeOfData = strlen(argv[1]);

	std::ifstream ifs(argv[2]);
	std::string line;
	std::string line2;
	int i = 0;	

	while(getline(ifs,line)){
		line2 = "";
		for(auto it = line.begin(); it < line.end(); it++){

			if(*it == ' '){
				line2 += ' ';
				continue;
			}

			int currentDataValue = argv[1][i] - '0';
			char newCharValue = (*it - currentDataValue);

			if(newCharValue < 97){
				int diff = 97 - newCharValue;
				newCharValue = 123 - diff;
				line2 += newCharValue;
			}

			else {
			line2 += newCharValue;
			}
			
			i++;
			if(i >= sizeOfData) i = 0;
		}
		ofs << line2 << std::endl;
	}

	
	return 0;
}
