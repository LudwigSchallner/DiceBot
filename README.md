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
  - name: "dmg"
    alias: 
      - "d"
    brief_explanation: "Command für einen W6 roll (DMG)."
    help_text: "Command für einen W6 roll (DMG)."
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
  - name: "zone"
    alias: 
      - "t"
      - "z"
      - "treffer"
    brief_explanation: "Command für einen Trefferzonenwurf."
    help_text: "Command für einen Trefferzonenwurf."
    dice: 
      face_number: 20
      default_count: 1
      result_to_text:
        1: "Beine (Links)"
        2: "Beine (Rechts)"
        3: "Beine (Links)"
        4: "Beine (Rechts)"
        5: "Beine (Links)"
        6: "Beine (Rechts)"
        7: "Bauch"
        8: "Bauch"
        9: "Arme (Links)"
        10: "Arme (Rechts)"
        11: "Arme (Links)"
        12: "Arme (Rechts)"
        13: "Arme (Links)"
        14: "Arme (Rechts)"
        15: "Brust"
        16: "Brust"
        17: "Brust"
        18: "Brust"
        19: "Kopf"
        20: "Kopf"
```

## Dice config and is may defined defaults
```
face_number: int
result_to_text: Mapping[int, str] = {}
sum_up: bool = False
sort: bool = False
default_count: int = 1
```
