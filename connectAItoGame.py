import os
import pickle
import pandas as pd

from AI.BFS import BFS
from AI.AStar import AStar
from collections import deque
from AI.AStar import PriorityQueue
from AI.DT.DecisionTree import DecisionTree
from AI.NN.network import NeuralNetwork
from static.constants import tree_path, models, bombid_to_img
from AI.GA.genetic import GeneticAlgorithm


class ConnectAItoGame():
    def __init__(self, grid_matrix):
        self.grid_matrix = [[grid_matrix[j][i] for j in range(len(grid_matrix))] for i in range(len(grid_matrix[0]))]

    def save_tree(self, tree):
        with open(f"{tree_path}tree.model", 'wb') as f:
            pickle.dump(tree, f)

    def load_tree(self):
        with open(f"{tree_path}tree.model", 'rb') as f:
            tree = pickle.load(f)
            return tree

    def getBFSPath(self, pos, direction, goal):
        return BFS(self.grid_matrix, goal).graphsearch(deque(), [], pos, direction)

    def getAStarPath(self, pos, direction, goal):
        return AStar(self.grid_matrix, goal).graphsearch(PriorityQueue(), [], pos, direction)

    def getDTDecision(self, to_predict):
        if not os.path.exists(f"{tree_path}tree.model"):
            data = pd.read_csv(f'{tree_path}decision_table.csv')
            labels = list(data.iloc[:, -1])
            attributes = data.keys().drop("action")
            tree = DecisionTree(data)
            tree.treelearn(data, attributes, max(set(labels), key=labels.count))
            self.save_tree(tree)
        else:
            tree = self.load_tree()
        return tree.predict(to_predict)

    def getNNDecision(self, model, bomb_id):
        return model.predict(models + bombid_to_img[bomb_id])

    def goTo(self, sapper, grid, moves, win):
        for move in moves:
            if move == "L":
                if sapper.direction == "L":
                    sapper.move_down(grid, win)
                elif sapper.direction == "R":
                    sapper.move_up(grid, win)
                elif sapper.direction == "U":
                    sapper.move_left(grid, win)
                elif sapper.direction == "D":
                    sapper.move_right(grid, win)
            elif move == "R":
                if sapper.direction == "R":
                    sapper.move_down(grid, win)
                elif sapper.direction == "L":
                    sapper.move_up(grid, win)
                elif sapper.direction == "D":
                    sapper.move_left(grid, win)
                elif sapper.direction == "U":
                    sapper.move_right(grid, win)

            elif move == "M":
                if sapper.direction == "L":
                    sapper.move_left(grid, win)
                elif sapper.direction == "R":
                    sapper.move_right(grid, win)
                elif sapper.direction == "U":
                    sapper.move_up(grid, win)
                elif sapper.direction == "D":
                    sapper.move_down(grid, win)

    def completeGame(self, sapper, grid, win):
        tree =  DecisionTree(pd.read_csv(f'{tree_path}decision_table.csv'))
        tree.treelearn(tree.examples, tree.attributes, max(set(tree.labels), key=tree.labels.count))
        model = NeuralNetwork(model_path="AI/NN/model/Model.h5")
        genetic = GeneticAlgorithm(100, 5000)
        genetic_decision = genetic.run([(0,0)], list(grid.bombs.keys()))
        points = deque()
        for i in range(1, len(genetic_decision)):
            points.append(genetic_decision[i])
        while points:
            next = points.popleft()
            pos = (int(sapper.y_pos / 60), int(sapper.x_pos / 60))
            path = self.getAStarPath(pos, sapper.direction, next)
            self.goTo(sapper, grid, path, win)
            if not points:
                return
            bomb_id = grid.bombs[next].id
            model.predict(models + bombid_to_img[bomb_id])
            bomb_info = grid.bombs[next].get_info()
            decision = tree.predict(bomb_info)
            if decision == "take":
                sapper.take_bomb(grid, win)
            elif decision == "detonete":
                sapper.detonate_bomb(grid, win)





