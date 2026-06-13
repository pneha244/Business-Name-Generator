from generator import generate_names


def run_basic_checks():
    # 1. valid input returns at least one name
    names = generate_names("Tech", industry="Software", style="modern", count=5)
    assert len(names) >= 1

    # 2. multiple keywords
    names2 = generate_names("Coffee Organic", industry="Food", style="creative", count=6)
    assert len(names2) == 6

    # 3. empty input raises
    try:
        generate_names("")
        raise SystemExit("expected ValueError for empty input")
    except ValueError:
        pass

    print("Basic checks passed")


if __name__ == "__main__":
    run_basic_checks()
