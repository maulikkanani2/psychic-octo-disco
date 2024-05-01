function exportPDF() {
    const url = window.location.href;
    const param = url.split('?')[1]
    if (param) {
        const docdate = url.split('?')[1].split('&')[0].split('=')
        const tankid = url.split('?')[1].split('&')[1].split('=')
        const apiUrl = `/download/pdf?${docdate[0]}=${docdate[1]}&${tankid[0]}=${tankid[1]}`
        window.open(apiUrl)
    }else{
        const apiUrl = '/download/pdf/'
        window.open(apiUrl, "_blank")
    }
}

function exportWellHeadPDF() {
    const url = window.location.href;
    const param = url.split('?')[1]
    if (param) {
        const timestamp = url.split('?')[1].split('&')[0].split('=')
        const device_name = url.split('?')[1].split('&')[1].split('=')
        const apiUrl = `/download/well_head_pdf?${timestamp[0]}=${timestamp[1]}&${device_name[0]}=${device_name[1]}`
        window.open(apiUrl)
    }else{
        const apiUrl = '/download/well_head_pdf/'
        window.open(apiUrl, "_blank")
    }
}

function exportWellHeadCSV() {
    const url = window.location.href;
    const param = url.split('?')[1]
    if (param) {
        const timestamp = url.split('?')[1].split('&')[0].split('=')
        const device_name = url.split('?')[1].split('&')[1].split('=')
        const apiUrl = `/download/well_head_csv?${timestamp[0]}=${timestamp[1]}&${device_name[0]}=${device_name[1]}`
        window.open(apiUrl)
    }else{
        const apiUrl = '/download/well_head_csv/';
        window.open(apiUrl, "_blank")
    }
}


function exportCSV() {
    const url = window.location.href;
    const param = url.split('?')[1]
    if (param) {
        const docdate = url.split('?')[1].split('&')[0].split('=')
        const tankid = url.split('?')[1].split('&')[1].split('=')
        const apiUrl = `/download/csv?${docdate[0]}=${docdate[1]}&${tankid[0]}=${tankid[1]}`
        window.open(apiUrl)
    }else{
        const apiUrl = '/download/csv/';
        window.open(apiUrl, "_blank")
    }
}

function gasMeterPDF() {
    const url = window.location.href;
    const param = url.split('?')[1]
    if (param) {
        const apiUrl = '/download/gas_meter_pdf?'+param
        window.open(apiUrl, "_blank")
    }else{
        const apiUrl = '/download/gas_meter_pdf/'
        window.open(apiUrl, "_blank")
    }
}

function gasMeterCsv() {
    const url = window.location.href;
    const param = url.split('?')[1]
    if (param) {
        const apiUrl = '/download/gas_meter_csv?'+param
        window.open(apiUrl, "_blank")
    }else{
        const apiUrl = '/download/gas_meter_csv/'
        window.open(apiUrl, "_blank")
    }
}

function docCompressorPDF() {
    const url = window.location.href;
    const param = url.split('?')[1]
    if (param) {
        const apiUrl = '/download/doc_compressor_pdf?'+param
        window.open(apiUrl, "_blank")
    }else{
        const apiUrl = '/download/doc_compressor_pdf/'
        window.open(apiUrl, "_blank")
    }
}

function docCompressorCSV() {
    const url = window.location.href;
    const param = url.split('?')[1]
    if (param) {
        const apiUrl = '/download/doc_compressor_csv?'+param
        window.open(apiUrl, "_blank")
    }else{
        const apiUrl = '/download/doc_compressor_csv/'
        window.open(apiUrl, "_blank")
    }
}

function docRunTicketPDF() {
    const url = window.location.href;
    const param = url.split('?')[1]
    if (param) {
        const apiUrl = '/download/doc_run_tickets_pdf?'+param
        window.open(apiUrl, "_blank")
    }else{
        const apiUrl = '/download/doc_run_tickets_pdf/'
        window.open(apiUrl, "_blank")
    }
}

function docRunTicketCSV() {
    const url = window.location.href;
    const param = url.split('?')[1]
    if (param) {
        const apiUrl = '/download/doc_run_ticket_csv?'+param
        window.open(apiUrl, "_blank")
    }else{
        const apiUrl = '/download/doc_run_ticket_csv/'
        window.open(apiUrl, "_blank")
    }
}

function docWaterDispositionCSV() {
    const url = window.location.href;
    const param = url.split('?')[1]
    if (param) {
        const apiUrl = '/download/doc_water_disposition_csv?'+param
        window.open(apiUrl, "_blank")
    }else{
        const apiUrl = '/download/doc_water_disposition_csv/'
        window.open(apiUrl, "_blank")
    }
}

