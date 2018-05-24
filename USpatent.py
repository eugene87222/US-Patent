import warnings
warnings.filterwarnings('ignore')

import os
from bs4 import BeautifulSoup
import DownloadHtml
import ParseHtml
import GetAbstract

def process_fields(field1, field2):
    OptionDict = {}
    file = open('FieldList.txt', 'r')
    for line in file:
        op = line.split(',')
        OptionDict[op[0].rstrip().lstrip()] = op[1].rstrip().lstrip()
    return OptionDict[field1], OptionDict[field2]

def process_BooleanOp(BooleanOp):
    if BooleanOp == 'ANDNOT':
        return 'NOT'
    else:
        return BooleanOp

def process_patents(term1, field1, term2, field2, BooleanOp, switch_DOWNLOAD, switch_PARSE, switch_TXT):
    if BooleanOp == '':
        BooleanOp = 'AND'
    if field1 == '':
        field1 = 'All Fields'
    if field2 == '':
        field2 = 'All Fields'

    print ('Term1: '+term1+' with field: '+field1)
    print (BooleanOp)
    print ('Term2: '+term2+' with field: '+field2)
    
    BooleanOp = process_BooleanOp(BooleanOp)
    field1, field2 = process_fields(field1, field2)

    if switch_DOWNLOAD:
        DownloadHtml.download_html(term1, field1, term2, field2, BooleanOp)
    
    if switch_PARSE:
        folder = term1+'_AND_'+term2
        files = os.listdir(folder+'/html')

        CPC_dict = dict()
        IPC_dict = dict()
        
        countries = list()
        patentNos = list()
        dates = list()
        titles = list()
        abstracts = list()
        applicants = list()
        CPCs = list()
        IPCs = list()

        for file in files:
            html = BeautifulSoup(open(folder +'/html/'+file, 'r'))

            country, patentNo, date, title, abstract, applicant, CPC, IPC = ParseHtml.parse_html(html)

            countries.append(country)
            patentNos.append(patentNo)
            dates.append(date)
            titles.append(title)
            abstracts.append(abstract)
            if not len(applicant):
                applicants.append('None')
            else:
                applicants.append('; '.join([i for i in applicant]))
            CPCs.append("; ".join([i for i in CPC]))
            IPCs.append("; ".join([i for i in IPC]))

            for i in CPC:
                if i in CPC_dict:
                    CPC_dict[i] += 1
                else:
                    CPC_dict[i] = 1

            for i in IPC:
                if i in IPC_dict:
                    IPC_dict[i] += 1
                else:
                    IPC_dict[i] = 1
            
        ParseHtml.PatentInfo2excel(folder, countries, patentNos, dates, titles, abstracts, applicants, CPCs, IPCs)
        # CPC2excel(folder, list(CPC_dict.keys()))
        # IPC2excel(folder, list(IPC_dict.keys()))
        ParseHtml.Statistic2excel(folder, IPC_dict, CPC_dict)

    if switch_TXT:
        folder = term1+'_AND_'+term2
        if not os.path.exists(folder+'/txt'):
            os.makedirs(folder+'/txt')
        GetAbstract.get_A_C_D(folder)