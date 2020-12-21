import traceback
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import exc

ERROR_PREFIX = "ERROR:"
ERROR_ALREADY_EXISTS = "Already Exists"


def error_printer(error_string):
    print(error_string)
    traceback.print_exc()


class CoreSQLAlchemy(SQLAlchemy):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


db = CoreSQLAlchemy()


class BaseModel:
    @classmethod
    def add_new_to_database(cls, obj):
        try:
            db.session.add(obj)
            db.session.flush()

            db.session.refresh(obj)

            db.session.commit()

            return str(obj.id)

        except exc.DataError as e:
            error_printer("DB Core exception: " + str(e))
            db.session.rollback()
            return f'{ERROR_PREFIX} {cls.__name__} Parameters Invalid'

        except exc.ProgrammingError as e:
            error_printer("DB Core exception: " + str(e))
            db.session.rollback()
            return f'{ERROR_PREFIX} Table Does Not Exist or There Were An Invalid Number of Parameters'

        except exc.IntegrityError as e:
            error_printer("DB Core exceptions: " + str(e))
            db.session.rollback()
            return f'{ERROR_PREFIX} {cls.__name__} {ERROR_ALREADY_EXISTS}'
