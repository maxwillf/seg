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
	std::cout << sizeOfData << std::endl;

	std::ifstream ifs(argv[2]);
	std::string line;
	std::string line2;
	std::stringstream ss;
	int i = 0;	
	while(getline(ifs,line)){
		//ss = std::stringstream(line);
		line2 = "";
		for(auto it = line.begin(); it < line.end(); it++){
			int currentDataValue = argv[1][i] - '0';
			int newCharValue = (*it + currentDataValue);
			/*if(*it == 'n'){
				std::cout << currentDataValue << std::endl;
				std::cout << *it << std::endl;
				std::cout << newCharValue << std::endl;
			}*/
			//std::cout << int(line[i]) << std::endl;
			//std::cout << newCharValue << std::endl;
			if(newCharValue > 122){
				std::cout << currentDataValue << std::endl;
				std::cout << *it << std::endl;
				std::cout << newCharValue << std::endl;
				line2 += (newCharValue - 97) % 26;
			}
			else {
			line2 += newCharValue;
			}

			i++;
			if(i > sizeOfData) i = 0;
		}
		std::cout << line2 << std::endl;
	}

	
	return 0;
}
