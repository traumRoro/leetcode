/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */

struct ListNode* mergeTwoLists(struct ListNode* l1, struct ListNode* l2){
    struct ListNode *root;
    struct ListNode *node;
    
    if (l1 && ( !l2 || l1->val <= l2->val))
    {
        node =  l1;
        l1 = l1->next;
    }
    else if (l2 && ( !l1 || l1->val > l2->val))
    {
        node =  l2;
        l2 = l2->next; 
    }
    root = node;
    while (l1 || l2)
    {
        if (l1 && ( !l2 || l1->val <= l2->val))
        {
            node->next =  l1;
            l1 = l1->next;
        }
        else if (l2 && ( !l1 || l1->val > l2->val))
        {
            node->next =  l2;
            l2 = l2->next;
        }
        node = node->next;
    }
    node = NULL;
    return (root);
}