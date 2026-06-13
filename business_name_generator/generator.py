import random
import re
from typing import List


def _split_words(text: str) -> List[str]:
    if not text:
        return []
    parts = re.split(r"[^A-Za-z0-9]+", text)
    return [p.capitalize() for p in parts if p and len(p) > 0]


def _semantic_tokens(words: List[str]) -> List[str]:
    expanded = []
    for word in words:
        expanded.append(word)
        stems = SEMANTIC_STEMS.get(word.lower())
        if stems:
            expanded.extend(stems)
    return list(dict.fromkeys(expanded))


def _score_name(name: str, keywords: List[str], industry_words: List[str], style: str) -> int:
    score = 0
    lower_name = name.lower()
    for kw in keywords:
        if kw.lower() in lower_name:
            score += 10
    for iw in industry_words:
        if iw.lower() in lower_name:
            score += 6
    if style.lower() in lower_name:
        score += 4
    for kw in _semantic_tokens(keywords + industry_words):
        if kw.lower() in lower_name:
            score += 2
    score -= max(0, (len(name) - 20) // 5)
    return score


STYLE_ADJECTIVES = {
    "modern": ["Neo", "Next", "Bright", "Urban", "Flux"],
    "professional": ["Prime", "Apex", "Cornerstone", "Pinnacle", "Summit"],
    "creative": ["Blue", "Moon", "Wild", "Spark", "Pixel"],
}

SEMANTIC_STEMS = {
    "tech": ["Cyber", "Byte", "Stream", "Pulse", "Logic"],
    "digital": ["Pixel", "Net", "Cloud", "Wave", "Matrix"],
    "food": ["Gourmet", "Fresh", "Harvest", "Bite", "Flavor"],
    "coffee": ["Brew", "Roast", "Bean", "Cup", "Blend"],
    "health": ["Well", "Vital", "Fit", "Care", "Pure"],
    "finance": ["Capital", "Trust", "Wealth", "Prime", "Ledger"],
    "education": ["Learn", "Bright", "Scholar", "Mind", "Academy"],
}

SUFFIXES = ["Labs", "Studios", "Works", "Co", "Solutions", "Systems", "Forge", "Hub", "Collective"]
PREFIXES = ["Alpha", "Beta", "Meta", "Omni", "True", "Fresh"]


def generate_names(
    text_input: str,
    industry: str = "",
    style: str = "modern",
    count: int = 8,
) -> List[str]:
    """Generate up to `count` business name suggestions based on inputs.

    Raises ValueError if text_input is empty or count < 1.
    """
    if not text_input or not text_input.strip():
        raise ValueError("Please provide keywords, industry, or a description.")
    if count < 1:
        raise ValueError("Count must be at least 1")

    keywords = _split_words(text_input)
    industry_words = _split_words(industry)
    pool = []

    # core combinations
    for k in keywords:
        for s in SUFFIXES:
            pool.append(f"{k}{s}")
        for p in PREFIXES:
            pool.append(f"{p}{k}")

    # join keywords
    if len(keywords) >= 2:
        for i in range(len(keywords)):
            for j in range(i + 1, len(keywords)):
                pool.append(keywords[i] + keywords[j])
                pool.append(keywords[j] + keywords[i])

    # adjective + keyword
    adjectives = STYLE_ADJECTIVES.get(style.lower(), STYLE_ADJECTIVES["modern"])
    for a in adjectives:
        for k in keywords:
            pool.append(f"{a}{k}")
            pool.append(f"{k}{a}")

    # industry combos
    for iw in industry_words:
        for k in keywords:
            pool.append(f"{k}{iw}")
            pool.append(f"{iw}{k}")

    # filler combinations if pool too small
    pool.extend([f"{random.choice(PREFIXES)}{random.choice(keywords)}{random.choice(SUFFIXES)}" for _ in range(10)])

    # sanitize and score the generated pool
    def clean(name: str) -> str:
        return re.sub(r"\s+", "", name)

    unique_candidates = {}
    for item in pool:
        name = clean(item)
        if name.lower() in unique_candidates:
            continue
        tokens = [t.lower() for t in keywords + industry_words]
        if tokens and not any(tok in name.lower() for tok in tokens):
            continue
        unique_candidates[name] = _score_name(name, keywords, industry_words, style)

    scored = sorted(unique_candidates.items(), key=lambda item: (-item[1], item[0]))
    result = [name for name, score in scored[:count]]

    if len(result) < count:
        fallback = []
        candidate_pool = [f"{random.choice(PREFIXES)}{random.choice(SUFFIXES)}", f"{random.choice(SUFFIXES)}{random.choice(PREFIXES)}"]
        seen = set(name.lower() for name in result)
        while len(result) + len(fallback) < count:
            cand = random.choice(candidate_pool)
            if cand.lower() not in seen:
                fallback.append(cand)
                seen.add(cand.lower())
        result.extend(fallback)

    return result[:count]


if __name__ == "__main__":
    print(generate_names("Tech", industry="Software", style="modern", count=8))
