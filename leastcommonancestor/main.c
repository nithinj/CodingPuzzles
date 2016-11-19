/*	"Given the root of a Binary Tree along with two integer values. Assume that both integers are present in the tree.
 *	Find the LCA (Least Common Ancestor) of the two nodes with values of the given integers.
 *	2 pass solution is easy. You must solve this in a single pass."
 */

#include<stdio.h>
#include<stdlib.h>
#include "binarytree.h"


node *root = 0;
int a,b;

void createtree()
{
  int key;
  while(1)
  {
	printf("Enter Num:");
	scanf("%d", &key);
	if(key==-1)
		break;
	insert(key, &root);
	printf("Tree Looks Like\n");
	print_t(root);
	printf("Enter '-1' to stop instead of number\n");
  }
}

int findcommonancestor(node *root, int *out)
{
  int left=0,right=0;
  if(root != NULL)
  {
	left = findcommonancestor(root->left, out);
	right = findcommonancestor(root->right, out);

	if(left+right == 2)
	{
               *out =  root->key_value;
		return 0;
	}

        if(root->key_value == a || root->key_value == b) 	//We assumes that the value is not repeated.
	{
		if(left+right==1)
		{
		     *out =  root->key_value;
		     return 0;
		}
		return 1;
	}
	return left+right;
  }
}
  
  

main()
{
  createtree();
  char ch='W';
  while(ch == 'W' | ch == 'w')
  {
  printf("Enter two numbers in binary tree\n");
  scanf("%d %d", &a, &b);
  int output=0;
  findcommonancestor(root,  &output);
  if(output==0)
	printf("Could not find common ancestor\n");
  else
	printf("Common Ancestor: %d\n", output);
   printf("W. More  S. Stop\n");
   scanf(" %c", &ch);
  }
  destroy_tree(root);
}
