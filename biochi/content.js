function isChinese(char) {
  return /[\u4e00-\u9fa5]/.test(char);
}

// ✅ 使用原生的 Intl.Segmenter 替代 fakeSegment
function segmentTextIntl(text) {
  const segmenter = new Intl.Segmenter("zh", { granularity: "word" });
  const segments = segmenter.segment(text);
  return Array.from(segments, s => s.segment);
}

// ✅ 每个词首字加粗
function applyBionic(text) {
  const segments = segmentTextIntl(text);
  return segments
    .map(word => {
      if (word.length >= 2 && isChinese(word[0])) {
        return `<span style="font-weight: 800; font-size: 110%">${word[0]}</span>${word.slice(1)}`;
      } else {
        return word;
      }
    })
    .join("");
}

// ✅ 遍历页面节点并替换文本
function walk(node) {
  if (node.nodeType === Node.TEXT_NODE && node.nodeValue.trim()) {
    const span = document.createElement("span");
    span.innerHTML = applyBionic(node.nodeValue);
    node.replaceWith(span);
  } else if (node.nodeType === Node.ELEMENT_NODE) {
    node.childNodes.forEach(walk);
  }
}

// ✅ 启动处理整个页面
walk(document.body);