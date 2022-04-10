# 二叉树

class Node(object):
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        return f"Node(data: {self.data}, left: {self.left if self.left is None else self.left.data}, " \
               f"right: {self.right if self.right is None else self.right.data})"

    def __repr__(self):
        return f"Node(data: {self.data}, left: {self.left if self.left is None else self.left.data}, " \
               f"right: {self.right if self.right is None else self.right.data})"


class BinaryTree(object):
    def __init__(self, root):
        self.root = self._build_tree(root)

    def _build_tree(self, root):
        if isinstance(root, Node):
            return root
        elif isinstance(root, list):
            if not root:
                return None
            root_ = Node(root.pop(0))
            stack = [root_]
            while stack:
                node = stack.pop(0)
                if root:
                    left = Node(root.pop(0))
                    stack.append(left)
                    node.left = left
                if root:
                    right = Node(root.pop(0))
                    stack.append(right)
                    node.right = right
            return root_
        else:
            return Node(root)

    def preorder_traversal_recursive(self):
        """
        二叉树的前序遍历（递归版本）
        :return:
        """
        def __preorder_traversal_recursive(node):
            if node is None:
                return
            result.append(node.data)
            __preorder_traversal_recursive(node.left)
            __preorder_traversal_recursive(node.right)

        result = []
        __preorder_traversal_recursive(self.root)
        print(f"前序遍历（递归）：{','.join([str(i) for i in result])}")
        return result

    def preorder_traversal(self):
        """
        二叉树的前序遍历（非递归版本）
        :return:
        """
        stack = []
        result = []
        cur = self.root
        while stack or cur:
            while cur:
                stack.append(cur)
                result.append(cur.data)
                cur = cur.left
            cur = stack.pop()
            cur = cur.right
        print(f"前序遍历：{','.join([str(i) for i in result])}")
        return result

    def preorder_traversal_morris(self):
        """
        二叉树的前序遍历（morris版本）
        :return:
        """
        result = []
        if not self.root:
            return result

        p1 = self.root
        while p1:
            p2 = p1.left
            if p2:
                while p2.right and p2.right != p1:
                    p2 = p2.right
                if not p2.right:
                    result.append(p1.data)
                    p2.right = p1
                    p1 = p1.left
                    continue
                else:
                    p2.right = None
            else:
                result.append(p1.data)
            p1 = p1.right
        print(f"前序遍历（morris版本）：{','.join([str(i) for i in result])}")
        return result


    def inorder_traversal_recursive(self):
        """
        二叉树的中序遍历（递归版本）
        :return:
        """
        def __inorder_traversal_recursive(node):
            if not node:
                return None
            __inorder_traversal_recursive(node.left)
            result.append(node.data)
            __inorder_traversal_recursive(node.right)

        result = []
        __inorder_traversal_recursive(self.root)
        print(f"中序遍历（递归）：{','.join([str(i) for i in result])}")
        return result

    def inorder_traversal(self):
        """
        二叉树的中序遍历（非递归版本）
        :return:
        """
        stack = []
        result = []
        cur = self.root
        while stack or cur:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            result.append(cur.data)
            cur = cur.right
        print(f"中序遍历：{','.join([str(i) for i in result])}")
        return result

    def inorder_traversal_morris(self):
        """
        二叉树的中序遍历（morris版本）
        :return:
        """
        result = []
        if not self.root:
            return result

        node = self.root
        pre = None
        while node:
            if node.left:
                pre = node.left
                while pre.right:
                    pre = pre.right
                pre.right = node
                tmp = node
                node = node.left
                tmp.left = None
            else:
                result.append(node.data)
                node = node.right
        print(f"中序遍历（morris版本）：{','.join([str(i) for i in result])}")
        return result

    def postorder_traversal_recursive(self):
        """
        二叉树的后序遍历（递归版本）
        :return:
        """
        def __postorder_traversal_recursive(node):
            if node is None:
                return
            __postorder_traversal_recursive(node.left)
            __postorder_traversal_recursive(node.right)
            result.append(node.data)

        result = []
        __postorder_traversal_recursive(self.root)
        print(f"后序遍历（递归）：{','.join([str(i) for i in result])}")
        return result

    def postorder_traversal_reverse(self):
        """
        二叉树的后序遍历（reverse版本）
        :return:
        """
        stack = []
        result = []
        cur = self.root
        while stack or cur:
            while cur:
                stack.append(cur)
                result.append(cur.data)
                cur = cur.right
            cur = stack.pop()
            cur = cur.left
        print(f"后序遍历（reverse版本）：{','.join([str(i) for i in result[::-1]])}")
        return result[::-1]

    def postorder_traversal_morris(self):
        """
        二叉树的后序遍历（morris版本）
        :return:
        """
        def addPath(node: Node):
            count = 0
            while node:
                count += 1
                res.append(node.data)
                node = node.right
            i, j = len(res) - count, len(res) - 1
            while i < j:
                res[i], res[j] = res[j], res[i]
                i += 1
                j -= 1

        if not self.root:
            return list()

        res = list()
        p1 = self.root

        while p1:
            p2 = p1.left
            if p2:
                while p2.right and p2.right != p1:
                    p2 = p2.right
                if not p2.right:
                    p2.right = p1
                    p1 = p1.left
                    continue
                else:
                    p2.right = None
                    addPath(p1.left)
            p1 = p1.right

        addPath(self.root)
        print(f"后序遍历（morris版本）：{','.join([str(i) for i in res])}")
        return res

    def postorder_traversal(self):
        """
        二叉树的后序遍历
        :return:
        """
        if not self.root:
            return list()

        res = list()
        stack = list()
        prev = None
        node = self.root

        while node or stack:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            if not node.right or node.right == prev:
                res.append(node.data)
                prev = node
                node = None
            else:
                stack.append(node)
                node = node.right
        print(f"后序遍历：{','.join([str(i) for i in res])}")
        return res

    def level_order_traversal(self):
        """
        层序遍历
        :return:
        """
        stack = [self.root]
        result = []
        while stack:
            node = stack.pop(0)
            result.append(node.data)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        print(f"层序遍历：{','.join([str(i) for i in result])}")
        return result

    def z_level_order_traversal(self):
        """
        Z字型遍历
        :return:
        """
        stack = [self.root]
        result = []
        flag = 1
        while stack:
            n = len(stack)
            temp = []
            for _ in range(n):
                node = stack.pop(0)
                temp.append(node.data)
                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)
            if flag == -1:
                temp = temp[::-1]
            result.append(temp)
            flag *= -1
        result = sum(result, [])
        print(f"Z字型遍历：{','.join([str(i) for i in result])}")
        return result


if __name__ == "__main__":
    l = [0, 1,2,3,4,5,6,7,8,9]
    tree = BinaryTree(l)
    tree.preorder_traversal_recursive()
    tree.preorder_traversal()
    tree.preorder_traversal_morris()
    tree.inorder_traversal_recursive()
    tree.inorder_traversal()
    # tree.inorder_traversal_morris()
    tree.postorder_traversal_recursive()
    tree.postorder_traversal_reverse()
    tree.postorder_traversal_morris()
    tree.postorder_traversal()
    tree.level_order_traversal()
    tree.z_level_order_traversal()
