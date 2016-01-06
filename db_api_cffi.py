import cffi

ffi = cffi.FFI()

ffi.cdef("""
    extern "Python" {
        void *db_get_cursor();
		void db_close_cursor(void *);
        void db_prepare(void *, char *);
        void db_execute(void *);
        void *db_fetchone(void *);
        int db_get_int(void *, int, int *);
        float db_get_float(void *, int, int *);
        char * db_get_string(void *, int, int *);
    }
""", dllexport=True)

ffi.embedding_init_code("import db_api")

ffi.set_source("_db_api", "")

ffi.emit_c_code('_db_api.c')
