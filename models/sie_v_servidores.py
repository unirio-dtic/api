# DESC_SITUACAO = [aposentado, ativo, instituidor de pensao]

#  View or materialized query table "DBSM.V_SERVIDORES" cannot be used because it has been marked inoperative.
# Field("NOME_FUNCIONARIO", "string", length=80),
dbSie.define_table( "V_SERVIDORES",
                    Field("MATR_EXTERNA", "integer"),
                    Field("ID_CONTRATO_RH", "integer"),
                    Field("SEXO", "string", length=1),
                    Field("MATR_EXTERNA", "integer"),
                    Field("DT_ADMISSAO_SP", "date"),
                    Field("DT_ADMISSAO_INST", "date"),
                    Field("DT_ADMISSAO_CARGO", "date"),
                    Field("DT_DEMISSAO", "date"),
                    Field("DT_APOSENTADORIA", "date"),
                    Field("DT_POSSE", "date"),
                    Field("DT_NOMEACAO", "date"),
                    Field("ID_CARGO", "date"),
                    Field("DESC_CARGO", "string"),
                    Field("DESC_LOT_EXERCICIO", "string"),
                    Field("DESC_LOT_OFICIAL", "string"),
                    Field("ESTADO_CIVIL_ITEM", "integer"),
                    Field("DESC_ESTADO_CIVIL", "string"),
                    Field("DESC_FORMAINGRESSO", "string"),
                    Field("DESC_REG_JURIDICO", "string"),
                    Field("SITUACAO_ITEM", "integer"),
                    Field("DESC_SITUACAO", "string"),
                    Field("DESC_JORNADA_TRAB", "string"),
                    Field("ETNIA_ITEM", "integer"),
                    Field("DESC_ETNIA", "string"),
                    migrate=False
                     )