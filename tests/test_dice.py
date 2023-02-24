from dice_bot import dice


def test_dice():
    """Test basic dice behavior."""
    face_number = 6
    dice_six = dice.Dice(face_number=face_number)
    for dice_result in dice_six(100):
        assert dice_result in (range(1, face_number + 1))
