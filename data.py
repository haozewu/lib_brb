import math


class Data(object):

    def __init__(self, antecedent_id, antecedent_name,
                 attribute_weight, ref_val, ref_title,
                 consequent_values, crisp_val, parent,
                 is_input, input_val="0"):
        self.name = ""
        self.antecedent_id = antecedent_id
        self.antecedent_name = antecedent_name
        self.attribute_weight = attribute_weight  # 属性权重 a_i
        self.ref_title = ref_title  # 参考级别名称列表
        self.ref_val = ref_val  # 参考级别对应的数值列表
        self.consequent_values = consequent_values
        self.crisp_val = crisp_val
        self.parent = parent
        self.input_val = input_val  # 节点的输入值（叶子来自用户，上层来自子节点聚合）
        self.transformed_val = [0 for _ in range(len(self.ref_val))]  # 输入模糊化后的隶属度/ belief
        self.is_input = is_input  # 是否已有输入（true 表示叶子或已计算好的父节点）
