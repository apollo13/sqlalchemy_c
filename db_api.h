#pragma once

extern void* db_get_cursor();
extern void db_close_cursor(void*);
extern void db_prepare(void*, char*);
extern void db_execute(void*);
extern void* db_fetchone(void*);
extern int db_get_int(void *, int, int *);
extern float db_get_float(void *, int, int *);
extern char * db_get_string(void *, int, int *);
