#include <iostream>
#include <string>
#include <fstream>

int main(int argc, char * argv[]){
	
	std::string alfabeto = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ ?,";
	unsigned char character;	
	int chave = 0;
	std::string outputPath = argv[2];
	std::ifstream input(argv[1]);
	std::ofstream output(outputPath);
	while(chave < alfabeto.size()) {	
		output << "Chave " << chave << std::endl;
		while(input >> character){
			int index = alfabeto.find(character);
			if(index != std::string::npos){
				int newIndex = index - chave;

				if(newIndex < 0) {
					newIndex = alfabeto.size() + newIndex;
				}
				else {
					newIndex = newIndex % alfabeto.size();
				}

				output << alfabeto[newIndex];	
			}
			else {
				output << character;				
			}
		}
		chave++;
		input = std::ifstream(argv[1]);
		output << std::endl << std::endl;
	}

	// dê 
	// compilar com g++ -std=c++11 caesar.cpp -o caesar
	// rodar com ./caesar input.txt out
	// cat out33 no shell e lá estará a mensagem decodificada
}
