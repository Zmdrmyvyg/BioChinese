import jieba

def bionic_reading(text):
    words = jieba.lcut(text)
    result = []

    for word in words:
        length = len(word)
        if length == 1:
            result.append(word)
        elif length in [2, 3]:
            # 把第一个字包在 .bionic 里，其余不变
            result.append(f"<span class='bionic'>{word[0]}</span>{word[1:]}")
        else:  # jieba对"人工智能"这样的词不会再细分了，我们希望能进一步划分出子结构"人工"和"智能"
            subwords = list(jieba.cut(word))
            formatted = ""
            for sub in subwords:
                if len(sub) == 1:
                    formatted += sub
                else:
                    formatted += f"<span class='bionic'>{sub[0]}</span>{sub[1:]}"
            result.append(formatted)


    return ''.join(result)

# 示例文本
text = "我最近在学习人工智能和自然语言处理，觉得非常有趣。"
html_result = bionic_reading(text)

# 输出完整 HTML 文件，带样式
html_template = f"""<html>
<head>
  <meta charset="utf-8">
  <style>
    .bionic {{
      font-weight: bold;
      color: #000;
      background-color: rgba(0, 0, 0, 0);
      padding: 0 0px;
      border-radius: 0px;
    }}
  </style>
</head>
<body>
  <p>{html_result}</p>
</body>
</html>
"""

# 写入文件
with open("output.html", "w", encoding="utf-8") as f:
    f.write(html_template)

print("✅ 已生成 output.html，请用浏览器打开查看效果")