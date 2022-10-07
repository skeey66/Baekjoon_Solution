#include <bits/stdc++.h>
using namespace std;

const int MX = 1000005;
int dat[MX];
int top_pos = 0, num, num2;
string dic;

void push() {
	cin >> num2;
	dat[top_pos] = num2;
	top_pos++;

}

void pop() {
	if (top_pos == 0) {
		cout << "-1" << endl;
	}
	else {
		cout << dat[top_pos - 1] << endl;
		top_pos--;
	}
	

}
void size() {
	cout << top_pos  << endl;

}
void empty() {
	if (top_pos == 0) {
		cout << "1" << endl;
	}
	else {
		cout << "0" << endl;
	}

}

void top() {
	if (top_pos == 0) {
		cout << "-1" << endl;
	}
	else {
		cout << dat[top_pos - 1] << endl;
	}

}




int main() {

	cin >> num;

	for (int i = 0; i < num; i++) {
		cin >> dic;
		if (dic == "push") {
			push();
		}
		else if (dic == "pop") {
			pop();
		}
		else if (dic == "size") {
			size();
		}
		else if (dic == "empty") {
			empty();
		}
		else if (dic == "top") {
			top();
		}
	}
	

}