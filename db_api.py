import cffi
from sqlalchemy import create_engine

ffi = cffi.FFI()

engine = create_engine('sqlite:///:memory:', echo=False)

handles = []


class Row(object):
    def __init__(self, row):
        self.row = row
        self.handlers = {}

    def __del__(self):
        print "DESTROYING ROW!"


class Cursor(object):
    def __init__(self):
        self._init()

    def _init(self):
        self.statement = ''
        self.args = []
        self.result = None
        self.current_row_handler = None

    def fetchone(self):
        row = self.result.fetchone()
        if row is not None:
            handle = ffi.new_handle(Row(row))
            self.current_row_handler = handle
        else:
            handle = ffi.NULL
        return handle

    def __del__(self):
        print "DESTROYING CURSOR!"


def db_get_cursor():
    cursor = Cursor()
    handle = ffi.new_handle(cursor)
    handles.append(handle)
    return handle


def db_close_cursor(cursor_handle):
    cursor = ffi.from_handle(cursor_handle)
    if cursor.result:
        cursor.result.close()
    handles.remove(cursor_handle)


def db_prepare(cursor_handle, statement):
    cursor = ffi.from_handle(cursor_handle)
    if cursor.result:
        cursor.result.close()
    cursor._init()
    cursor.statement = ffi.string(statement)


def db_execute(cursor_handle):
    cursor = ffi.from_handle(cursor_handle)
    cursor.result = engine.execute(cursor.statement, cursor.args)


def db_fetchone(cursor_handle):
    cursor = ffi.from_handle(cursor_handle)
    return cursor.fetchone()


def db_get_string(row_handle, index, error):
    row = ffi.from_handle(row_handle)
    error[0] = 0
    try:
        if index not in row.handlers:
            row.handlers[index] = ffi.new("char[]", row.row[index].encode('utf-8'))
        return row.handlers[index]
    except Exception:
        error[0] = 1
    return ffi.NULL


def db_get_int(row_handle, index, error):
    row = ffi.from_handle(row_handle)
    error[0] = 0
    try:
        return int(row.row[index])
    except Exception:
        error[0] = 1
    return 0


def db_get_float(row_handle, index, error):
    row = ffi.from_handle(row_handle)
    error[0] = 0
    try:
        return float(row.row[index])
    except Exception:
        error[0] = 1
    return 0
