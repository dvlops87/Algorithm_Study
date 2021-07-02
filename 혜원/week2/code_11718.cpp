#include <iostream>
#include <string>

int main() {
	std::string str;
	while (1) {
		getline(std::cin, str);
		if (str=="") {
			break;
		}
		std::cout << str << std::endl;
	}
	return 0;
}

//getline 사용법 다시 보고
//이 문제는 왜 정답인지 모르겠다. 각 줄 공백 시작과 공백 끝 않는 조건 돌려보면
//안맞는데 왜 백준은 답인지 모르겠다.