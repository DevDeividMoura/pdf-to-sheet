import pandas as pd
from fastapi import HTTPException

from app.core.file_handler import get_text_from_pdf
from app.utils.date_utils import is_valid_date
from app.schemas.pdf_schema import PDFResponse


class PDFProcessor:
    def __init__(self):
        self.headers = [
            'Data', 'Dta.', 'Hr.', 'Produto', 'NF.', 'Nro.', 'Odômetro',
            'Média', 'Qtde.', 'Vlr. Unit.', 'Acrés.', 'Desc.', 'Total', 'ID Produto', 'Placa'
        ]
        self.car_map = {
            'QJN7446':'AMAROK (QJN-7446)',
            'RKW5F47': 'STRADA (RKW-5F47)',
            'QJO2119': 'STRADA (QJO-2119)',
            'MMM1294': 'STRADA (MMM-1294)',
            'RAG7458': 'SAVEIRO (RAG-7458)',
            'RDV4B25': 'SAVEIRO (RDV-4B25)',
            'RXK4G83': 'JIMNY (RXK-4G83)',
            'QII4435': 'SAVEIRO (QII-4435)',
        }

    async def process_pdf(self, file_stream):
        try:
            text = await get_text_from_pdf(file_stream)
            processed_data = self._process_pdf_text(text)
            
            return PDFResponse(
                success=True,
                message="Data extracted successfully",
                data=processed_data
            )
        
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    def _process_pdf_text(self, text: str):
        data_list = []
        lines = text.splitlines()
        parsed_lines = self._parse_lines(lines)
        
        for i, line in enumerate(parsed_lines):
            if 'Placa:' in line and 'Veículo:' in line:
                plate = line[1]
                for subsequent_line in parsed_lines[i+1:]:
                    if is_valid_date(subsequent_line[0]):
                        subsequent_line.append(plate)
                        data_list.append(subsequent_line)
                    else:
                        break

        return self._create_dataframe(data_list)

    def _parse_lines(self, lines):
        return [
            line.split(" ")[:3] + [" ".join(line.split(" ")[3:-10])] + line.split(" ")[-10:]
            for line in lines
        ]

    def _create_dataframe(self, data_list):
        df = pd.DataFrame(data_list, columns=self.headers)
        df.insert(df.columns.get_loc('Data') + 1, 'Posto', 'Kastelly')
        # df['Placa'] = df['Placa'].map(self.car_map)
        # Mapeando com checagem de existência na `car_map` e substituindo `NaN`
        df['Placa'] = df['Placa'].apply(lambda x: self.car_map.get(x, ''))
        selected_columns = ['Data', 'Posto', 'Total', 'Placa', 'Odômetro']
        return df[selected_columns].to_dict(orient='records')
