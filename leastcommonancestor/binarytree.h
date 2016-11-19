typedef struct Node
{
  int key_value;
  struct Node *left;
  struct Node *right;
}node;

void destroy_tree(node *);
void insert(int, node **);
void print_t(node *);
