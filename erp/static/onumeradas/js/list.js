$(function () {
    $('#data').DataTable({
        responsive: true,
        autoWidth: false,
        destroy: true,
        deferRender: true,
        ajax: {
            url: window.location.pathname,
            type: 'POST',
            data: {
                'action': 'searchdata'
            },
            dataSrc: ""
        },
        columns: [
            {"data": "position"},
            {"data": "orden"},
            {"data": "cod_cliente"},
            {"data": "referencia"},
            {"data": "mercaderia"},
            {"data": "nave"},
            {"data": "fch_eta"},
            {"data": "cod_alm"},
            {"data": "vcto_alm"},
            {"data": "fch_sobrstadia"},
            {"data": "status_ultimo"},
        ],
        columnDefs: [
            {
                targets: [0],
                class: 'text-center',
                render: function (data, type, row) {
                    return '<a href="/erp/onumeradas/edit/' + row.id + '/">'+ data +'</a>';
                }
            },
           {
                targets: [1],
                class: 'text-center',
                render: function (data, type, row) {
                    return (row.orden + '<br>' + row.aduana + '*' + row.regimen + '*' + row.tipo_despacho);
                }
            }
        ],
        initComplete: function (settings, json) {

        }
    });
});