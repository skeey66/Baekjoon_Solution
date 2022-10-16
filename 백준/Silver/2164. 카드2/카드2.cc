#include <bits/stdc++.h>
using namespace std;

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);

	queue<int> q;
	int num,tmp,result;
	
	cin >> num;

	for (int i = 1; i <= num; i++) {
		q.push(i);
	}
	while (q.size() != 1) {
		q.pop();
		tmp = q.front();
		q.push(tmp);
		q.pop();

	}
	result = q.front();
	cout << result;

}