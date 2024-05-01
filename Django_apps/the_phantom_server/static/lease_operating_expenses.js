try {
    let tableBody = document.getElementById('lease-body');

    let backendData = document.getElementById('backendData').value;
    let objData = JSON.parse(backendData);
    let objValue = Object.entries(objData)
    objValue.map((item, index) => {
        tableBody.innerHTML += `<tr data-toggle="collapse" data-target="#lease${index}" class="accordion-toggle"><td>${item[0]}</td></tr>
                                <tr>
                                    <td colspan="5" class="hiddenRow p-1" style="background-color: ghostwhite;">
                                        <div  class="accordian-body collapse" id="lease${index}">
                                            <table class="w-100">
                                                <tbody id="bodyIndex${index}">
                                                    
                                                </tbody>
                                            </table>
                                        </div>
                                    </td>
                                </tr>`
        let innnerItem = document.getElementById(`bodyIndex${index}`)
        item[1].map((data) => {
            var formattedNumber = new Intl.NumberFormat('en-US', {
                style: 'decimal',
                minimumFractionDigits: 2,
                maximumFractionDigits: 2
            }).format(data.Amount);
            innnerItem.innerHTML += `
            <tr>
                <td>${data.Period}</td>
                <td>---</td>
                <td>${formattedNumber}</td>
                <td>---</td>
            </tr>`
        })
    })
} catch (error) {
    console.error("Error parsing JSON data:", error);
}