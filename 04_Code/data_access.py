# Dependencies and boilerplate
# Python SQL toolkit and Object Relational Mapper
import models
from models import DataAnalyticsJob


class DataAccess():
    def insert_to_tables(self, db, data_result):
        try: 
            db.session.bulk_insert_mappings(DataAnalyticsJob, data_result)
            db.session.commit()
        except:
            db.session.rollback()
        return
        #Base = declarative_base()
        # Create an engine to a SQLite database file
        #Unix/Mac - 4 initial slashes in total
        #engine = create_engine('sqlite:////absolute/path/to/foo.db')
        #engine = create_engine("sqlite:///db/datanalyticsjobs.sqlite")
        # Create a connection to the engine called `conn`
        #conn = engine.connect()
        # Use `create_all` to create the customers table in the database
        #Base.metadata.create_all(engine)
        # Use MetaData from SQLAlchemy to reflect the tables
        ### BEGIN SOLUTION
        #metadata = MetaData(bind=engine)
        #metadata.reflect()
        ### END SOLUTION
        # Save the reference to the `customers` table as a variable called `table`
        #table = sqlalchemy.Table('job_position', metadata, autoload=True)
        # Use `table.delete()` to remove any pre-existing data.
        # Note that this is a convenience function so that you can re-run the example code multiple times.
        # You would not likely do this step in production.
       # conn.execute(table.delete())
        # Use `table.insert()` to insert the data into the table
        # The SQL table is populated during this step
        #conn.execute(table.insert(), data_result)