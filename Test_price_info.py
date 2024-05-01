import price_info

def test_total_cost_shopping():
    assert(price_info.total_cost_shopping() == 46.75)

def test_cost_of_fruit():
    fruit = 'watermelon'
    quantity = 5
    assert(price_info.cost_of_fruits(fruit, quantity) == 32.5)