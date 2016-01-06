#include <stdio.h>

#include "db_api.h"


int main(void)
{
	void* c = db_get_cursor();
	void* c2 = db_get_cursor();
    db_prepare(c, "SELECT 1, 'asd', 9.90");
    db_prepare(c2, "SELECT 2, 'bfd', 9");
    db_execute(c);
    db_execute(c2);
    void* r;
    while ((r = db_fetchone(c))) {
        printf("GOT ROW\n");
        int error;
        printf("%d\n", db_get_int(r, 0, &error));
        printf("%f\n", db_get_float(r, 2, &error));
        printf("%s\n", db_get_string(r, 1, &error));
    }
    while ((r = db_fetchone(c2))) {
        printf("GOT ROW\n");
        int error;
        printf("%d\n", db_get_int(r, 0, &error));
        printf("%f\n", db_get_float(r, 2, &error));
        printf("%s\n", db_get_string(r, 1, &error));
    }
    db_close_cursor(c);
    db_close_cursor(c2);
    printf("FINISHING PROGRAM\n");
    return 0;
}
