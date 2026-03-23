Wer's Compact Conlang Manager, or WCCM, is a simple command-line tool designed to make conlanging ever so slightly faster and easier by converting a simple, customizeable syntax into clean and readable conlang dictionaries.

I built this because spreadsheets had too much visual clutter and other existing tools were really overkill.
All you need to do is type your properties with shorthands you can customize, and you'll receive a nicely formatted text file.

For example, this:

```
Agná 
$agˈna
%noun
#animals
?bird
~Masculine
+ágnaya
;gen :ágnand
```

Turns into this:
Agná
 \[agˈna] bird, plural: ágnaya
Gender: Masculine
POS: Noun
Semantic field: animals
Cases:
  gen: ágnand

## Installation

1. install Python 3.6 or newer from [python.org](https://python.org)
2. download or clone this repository
3. no additional packages are needed, uses only python standard library!

# Usage:
Open up your console/terminal inside the wccm folder, and run this command:
```bash
py wccm.py file.wccm
```

Outputs to `Lexicon.txt`

# Syntax

WCCM uses symbols to represent different properties. Their order is irrelevant, as long as the plain word is always first. 

## Lexicon
(Lexicon-related syntax goes in `.wccm` files).

| Symbol       | Field                 | Example                    |
| ------------ | --------------------- | -------------------------- |
| (None)       | Word                  | **Kat**                    |
| `$`          | IPA                   | **$kæt**                   |
| `#`          | Semantic field        | **\#animal**               |
| `~`          | Gender                | **~M**                     |
| `?`          | Translation           | **?Cat**                   |
| `+`          | Plural form(s)        | **+Cats**                  |
| `;` and `:`  | Case name / case form | **;gen :cat's**            |
| `=`          | Synonym(s)            | **=feline**                |
| `!`          | Antonym(s)            | **!dog**                   |
| `%`          | Part of speech        | **%noun**                  |
| `*`          | Etymology             | **\*from 'kaltnaen' **     |
| `\|` and `/` | Conjugations          | **\|3rd sg present /does** |
| `@` and `:`  | Custom                | **@class :animal**         |
## Inventory
(Inventory-related information goes in `.cmi` files).

| Symbol | Field     | Example      |
| ------ | --------- | ------------ |
| `.`    | consonant | **.TH**      |
| `,`    | vowel     | **.3**       |
| `^`    | Tone      | **\^rising** |

Don't like this set of symbols? That's completely fine! You can edit them anytime by going into `config.json`.

## IPA 
I know that typing IPA symbols can be tedious if you don't have the tools, which is why I implemented a function to let you map a character to an IPA sound, to make writing transcriptions easier!
# Configuration 

`config.json` lets you customize:
- what each symbol means (which property it represents)
- IPA character mapping (e.g., `:` -> `ː`)
- default output file

```json
{
    "ipa": {
        "S": "ʃ",
        "T": "θ",
        "R": "ɾ",
        "B": "β",
        "D": "ð",
        "N": "ŋ",
        "J": "ʲ",
        "Z": "ʒ",
        ":": "ː",
        "'": "ˈ",
        "ny": "ɲ",
        "W": "ʷ",
        "H": "ʰ",
        "A": "ɑ",
        "E": "ə",
        "I": "ɪ",
        "3": "ɛ",
        "O": "ɔ",
        "U": "ʊ",
        "^": "ʌ",
        "X": "χ"
    },
    "props": {
        "$": "ipa",
        "#": "field",
        "%": "pos",
        "_": "comment",
        "~": "gender",
        "=": "synonym",
        "!": "antonym",
        "+": "plural",
        "?": "meaning",
        "*": "etymology",
        ";": "case",
        "|": "conjugations",
        "@": "custom"
    },
    "inv":  {
        ".":  "consonant",
        ",": "vowel",
        "^": "tone"
    },
    "prefs": {
        "output": {
            "defaultFileName": "lexicon",
            "defaultFormat": ".txt"
        }
    }
}
```

For the IPA replacement mapping, the character on the left is the character that the program will replace. So, essentially, if your IPA is "SaTaZ", with the default configurations (the ones showed above) it would turn into "ʃaθaʒ". You can add/remove as many as you want! (As long as you don't map 1 character to 2 symbols or use digraphs).

Same goes for the properties, although it is very important that you do **not** alter the keywords, otherwise the tool will break.

As you might've guessed, you can also choose the default name and format of the output file! The name can be anything you want, and the file extension can be either `.txt` or `.md`. A `lexicon.json` file is always automatically generated, which is why `.json` isn't an option in preferences.
## Limitations 

Currently, the case symbols (`;` and `:`) can't be customized, as well as the conjugation symbols (`|` and `/`).
If you ever want to remap a symbol, as said before, you're allowed (and encouraged) to do so! However, it is very important that you don't map `\` to anything. Since i don't want to confuse you with tech talk, basically, `\` is a special character and if you try to use it for mapping the configuration file is going to break.

Other than that, you should be able to change pretty much anything!

# About

WCCM started as just a little personal tool I developed because I'm stubborn and don't like any of the tools that already exist, and now I'm sharing it in case someone finds it useful as well.

# Feedback is appreciated! 

This is my first time actually finishing and sharing a project, so I'd genuinely *love* to hear suggestions or ideas for future versions, as well as bug reports and other stuff like that.
You can contact me pretty much any time in [my twitter (I'm not calling it 'X')](https://x.com/wernasho)
