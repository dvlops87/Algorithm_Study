#include <iostream>
#include <stack>
#include <string>

using namespace std;

int check(string str) {
	stack <int> s;
	int len = str.length();
	int temp = 0;
	int ans = 0;

	for (int i = 0; i < len; i++) {
		
		if (str[i] == '(') s.push(-1);
		else if (str[i] == '[') s.push(-3);
		
		else if (s.empty())  
			return 0;
		else {
			if (s.top() == -1 && str[i] == ')') {
				s.pop();
				s.push(2);
			}
			else if (s.top() == -3 && str[i] == ']') {
				s.pop();
				s.push(3);
			}
			
			else {
				temp = 0;
				while (s.top() != -1 && s.top() != -3) {
					temp += s.top();
					s.pop();

					if (s.empty()) 
						return 0;
				}
				if (s.top() == -1 && str[i] == ')') {
					temp *= 2;
					s.pop();
				}
				else if (s.top() == -3 && str[i] == ']') {
					temp *= 3;
					s.pop();
				}
				else
					return 0;   

				s.push(temp);
			}
		}
	}

	while (!s.empty()) {
		if (s.top() == -1 || s.top() == -3)
			return 0;

		ans += s.top();
		s.pop();
	}
	return ans;
}

int main() {
	string bracket;

	cin >> bracket;
	cout << check(bracket);
}