import ruamel.yaml

yaml = ruamel.yaml.YAML()

currency_codes=["ADP","AED","AFA","AFN","ALK","ALL","AMD","ANG","AOA","AOK","AON","AOR","ARA","ARP","ARS","ARY","ATS","AUD","AWG","AYM","AZM","AZN","BAD","BAM","BBD","BDT","BEC","BEF","BEL","BGJ","BGK","BGL","BGN","BHD","BIF","BMD","BND","BOB","BOP","BOV","BRB","BRC","BRE","BRL","BRN","BRR","BSD","BTN","BUK","BWP","BYB","BYN","BYR","BZD","CAD","CDF","CHC","CHE","CHF","CHW","CLF","CLP","CNY","COP","COU","CRC","CSD","CSJ","CSK","CUC","CUP","CVE","CYP","CZK","DDM","DEM","DJF","DKK","DOP","DZD","ECS","ECV","EEK","EGP","ERN","ESA","ESB","ESP","ETB","EUR","FIM","FJD","FKP","FRF","GBP","GEK","GEL","GHC","GHP","GHS","GIP","GMD","GNE","GNF","GNS","GQE","GRD","GTQ","GWE","GWP","GYD","HKD","HNL","HRD","HRK","HTG","HUF","IDR","IEP","ILP","ILR","ILS","INR","IQD","IRR","ISJ","ISK","ITL","JMD","JOD","JPY","KES","KGS","KHR","KMF","KPW","KRW","KWD","KYD","KZT","LAJ","LAK","LBP","LKR","LRD","LSL","LSM","LTL","LTT","LUC","LUF","LUL","LVL","LVR","LYD","MAD","MDL","MGA","MGF","MKD","MLF","MMK","MNT","MOP","MRO","MRU","MTL","MTP","MUR","MVQ","MVR","MWK","MXN","MXP","MXV","MYR","MZE","MZM","MZN","NAD","NGN","NIC","NIO","NLG","NOK","NPR","NZD","OMR","PAB","PEH","PEI","PEN","PES","PGK","PHP","PKR","PLN","PLZ","PTE","PYG","QAR","RHD","ROK","ROL","RON","RSD","RUB","RUR","RWF","SAR","SBD","SCR","SDD","SDG","SDP","SEK","SGD","SHP","SIT","SKK","SLL","SOS","SRD","SRG","SSP","STD","STN","SUR","SVC","SYP","SZL","THB","TJR","TJS","TMM","TMT","TND","TOP","TPE","TRL","TRY","TTD","TWD","TZS","UAH","UAK","UGS","UGW","UGX","USD","USN","USS","UYI","UYN","UYP","UYU","UYW","UZS","VEB","VEF","VES","VNC","VND","VUV","WST","XAF","XAG","XAU","XBA","XBB","XBC","XBD","XCD","XDR","XEU","XFO","XFU","XOF","XPD","XPF","XPT","XRE","XSU","XTS","XUA","XXX","YDD","YER","YUD","YUM","YUN","ZAL","ZAR","ZMK","ZMW","ZRN","ZRZ","ZWC","ZWD","ZWL","ZWN","ZWR"]
country_codes=["AD","AE","AF","AG","AI","AL","AM","AO","AQ","AR","AS","AT","AU","AW","AX","AZ","BA","BB","BD","BE","BF","BG","BH","BI","BJ","BL","BM","BN","BO","BQ","BR","BS","BT","BV","BW","BY","BZ","CA","CC","CD","CF","CG","CH","CI","CK","CL","CM","CN","CO","CR","CU","CV","CW","CX","CY","CZ","DE","DJ","DK","DM","DO","DZ","EC","EE","EG","EH","ER","ES","ET","FI","FJ","FK","FM","FO","FR","GA","GB","GD","GE","GF","GG","GH","GI","GL","GM","GN","GP","GQ","GR","GS","GT","GU","GW","GY","HK","HM","HN","HR","HT","HU","ID","IE","IL","IM","IN","IO","IQ","IR","IS","IT","JE","JM","JO","JP","KE","KG","KH","KI","KM","KN","KP","KR","KW","KY","KZ","LA","LB","LC","LI","LK","LR","LS","LT","LU","LV","LY","MA","MC","MD","ME","MF","MG","MH","MK","ML","MM","MN","MO","MP","MQ","MR","MS","MT","MU","MV","MW","MX","MY","MZ","NA","NC","NE","NF","NG","NI","NL","NO","NP","NR","NU","NZ","OM","PA","PE","PF","PG","PH","PK","PL","PM","PN","PR","PS","PT","PW","PY","QA","RE","RO","RS","RU","RW","SA","SB","SC","SD","SE","SG","SH","SI","SJ","SK","SL","SM","SN","SO","SR","SS","ST","SV","SX","SY","SZ","TC","TD","TF","TG","TH","TJ","TK","TL","TM","TN","TO","TR","TT","TV","TW","TZ","UA","UG","UM","US","UY","UZ","VA","VC","VE","VG","VI","VN","VU","WF","WS","YE","YT","ZA","ZM","ZW"]

