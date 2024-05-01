
window.onload = function () {
    // Get all toggle-rows
    let rows = document.querySelectorAll('.toggle-row');

    // Attach event listener to each row
    for (let i = 0; i < rows.length; i++) {
        rows[i].addEventListener('click', function () {
            toggleRow(this.id);
        });
    }

    // Function to toggle row visibility
    function toggleRow(rowId) {
        let row = document.getElementById(rowId);
        // get next element node - the hidden row
        let nextRow = row.nextElementSibling;
        // get previous element node - the row above
        let previousRow = row.previousElementSibling;

        if (!nextRow.className.includes("hidden") && !previousRow.className.includes("hidden")) {
            console.error("both following and previous rows are not hidden");
            return;
        }

        function toggleDisplay(row) {
            if (row.style.display === 'none' || row.style.display === '') {
                row.style.display = 'table-row';
                row.querySelector('.toggle-btn').innerText = '-';
            } else {
                row.style.display = 'none';
                row.querySelector('.toggle-btn').innerText = '+';
            }
        }

        // Toggle next row
        if (nextRow.className.includes("hidden")) {
            toggleDisplay(nextRow);
        }

        // Toggle previous row
        if (previousRow && previousRow.className.includes("hidden")) {
            toggleDisplay(previousRow);
        }
    }
};


let seconds = 2; // wherever you get this value from
let countdownElement = document.getElementById('countdown');
let docRunCountDownElement = document.getElementById('docruncountdown');
let DocCompressCountDownElement = document.getElementById('doccompresscountdown');
let DocWaterCountDownElement = document.getElementById('docwatercountdown');
let DocWellTestsCountDownElement = document.getElementById('docwelltestscountdown');
let ModemCountDownElement = document.getElementById('modemcountdown');
let DeviceCountDownElement = document.getElementById('devicecountdown');
let TagCountDownElement = document.getElementById('tagcountdown');
let deviceInputCountDownElement = document.getElementById('deviceInputCountDown');

let interval = countdownElement && Number.isInteger(seconds) && setInterval(function () {
    countdownElement.textContent = --seconds;
    if (seconds <= 0) {
        clearInterval(interval);
        try {
            window.location.href = "gas_meter";
        } catch (e) {
            console.error("Failed to redirect: ", e);
        }
    }
}, 1000);

let docRunCountDownElementInterval = docRunCountDownElement && Number.isInteger(seconds) && setInterval(function () {
    docRunCountDownElement.textContent = --seconds;
    if (seconds <= 0) {
        clearInterval(docRunCountDownElementInterval);
        try {
            window.location.href = "doc_run_tickets";
        } catch (e) {
            console.error("Failed to redirect: ", e);
        }
    }
}, 1000);

let DocCompressCountDownElementInterval = DocCompressCountDownElement && Number.isInteger(seconds) && setInterval(function () {
    DocCompressCountDownElement.textContent = --seconds;
    if (seconds <= 0) {
        clearInterval(DocCompressCountDownElementInterval);
        try {
            window.location.href = "doc_compressor";
        } catch (e) {
            console.error("Failed to redirect: ", e);
        }
    }
}, 1000);

let DocWaterCountDownElementInterval = DocWaterCountDownElement && Number.isInteger(seconds) && setInterval(function () {
    DocWaterCountDownElement.textContent = --seconds;
    if (seconds <= 0) {
        clearInterval(DocWaterCountDownElementInterval);
        try {
            window.location.href = "doc_water_disposition";
        } catch (e) {
            console.error("Failed to redirect: ", e);
        }
    }
}, 1000);

let DocWellTestsCountDownElementInterval = DocWellTestsCountDownElement && Number.isInteger(seconds) && setInterval(function () {
    DocWellTestsCountDownElement.textContent = --seconds;
    if (seconds <= 0) {
        clearInterval(DocWellTestsCountDownElementInterval);
        try {
            window.location.href = "doc_well_tests";
        } catch (e) {
            console.error("Failed to redirect: ", e);
        }
    }
}, 1000);

let ModemCountDownElementElementInterval = ModemCountDownElement && Number.isInteger(seconds) && setInterval(function () {
    ModemCountDownElement.textContent = --seconds;
    if (seconds <= 0) {
        clearInterval(ModemCountDownElementElementInterval);
        try {
            window.location.href = "create_modem";
        } catch (e) {
            console.error("Failed to redirect: ", e);
        }
    }
}, 1000);

