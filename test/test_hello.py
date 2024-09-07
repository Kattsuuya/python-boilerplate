from hello import make_hello_string


class TestMakeHelloString:
    class Test正常系:
        def test_正常な入力_名前あり(self):
            # Arrange
            name = "Alice"

            # Act
            result = make_hello_string(name)

            # Assert
            assert result == "Hello, Alice!"

    class Test異常系:
        def test_空文字入力(self):
            # Arrange
            name = ""

            # Act & Assert
            try:
                make_hello_string(name)
            except ValueError as e:
                assert str(e) == "名前が空です"
