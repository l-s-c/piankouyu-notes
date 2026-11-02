# 哪些高星人物 Skill 值得这本笔记参考

最接近鱼博直播问答的是花叔的张雪峰 Skill。同样有人带着很具体的难题来问：不光想知道老师考虑什么，还想知道老师会选哪一个。这个项目有一处很好的自检：如果写了好几段，读者还不知道你的判断，就从给判断的那一句重新开始。[回答规则与失败示例](https://github.com/alchaincyf/zhangxuefeng-skill/blob/38bbd944e2ecbd7ec0232a7448fcb27ab4710da0/SKILL.md#L69-L103)

以下星数是 **2026-11-02 查询 GitHub API** 所得，按各自仓库单独计数。链接指向阅读时的文件版本。它们是第三方整理；这里比较的是编辑方法，不用外部角色生成的回答给鱼博的观点作证。

| 参考项目 | Stars | 在文件里实际看到了什么 | 用在鱼博笔记的哪一处 |
| --- | ---: | --- | --- |
| [张雪峰 · alchaincyf](https://github.com/alchaincyf/zhangxuefeng-skill) | 10,686 | [规则](https://github.com/alchaincyf/zhangxuefeng-skill/blob/38bbd944e2ecbd7ec0232a7448fcb27ab4710da0/SKILL.md#L73-L103)要求给明确判断；[模拟问答](https://github.com/alchaincyf/zhangxuefeng-skill/blob/38bbd944e2ecbd7ec0232a7448fcb27ab4710da0/examples/demo-conversation.md#L8-L22)先问考生家里有没有金融行业资源，再根据这个条件给选择。 | [餐桌营养](../knowledge/food.md)先写补蛋白选鸡蛋，再讲买海参的钱花在口味上值不值。只追问会改变答案的事。 |
| [倪海厦 · jangviktor-web](https://github.com/jangviktor-web/nihaixia) | 3,964 | [检索规则](https://github.com/jangviktor-web/nihaixia/blob/5506209ac1ff767c79ddaa816ccb0ef7b8e4ddbb/SKILL.md#L218-L230)把读者的关键词指向具体讲义，查不到就明确写没找到；另设[常见问题速查](https://github.com/jangviktor-web/nihaixia/blob/5506209ac1ff767c79ddaa816ccb0ef7b8e4ddbb/SKILL.md#L446-L453)。 | 在[来源索引](../sources.md)用“鸡蛋”“粑粑”“喝粥”直达切片和时间点。借的是查法，不采用这个项目的诊疗内容。 |
| [毛选方法论 · leezythu](https://github.com/leezythu/maoxuan-skill) | 1,266 | [知识卡实例](https://github.com/leezythu/maoxuan-skill/blob/4376a65020b1fd96af65052ccd30accaddedc3f1/SKILL.md#L39-L62)从一句主张出发，接原著、事例、应用和局限。蒸馏对象是著作中的方法。 | [知识体系](../knowledge/README.md)让一条判断串起几次问答。[控糖和选主食](../knowledge/habits.md)用大碴粥、玉米面糊、土豆泥解释他如何选做法，也留住原料、份量和人群的限制。 |
| [乔布斯 · alchaincyf](https://github.com/alchaincyf/steve-jobs-skill) | 972 | [产品判断规则](https://github.com/alchaincyf/steve-jobs-skill/blob/098f61f49719f0cb2ea6535c0d8eaaa0b22c0180/SKILL.md#L79-L96)要求对实际存在的功能下判断：好就说哪个交互好，建议砍就指出砍哪里。 | [直播问答](../dialogues.md)中写清改哪一样：想少喝甜的，绿豆水里就别放黄冰糖；换糖的颜色并没有减少用量。 |

另外核过一个星数很高的例子：[Karpathy 编程指南](https://github.com/multica-ai/andrej-karpathy-skills/blob/2c606141936f1eeef17fa3043a72095b4765b9c2/skills/karpathy-guidelines/SKILL.md)当时有 228,237 stars。它把 Karpathy 对模型写代码的观察提成几条行为准则，适合学怎么写出可检验的动作；没有把它当成完整的人物或说话风格范本。

## 用四个问题检验“有没有答案”

[女娲 · 37,163 stars](https://github.com/alchaincyf/nuwa-skill)是生成人物 Skill 的工具，这是**母仓库**的星数。它的[验证方法](https://github.com/alchaincyf/nuwa-skill/blob/7c7edfeb9d90a28b1f79e7847e1ba27a698cdc24/SKILL.md#L528-L547)把本人答过的问题、未答过的邻近问题、说话风格分开检查。这一版拿下面四问做了对读：

| 问题 | 读完笔记应该能给的回答 | 对照什么 |
| --- | --- | --- |
| 榴莲是不是水果之王？ | 鱼博自己选苹果。“水果之粑粑”那个包袱后面，他还比了价格、纤维和热量。 | [原片 00:01](https://www.bilibili.com/video/BV1UDKm6NES3/?t=1)。只记住骂法，没说出他选谁，不算答完。 |
| 家里的大碴粥也不能喝？ | 保留颗粒的，他认可。换成磨细的玉米面糊，他更愿意吃整粒玉米。 | [大碴粥](https://www.douyin.com/video/7643014016936464315) · [玉米面 01:08](https://www.bilibili.com/video/BV1q2XjB6EB9/?t=68)。不能套用批评白粥的半句话。 |
| 读博到底上不上课？ | 他自己上过，开头约三个月有课，后来主要做研究。 | [切片后半段](https://www.douyin.com/video/7632984440238993103)。听完追问，不能只留“博士不上课”。 |
| 鱼博会不会推荐我手上这款高蛋白饼干？ | **现有材料没有他对这款饼干的评价。** 如果买它是为了补蛋白，可以拿每份蛋白质量、价格和自己常吃的鸡蛋作比较；这是整理者借用他的思路，不能写成鱼博推荐或反对这款。 | [鸡蛋问答](https://www.douyin.com/video/7624116410029914515)只提供比较的起点；它不能给新商品背书。 |

[回首页](../README.md) · [看实际问答](../dialogues.md) · [看表达风格](../voice.md)
