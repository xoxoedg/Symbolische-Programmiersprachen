| Muster   | Bedeutung                                | Beispiel                      |        |         |
| -------- | ---------------------------------------- | ----------------------------- | ------ | ------- |
| `.`      | beliebiges Zeichen (außer Zeilenumbruch) | `a.c` → „abc“, „axc“          |        |         |
| `\d`     | Ziffer (0–9)                             | `\d\d` → zwei Zahlen          |        |         |
| `\w`     | Buchstabe oder Zahl oder `_`             |                               |        |         |
| `\s`     | Whitespace (Leerzeichen, Tab etc.)       |                               |        |         |
| `+`      | 1 oder mehr Wiederholungen               | `\d+` → „1“, „123“            |        |         |
| `*`      | 0 oder mehr Wiederholungen               | `a*` → "", "a", "aa"          |        |         |
| `?`      | 0 oder 1 Wiederholung                    | `colou?r` → „color“, „colour“ |        |         |
| `{n,m}`  | n bis m Wiederholungen                   | `\d{2,4}` → 2–4 Ziffern       |        |         |
| `^`      | Anfang des Strings                       | `^Hallo`                      |        |         |
| `$`      | Ende des Strings                         | `Welt$`                       |        |         |
| `[abc]`  | Zeichenklasse („a“ oder „b“ oder „c“)    |                               |        |         |
| `[^abc]` | Negation – alles außer a, b, c           |                               |        |         |
| `( )`    | Gruppe / Teilmuster                      |                               |        |         |
| `        | `                                        | Oder-Operator                 | `(Hund | Katze)` |

---

- re.search(pattern, string) -> sucht überall
- re.match(pattern, string) -> sucht nachdem pattern am Anfang