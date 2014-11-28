# -*- coding: utf-8 -*-

dbSie.define_table("DOCUMENTOS",
                   Field("ID_DOCUMENTO", "integer"),
                   Field("ID_TIPO_DOC", "integer"),
                   Field("NUM_PROCESSO", "string"),
                   Field("ID_PROCEDENCIA", "integer"),
                   Field("TIPO_PROCEDENCIA", "string"),
                   Field("ID_INTERESSADO", "integer"),
                   Field("TIPO_INTERESSADO", "string"),
                   Field("SITUACAO_ATUAL", "integer"),
                   Field("ID_PROPRIETARIO", "integer"),
                   Field("TIPO_PROPRIETARIO", "integer"),
                   Field("ID_DOC_AGREGADO", "integer"),
                   Field("ID_TIPO_DOC_AGREG", "integer"),
                   Field("TIPO_AGREGACAO", "string"),
                   Field("DT_AGREGACAO", "date"),
                   Field("ID_ASSUNTO", "integer"),
                   Field("RESUMO_ASSUNTO", "string"),
                   Field("DT_CRIACAO", "date"),
                   Field("HR_CRIACAO", "time"),
                   Field("DT_ARQUIVAMENTO", "date"),
                   Field("DT_LIMITE_ARQ", "date"),
                   Field("ID_ESPACO", "integer"),
                   Field("ID_CRIADOR", "integer"),
                   Field("IND_ELIMINADO", "string"),
                   Field("IND_DEFERIDO", "string"),
                   Field("DOCUMENTO_ORIGEM", "string"),
                   Field("DT_DOC_ORIGEM", "date"),
                   Field("DT_RECEBIMENTO", "date"),
                   # Field("OBSERVACAO","CLOB"),
                   Field("COD_OPERADOR", "integer"),
                   Field("DT_ALTERACAO", "date"),
                   Field("HR_ALTERACAO", "time"),
                   Field("CONCORRENCIA", "integer"),
                   Field("TEMPO_ESTIMADO", "integer"),
                   Field("IND_AGENDAMENTO", "string"),
                   Field("IND_RESERVADO", "string"),
                   primarykey=["ID_DOCUMENTO"],
                   migrate=False)
