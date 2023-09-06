#include <stdio.h>
#include <stdlib.h>
#include <malloc.h>

typedef int element;

//구조체 정의
typedef struct ListNode {
    element data;
    struct ListNode* link;
} ListNode;

//앞부분에 노드 삽입
ListNode* insert_first(ListNode* head, int value) {
    ListNode* p = (ListNode*)malloc(sizeof(ListNode));
    p->data = value;
    p->link = head;
    head = p;
    return head;
}

//pre노드 뒤에 노드삽입
ListNode* insert(ListNode* head, ListNode* pre, int value){
    ListNode* p = (ListNode*)malloc(sizeof(ListNode));
    p->data = value;
    p->link = head;
    pre->link = p;
    return head;
}

//앞부분 노드 삭제
ListNode* delete_first(ListNode* head){
    ListNode* removed;
    if(head == NULL) return NULL;
    removed = head;
    head = removed->link;
    free(removed);
    return head;
}

// pre가 가르키는 다음 노드삭제
ListNode* delete(ListNode* head, ListNode* pre){
    ListNode* removed;
    removed = pre->link;
    pre->link = removed->link;
    free(removed);
    return head;
}

//리스트 출력
ListNode* print_list(ListNode* head){
    for(ListNode* p; p != NULL; p = p->link)
        printf("%d->",p->data);
    printf("NULL\n");
}

