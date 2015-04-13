# coding=utf-8=
from .base import BaseTableDefiner
from gluon.dal import Field


class DB2TableDefiner(BaseTableDefiner):
    types = {
        'BIGINT': 'bigint',
        'BLOB': 'blob',
        'CHARACTER': 'string',
        'CLOB': 'text',
        'DATE': 'date',
        'DECIMAL': 'decimal',
        'DOUBLE': 'double',
        'INTEGER': 'integer',
        'LONG VARCHAR': 'text',
        'SMALLINT': 'integer',
        'TIME': 'time',
        'TIMESTAMP': 'datetime',
        'VARCHAR': 'string'
    }

    def __init__(self, datasource, schema, **kwargs):
        super(DB2TableDefiner, self).__init__(datasource, schema, **kwargs)
        self.__define_source_tables()
        self._define_tables()

    def __define_source_tables(self):
        self.db.define_table(
            'TABLES',
            Field('TABNAME'),
            Field('TABSCHEMA'),
            migrate=False,
            rname='SYSCAT.TABLES',
            primarykey=['TABNAME', 'TABSCHEMA']
        )

        self.db.define_table(
            'VIEWS',
            Field('VIEWNAME'),
            Field('VIEWSCHEMA'),
            migrate=False,
            rname='SYSCAT.VIEWS',
            primarykey=['VIEWNAME', 'VIEWSCHEMA']
        )

        self.db.define_table(
            'COLUMNS',
            Field('TABNAME'),
            Field('TABSCHEMA'),
            Field('COLNAME'),
            Field('COLNO'),
            Field('LENGTH', 'integer'),
            Field('NULLS'),
            Field('SCALE'),
            Field('TYPENAME'),
            Field('REMARKS'),
            migrate=False,
            rname='SYSCAT.COLUMNS',
            primarykey=['TABSCHEMA', 'TABNAME', 'COLNAME']
        )

        self.db.define_table(
            'INDEXES',
            Field('TABSCHEMA'),
            Field('TABNAME'),
            Field('COLNAMES'),
            Field('UNIQUERULE'),
            migrate=False,
            rname='SYSCAT.INDEXES',
            primarykey=['TABSCHEMA', 'TABNAME']
        )

    def _fetch_indexes(self):
        rows = self.db((self.db.INDEXES.TABSCHEMA == self.schema) & (self.db.INDEXES.UNIQUERULE == 'P')).select(
            self.db.INDEXES.TABNAME,
            self.db.INDEXES.COLNAMES
        )
        return {table.TABNAME: table.COLNAMES.split('+')[1:] for table in rows}

    @property
    def __tables(self):
        """
        :rtype : tuple
        """
        table_names = self.db(self.db.TABLES.TABSCHEMA == self.schema).select(self.db.TABLES.TABNAME)
        return {table.TABNAME: [] for table in table_names}

    def _fetch_columns(self):
        cols = self.db(self.db.COLUMNS.TABSCHEMA == self.schema).select(
            self.db.COLUMNS.TABNAME,
            self.db.COLUMNS.COLNAME,
            self.db.COLUMNS.LENGTH,
            self.db.COLUMNS.TYPENAME,
            self.db.COLUMNS.REMARKS
        )
        for col in cols:
            try:
                self.__tables[col.TABNAME].append(
                    Field(col.COLNAME, self.types[col.TYPENAME], length=col.LENGTH, label=col.REMARKS))
            except KeyError:
                print "Não foi possível adicionar a coluna %s de %s - tipo %s desconhecido" % (
                    col.COLNAME, col.TABNAME, col.TYPENAME)

        return self.__tables

    def refresh_cache(self):
        #TODO Escrever método para dar refresh na lista de tabelas para atualizar alterações feitas na estrutura sem que seja necessário reiniciar o webserver
        raise NotImplementedError