function docWellTestsCSV() {
    const url = window.location.href;
    const param = url.split('?')[1]
    if (param) {
        const apiUrl = '/download/doc_well_tests_csv?'+param
        window.open(apiUrl, "_blank")
    }else{
        const apiUrl = '/download/doc_well_tests_csv/'
        window.open(apiUrl, "_blank")
    }
}

function gasSalesPdf() {
    const url = window.location.href;
    const param = url.split('?')[1]
    if (param) {
        const apiUrl = "exports/gas_sales_pdf?"+param
        window.open(apiUrl, "_blank")
    }else{
        const apiUrl = "exports/gas_sales_pdf/"
        window.open(apiUrl, "_blank")
    }
}

function gasSalesCsv() {
    const url = window.location.href;
    const param = url.split('?')[1]
    if (param) {
        const apiUrl = "exports/gas_sales_csv?"+param
        window.open(apiUrl, "_blank")    
    }else{
        const apiUrl = "exports/gas_sales_csv/"
        window.open(apiUrl, "_blank")
    }
}

function oilAndCondensatePdf() {
    const url = window.location.href;
    const param = url.split('?')[1]
    if (param) {
        const apiUrl = "exports/oil_and_condensate_pdf?"+param
        window.open(apiUrl, "_blank")        
    }else{
        const apiUrl = "exports/oil_and_condensate_pdf/"
        window.open(apiUrl, "_blank")
    }
}

function oilAndCondensateCsv() {
    const url = window.location.href;
    const param = url.split('?')[1]
    if (param) {
        const apiUrl = "exports/oil_and_condensate_csv?"+param
        window.open(apiUrl, "_blank")    
    }else{
        const apiUrl = "exports/oil_and_condensate_csv/"
        window.open(apiUrl, "_blank")    
    }
}

function naturalGasLiquidsSalesPdf() {
    const url = window.location.href;
    const param = url.split('?')[1]
    if (param) {
        const apiUrl = "exports/natural_gas_liquids_sales_pdf?"+param
        window.open(apiUrl, "_blank")    
    }else{
        const apiUrl = "exports/natural_gas_liquids_sales_pdf/"
        window.open(apiUrl, "_blank")
    }
}

function naturalGasLiquidsSalesCsv() {
    const url = window.location.href;
    const param = url.split('?')[1]
    if (param) {
        const apiUrl = "exports/natural_gas_liquids_sales_csv?"+param
        window.open(apiUrl, "_blank")    
    }else{
        const apiUrl = "exports/natural_gas_liquids_sales_csv/"
        window.open(apiUrl, "_blank")
    }
}

function leaseOperatingExpensesPdf() {
    const url = window.location.href;
    const param = url.split('?')[1]
    if (param) {
        const apiUrl = "exports/lease_operating_expenses_pdf?"+param
        window.open(apiUrl, "_blank")
    }else{
        const apiUrl = "exports/lease_operating_expenses_pdf/"
        window.open(apiUrl, "_blank")
    }
}

function leaseOperatingExpensesCsv() {
    const url = window.location.href;
    const param = url.split('?')[1]
    if (param) {
        const apiUrl = "exports/lease_operating_expenses_csv?" + param
        window.open(apiUrl, "_blank")
    } else {
        const apiUrl = "exports/lease_operating_expenses_csv/"
        window.open(apiUrl, "_blank")
    }
}

function expensesPdf() {
    const url = window.location.href;
    const param = url.split('?')[1]
    if (param) {
        const apiUrl = "exports/expenses_pdf?" + param
        window.open(apiUrl, "_blank")
    } else {
        const apiUrl = "exports/expenses_pdf/"
        window.open(apiUrl, "_blank")
    }
}

function expensesCsv() {
    const url = window.location.href;
    const param = url.split('?')[1]
    if (param) {
        const apiUrl = "exports/expenses_csv?" + param
        window.open(apiUrl, "_blank")
    } else {
        const apiUrl = "exports/expenses_csv/"
        window.open(apiUrl, "_blank")
    }
}

function accountsPdf() {
    const url = window.location.href;
    const param = url.split('?')[1]
    if (param) {
        const apiUrl = "exports/accounts_pdf?" + param
        window.open(apiUrl, "_blank")
    } else {
        const apiUrl = "exports/accounts_pdf/"
        window.open(apiUrl, "_blank")
    }
}

function accountsCsv() {
    const url = window.location.href;
    const param = url.split('?')[1]
    if (param) {
        const apiUrl = "exports/accounts_csv?" + param
        window.open(apiUrl, "_blank")
    } else {
        const apiUrl = "exports/accounts_csv/"
        window.open(apiUrl, "_blank")
    }
}

const csvBtn = document.getElementById('csv');
const pdfBtn = document.getElementById('pdf');