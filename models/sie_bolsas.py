dbSie.define_table("BOLSAS",
                   Field('ID_BOLSA', 'integer'),
                   Field('COD_BOLSA', 'string'),
                   Field('DESCR_BOLSA', 'string'),
                   Field('IND_PERCENTUAL', 'string'),
                   Field('VL_BOLSA', 'float'),
                   Field('PC_BOLSA', 'float'),
                   Field('QT_BOLSA', 'integer'),
                   Field('VL_LIMITE', 'float'),
                   Field('VAGAS_OFERECIDAS', 'integer'),
                   Field('TIPO_BOLSISTA', 'string'),
                   Field('SITUACAO_BOLSA', 'string'),
                   Field('IND_RELATORIO', 'string'),
                   Field('ID_SIMULACAO_INC', 'integer'),
                   Field('ID_SIMULACAO_EXC', 'integer'),
                   Field('ID_ENT_EXTERNA', 'integer'),
                   Field('OBS_BOLSA', 'clob'),
                   Field('COD_OPERADOR', 'integer'),
                   Field('DT_ALTERACAO', 'date'),
                   Field('HR_ALTERACAO', 'time'),
                   Field('CONCORRENCIA', 'integer'),
                   Field('IND_FREQUENCIA', 'string'),
                   Field('GRUPO_TAB', 'integer'),
                   Field('GRUPO_ITEM', 'integer'),
                   Field('TIPO_BOLSA_TAB', 'integer'),
                   Field('TIPO_BOLSA_ITEM', 'integer'),
                   Field('ID_CAD_CONV_PGTO', 'integer'),
                   Field('IND_UNICA_OCOR', 'string'),
                   Field('VAGAS_OCUPADAS', 'integer'),
                   Field('ENDERECO_FISICO', 'string'),
                   primarykey=['ID_BOLSA'],
                   migrate=False
)