# AGENTS.md

## 1. 项目概述
AI知识库助手项目旨在自动化采集GitHub Trending和Hacker News的AI/LLM/Agent领域技术动态，通过AI分析生成结构化JSON知识条目，并支持多渠道分发。

## 2. 技术栈
- Python 3.12
- OpenCode + 国产大模型
- LangGraph
- OpenClaw

## 3. 编码规范
- PEP 8
- snake_case命名规范
- Google风格docstring
- 禁止使用裸print()

## 4. 项目结构
```
.opencode/
  agents/
  skills/
knowledge/
  raw/
  articles/
```

## 5. 知识条目JSON格式
```json
{
  "id": "unique_id",
  "title": "标题",
  "source_url": "https://example.com",
  "summary": "摘要内容",
  "tags": ["AI", "LLM"],
  "status": "published"
}
```

## 6. Agent角色概览
| 角色     | 职责               |
|----------|--------------------|
| 采集     | 数据采集           |
| 分析     | 内容分析           |
| 整理     | 结构化存储         |

## 7. 红线
- 禁止未经授权的数据采集
- 禁止泄露用户隐私
- 禁止篡改原始数据
- 禁止使用未授权API