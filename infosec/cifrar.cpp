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
			int currentDataValue = argv[1][i] - 96;
			int newCharValue = (line[i] + currentDataValue);
			//std::cout << int(line[i]) << std::endl;
			//std::cout << newCharValue << std::endl;
			if(newCharValue > 122){
				line2 += (97 + ((newCharValue - 97) % 26));
			}
			else {
			line2 += (line[i] + argv[1][i] % sizeOfData);
			}
			i++;
		}
		std::cout << line2 << std::endl;
	}

	
	return 0;
}