let DeviceCountDownElementInterval = DeviceCountDownElement && Number.isInteger(seconds) && setInterval(function () {
    DeviceCountDownElement.textContent = --seconds;
    if (seconds <= 0) {
        clearInterval(DeviceCountDownElementInterval);
        try {
            window.location.href = "create_device";
        } catch (e) {
            console.error("Failed to redirect: ", e);
        }
    }
}, 1000);

let TagCountDownElementInterval = TagCountDownElement && Number.isInteger(seconds) && setInterval(function () {
    TagCountDownElement.textContent = --seconds;
    if (seconds <= 0) {
        clearInterval(TagCountDownElementInterval);
        try {
            window.location.href = "create_tag";
        } catch (e) {
            console.error("Failed to redirect: ", e);
        }
    }
}, 1000);

let deviceInputCountDownElementInterval = deviceInputCountDownElement && Number.isInteger(seconds) && setInterval(function () {
    deviceInputCountDownElement.textContent = --seconds;
    if (seconds <= 0) {
        clearInterval(deviceInputCountDownElementInterval);
        try {
            window.location.href = "create_device_input";
        } catch (e) {
            console.error("Failed to redirect: ", e);
        }
    }
}, 1000);




function toggleActive(sectionId) {
    const sections = ['section1', 'section2', 'section3', 'section4'];
    const selectedTab = document.getElementById('tab' + sectionId.slice(-1));

    sections.forEach(section => {
        const tab = document.getElementById('tab' + section.slice(-1));
        if (section === sectionId) {
            tab.classList.add('d-flex');
            tab.classList.remove('d-none');
        } else {
            tab.classList.remove('d-flex');
            tab.classList.add('d-none');
        }
    });

    const navLinks = document.querySelectorAll('.nav-link');
    navLinks.forEach(link => {
        if (link.id === sectionId) {
            link.classList.add('active');
        } else {
            link.classList.remove('active');
        }
    });
}

function setupTableRowSelection() {
    // Select all table rows with the 'selectable-row' class
    $('.selectable-row').click(function () {
        // Remove 'selected' class from siblings
        $(this).addClass('selected').siblings().removeClass('selected');

        // Get data from the 'Fire' column of the selected row
        var fireColumnData = $(this).find('td:eq(2)').text(); // Adjust the index as needed

        // Log or display the 'fire' column data
        console.log('Fire Column Data:', fireColumnData);

        // If you want to use the data elsewhere or display it in some way, do so here
        // Example: $('#someElement').text(fireColumnData);
    });
}

// Call the function when the document is ready
$(document).ready(function () {
    setupTableRowSelection();
});

// var closeOpenEye = {
//     'close': `<span class="glyphicon glyphicon-eye-open"><svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-eye" viewBox="0 0 16 16">
//     <path d="M16 8s-3-5.5-8-5.5S0 8 0 8s3 5.5 8 5.5S16 8 16 8M1.173 8a13 13 0 0 1 1.66-2.043C4.12 4.668 5.88 3.5 8 3.5s3.879 1.168 5.168 2.457A13 13 0 0 1 14.828 8q-.086.13-.195.288c-.335.48-.83 1.12-1.465 1.755C11.879 11.332 10.119 12.5 8 12.5s-3.879-1.168-5.168-2.457A13 13 0 0 1 1.172 8z"/>
//     <path d="M8 5.5a2.5 2.5 0 1 0 0 5 2.5 2.5 0 0 0 0-5M4.5 8a3.5 3.5 0 1 1 7 0 3.5 3.5 0 0 1-7 0"/>
//   </svg></span>`,
//     'open': `<span class="glyphicon glyphicon-eye-open"><svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-eye-slash" viewBox="0 0 16 16">
//   <path d="M13.359 11.238C15.06 9.72 16 8 16 8s-3-5.5-8-5.5a7 7 0 0 0-2.79.588l.77.771A6 6 0 0 1 8 3.5c2.12 0 3.879 1.168 5.168 2.457A13 13 0 0 1 14.828 8q-.086.13-.195.288c-.335.48-.83 1.12-1.465 1.755q-.247.248-.517.486z"/>
//   <path d="M11.297 9.176a3.5 3.5 0 0 0-4.474-4.474l.823.823a2.5 2.5 0 0 1 2.829 2.829zm-2.943 1.299.822.822a3.5 3.5 0 0 1-4.474-4.474l.823.823a2.5 2.5 0 0 0 2.829 2.829"/>
//   <path d="M3.35 5.47q-.27.24-.518.487A13 13 0 0 0 1.172 8l.195.288c.335.48.83 1.12 1.465 1.755C4.121 11.332 5.881 12.5 8 12.5c.716 0 1.39-.133 2.02-.36l.77.772A7 7 0 0 1 8 13.5C3 13.5 0 8 0 8s.939-1.721 2.641-3.238l.708.709zm10.296 8.884-12-12 .708-.708 12 12z"/>
// </svg></span>`
// }
var closeOpenEye = {
    'close': `<span class="glyphicon glyphicon-eye-open" style="font: 30px bold;">-</span>`,
    'open': `<span class="glyphicon glyphicon-eye-open" style="font: 30px bold;">+</span>`
}

