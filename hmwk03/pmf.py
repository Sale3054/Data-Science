node * Delete(node * head, int value)
{
    node* currentNode = head;
    if(head->key == value)
    {
        node * temp = head;
        head = head->next; 
        head-> prev = NULL;
        delete temp;
    }
    while(currentNode->next != NULL)
    {
        if(currentNode->key == value)
        {
            currentNode->prev->next = currentNode->next;    
            delete currentNode;
        }
        currentNode = currentNode->next;
    }
    if(currentNode->next == NULL && currentNode->key == value)
    {
        currentNode->prev->next = NULL;
        delete currentNode;
    }
    return head;
    
}