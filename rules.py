class Rules(object):
    def __init__(self):
        self.rule_weight = 1  # 规则权重 w_r
        self.parent = ""  # 父节点 id
        self.combinations = []  # 前件参考值的组合索引
        self.consequence_val = []  # 后件 belief 向量或字典
        self.matching_degree = None  # 匹配度 u_r
        self.activation_weight = None  # 激活权重 a_r

