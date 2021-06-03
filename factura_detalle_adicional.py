import os
import xml.etree.ElementTree as ET
import pandas as pd

path = 'D:/Escritorio/ORTIZ CORNEJO JOSE PATRICIO/2021/Archivo Digital/05 Mayo/Factura xml/'
row = {}
df = pd.DataFrame(row)
with os.scandir(path) as ficheros:
    for fichero in ficheros:
        name_file = fichero.name
        tree = ET.parse(path+name_file)
        root = tree.getroot()
        for child in root:
            if child.tag =='comprobante':
                comprobante = child.text
                c = ET.fromstring(comprobante)
                for x in range(len(c)):
                    if c[x].tag == 'infoTributaria':
                        for i in c[x]:
                            if i.tag == 'secuencial':
                                row['1'] = i.text
                    if c[x].tag == 'infoAdicional':
                        for index, i in enumerate(c[x]):#(i.attrib)
                            row[index+2] = i.text
                        df = df.append(row, ignore_index=True)
                        print(df)
df.to_excel(path+'resumen_info.xlsx', index=False, sheet_name='Resumen')