

def div(num1, num2):
    # 断言：断定  assert 后面的语句是成立的，如果不成立会抛出 AssertionError 异常，并且会随其打印出
    # 断言在定义的时候给出的提示
    assert isinstance(num1, int), "num1应该传整数"
    assert isinstance(num2, int), "num2应该传整数"
    assert num2 != 0, "除数不能为0"
    print(num1/num2)


if __name__ == '__main__':
    div(100, 0)