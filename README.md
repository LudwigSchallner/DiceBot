# DiceBot

## Install
```
git clone https://github.com/LudwigSchallner/DiceBot.git
cd DiceBot
pip install .
dice --config-path some.yaml
```

## Config
```
bot_config:
  token: <insert_your_bot_token>
  command_prefix:
    - "!"
    - "."
    - "^"
dices:
  - name: "roll"
    alias:
      - "r"
      - "probe"
    brief_explanation: "Command für einen W20 wurf."
    help_text: "Command für einen W20 wurf."
    dice:
      _target_: dice_bot.dice.<type_of_type> 
      face_number: 20
      default_count: 3

```
