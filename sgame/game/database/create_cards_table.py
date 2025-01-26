from mysql.connector.cursor_cext import MySQLCursorAbstract


def create_cards_table(cursor: MySQLCursorAbstract) -> None:
    cursor.execute(
        """
    CREATE TABLE IF NOT EXISTS cards (
        id INTEGER AUTO_INCREMENT,
        name TEXT NOT NULL,
        cost INTEGER NOT NULL,
        reward INTEGER NOT NULL,
        card_type TEXT(10) NOT NULL,
        spicy_level INTEGER NOT NULL,
        description TEXT(1024),
        PRIMARY KEY (id),
        UNIQUE (name(255))
    )
    """
    )
