# expirmental

def authorExists(authorName):
    query = (f"""SELECT authorName 
              FROM tbl_author
              WHERE authorName = '{authorName}' """)
    myCursor.execute(query)
    if not myCursor.fetchall():
        return False
    else:
        return True

        boolAuthorExists = authorExists(authorName)
    if boolAuthorExists:
        print("This Author exists")
    else:
        print("Doesn't exist")
