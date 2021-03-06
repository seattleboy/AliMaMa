# **赛题内容**

本次比赛以阿里电商广告为研究对象，提供了淘宝平台的海量真实交易数据，参赛选手通过人工智能技术构建预测模型预估用户的购买意向，即给定广告点击相关的用户（user）、广告商品（ad）、检索词（query）、上下文内容（context）、商店（shop）等信息的条件下预测广告产生购买行为的概率（pCVR），形式化定义为：pCVR=P(conversion=1 | query, user, ad, context, shop)。

结合淘宝平台的业务场景和不同的流量特点，我们定义了以下两类挑战：

（1）日常的转化率预估

（2）特殊日期的转化率预估

# **评估指标**

通过logarithmic loss（记为logloss）评估模型效果（越小越好）， 公式如下：

 ![](data:image/*;base64,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)

其中N表示测试集样本数量，yi表示测试集中第i个样本的真实标签，pi表示第i个样本的预估转化率。

# **数据说明**

本次比赛为参赛选手提供了5类数据（基础数据、广告商品信息、用户信息、上下文信息和店铺信息）。基础数据表提供了搜索广告最基本的信息，以及&quot;是否交易&quot;的标记。广告商品信息、用户信息、上下文信息和店铺信息等4类数据，提供了对转化率预估可能有帮助的辅助信息。

用于初赛的数据包含了若干天的样本。最后一天的数据用于结果评测，对选手不公布；其余日期的数据作为训练数据，提供给参赛选手；。

在上述各张数据表中，绝大部分样本包含了完整的字段数据，也有少部分样本缺乏特定字段的数据。如果一条样本的某个字段为&quot;-1&quot;，表示这个样本的对应字段缺乏数据。

**3月1日补充说明：**

**关于样本和字段分隔符的说明：**

每条样本单独占一行，使用&quot;\r&quot;（回车符）进行分割。同一条样本的各个字段，使用空格进行分割。冒号&quot;:&quot;、逗号&quot;,&quot;和分号&quot;;&quot; 都是一个字段内部的分隔符号。各个字段的含义和拼接格式，请参见&quot;数据说明&quot;部分。

使用 Windows 系统的选手请注意，使用Windows记事本打开比赛数据时无法正常显示换行格式，请使用 Notepad++ 或 UltraEdit 等文本编辑器进行浏览。

**基础数据**

| 字段 | 解释 |
| --- | --- |
| instance\_id | 样本编号，Long |
| is\_trade | 是否交易的标记位，Int类型；取值是0或者1，其中1 表示这条样本最终产生交易，0 表示没有交易 |
| item\_id | 广告商品编号，Long类型 |
| user\_id | 用户的编号，Long类型 |
| context\_id | 上下文信息的编号，Long类型 |
| shop\_id | 店铺的编号，Long类型 |

**广告商品信息**

| 字段 | 解释 |
| --- | --- |
| item\_id | 广告商品编号，Long类型 |
| item\_category\_list | 广告商品的的类目列表，String类型；从根类目（最粗略的一级类目）向叶子类目（最精细的类目）依次排列，数据拼接格式为 &quot;category\_0;category\_1;category\_2&quot;，其中 category\_1 是 category\_0 的子类目，category\_2 是 category\_1 的子类目 |
| item\_property\_list | 广告商品的属性列表，String类型；数据拼接格式为 &quot;property\_0;property\_1;property\_2&quot;，各个属性没有从属关系 |
| item\_brand\_id | 广告商品的品牌编号，Long类型 |
| item\_city\_id | 广告商品的城市编号，Long类型 |
| item\_price\_level | 广告商品的价格等级，Int类型；取值从0开始，数值越大表示价格越高 |
| item\_sales\_level | 广告商品的销量等级，Int类型；取值从0开始，数值越大表示销量越大 |
| item\_collected\_level | 广告商品被收藏次数的等级，Int类型；取值从0开始，数值越大表示被收藏次数越大 |
| item\_pv\_level | 广告商品被展示次数的等级，Int类型；取值从0开始，数值越大表示被展示次数越大 |

**用户信息**

| 字段 | 解释 |
| --- | --- |
| user\_id | 用户的编号，Long类型 |
| user\_gender\_id | 用户的预测性别编号，Int类型；0表示女性用户，1表示男性用户，2表示家庭用户 |
| user\_age\_level | 用户的预测年龄等级，Int类型；数值越大表示年龄越大 |
| user\_occupation\_id | 用户的预测职业编号，Int类型 |
| user\_star\_level | 用户的星级编号，Int类型；数值越大表示用户的星级越高 |

**上下文信息**

| 字段 | 解释 |
| --- | --- |
| context\_id | 上下文信息的编号，Long类型 |
| context\_timestamp | 广告商品的展示时间，Long类型；取值是以秒为单位的Unix时间戳，以1天为单位对时间戳进行了偏移 |
| context\_page\_id | 广告商品的展示页面编号，Int类型；取值从1开始，依次增加；在一次搜索的展示结果中第一屏的编号为1，第二屏的编号为2 |
| predict\_category\_property | 根据查询词预测的类目属性列表，String类型；数据拼接格式为 &quot;category\_A:property\_A\_1,property\_A\_2,property\_A\_3;category\_B:-1;category\_C:property\_C\_1,property\_C\_2&quot; ，其中 category\_A、category\_B、category\_C 是预测的三个类目；property\_B 取值为-1，表示预测的第二个类目 category\_B 没有对应的预测属性 |

**店铺信息**

| 字段 | 解释 |
| --- | --- |
| shop\_id | 店铺的编号，Long类型 |
| shop\_review\_num\_level | 店铺的评价数量等级，Int类型；取值从0开始，数值越大表示评价数量越多 |
| shop\_review\_positive\_rate | 店铺的好评率，Double类型；取值在0到1之间，数值越大表示好评率越高 |
| shop\_star\_level | 店铺的星级编号，Int类型；取值从0开始，数值越大表示店铺的星级越高 |
| shop\_score\_service | 店铺的服务态度评分，Double类型；取值在0到1之间，数值越大表示评分越高 |
| shop\_score\_delivery | 店铺的物流服务评分，Double类型；取值在0到1之间，数值越大表示评分越高 |
| shop\_score\_description | 店铺的描述相符评分，Double类型；取值在0到1之间，数值越大表示评分越高 |
