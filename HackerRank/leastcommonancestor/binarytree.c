#include<stdio.h>
#include<malloc.h>
#include "binarytree.h"



void destroy_tree(node *leaf)
{
  if( leaf != NULL )
  {
      destroy_tree(leaf->left);
      destroy_tree(leaf->right);
      free( leaf );
  }
}

void insert(int key, node **root)
{
    node *leaf = (node*) malloc( sizeof( node ) );
    leaf->key_value = key;
    /* initialize the children to null */
    leaf->left = NULL;    
    leaf->right = NULL;
    if( *root == NULL )
	*root = leaf;
    else
    {
	char opt='A';
	printf("you are at node:%d, press A-left D-right\n", (*root)->key_value);
	scanf(" %c",&opt);
        if(opt == 'A' || opt == 'a')
	{
            if((*root)->left == NULL)
		(*root)->left = leaf; 
            else	
		insert( key, &(*root)->left );
        }
        else
        {
	    if((*root)->right == NULL)
                (*root)->right = leaf;
            else 
                insert( key, &(*root)->right );
        }
    }
}


int _print_t(node *tree, int is_left, int offset, int depth, char s[20][255])
{
    char b[20];
    int width = 5, i;

    if (!tree) return 0;

    sprintf(b, "(%03d)", tree->key_value);

    int left  = _print_t(tree->left,  1, offset,                depth + 1, s);
    int right = _print_t(tree->right, 0, offset + left + width, depth + 1, s);

#ifdef COMPACT
    for (i = 0; i < width; i++)
        s[depth][offset + left + i] = b[i];

    if (depth && is_left) {

        for (i = 0; i < width + right; i++)
            s[depth - 1][offset + left + width/2 + i] = '-';

        s[depth - 1][offset + left + width/2] = '.';

    } else if (depth && !is_left) {

        for (i = 0; i < left + width; i++)
            s[depth - 1][offset - width/2 + i] = '-';

        s[depth - 1][offset + left + width/2] = '.';
    }
#else
    for (i = 0; i < width; i++)
        s[2 * depth][offset + left + i] = b[i];

    if (depth && is_left) {

        for (i = 0; i < width + right; i++)
            s[2 * depth - 1][offset + left + width/2 + i] = '-';

        s[2 * depth - 1][offset + left + width/2] = '+';
        s[2 * depth - 1][offset + left + width + right + width/2] = '+';

    } else if (depth && !is_left) {

        for (i = 0; i < left + width; i++)
            s[2 * depth - 1][offset - width/2 + i] = '-';

        s[2 * depth - 1][offset + left + width/2] = '+';
        s[2 * depth - 1][offset - width/2 - 1] = '+';
    }
#endif

    return left + width + right;
}

void print_t(node *tree)
{
    int i;
    char s[20][255];
    for (i = 0; i < 20; i++)
        sprintf(s[i], "%80s", " ");

    _print_t(tree, 0, 0, 0, s);

    for (i = 0; i < 20; i++)
        printf("%s\n", s[i]);
}