import gspread
import numpy as np
import pandas as pd
import yaml
from pandas import DataFrame
from copy import deepcopy

SCOPES = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
SPREADSHEET_ID = '1PwTjGAAmqX1Aa2W1qvxSLbJ9j_v79Reg0zej496oRb4'



def load_gsheet_as_df(worksheet_name):
    google_account = gspread.oauth()
    sheet = google_account.open_by_key(SPREADSHEET_ID)
    worksheet = sheet.worksheet(worksheet_name)
    df = read_gsheet(worksheet=worksheet)
    return df


def read_gsheet(worksheet: gspread.Worksheet) -> pd.DataFrame:
    if not worksheet:
        return pd.DataFrame()
    df = pd.DataFrame(worksheet.get_all_records(head=1), dtype=str)
    print(df.columns)
    return df

def get_lovs(lov):
    accepted_values = []
    if lov:
        if lov.strip().startswith("ISO-3166"):
            accepted_values = deepcopy(country_codes)
        elif lov.strip().startswith("ISO-4217"):
            accepted_values = deepcopy(currency_codes)
        else:
            accepted_values = lov.split(",")
    return accepted_values


def build_dbt_schema(df, schema_file_location):
    tgroups = df.groupby("TABLE")
    models = []
    for tname, group in tgroups:
        if tname not in ('correspondent_account', 'lob_master', 'operational_risk_data', 'operational_risk_loss_data',
                         'ops_risk_customer_complaints', 'ops_risk_litigation_cases', 'repo_data', 'investments_data',
                         'casa_ax'):
            continue
        else:
            columns = []
            pk_columns = []
            for index, row in group.iterrows():
                if row.COLUMN == 'reporting_date':
                    continue

                is_not_null = row.MANDATORY == 'Y'
                schema = row.SCHEMA.lower()
                database = row.DATABASE.lower()
                has_lov = row.LOV
                if row.CONSTRAINT == 'PK':
                    pk_columns.append(row.COLUMN)

                col_tests = []
                if (is_not_null or has_lov):

                    accepted_values = get_lovs(row.LOV)

                    if has_lov and is_not_null:
                        col_tests.append("not_null")
                        # col_tests.append({"accepted_values": {"values": accepted_values}})
                        formatted_av = [f"'{av}'" for av in accepted_values]
                        col_tests.append({"accepted_values_as_set": {"values": f"({','.join(formatted_av)})"}})
                    elif has_lov:
                        formatted_av = [f"'{av}'" for av in accepted_values]
                        col_tests.append({"accepted_values_or_null": {"values": f"({','.join(formatted_av)})"}})
                    elif is_not_null:
                        col_tests.append("not_null")

                # DataType checks
                #             if row.DATATYPE=='DATE':
                #                 col_tests.append({"dbt_expectations.expect_column_values_to_be_in_type_list": {"column_type_list": ["date", "datetime"]}})
                #             elif row.DATATYPE=='NUMBER':
                #                 col_tests.append({"dbt_expectations.expect_column_values_to_be_in_type_list": {"column_type_list": ["number"]}})

                if col_tests:
                    columns.append({
                        "name": row.COLUMN,
                        "tests": col_tests
                    })

        ttests = [
            {
                "dbt_utils.unique_combination_of_columns": {
                    "combination_of_columns": [pk_columns] + ['_source_updated_at']
                }
            }

        ]

        if columns:
            tschema = {
                "name": f"{database}__{schema}__{tname}",
                "description": f"{database}__{schema}__{tname}",
                "columns": columns,
                "ttests": ttests
            }

            models.append(tschema)


    schema = {
        "version": 2,
        "models": models
    }

    with open(schema_file_location, 'w') as file:
        yaml.dump(schema, file)


if __name__ == '__main__':
    reg_df = load_gsheet_as_df('Reg Quality checks')
    ldm_df = load_gsheet_as_df('LDM Quality checks')

    reg_df = reg_df.query("R1=='YES'")
    reg_df["TABLE"] = reg_df["TABLE"].str.lower()
    reg_df["COLUMN"] = reg_df["COLUMN"].str.lower()

    ldm_df = ldm_df.query("R1=='YES'")
    ldm_df["TABLE"] = ldm_df["TABLE"].str.lower()
    ldm_df["COLUMN"] = ldm_df["COLUMN"].str.lower()
    #build_dbt_schema(reg_df,"/Users/arun.manivannan/projects/digibank-transformer/models/gold/axiom/gold__axiom__schema.yml")
    build_dbt_schema(ldm_df, "/Users/arun.manivannan/projects/digibank-transformer/models/silver/onboarding_master/silver__onboarding_master__schema.yml")