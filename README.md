# DiceBot

## Install

git clone https://github.com/LudwigSchallner/DiceBot.git
cd DiceBot
pip install .
python /path/to/DiceBot/src/dice_bot/cli.py --config-path some.yaml

## Config

bot_config:
  token: <insert_your_bot_token>
  command_prefix: 
    - "!"
    - "."
    - "^"
dices:
  - name: "dmg"
    alias: 
      - "d"
    brief_explanation: "Command für einen W6 roll (DMG)."
    help_text: "Command für einen W6 roll (DMG).\nOhne Ansatz der Würfel wird mit einem Würfel gewürfelt."
    dice: 
      face_number: 6
      sum_up: True
  - name: "roll"
    alias: 
      - "r"
      - "probe"
    brief_explanation: "Command für einen W20 wurf."
    help_text: "Command für einen W20 wurf."
    dice: 
      face_number: 20
      default_count: 3

# dice config and is may defined defaults
  face_number: int
  result_to_text: Mapping[int, str] = {}
  sum_up: bool = False
  sort: bool = False
  default_count: int = 1

