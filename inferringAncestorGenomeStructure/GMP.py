import gurobipy as gp
from gurobipy import *
import pandas as pd
import copy
from dataSturcture.adjacencyMatrix import AdjacencyMatrix


class GMP:
    def __init__(self, adjacency_file,target_copy_number=1):
        self.adjacency_file = adjacency_file
        self.__target_copy_number = target_copy_number
        # 观测的值向量，邻接的对应名字，邻接的分区range信息，邻接的对称信息，对角信息，矩阵的列名信息
        self.__observation_adjacency_vectors_value, \
        self.__adjacency_name, \
        self.__vector_range_value, \
        self.__vector_symmetry_value, \
        self.__diagonal_value, \
        self.__matrix_items,self.__adjacency_no_tel = self.__building_compress_calculation_matrix()
        self.__variable_number = len(self.__observation_adjacency_vectors_value[0])
        self.__dim = len(self.__vector_range_value)

    def __building_compress_calculation_matrix(self):
        adjacency_relations = []  # 保存邻接关系
        matrix_items = []  # 矩阵的列名
        with open(self.adjacency_file) as af:
            while True:
                adjacency = []
                line = af.readline()[:-2]
                if not line:
                    break
                itemset = line.split(' ')
                index = 0
                while index < len(itemset):
                    adjacency.append([itemset[index], itemset[index + 1]])
                    if itemset[index] not in matrix_items:
                        matrix_items.append(itemset[index])
                    if itemset[index + 1] not in matrix_items:
                        matrix_items.append(itemset[index + 1])
                    index += 2
                adjacency_relations.append(adjacency)
        matrix_items = sorted(matrix_items)
        # 先构建大矩阵，
        # 然后生成邻接值向量
        # 表示每个行每个值包括的邻接对的向量，
        # 同时记录对称位置向量，
        # 记录每个项起止位置的向量
        adjacency_matrix = {}  # 创建初始邻接矩阵
        for i in matrix_items:
            adjacency_matrix[i] = {}
            for j in matrix_items:
                adjacency_matrix[i][j] = 0
        observation_adjacency_matrixs = []  # 储存邻接矩阵信息 包括文件内的全部矩阵
        for i in adjacency_relations:
            observation_adjacency_matrix = copy.deepcopy(adjacency_matrix)
            for j in i:
                observation_adjacency_matrix[j[0]][j[1]] += 1
                observation_adjacency_matrix[j[1]][j[0]] += 1
            observation_adjacency_matrixs.append(observation_adjacency_matrix)

        # 每个端点的邻接表格
        adjacency_table = {}  # 保存每个endpoint可能的候选，初始都是0
        for i in matrix_items:
            if i == '$':
                union_items = []
                for j in matrix_items:
                    union_items.append(j)
            else:
                union_items = []
                union_items.append('$')
                for j in observation_adjacency_matrixs:
                    for k in j[i].keys():
                        if j[i][k] != 0:
                            if k not in union_items:
                                union_items.append(k)
            adjacency_table[i] = {}
            for j in union_items:
                adjacency_table[i][j] = 0

        # 分区
        range_vector = {}  # 记录起始终止的位置信息
        adjacency_vector = {}  # 生成邻接表，每个表示一个邻接，按照endpoint排列，由item_vector记录范围信息
        start = 0
        count = 0
        for i in adjacency_table.keys():
            range_vector[i] = []
            range_vector[i].append(start)
            end = start
            for j in adjacency_table[i].keys():
                key = i + '@' + j
                adjacency_vector[key] = count
                end += 1
                count += 1
            range_vector[i].append(end)
            start = end

        # 对称vector，表示对称点的位置
        symmetry_vector = {}
        for i in adjacency_vector.keys():
            key = i.split('@')
            key_sym = key[1] + '@' + key[0]
            symmetry_vector[i] = adjacency_vector[key_sym]

        # 清空adjacency_vector
        empty_adjacency_vector = {}
        for i in adjacency_vector:
            empty_adjacency_vector[i] = 0
        observation_adjacency_vectors = []  # 生成每个的矩阵的列表
        for i in observation_adjacency_matrixs:
            observation_adjacency_vector = copy.deepcopy(empty_adjacency_vector)
            for j in i.keys():
                for k in i[j].keys():
                    if i[j][k] != 0:
                        key = j + '@' + k
                        observation_adjacency_vector[key] += i[j][k]
            observation_adjacency_vectors.append(observation_adjacency_vector)

        # 数值向量化
        adjacency_name = list(observation_adjacency_vectors[0].keys())  # 保存每个元素的意义
        observation_adjacency_vectors_value = []  # 转变为向量形式，不使用字典存储，名字使用adjacency_name保存
        for i in observation_adjacency_vectors:
            observation_adjacency_vector_value = []
            for j in i.keys():
                observation_adjacency_vector_value.append(i[j])
            observation_adjacency_vectors_value.append(observation_adjacency_vector_value)

        vector_range_value = []  # 将字典存储的范围信息转换为列表
        for i in range_vector.keys():
            ranges = range_vector[i]
            vector_range_value.append(ranges)
        vector_symmetry_value = []  # 列表化对称信息
        for i in symmetry_vector.keys():
            vector_symmetry_value.append(symmetry_vector[i])

        diagonal_value = []  # 如果对称位置是自己则是对角为，记录对角位情况
        for i in range(len(vector_symmetry_value)):
            if vector_symmetry_value[i] == i:
                diagonal_value.append(i)

        adjacency_no_tel = []
        for i in range(len(adjacency_name)):
            if '$' not in adjacency_name[i]:
                adjacency_no_tel.append(i)

        return observation_adjacency_vectors_value, \
               adjacency_name, \
               vector_range_value, \
               vector_symmetry_value, \
               diagonal_value, \
               matrix_items,adjacency_no_tel

    def optimization(self):
        try:
            self.__m = gp.Model()
            # 定义布尔变量

            ancestor = self.__m.addVars(self.__variable_number, vtype=GRB.INTEGER,
                                        name="ancestor")


            # z = self.__m.addVars(len(self.__observation_adjacency_vectors_value),
            #                      (self.__variable_number - self.__vector_range_value[0][1]),
            #                      vtype=GRB.INTEGER, name="z")
            #
            # l = self.__m.addVars(len(self.__observation_adjacency_vectors_value),
            #                      (self.__variable_number - self.__vector_range_value[0][1]),
            #                      vtype=GRB.INTEGER, lb=-1000, name="l")

            # Scoj
            # z = self.__m.addVars(len(self.__observation_adjacency_vectors_value),
            #                      len(self.__adjacency_no_tel),
            #                      vtype=GRB.INTEGER, name="z")
            #
            # l = self.__m.addVars(len(self.__observation_adjacency_vectors_value),
            #                      len(self.__adjacency_no_tel),
            #                      vtype=GRB.INTEGER, lb=-1000, name="l")

            # Scoj-cap
            z = self.__m.addVars(len(self.__observation_adjacency_vectors_value),
                                 (self.__variable_number),
                                 vtype=GRB.INTEGER, name="z")

            l = self.__m.addVars(len(self.__observation_adjacency_vectors_value),
                                 (self.__variable_number),
                                 vtype=GRB.INTEGER, lb=-1000, name="l")

            self.__m.update()
            # self.__m.setObjective(gp.quicksum(z[i, j]
            #      for j in range(self.__variable_number - self.__vector_range_value[0][1])
            #      for i in range(len(self.__observation_adjacency_vectors_value))), GRB.MINIMIZE)

            #Scoj
            # self.__m.setObjective(gp.quicksum(z[i, j]
            #                     for j in range(len(self.__adjacency_no_tel))
            #                     for i in range(len(self.__observation_adjacency_vectors_value))),
            #                       GRB.MINIMIZE)

            # Scoj-cap
            self.__m.setObjective(gp.quicksum(z[i, j]
                                for j in range(self.__variable_number)
                                for i in range(len(self.__observation_adjacency_vectors_value))),
                                  GRB.MINIMIZE)



            self.__m.addConstrs((
                (ancestor[i] - self.__target_copy_number) * ancestor[i] <= 0
                for i in range(self.__variable_number)), name='range'
            )
            # for i in range(len(self.__observation_adjacency_vectors_value)):
            #     for j in range(self.__variable_number - self.__vector_range_value[0][1]):
            #         self.__m.addConstr((l[i, j] == (ancestor[j + self.__vector_range_value[0][1]] -
            #                      self.__observation_adjacency_vectors_value[i][j + self.__vector_range_value[0][1]])),
            #                            name='target_pre' + str(i) + str(j))
            #         self.__m.addConstr((z[i, j] == abs_(l[i,j])),
            #                            name='target'+str(i)+str(j))

            # Scoj
            # for i in range(len(self.__observation_adjacency_vectors_value)):
            #     for j in range(len(self.__adjacency_no_tel)):
            #         self.__m.addConstr((l[i, j] == (ancestor[j] - self.__observation_adjacency_vectors_value[i][j])),
            #                            name='target_pre' + str(i) + str(j))
            #         self.__m.addConstr((z[i, j] == abs_(l[i,j])),
            #                            name='target'+str(i)+str(j))

            # Scoj-cap
            for i in range(len(self.__observation_adjacency_vectors_value)):
                for j in range(self.__variable_number):
                    self.__m.addConstr((l[i, j] == (ancestor[j] - self.__observation_adjacency_vectors_value[i][j])),
                                       name='target_pre' + str(i) + str(j))
                    self.__m.addConstr((z[i, j] == abs_(l[i,j])),
                                       name='target'+str(i)+str(j))

            self.__m.addConstrs((ancestor[i] - ancestor[self.__vector_symmetry_value[i]] == 0
                                 for i in range(self.__variable_number)), name='symmetry')
            self.__m.addConstrs((gp.quicksum(ancestor[j + self.__vector_range_value[i + 1][0]]
                                             for j in range(
                self.__vector_range_value[i + 1][1] - self.__vector_range_value[i + 1][0])) == self.__target_copy_number
                                 for i in range(self.__dim - 1)), name='row_unique')
            self.__m.addConstrs((ancestor[i] == 0
                                 for i in self.__diagonal_value), name='Diagonal')
            self.__m.optimize()
            print('Obj: %g' % self.__m.objVal)
        except gp.GurobiError as e:
            print('Error code ' + str(e.errno) + ': ' + str(e))

        except AttributeError:
            print('Encountered an attribute error')

    def ancestor_adjacency_matrix(self):
        result = []
        for v in self.__m.getVars():
            if v.Varname.startswith('ancestor'):
                result.append(v.x)
        self.__adjacency_matrix = {}
        for i in self.__matrix_items:
            self.__adjacency_matrix[i] = {}
            for j in self.__matrix_items:
                self.__adjacency_matrix[i][j] = 0
        for i in range(len(self.__adjacency_name)):
            if result[i] != 0:
                keys = self.__adjacency_name[i].split('@')
                self.__adjacency_matrix[keys[0]][keys[1]] = result[i]
        self.__adjacency_matrix = pd.DataFrame(self.__adjacency_matrix)
        adjacency_matrix = AdjacencyMatrix()
        adjacency_matrix.readFromMatrix(self.__adjacency_matrix)
        return adjacency_matrix


