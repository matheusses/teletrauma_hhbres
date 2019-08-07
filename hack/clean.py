import pandas
import math


def dropUnwantedColumns(df):
    columnsToDrop = [
        'ID',
        'ATENDIMENTO',
        'PACIENTE',
        'DS_SERVICO',
        'UNIDADE',
        'MOTIVO_ALTA',
        #'AGRUPA_ALTA', # Indica se foi óbito
        'STATUS',
        'DATA_ALTA_E_ATEN',
        '....CID',
        '....DS_CID',
        '....GRUPO_CID',
        '....CASOS_PREENCHIDOS',
        '....QT_PRESTADOR',
        '....DS_SGRU_CID',
        '....DS_GRU_CID',
        'PRESTADOR',
        'NR_CEP',
        'CD_UF',
        'CEP_INIT',
        'CD_CID_INT',
        'Procedencia.BUSCA_PROCEDENCIA',
        'table_procedencia.DS_LOC_PROCED',
        'table_procedencia.SN_PROCEDENCIA_EXTERNA',
        'DS_TIPO_INTERNACAO',
        'CD_TIP_ACOM',
        'DS_TIP_ACOM',
    ]
    df.drop(columnsToDrop, inplace=True, axis=1)
    return df


def addSectionAndSubregion(df):
    # Adiciona setor e subregião com base no CEP
    df['SETOR'] = df['CEP_INIT'].apply(lambda x: math.ceil(x/10))
    df['SUBREGIAO'] = df['CEP_INIT'].apply(lambda x: math.ceil(x/100))
    return df


def removeProc(dataframe):
    # Remove linhas com base na Procedência
    procToRemove = ["DOMICILIO", "DEMANDA ESPONTANEA", "POLICIA", "OUTRAS PROCEDENCIAS", "TRABALHO", "VIA URBANA", "...", "...."]
    dataframe = dataframe[dataframe['Procedencia'].isin(procToRemove) == False]
    return dataframe


def removeCities(dataframe):
    # Remove linhas com base na Cidade
    citiesToKeep = ["SAO PAULO"]
    return dataframe[dataframe['CIDADE'].isin(citiesToKeep)]


def fixAgeGroup(df):
    # Corrige valores de Faixa Etária
    df.loc[df['FX_ETARIA'] == '5-Sep', 'FX_ETARIA'] = '05 - 09'
    df.loc[df['FX_ETARIA'] == 'Oct-14', 'FX_ETARIA'] = '10 - 14'
    df.loc[df['FX_ETARIA'] == '0 - 04', 'FX_ETARIA'] = '00 - 04'
    df.loc[df['FX_ETARIA'] == '80 -', 'FX_ETARIA'] = '80 - 99'
    return df


def cleanIt(df):
    df = addSectionAndSubregion(df)
    df = dropUnwantedColumns(df)
    df = removeProc(df)
    df = removeCities(df)
    df = fixAgeGroup(df)

    return df



