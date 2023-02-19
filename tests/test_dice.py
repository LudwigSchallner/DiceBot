from dice_bot import dice


def test_dice():
    """Test basic dice behavior."""
    dice_six = dice.Dice(face_number=6, command="roll")
    assert dice_six() in range(0, 6)
