# GMP SIL Workbench Skill

An independent agent skill for integrating existing projects with GMP, preserving architecture, and validating shared control code through SIL.

面向使用 GMP 的开发者：帮助 AI 理解已有工程，复用 GMP 的组件、调度和平台接口，实施局部修改，并用与改动范围相匹配的证据验证结果。适用于新建工程、融合已有工程、独立模块修改和 SIL 诊断。

本仓库是使用方法与 skill，不包含 GMP 上游源码、私有工程、固件或实验数据。GMP 上游见 [javnson/gmp_pro](https://github.com/javnson/gmp_pro)。本项目独立维护，非 GMP 官方发布。

## 核心原则

- 先复用合适的 suite 和组件，再在原工程边界内适配；已有工程不重复生成。
- 公共控制、用户逻辑、组件、board 和 xplt 各有明确职责，硬件与 SIL 引用同一公共源码。
- 接口核对包含单位、基值、方向、状态、限幅、时序和输出门控。
- 参数只有一个权威源；核对编译后的选择、模型实际消费者和运行产物。
- 构建、同输入回放、实际 C 闭环、UDP SIL、GUI 与实板分别提供证据。
- 测试规模随改动决定；保留原始数据、失败判据与用户已有修改。

## 安装与使用

克隆此独立仓库：

```text
git clone https://github.com/minnyee/gmp-sil-workbench-skill.git
```

将 `skills/gmp-sil-workbench` 整个目录复制到所用 agent 的技能目录。Codex 的个人技能目录通常是 `~/.codex/skills`；已存在同名 skill 时先比较并备份，不覆盖未确认的本地修改。也可以让支持读取本地指令的工具直接读取 [SKILL.md](skills/gmp-sil-workbench/SKILL.md)。

调用示例：

```text
使用 $gmp-sil-workbench 分析这个现有 GMP 工程的 src、board、xplt
及 preset 归属，并核对两个平台是否引用同一公共源码。
```

首次接入先提供或让 agent 从工程中找到：GMP 依赖、活动 suite、目标平台、参数入口、构建配置、SIL 模型与控制程序。按[项目上下文](skills/gmp-sil-workbench/references/project-context.md)确认实际路径，不需要使用作者的机器或目录。

## 内容组织

| 内容 | 入口 |
|---|---|
| 任务分流与必要约束 | [SKILL.md](skills/gmp-sil-workbench/SKILL.md) |
| GMP 优势与架构取舍 | [principles.md](skills/gmp-sil-workbench/references/principles.md) |
| 融合已有工程与接口核对 | [integration.md](skills/gmp-sil-workbench/references/integration.md) |
| 独立模块及生命周期 | [modules.md](skills/gmp-sil-workbench/references/modules.md) |
| SIL 与证据分层 | [validation.md](skills/gmp-sil-workbench/references/validation.md) |
| 使用者工程映射 | [project-context.md](skills/gmp-sil-workbench/references/project-context.md) |
| 板级、底层、结构与 preset 示例 | [preset-example.md](skills/gmp-sil-workbench/references/preset-example.md)、[示例文件](examples/preset-layout) |
| 对外公开范围 | [publication.md](skills/gmp-sil-workbench/references/publication.md) |

skill 本体可独立安装。仓库级示例与检查工具便于开发者阅读和维护，不是使用 skill 的运行依赖。

## 示例与检查范围

公开示例只展示板级配置、底层职责、工程结构及 preset 分配/选择。名称和数值是虚构说明值，不包含个人研究算法、参数组、测试工况或结果，也不构成完整电机工程。

检查仓库内链接、可移植性和 skill 元数据：

```text
python tools/check_repository.py
python -m unittest discover -s tests
```

使用支持 C11 的编译器检查示例配置：

```text
gcc -std=c11 -Wall -Wextra -Werror -pedantic -fsyntax-only examples/preset-layout/check_presets.c
```

这些检查不执行控制算法、SIL 或硬件操作。使用者的工程验收必须在其实际版本、配置和平台中另行完成。

## 贡献与许可

贡献范围和验证要求见 [CONTRIBUTING.md](CONTRIBUTING.md)。本仓库原创文档、skill 和示例采用 [MIT License](LICENSE)；GMP 及其他依赖遵守各自许可证。
