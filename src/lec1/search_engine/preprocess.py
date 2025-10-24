#!/usr/bin/env python3
"""
Simple query preprocessor for demo: tokenization + stopword removal.

Usage:
  python preprocess.py "今天我们学习Search Engine的基本原理！"
  python preprocess.py -l en "How to read files in Python?"
"""
from __future__ import annotations

import argparse
import json
import re
import string
import jieba
from typing import Iterable, List, Set

# Basic stopword lists
EN_STOP: Set[str] = {
    "a",
    "an",
    "the",
    "is",
    "are",
    "am",
    "and",
    "or",
    "but",
    "to",
    "of",
    "in",
    "on",
    "for",
    "with",
    "as",
    "by",
    "at",
    "from",
    "that",
    "this",
    "it",
    "be",
    "was",
    "were",
    "has",
    "have",
    "had",
    "not",
    "do",
    "does",
    "did",
    "you",
    "we",
    "they",
    "he",
    "she",
    "them",
    "him",
    "her",
    "our",
    "your",
    "their",
    "i",
    "me",
    "my",
    "mine",
    "yours",
    "ours",
    "theirs",
    "been",
    "so",
    "if",
    "then",
    "than",
}

ZH_STOP: Set[str] = {
    "的",
    "了",
    "在",
    "是",
    "和",
    "与",
    "及",
    "或",
    "而",
    "被",
    "也",
    "就",
    "都",
    "很",
    "还",
    "又",
    "比",
    "等",
    "这个",
    "那个",
    "我们",
    "你",
    "我",
    "他",
    "她",
    "它",
    "一个",
    "上",
    "下",
    "中",
    "对",
    "从",
    "到",
    "并",
    "把",
    "被",
    "及其",
    "以及",
    "其",
}

ZH_PUNCT = set(
    "，。；：、！？（）“”‘’《》【】—…·〈〉『』「」﹏﹑﹔﹕．｡＂＇｀＇，．／；：［］｛｝（）＜＞！？"
)
ALL_PUNCT = set(string.punctuation) | ZH_PUNCT


def _has_cjk(text: str) -> bool:
    return bool(
        re.search(r"[\u3040-\u30ff\u3400-\u4dbf\u4e00-\u9fff\uf900-\ufaff]", text)
    )


def _tokenize_en(text: str) -> List[str]:
    text = text.lower()
    # keep alphanumerics and simple contractions
    return re.findall(r"[a-z0-9]+(?:'[a-z0-9]+)?", text)


def _tokenize_zh(text: str) -> List[str]:
    tokens = jieba.lcut(text, cut_all=False)
    out: List[str] = []
    for t in tokens:
        if not t.strip():
            continue
        if t in ALL_PUNCT:
            continue
        # normalize ASCII words to lowercase (handles mixed queries)
        if re.fullmatch(r"[A-Za-z0-9]+", t):
            t = t.lower()
        out.append(t)
    return out


def preprocess_query(
    query: str, stop_words: Iterable[str] | None = None, lang: str = "auto"
) -> List[str]:
    """
    Tokenize and remove stopwords.

    Args:
        query: input text
        stop_words: optional iterable of stop words to remove
        lang: 'auto' | 'zh' | 'en'
    Returns:
        list of tokens after processing
    """
    if lang not in {"auto", "zh", "en"}:
        raise ValueError("lang must be 'auto', 'zh', or 'en'")

    if lang == "auto":
        lang = "zh" if _has_cjk(query) else "en"

    tokens = _tokenize_zh(query) if lang == "zh" else _tokenize_en(query)

    if stop_words is None:
        stop_words = ZH_STOP if lang == "zh" else EN_STOP

    sw: Set[str] = set(stop_words)
    # For English, tokens are lowercased; for Chinese, keep original
    filtered = [t for t in tokens if t not in sw]
    return filtered


def main() -> None:
    p = argparse.ArgumentParser(
        description="Query preprocessor: tokenize + remove stopwords"
    )
    p.add_argument("query", type=str, help="input query text")
    p.add_argument(
        "-l",
        "--lang",
        choices=["auto", "zh", "en"],
        default="auto",
        help="language mode",
    )
    args = p.parse_args()

    tokens = preprocess_query(args.query, lang=args.lang)
    print(json.dumps(tokens, ensure_ascii=False))


if __name__ == "__main__":
    main()