function showHideGasBtnEye() {
    const gasSalesBtn = document.getElementById('gasSalesBtn');
    if (gasSalesBtn.classList.contains('eye-open')) {
        gasSalesBtn.classList.remove('eye-open')
        gasSalesBtn.innerHTML = ''
        gasSalesBtn.innerHTML = closeOpenEye.open;
    } else {
        gasSalesBtn.classList.add('eye-open')
        gasSalesBtn.innerHTML = ''
        gasSalesBtn.innerHTML = closeOpenEye.close;
    }
}



function showHideOilAndCondensateBtnEye() {
    const oilAndCondensateBtn = document.getElementById('oilAndCondensateBtn');
    if (oilAndCondensateBtn.classList.contains('eye-open')) {
        oilAndCondensateBtn.classList.remove('eye-open')
        oilAndCondensateBtn.innerHTML = ''
        oilAndCondensateBtn.innerHTML = closeOpenEye.open;

    } else {
        oilAndCondensateBtn.classList.add('eye-open')
        oilAndCondensateBtn.innerHTML = ''
        oilAndCondensateBtn.innerHTML = closeOpenEye.close;
    }
}

function showHideNaturalGasLiquidsBtn() {
    const naturalGasLiquidsBtn = document.getElementById('naturalGasLiquidsBtn');
    if (naturalGasLiquidsBtn.classList.contains('eye-open')) {
        naturalGasLiquidsBtn.classList.remove('eye-open')
        naturalGasLiquidsBtn.innerHTML = ''
        naturalGasLiquidsBtn.innerHTML = closeOpenEye.open;

    } else {
        naturalGasLiquidsBtn.classList.add('eye-open')
        naturalGasLiquidsBtn.innerHTML = ''
        naturalGasLiquidsBtn.innerHTML = closeOpenEye.close;
    }
}

function showHideExpensesBtn() {
    const ExpensesBtn = document.getElementById('ExpensesBtn');
    if (ExpensesBtn.classList.contains('eye-open')) {
        ExpensesBtn.classList.remove('eye-open')
        ExpensesBtn.innerHTML = ''
        ExpensesBtn.innerHTML = closeOpenEye.open;

    } else {
        ExpensesBtn.classList.add('eye-open')
        ExpensesBtn.innerHTML = ''
        ExpensesBtn.innerHTML = closeOpenEye.close;
    }
}

function showHideLeaseOperatingExpensesBtn() {
    const leaseOperatingExpensesBtn = document.getElementById('leaseOperatingExpensesBtn');
    if (leaseOperatingExpensesBtn.classList.contains('eye-open')) {
        leaseOperatingExpensesBtn.classList.remove('eye-open')
        leaseOperatingExpensesBtn.innerHTML = ''
        leaseOperatingExpensesBtn.innerHTML = closeOpenEye.open;

    } else {
        leaseOperatingExpensesBtn.classList.add('eye-open')
        leaseOperatingExpensesBtn.innerHTML = ''
        leaseOperatingExpensesBtn.innerHTML = closeOpenEye.close;
    }
}


function showHideTotalSalesRevenueBtn() {
    const totalSalesRevenueBtn = document.getElementById('totalSalesRevenueBtn');
    if (totalSalesRevenueBtn.classList.contains('eye-open')) {
        totalSalesRevenueBtn.classList.remove('eye-open')
        totalSalesRevenueBtn.innerHTML = ''
        totalSalesRevenueBtn.innerHTML = closeOpenEye.open;

    } else {
        totalSalesRevenueBtn.classList.add('eye-open')
        totalSalesRevenueBtn.innerHTML = ''
        totalSalesRevenueBtn.innerHTML = closeOpenEye.close;
    }
}



