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
```
Agná
 [agˈna] bird, plural: ágnaya
Gender: Masculine
POS: Noun
Semantic field: animals
Cases:
  gen: ágnand
```
## Installation

1. install Python 3.6 or newer from [python.org](https://python.org)
2. download or clone this repository
3. no additional packages are needed, uses only python standard library!

# Usage:
Install it:
```
pip install wccm
```
Then you can just use it like this:
```
wccm file.wccm 
```

Outputs to `Lexicon.txt` by default.

# Syntax

WCCM uses symbols to represent different properties. Their order is irrelevant, as long as the plain word is always first. 

## Lexicon
(Lexicon-related syntax goes in `.wccm` files).

| Symbol       | Field                 | Example                       |
| ------------ | --------------------- | ----------------------------- |
| (None)       | Word                  | **Kat**                       |
| `$`          | IPA                   | **$kæt**                      |
| `#`          | Semantic field        | **\#animal**                  |
| `~`          | Gender                | **~M**                        |
| `?`          | Translation           | **?Cat**                      |
| `+`          | Plural form(s)        | **+Cats**                     |
| `;` and `:`  | Case name / case form | **;gen :cat's**               |
| `=`          | Synonym(s)            | **=feline**                   |
| `!`          | Antonym(s)            | **!dog**                      |
| `%`          | Part of speech        | **%noun**                     |
| `*`          | Etymology             | **\*from 'kaltnaen'**         |
| `\|` and `/` | Conjugations          | **\|3rd sg present /does**    |
| `@` and `:`  | Custom                | **@class :animte**            |
| `_`          | Comment               | **_ what do I even put here** |
## Inventory
(Inventory-related information goes in `.cmi` files).

| Symbol | Field        | Example      |
| ------ | ------------ | ------------ |
| `.`    | consonant    | **.tH**      |
| `,`    | vowel        | **,3**       |
| `^`    | Tone         | **\^rising** |
| `-`    | romanization | **-ñ :ny**   |

Don't like this set of symbols? That's completely fine! You can edit them anytime by going into `config.json`.

## IPA 
I know that typing IPA symbols can be tedious if you don't have the tools, which is why I implemented a function to let you map a character to an IPA sound, to make writing transcriptions easier!
# Configuration 

WCCM lets you customize:
- what each symbol means (which property it represents)
- IPA character mapping (e.g., `:` -> `ː`)
- default output file

Default configurations:
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
        "^": "tone",
        "-": "romanization"
    },
    "prefs": {
        "output": {
            "defaultFileName": "lexicon",
            "defaultFormat": ".txt"
        }
    }
}
```

For the IPA replacement mapping, the character on the left is the character that the program will replace. So, essentially, if your IPA is "SaTaZ", with the default configurations (the ones showed above) it would turn into "ʃaθaʒ". You can add/remove as many as you want! (As long as you don't map 1 character to 2 symbols).

Same goes for the properties, although it is very important that you do **not** alter the keywords, otherwise the tool will break.

As you might've guessed, you can also choose the default name and format of the output file! The name can be anything you want, and the file extension can be either `.txt` or `.md`. A `lexicon.json` file is always automatically generated, which is why `.json` isn't an option in preferences.

All you have to do to change your configs is write your file, save it as `.pref` and just use it as an argument:
```
wccm configs.pref 
```
and that's it!

<<<<<<< HEAD
Here's how this works:

```
ipamap set <characters> to <IPA>
propmap set <symbol(s)> to <property name>
default output format set <file extension>
default file name set <name>
invnetorymap set <symbol(s)> to <property>
```

=======
Here's the full `.pref` syntax:

| Symbol | Config                                                                      |
| ------ | --------------------------------------------------------------------------- |
| `;`    | none; comment                                                               |
| `:`    | IPA mapping                                                                 |
| `?`    | output preferences (default name and format of output file)                 |
| `,`    | edit property symbols (e.g., use `??` instead of `#` for semantic field)    |
| `/`    | inventory mapping (same as above but symbols used for inventory management) |

I'm aware that this can be confusing and hard to get used to, so I'm working to improve the way to manage configurations, but in the meantime you'll have to put up with that (sorry!)
>>>>>>> 4cb8b25e59dcdec6aa1c69413b60bf2f18279f6f

## Limitations 

If you ever want to remap a symbol, as said before, you're allowed (and encouraged) to do so! However, it is very important that you don't map `\` to anything. Since i don't want to confuse you with tech talk, basically, `\` is a special character and if you try to use it for mapping the configuration file is going to break.
And, for reasons that are truly beyond my knowledge, "field" (semantic field) and "comment" properties can't be modified? I'll try to fix it later; too tired to do it right now.

Other than that, you should be able to change pretty much anything!

# About

WCCM started as just a little personal tool I developed because I'm stubborn and don't like any of the tools that already exist, and now I'm sharing it in case someone finds it useful as well.

# Feedback is appreciated! 

This is my first time actually finishing and sharing a project, so I'd genuinely *love* to hear suggestions or ideas for future versions, as well as bug reports and other stuff like that.
Also, if you guys think that this is a bit "too technical" for the average conlanger, please let me know and I'll try my best to make it as intuitive and a little more non-coder friendly.
<<<<<<< HEAD
You can contact me pretty much any time in [**my twitter (I'm not calling it 'X')**](https://x.com/wernasho) or [**my reddit!**](https://reddit.com/user/wernasho)
=======
You can contact me pretty much any time in [my twitter (I'm not calling it 'X')](https://x.com/wernasho) or [my reddit!](https://reddit.com/user/wernasho)
>>>>>>> 4cb8b25e59dcdec6aa1c69413b60bf2f18279f6f
