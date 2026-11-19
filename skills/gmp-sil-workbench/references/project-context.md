# 接入使用者的工程

## 用项目事实填充路径和规则

本 skill 不绑定作者的本机目录、研究工程、固件或实验。接入前读取当前工程的 AGENTS.md、README、构建文件和相关已有记录，先识别下面的对象；已有说明足够时不另建配置文件。缺少影响执行的关键信息才询问用户，其余可以从工程继续核实。

| 对象 | 需要确认的内容 |
|---|---|
| GMP 依赖 | 根目录、版本、相关本地修改、许可证、只读边界、实际 include 路径 |
| 活动工程 | suite 路径、当前分支、已有未提交修改、原有结构与日常入口 |
| 参考工程 | 若是迁移：已验证原工程及版本、需要保留的行为和原判据 |
| 公共与平台源码 | 公共控制/组件/参数；各板包、xplt/CSP、主入口与 ISR |
| 参数来源 | 参数头/配置表/生成器谁是权威源；编译覆盖、运行量和模型快照 |
| 构建 | 主机与目标编译器、项目/配置、实际输出、预构建事件、链接脚本 |
| SIL | 活动 SLX、依赖库与 MEX、控制 EXE、工作目录、网络配置的生成方式 |
| 测量与时间 | 单位、标幺基值、控制/采样/PWM周期和分频、记录时刻与频率 |
| 记录 | 现有报告、参数编号、图目、原始数据、证据与缓存的职责 |
| 操作授权 | 当前任务范围，是否包含硬件下载/运行、外部发布和 Git 推送 |

没有板级目标的任务不需要强行填目标编译器；纯说明任务不需要准备运行环境。已有用户指令优先，不通过此表附加重复审批。

## 维护最小项目映射

若项目确实缺少可持续的接续信息，可把以下内容加入已有工程说明；不要求固定文件名或新增一份平行索引。

```text
GMP dependency: the selected external source and version
Active suite: the user's existing project
Reference baseline: only when migration requires one
Shared source / board / xplt: actual directories and build references
Preset authority: source, selection, overrides, and generated outputs
Host build / target build: exact project and configuration
SIL model / controller / working directory: explicitly paired artifacts
Existing records / raw data / cache: distinct ownership and retention
Current task: required change, unchanged baseline, relevant validation
```

此映射属于使用者本地工程，不自动提交到 skill 开源仓库。公开仓库仅保留通用说明和虚构结构示例。

## 核对工具能力后再调用

先查看当前 CLI 或脚本的帮助与实现，明确读写路径、生成覆盖、模型选择、EXE 选择和进程管理。名字叫 `run-sil` 不代表它绑定了本次构建；名为 `review` 的字段也未必实现审批机制。工具不合适时沿用项目已有入口，不为适应工具复制工程或改变参数体系。

新建任务命令只用于确实的新工程。对已有工程不默认使用覆盖选项；生成器运行前确认是否会擦除人工适配。明确创建的进程、端口和输出目录，避免误操作使用者正在运行的工具或硬件。

参数直接维护在 C preset 的工程，不恢复旧 JSON 生成流程；使用配置生成器的工程，也不擅自改成手工维护。关键是一个权威源、可核验的生成关系和完整消费者，而非统一成某种个人习惯。

## 记录和版本遵循使用者约定

同一目标跨会话继续原记录；独立目标、对象或冻结版本可以分支并接回原入口。参数编号与组名沿用现有体系，说明设计量、实现增益、单位和周期。若组名改动影响图例、记录或生成器，一并修正引用并保留原始证据。

改生成内容时同步真实生成器；移动文件时修复依赖、工作目录和链接。保护人工模型修改和原始数据，区分可重建缓存与尚未备份数据。只忽略具体可再生成的路径，忽略规则不能替代备份。

Git 只处理本次明确范围，不覆盖无关修改、不强推、不改写历史。是否提交或推送由用户和项目要求决定。本 skill 的开源仓库与使用者工程仓库相互独立，不自动把项目源码、实验数据或本地配置复制回公开仓库。
