vector<int> vec;
void preorder(Node* root) {
	if (root) {
		if (root->left)
			preorder(root->left);
		vec.push_back(root->data);
		if (root->right)
			preorder(root->right);
	}
}
bool checkBST(Node* root) {
	preorder(root);
	int i;
	for (i = 1; i < vec.size(); i++)
		if (vec[i - 1] >= vec[i])
			return 0;
	return 1;
}
