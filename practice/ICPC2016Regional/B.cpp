#include <iostream>
#include <unordered_map>
#include <vector>

using namespace std;

struct Node{
    int val;
    Node* next;
    Node* prev; 
};

int main(){
    int n, l, r, x, y, c=0;
    cin >> n >> l >> r;
    Node* head = new Node;
    Node* tail = new Node;
    head->val = 0;
    head->next = tail;
    head->prev = NULL;
    tail->val = -1;
    tail->next = NULL;
    tail->prev = head;
    Node* it = head;
    Node* h = head;
    int LLsize = 1;

    unordered_map<int, vector<Node*>> pos({{0, vector<Node*>{head}}});
    for (int t=0; t<n; t++){
        cin >> x >> y;
        if (pos.find(x) != pos.end()){
            for (auto &i:pos[x]){
                Node* temp = new Node;
                temp->val = y;
                temp->next = i->next;
                temp->prev = i;
                i->next = temp;
                if (i->next == tail){
                    tail->prev = temp;
                }
                
                pos[y].push_back(i->next);
                LLsize++;
                while(LLsize > 4){
                    Node* del = tail->prev;
                    del->prev->next = tail;
                    tail->prev = del->prev;
                    delete del;
                    LLsize--;
                }
            }
        }
    }

    while (it->next != NULL){
        cout << it->val << " ";
        it = it->next;
    }
    // while (c<l){
    //     if (it!=tail){
    //         c++;
    //         it = it->next;
    //     }
    //     else it = h;
    // }

    // while (c<r){
    //     if (it!=tail){
    //         cout << it->val << " ";
    //         c++;
    //         it = it->next;
    //     }
    //     else{
    //         it = h;
    //         // c++;
    //     }
    // }

    return 0;
}
