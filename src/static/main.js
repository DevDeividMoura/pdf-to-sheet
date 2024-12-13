function updateFileName() {
    const fileInput = document.getElementById('fileInput');
    const fileName = document.getElementById('fileName');
    if (fileInput.files.length > 0) {
        fileName.textContent = fileInput.files[0].name;
    } else {
        fileName.textContent = 'Nenhum arquivo selecionado...';
    }
}
function uploadFile() {
    const fileInput = document.getElementById('fileInput');
    if (fileInput.files.length > 0) {
        const file = fileInput.files[0];
        console.log('Selected file:', file);
        const reader = new FileReader();

        reader.onload = function (e) {
            const fileData = new Int8Array(e.target.result);
            console.log("Enviando PDF...");
            fetch('./api/v1/upload-pdf/', {
                method: 'POST',
                headers: {
                    'Accept': 'application/json',
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    file_data: [...fileData],
                    file_type: file.type,
                    file_name: file.name
                })
            }).then(response => response.json())
                .then(data => {
                    if (data.success) {
                        displayTable(data.data);
                    } else {
                        document.getElementById('result').textContent = 'Error: ' + data.message;
                    }
                })
                .catch(error => console.error('Error:', error));
        };

        reader.readAsArrayBuffer(file);
    } else {
        alert('Please select a file.');
    }
}
function displayTable(data) {
    const tableBox = document.getElementById('tableBox');
    tableBox.style.display = 'block'; // Mostra o container da tabela
    const resultDiv = document.getElementById('result');
    resultDiv.innerHTML = ''; // Limpa o conteúdo anterior

    // Cria a tabela
    const table = document.createElement('table');
    table.classList.add('table', 'is-striped', 'is-hoverable', 'is-fullwidth');

    // Cria os cabeçalhos da tabela
    const headers = ['Data', 'Posto', 'Total', 'Placa', 'Odômetro'];
    const thead = document.createElement('thead');
    const headerRow = document.createElement('tr');
    headers.forEach(headerText => {
        const th = document.createElement('th');
        th.appendChild(document.createTextNode(headerText));
        headerRow.appendChild(th);
    });
    thead.appendChild(headerRow);
    table.appendChild(thead);

    // Cria o corpo da tabela
    const tbody = document.createElement('tbody');
    data.forEach(item => {
        const row = document.createElement('tr');
        headers.forEach(header => {
            const cell = document.createElement('td');
            cell.appendChild(document.createTextNode(item[header] || ''));
            row.appendChild(cell);
        });
        tbody.appendChild(row);
    });
    table.appendChild(tbody);

    resultDiv.appendChild(table); // Adiciona a tabela ao container

    // Adiciona os botões de exportação
    const exportButtons = document.createElement('p');
    exportButtons.classList.add('buttons');

    const excelButton = document.createElement('button');
    excelButton.classList.add('button', 'is-success');
    excelButton.setAttribute('onclick', 'exportToExcel()');
    excelButton.setAttribute('title', 'Exportar para Excel');
    excelButton.innerHTML = `
        <span class="icon">
            <i class="fas fa-file-excel"></i>
        </span>
    `;

    const csvButton = document.createElement('button');
    csvButton.classList.add('button', 'is-success');
    csvButton.setAttribute('onclick', 'exportToCSV()');
    csvButton.setAttribute('title', 'Exportar para CSV');
    csvButton.innerHTML = `
        <span class="icon">
            <i class="fa-solid fa-file-csv"></i>
        </span>
    `;

    exportButtons.appendChild(excelButton);
    exportButtons.appendChild(csvButton);

    resultDiv.appendChild(exportButtons); // Adiciona os botões ao container
}

function exportToExcel() {
    // Verifica se a tabela existe
    const table = document.querySelector("#result table");
    if (!table) {
        alert("Nenhuma tabela encontrada para exportar!");
        return;
    }

    // Converte a tabela para um worksheet
    const workbook = XLSX.utils.book_new();
    const worksheet = XLSX.utils.table_to_sheet(table);

    // Adiciona o worksheet ao workbook
    XLSX.utils.book_append_sheet(workbook, worksheet, "Sheet1");

    // Salva o arquivo
    XLSX.writeFile(workbook, "tabela.xlsx");
}

function exportToCSV() {
    // Verifica se a tabela existe
    const table = document.querySelector("#result table");
    if (!table) {
        alert("Nenhuma tabela encontrada para exportar!");
        return;
    }

    // Extrai os dados da tabela
    let csvContent = "";
    const rows = table.querySelectorAll("tr");
    rows.forEach(row => {
        const cols = row.querySelectorAll("th, td");
        const rowContent = Array.from(cols)
            .map(col => `"${col.textContent.trim()}"`) // Escapa o conteúdo com aspas
            .join(",");
        csvContent += rowContent + "\n";
    });

    // Cria um arquivo Blob para download
    const blob = new Blob([csvContent], { type: "text/csv;charset=utf-8;" });
    const link = document.createElement("a");
    link.href = URL.createObjectURL(blob);
    link.download = "tabela.csv";

    // Adiciona ao DOM e simula o clique
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
}