function showHideGathringAndMarketingBtn() {
    const gathringAndMarketingBtn = document.getElementById('gathringAndMarketingBtn');
    if (gathringAndMarketingBtn.classList.contains('eye-open')) {
        gathringAndMarketingBtn.classList.remove('eye-open')
        gathringAndMarketingBtn.innerHTML = ''
        gathringAndMarketingBtn.innerHTML = closeOpenEye.open;

    } else {
        gathringAndMarketingBtn.classList.add('eye-open')
        gathringAndMarketingBtn.innerHTML = ''
        gathringAndMarketingBtn.innerHTML = closeOpenEye.close;
    }
}

function showHideLeaseOperatingExpensesBtn() {
    const leaseOperatingExpensesBtn = document.getElementById('leaseOperatingExpensesBtn');
    if (leaseOperatingExpensesBtn.classList.contains('eye-open')) {
        leaseOperatingExpensesBtn.classList.remove('eye-open')
        leaseOperatingExpensesBtn.innerHTML = ''
        leaseOperatingExpensesBtn.innerHTML = closeOpenEye.open;

    } else {
        leaseOperatingExpensesBtn.classList.add('eye-open')
        leaseOperatingExpensesBtn.innerHTML = ''
        leaseOperatingExpensesBtn.innerHTML = closeOpenEye.close;
    }
}

document.addEventListener('DOMContentLoaded', (event) => {
    const gasSalesBtn = document.getElementById('gasSalesBtn');
    const oilAndCondensateBtn = document.getElementById('oilAndCondensateBtn');
    const naturalGasLiquidsBtn = document.getElementById('naturalGasLiquidsBtn');
    const gathringAndMarketingBtn = document.getElementById('gathringAndMarketingBtn');
    const leaseOperatingExpensesBtn = document.getElementById('leaseOperatingExpensesBtn');
    const totalSalesRevenueBtn = document.getElementById('totalSalesRevenueBtn');


    if (gasSalesBtn.classList.contains('eye-open')) {
        gasSalesBtn.classList.remove('eye-open')
    } else if (oilAndCondensateBtn.classList.contains('eye-open')) {
        oilAndCondensateBtn.classList.add('eye-open')
    } else if (!oilAndCondensateBtn.classList.contains('eye-open')) {
        oilAndCondensateBtn.classList.remove('eye-open')
    } else if (naturalGasLiquidsBtn.classList.contains('eye-open')) {
        naturalGasLiquidsBtn.classList.remove('eye-open')
    } else if (!naturalGasLiquidsBtn.classList.contains('eye-open')) {
        naturalGasLiquidsBtn.classList.add('eye-open')
    } else if (totalSalesRevenueBtn.classList.contains('eye-open')) {
        totalSalesRevenueBtn.classList.remove('eye-open')
    } else if (!totalSalesRevenueBtn.classList.contains('eye-open')) {
        totalSalesRevenueBtn.classList.add('eye-open')
    } else if (gathringAndMarketingBtn.classList.contains('eye-open')) {
        gathringAndMarketingBtn.classList.remove('eye-open')
    } else if (!gathringAndMarketingBtn.classList.contains('eye-open')) {
        gathringAndMarketingBtn.classList.add('eye-open')
    }else if (leaseOperatingExpensesBtn.classList.contains('eye-open')) {
        leaseOperatingExpensesBtn.classList.remove('eye-open')
    } else if (!leaseOperatingExpensesBtn.classList.contains('eye-open')) {
        leaseOperatingExpensesBtn.classList.add('eye-open')
    }
    else {
        gasSalesBtn.classList.add('eye-open')
    }

    gasSalesBtn.innerHTML = closeOpenEye.open;
    oilAndCondensateBtn.innerHTML = closeOpenEye.open;
    naturalGasLiquidsBtn.innerHTML = closeOpenEye.open;
    leaseOperatingExpensesBtn.innerHTML = closeOpenEye.open;
    totalSalesRevenueBtn.innerHTML = closeOpenEye.open;
    gathringAndMarketingBtn.innerHTML = closeOpenEye.open;
})

$(document).ready(function () {
    $('#range').on('change', function(){
        $('#finance').submit()
    })
    $('#period').on('change', function(){
        $('#finance').submit()
    })
    $('#well_view').on('change', function(){
        $('#well_view_form').submit()
    })
})


function history_back() {
    window.history.back();
} 


function storeData(id) {
    let storeDataForm = document.getElementById('storeDataForm');
    let store_id = document.getElementById('store_id')
    store_id.value = id;    
    storeDataForm.submit()
    $('#store_zip_data').modal('show');
}

function ptrFormSubmit(id) {
    let ptrid = document.getElementById("ptrid");
    ptrid.value = id
    $('#ptridform').submit()
}