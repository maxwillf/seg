#include <iostream>
#include <string>
#include <fstream>

int main(int argc, char * argv[]){
	
	std::string alfabeto = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ ?,";
	unsigned char character;	
	unsigned int chave = 1;
	std::string outputPath = argv[2];
	std::string originalOutPath = outputPath;
	outputPath += '1';
	std::ifstream input(argv[1]);
	std::ofstream output(outputPath);
	
	while(chave < alfabeto.size()) {	
		while(input >> character){
			int index = alfabeto.find(character);
			if(index != std::string::npos){
				int newIndex = (index + chave) % alfabeto.size();
				output << alfabeto[newIndex];				
			}
			else {
				output << character;				
			}
		}
		chave++;
		input = std::ifstream(argv[1]);
		outputPath = (originalOutPath + std::to_string(chave));
		output = std::ofstream(outputPath);
	}

	// dê 
	// compilar com g++ -std=c++11 caesar.cpp -o caesar
	// rodar com ./caesar input.txt out
	// cat out22 no shell e lá estará a mensagem decodificada
}
