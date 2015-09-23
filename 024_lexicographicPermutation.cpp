//
//  main.cpp
//  euler
//
//  Created by Hieu Do on 9/7/15.
//  Copyright (c) 2015 Hieu Do. All rights reserved.
//
// Refer to this article for some background: http://www.geeksforgeeks.org/lexicographic-permutations-of-string/
// Solution to Euler Problem 24: https://projecteuler.net/problem=24

#include <iostream> // cout cerr
#include <string> //string
#include <vector> //vector
#include <algorithm> //sort
using namespace std;

int findFirstCharIndex(string permutation);
int findCeilingIndex(string permutation, const int& firstCharIndex);
void swap(char* a, char* b);

int main() {
    int counter = 725761; //9! permutations start with 0, 1, 2, etc. => the first permutation starting with 2 is sorted 725,761st (9!x2 + 1)
    string permutation = "013456789"; //permutations starting with 2 will cover from the 725,761st to 1,088,640th permutation
    bool isFinished = false;
    while (!isFinished) {
        int firstCharIndex = findFirstCharIndex(permutation);
        if (firstCharIndex < 0) {
            isFinished = true;
        }
        int ceilingIndex = findCeilingIndex(permutation, firstCharIndex);
        swap(&permutation[firstCharIndex], &permutation[ceilingIndex]);
        sort (permutation.begin() + firstCharIndex + 1, permutation.end());
        counter++;
        if (counter == 1000000) {
            cout << "The 1 millionth lexicographic permutation is: 2" << permutation << endl;
        }
    }
    return 0;
}

// Find the index of the first character
int findFirstCharIndex(string permutation) {
    int i;
    for (i = (int)(permutation.size())-2; i >= 0; i--) {
        if (permutation[i] < permutation[i+1]) {
            return i;
        }
    }
    return i;
}

// Find the index of the ceiling character
int findCeilingIndex(string permutation, const int& firstCharIndex) {
    int ceilingIndex;
    vector<int> temp;
    for (int i = (int)(permutation.size())-1; i > firstCharIndex; i--) {
        if (permutation[firstCharIndex] < permutation[i]) {
            temp.push_back(permutation[i]);
        }
    }
    ceilingIndex = (int)permutation.find(*(min_element(temp.begin(), temp.end())), 0);
    return ceilingIndex;
}

// Swap the first and ceiling character
void swap(char* a, char* b) {
    char t = *a;
    *a = *b;
    *b = t;
}