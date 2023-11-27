import numpy as np

class DecisionTree():
    def __init__(self, data):
        self.examples = data.copy()
        self.attributes = data.keys().drop(self.examples.keys()[-1])
        self.labels = list(data.iloc[:,-1])
        self.labels_names = set(self.labels)
        self.tree = None

    def total_entropy(self):
        entropy = 0
        for atr in self.labels_names:
            P_atr = list(self.examples.iloc[:,-1]).count(atr) / len(self.examples.iloc[:,-1])
            entropy += -P_atr*np.log2(P_atr)
        return entropy


    def cur_entropy(self, C, atr_C):
        entropy = 0
        for l_name in self.labels_names:
            P_atr = self.P(C,atr_C, l_name)
            if P_atr != 0:
                entropy += -P_atr*np.log2(P_atr)
        return entropy

    def P(self, C,atr_C, l_name):
        atr_C_count = 0
        C_cnames = 0
        for i in range(len(C)):
            if C[i] == atr_C:
                atr_C_count += 1
                if l_name == list(self.examples.iloc[:,-1])[i]:
                    C_cnames += 1
        return C_cnames/atr_C_count

    def E(self, C):
        entropy = 0
        for atr in set(C):
            P_atr = C.count(atr)/len(C)
            if P_atr != 0:
                entropy += P_atr * self.cur_entropy(C, atr)
        return entropy

    def info_gain(self, C):
        s = self.E(C)
        return self.total_entropy() - self.E(C)


    def treelearn(self, examples, attributes, default_class):
        labels = list(examples.iloc[:,-1])
        if len(examples) == 0:
            return default_class
        elif len(set(labels)) == 1:
            return labels[0]
        elif len(attributes) == 0:
            return max(set(labels), key=labels.count)
        else:
            best_gain = self.info_gain(list(examples[attributes[0]]))
            best_attribute = attributes[0]
            for atr in attributes:
                gain = self.info_gain(list(examples[atr]))
                if gain > best_gain:
                    best_gain = gain
                    best_attribute = atr
            tree = {best_attribute: {}}
            for atr_value in set(examples[best_attribute]):
                new_examples = examples[examples[best_attribute] == atr_value].drop(best_attribute, axis=1)
                new_attributes = attributes.drop(best_attribute)
                tree[best_attribute][atr_value] = self.treelearn(new_examples, new_attributes, max(set(labels), key=labels.count))
        self.tree = tree
        return tree

    def predict(self, example, tree=None):
        if not tree:
            tree = self.tree
        if isinstance(tree, str):
            return tree
        else:
            ex_keys = list(example.keys())
            for ex_atr in ex_keys:
                tree_keys = list(tree.keys())
                for tree_atr in tree_keys:
                    if ex_atr == tree_atr:
                        value = example[ex_atr]
                        example.pop(ex_atr)
                        return self.predict(example, tree[tree_atr][value])