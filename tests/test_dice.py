from dice_bot import dice


def test_dice():
    """Test basic dice behavior."""
    number = 6
    dice_six = dice.Dice(number=6, command="roll")
    assert dice_six._roll_dice() in range(0, number)
