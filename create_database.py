import sqlite3

connection = sqlite3.connect('morse_dictionary.db')
cursor = connection.cursor()

cursor.execute(
    """CREATE TABLE IF NOT EXISTS russian(rus_letter STRING PRIMARY KEY, morse_letter STRING)""")
cursor.execute("""INSERT INTO russian VALUES ('а', '•-')""")
cursor.execute("""INSERT INTO russian VALUES ('б', '-•••')""")
cursor.execute("""INSERT INTO russian VALUES ('в', '•--')""")
cursor.execute("""INSERT INTO russian VALUES ('г', '--•')""")
cursor.execute("""INSERT INTO russian VALUES ('д', '-••')""")
cursor.execute("""INSERT INTO russian VALUES ('е', '•')""")
cursor.execute("""INSERT INTO russian VALUES ('ё', '•')""")
cursor.execute("""INSERT INTO russian VALUES ('ж', '•••-')""")
cursor.execute("""INSERT INTO russian VALUES ('з', '--••')""")
cursor.execute("""INSERT INTO russian VALUES ('и', '••')""")
cursor.execute("""INSERT INTO russian VALUES ('й', '•---')""")
cursor.execute("""INSERT INTO russian VALUES ('к', '-•-')""")
cursor.execute("""INSERT INTO russian VALUES ('л', '•-••')""")
cursor.execute("""INSERT INTO russian VALUES ('м', '--')""")
cursor.execute("""INSERT INTO russian VALUES ('н', '-•')""")
cursor.execute("""INSERT INTO russian VALUES ('о', '---')""")
cursor.execute("""INSERT INTO russian VALUES ('п', '•--•')""")
cursor.execute("""INSERT INTO russian VALUES ('р', '•-•')""")
cursor.execute("""INSERT INTO russian VALUES ('с', '•••')""")
cursor.execute("""INSERT INTO russian VALUES ('т', '-')""")
cursor.execute("""INSERT INTO russian VALUES ('у', '••-')""")
cursor.execute("""INSERT INTO russian VALUES ('ф', '••-•')""")
cursor.execute("""INSERT INTO russian VALUES ('х', '••••')""")
cursor.execute("""INSERT INTO russian VALUES ('ц', '-•-•')""")
cursor.execute("""INSERT INTO russian VALUES ('ч', '---•')""")
cursor.execute("""INSERT INTO russian VALUES ('ш', '----')""")
cursor.execute("""INSERT INTO russian VALUES ('щ', '--•-')""")
cursor.execute("""INSERT INTO russian VALUES ('ъ', '•--•-•')""")
cursor.execute("""INSERT INTO russian VALUES ('ы', '-•--')""")
cursor.execute("""INSERT INTO russian VALUES ('ь', '-••-')""")
cursor.execute("""INSERT INTO russian VALUES ('э', '•••-•••')""")
cursor.execute("""INSERT INTO russian VALUES ('ю', '••--')""")
cursor.execute("""INSERT INTO russian VALUES ('я', '•-•-')""")

cursor.execute(
    """CREATE TABLE IF NOT EXISTS english(eng_letter STRING PRIMARY KEY, morse_letter STRING)""")
cursor.execute("""INSERT INTO english VALUES ('a', '•-')""")
cursor.execute("""INSERT INTO english VALUES ('b', '-•••')""")
cursor.execute("""INSERT INTO english VALUES ('c', '-•-•')""")
cursor.execute("""INSERT INTO english VALUES ('d', '-••')""")
cursor.execute("""INSERT INTO english VALUES ('e', '•')""")
cursor.execute("""INSERT INTO english VALUES ('f', '••-•')""")
cursor.execute("""INSERT INTO english VALUES ('g', '--•')""")
cursor.execute("""INSERT INTO english VALUES ('h', '••••')""")
cursor.execute("""INSERT INTO english VALUES ('i', '••')""")
cursor.execute("""INSERT INTO english VALUES ('j', '•---')""")
cursor.execute("""INSERT INTO english VALUES ('k', '-•-')""")
cursor.execute("""INSERT INTO english VALUES ('l', '•-••')""")
cursor.execute("""INSERT INTO english VALUES ('m', '--')""")
cursor.execute("""INSERT INTO english VALUES ('n', '-•')""")
cursor.execute("""INSERT INTO english VALUES ('o', '---')""")
cursor.execute("""INSERT INTO english VALUES ('p', '•--•')""")
cursor.execute("""INSERT INTO english VALUES ('q', '--•-')""")
cursor.execute("""INSERT INTO english VALUES ('r', '•-•')""")
cursor.execute("""INSERT INTO english VALUES ('s', '•••')""")
cursor.execute("""INSERT INTO english VALUES ('t', '-')""")
cursor.execute("""INSERT INTO english VALUES ('u', '••-')""")
cursor.execute("""INSERT INTO english VALUES ('v', '•••-')""")
cursor.execute("""INSERT INTO english VALUES ('w', '•--')""")
cursor.execute("""INSERT INTO english VALUES ('x', '-••-')""")
cursor.execute("""INSERT INTO english VALUES ('y', '-•--')""")
cursor.execute("""INSERT INTO english VALUES ('z', '--••')""")

cursor.execute("""CREATE TABLE IF NOT EXISTS numbers(number STRING PRIMARY KEY, morse_num STRING)""")
cursor.execute("""INSERT INTO numbers VALUES('0', '-----')""")
cursor.execute("""INSERT INTO numbers VALUES('1', '•----')""")
cursor.execute("""INSERT INTO numbers VALUES('2', '••---')""")
cursor.execute("""INSERT INTO numbers VALUES('3', '•••--')""")
cursor.execute("""INSERT INTO numbers VALUES('4', '••••-')""")
cursor.execute("""INSERT INTO numbers VALUES('5', '•••••')""")
cursor.execute("""INSERT INTO numbers VALUES('6', '-••••')""")
cursor.execute("""INSERT INTO numbers VALUES('7', '--•••')""")
cursor.execute("""INSERT INTO numbers VALUES('8', '---••')""")
cursor.execute("""INSERT INTO numbers VALUES('9', '----•')""")

cursor.execute("""CREATE TABLE IF NOT EXISTS symbols(symbol STRING PRIMARY KEY, morse_sym STRING)""")
cursor.execute("""INSERT INTO symbols VALUES('.', '•-•-•-')""")
cursor.execute("""INSERT INTO symbols VALUES(',', '--••--')""")
cursor.execute("""INSERT INTO symbols VALUES('!', '-•-•--')""")
cursor.execute("""INSERT INTO symbols VALUES('?', '••--••')""")
cursor.execute("""INSERT INTO symbols VALUES('-', '-••••-')""")
cursor.execute("""INSERT INTO symbols VALUES('+', '•-•-•')""")
cursor.execute("""INSERT INTO symbols VALUES('=', '-•••-')""")
cursor.execute("""INSERT INTO symbols VALUES('(', '-•--•')""")
cursor.execute("""INSERT INTO symbols VALUES(')', '-•--•-')""")
cursor.execute("""INSERT INTO symbols VALUES(';', '-•-•-•')""")
cursor.execute("""INSERT INTO symbols VALUES(':', '---•••')""")
cursor.execute("""INSERT INTO symbols VALUES('"', '•-••-•')""")

connection.commit()
connection.close()
