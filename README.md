# lib_brb

tree_traversal_bottom_up.py为程序入口。

Python 文件

data.py: 节点数据模型，存储节点 id、名称、参考值/标题、权重、父节点、输入值等，并初始化模糊化用的 transformed_val。
rules.py: 单条规则的数据结构，含规则权重、组合、后件 belief、匹配度、激活权重等。
manipulate_data.py: 早期/简化版 BRB 计算，仅处理两个前件节点生成规则库，做输入模糊化、匹配度/激活权重计算、belief 更新与聚合，针对 single_tree.json 的例子。
manipulate_data_new.py: 改进版 BRB 模块，可处理任意数量的子节点组合，自动生成规则库、输入模糊化、激活权重、belief 更新与聚合（证据推理公式），用于多子节点合成父节点。
tree_traversal_bottom_up.py: 运行底向上树遍历，按父子关系分层调用 RuleBase（来自 manipulate_data_new.py）逐层把叶子输入汇总到根，计算各父节点的 belief 和 crisp 值。
learn.py: 小实验脚本，演示笛卡尔积组合/循环输出，和主逻辑无关。


JSON 文件

single_tree.json: 简单示例树的数据（节点参考值、权重、父子关系、是否输入），供演示/测试。
2nd_order_tree.json: 二层/次级树结构示例数据。
agriculture_tree.json: 农业场景的较大树示例数据。
data.json: 另一份节点数据示例，结构类似前面。
temp_data.json: 包含多节点的示例输入，很多叶子节点已有输入值，用于运行底向上聚合。
test_tree_traversal.json: 用于测试遍历/聚合流程的树数据。