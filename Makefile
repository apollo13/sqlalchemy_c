CC=gcc
CFLAGS=-c -Wall
LDFLAGS=
SOURCES=main.c
OBJECTS=$(SOURCES:.c=.o)
EXECUTABLE=main

all: $(SOURCES) $(EXECUTABLE)

$(EXECUTABLE): $(OBJECTS) _db_api.so
	$(CC) $(LDFLAGS) $(OBJECTS) _db_api.so -o $@

_db_api.c: db_api_cffi.py
	python db_api_cffi.py

_db_api.so: _db_api.c
	$(CC) -shared -fPIC _db_api.c -o $@ -lpython2.7 -I/usr/include/python2.7

.c.o:
	$(CC) $(CFLAGS) $< -o $@
