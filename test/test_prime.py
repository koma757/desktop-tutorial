from prime import is_prime


def test_is_prime():
    assert not is_prime(1)
    assert is_prime(2)
    assert is_prime(3)
    assert not is_prime(4)
    assert is_prime(5)
    assert not is_prime(6)
    assert is_prime(7)
    assert not is_prime(8)
    assert not is_prime(9)
    assert not is_prime(10)
    assert is_prime(11)
    assert is_prime(13)
    assert is_prime(17)
    assert is_prime(19)
    assert is_prime(23)
    assert not is_prime(25)
    assert is_prime(29)
    assert not is_prime(30)
    assert is_prime(31)
    assert not is_prime(33)
    assert is_prime(37)
    assert is_prime(41)
    assert is_prime(43)
    assert not is_prime(49)
    assert is_prime(53)
    # 他のテストケースも同様に追加


# コードの最後に、以下を追加します。
if __name__ == "__main__":
    # このブロックが実行されるとき、pytestコマンドによって
    # ファイルが直接実行されたことを意味します。
    # この場合、pytest.main()を呼び出してテストを実行します。
    import pytest
    pytest.main()