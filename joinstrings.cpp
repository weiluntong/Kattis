#include <bits/stdc++.h>

using namespace std;

struct node
{
    int data;
    node *next;
};

class linked_list
{
public:
    node *head,*tail;
    linked_list()
    {
        head = NULL;
        tail = NULL;
    }
};

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    int n;
    cin >> n;
    vector<string> s = {""};
    for (int i = 0; i < n; i++)
    {
        string temp;
        cin >> temp;
        s.push_back(temp);
    }

    if(n == 1) {		
        cout << s[1];		
        return 0;		
    }

    vector<linked_list> graph(n+1);
    for (int i = 1; i < n+1; i++)
    {
        node *temp = new node();
        temp->data = i;
        temp->next = NULL;
        graph[i].head = temp;
        graph[i].tail = temp;
    }

    int i0, i1;
    for (int i = 0; i < n-1; i++)
    {
        cin >> i0 >> i1;
        linked_list *first = &graph[i0];
        linked_list *second = &graph[i1];
        first->tail->next = second->head;
        first->tail = second->tail;
    }

    node *print = graph[i0].head;
    while (print)
    {
        cout << s[print->data];
        print = print->next;
    }
    cout << endl;
    return 0;
}