#include <iostream>

using namespace std;

int main() {
	int ind = 0;
	int min = -1000000;
	int max = 1000000;

	cin >> ind;
	int arr[1000001];

	for (int i = 0; i < ind; i++) {
		cin >> arr[i];
		if (max < arr[i]) max = arr[i];
		if (min > arr[i]) min = arr[i];
	}
	cout << min << ' ' << max;

	return 0;

}

//배열의 크기가 너무 쓸데없이 커지는거 같아서 다른 사람들은 어떻게 했나
//찾아봤는데 int arr[ind]; 이런식으로 배열 크기를 변수로 선언해서 했다.
//근데 나는 왜 안되는걸까리