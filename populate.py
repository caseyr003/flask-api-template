from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database import Base, Item, User

engine = create_engine('sqlite:///sample.db')

# Bind engine to the metadata of the Base class for DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)

# changes to database are in staging until session.commit() is called
session = DBSession()

# Sample user 01 with items
user01 = User(name="Sample User01")
session.add(user01)
item01 = Item(user=user01, name="Sample Item01",
              description="This is sample item 01.")
session.add(item01)
item02 = Item(user=user01, name="Sample Item02",
              description="This is sample item 02.")
session.add(item02)
item03 = Item(user=user01, name="Sample Item03",
              description="This is sample item 03.")
session.add(item03)

# Sample user 02 with items
user02 = User(name="Sample User02")
session.add(user02)
item04 = Item(user=user02, name="Sample Item04",
              description="This is sample item 04.")
session.add(item04)
item05 = Item(user=user02, name="Sample Item05",
              description="This is sample item 05.")
session.add(item05)
item06 = Item(user=user02, name="Sample Item06",
              description="This is sample item 06.")
session.add(item06)

# Commit data to database
session.commit()

print("Sample data added...")
