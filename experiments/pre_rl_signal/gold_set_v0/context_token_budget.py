from __future__ import annotations

import argparse
import hashlib
from pathlib import Path
from typing import Any


TOKENIZER_MODEL = "Qwen/Qwen3-8B-Base"
TOKENIZER_REVISION = "49e3418fbbbca6ecbdf9608b4d22e5a407081db4"
TOKENIZER_SHA256 = "c0382117ea329cdf097041132f6d735924b697924d6f6fc3945713e96ce87539"
MAX_CONTEXT_TOKEN_SPREAD = 8

# Exact token counts under the pinned tokenizer, keyed by the SHA-256 digest of
# the UTF-8 context text. Hash locking lets ordinary fixture validation detect
# stale evidence without requiring the 11 MB tokenizer asset in every checkout.
EXPECTED_TOKEN_COUNTS = {
    "2cefb3e44ef8c4fffc41769de9e87a0022dab519d774a8c6b720d5d97832114f": 32,
    "302fc1274daea24c8d61e33cf69a406848c9e2ad87b89b4065e9885d959b830f": 32,
    "3125383ca94f678233fd52b2f8f920cb16f49df3b2b0207f3de497532c4604fa": 35,
    "3f0acb982cb2fa12fb13f957cd26315890b1ae02b2c628f028b15c23c14edb91": 32,
    "4f2a05ff09000a44dee6d51827cacdfa357952ebab110db13ee897fd5d91e035": 27,
    "5e9c220490d7675b14d7c17303ba0322445b4aa66267b4e5c18d3b5dae7300a0": 31,
    "6a17fe496cff640efd4801b2c9f2e34d7b491be905fd51c8743337580468d612": 31,
    "6f5eb4b898d8aa1cabf1683edd0fa346f7caa5c8a6005a3e4fea11554318a2b9": 28,
    "71dab19631d52e207f5031eae9f1ad96d611ecf357f44144d42bfb9cb763f9fe": 31,
    "7a02646aabc8d8739368f290a0cfc9d3ff01dbd57ed74667f220811ad8b7e805": 33,
    "7c02aca8b5838764b57c9d6720338221235dfcbed12b3233b167ec827b81a1ae": 31,
    "7efc777f10ee63ed8f200ec78ae675793ee8aa89aa33363c78ee2d7aab74bee8": 33,
    "8020e49fad0c32037b16cfacb8082c56a39ed58d9f213a02fdf7fabe5aac6fe4": 32,
    "90eaca49f1b16e932e3b7dba1137e18090cdcfabb654c043091de32ca25c5200": 35,
    "97753c880c1c8a9106f905e41a401bd8a126478006c222ee6da998b565cd3ef2": 30,
    "99eaa3946d74fabd82879f6d40ca67ffabab7fa9c7028f907253a3915e1ddb42": 34,
    "9cc6f055c6c5b0154b9d9d9bf2929572dd095538962a09b0306a7c003ec6ebfb": 35,
    "b2443ba0e9dd95363c16d19583fea81f2f664a3d308ec55ecb373a3d983f1720": 32,
    "bc14b19e69163dc12207d10fe29e3b2fd364ae91222a767c0bdeb54a7a6d2bd0": 33,
    "e7414016dedf7abe15d499bd3547a17032bb80f399ec0677bad78a0024d6665e": 31,
    "e7d64a5b1f74a1d74e1e880292465c5c383e58d5cfb1f4c332648caeb1ed62eb": 33,
    "eb489eb3f2f2bf9950371035a934d56f30645ff721ba2f35e786977aecf0762d": 33,
    "ef913ff79bfffefde92e436ecdc011acd60234b3939ecd8111969b18bf29bb83": 29,
    "f393e31134f8cdeb6286f806c2265905466cda292e9ffb469618d096543fc388": 30,
    "f3f20dae679e1416308a296477b052b4f83eb54bca4995cb810863fcbd6e7b6b": 31,
    "f859345c5ec91017f759ec5d02b3cdc6f9ee652345b1282fcd6aaf9bcf05c36c": 27,
}


def _digest(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def _condition_texts(public: dict[str, Any]) -> list[tuple[str, dict[str, str]]]:
    shuffled_pool = public["shuffled_pool"]
    result: list[tuple[str, dict[str, str]]] = []
    for situation in public["situations"]:
        texts = dict(situation["contexts"])
        texts["shuffled"] = shuffled_pool[situation["shuffled_context_id"]]
        result.append((situation["id"], texts))
    return result


def validate_context_token_budget(public: dict[str, Any]) -> dict[str, dict[str, int]]:
    counts_by_situation: dict[str, dict[str, int]] = {}
    observed_digests: set[str] = set()
    for sid, texts in _condition_texts(public):
        counts: dict[str, int] = {}
        for condition, text in texts.items():
            digest = _digest(text)
            observed_digests.add(digest)
            assert digest in EXPECTED_TOKEN_COUNTS, (sid, condition, digest)
            counts[condition] = EXPECTED_TOKEN_COUNTS[digest]
        assert max(counts.values()) - min(counts.values()) <= MAX_CONTEXT_TOKEN_SPREAD
        counts_by_situation[sid] = counts
    assert observed_digests == set(EXPECTED_TOKEN_COUNTS)
    return counts_by_situation


def validate_tokenizer_asset(public: dict[str, Any], tokenizer_json: Path) -> None:
    assert hashlib.sha256(tokenizer_json.read_bytes()).hexdigest() == TOKENIZER_SHA256
    try:
        from tokenizers import Tokenizer
    except ImportError as exc:
        raise SystemExit("tokenizer-backed validation requires the `tokenizers` package") from exc

    tokenizer = Tokenizer.from_file(str(tokenizer_json))
    for sid, texts in _condition_texts(public):
        for condition, text in texts.items():
            actual = len(tokenizer.encode(text, add_special_tokens=False).ids)
            expected = EXPECTED_TOKEN_COUNTS[_digest(text)]
            assert actual == expected, (sid, condition, actual, expected)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--tokenizer-json", required=True, type=Path)
    args = parser.parse_args()

    from public_fixtures import build_public

    public = build_public()
    counts = validate_context_token_budget(public)
    validate_tokenizer_asset(public, args.tokenizer_json)
    print(
        f"validated context budget with {TOKENIZER_MODEL}@{TOKENIZER_REVISION}: "
        f"{len(counts)} situations / max spread {MAX_CONTEXT_TOKEN_SPREAD} tokens"
    )


if __name__ == "__main__":
    main()
