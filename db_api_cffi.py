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

ffi.embedding_init_code("""
    import db_api

    ffi.def_extern()(db_api.db_get_cursor)
    ffi.def_extern()(db_api.db_close_cursor)
    ffi.def_extern()(db_api.db_prepare)
    ffi.def_extern()(db_api.db_execute)
    ffi.def_extern()(db_api.db_fetchone)
    ffi.def_extern()(db_api.db_get_string)
    ffi.def_extern()(db_api.db_get_int)
    ffi.def_extern()(db_api.db_get_float)
""")

ffi.set_source("_db_api", """
""")

ffi.emit_c_code('_db_api.c')
