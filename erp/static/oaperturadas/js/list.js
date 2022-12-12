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
            {"data": "cod_eac"},
            {"data": "orden"},
            {"data": "nomb_cliente"},
            {"data": "referencia"},
            {"data": "mercaderia"},
            {"data": "nave"},
            {"data": "cod_alm"},
            {"data": "vcto_alm"},
            {"data": "fch_sobrstadia"},
            {"data": "status_ultimo"},
        ],
        columnDefs: [
            {
                targets: [-1],
                class: 'text-center',
                render: function (data, type, row) {
                    let nuevostatus = row.status_ultimo[0].toUpperCase() + row.status_ultimo.slice(1).toLowerCase();
                    return (row.fch_status.bold() + ': ' + nuevostatus);
                }
            },
            {
                targets: [0],
                class: 'text-center',
                render: function (data, type, row) {
                    return '<a href="/erp/oaperturadas/edit/' + row.id + '/">'+ data +'</a>';
                }
            },
            {
                targets: [1],
                class: 'text-center',
                render: function (data, type, row) {
                    aniox = new Date().getFullYear()
                    mesxx = new Date().getMonth() +1
                    diax = new Date().getDate()
                    fechacompletahoy = aniox + '-' + mesxx + '-' + diax
                    fechaInicio = new Date(row.fch_apertura).getTime();
                    fechaFin    = new Date(fechacompletahoy).getTime();

                    diff = fechaFin - fechaInicio;
                    return ''+ diff/(1000*60*60*24) + ' Dias' + '<br>' + row.cod_eac +'';
                }
            },
           {
                targets: [2],
                class: 'text-center',
                render: function (data, type, row) {
                    if (row.tipo_carga == 'CTN') {
                        return (row.orden.bold() + '<br>' + row.aduana + '*' + row.regimen + '<br>' + 'ctn:20:' + row.ctn20 + ' ' + '40:' + row.ctn40);
                    }else{
                        return (row.orden.bold() + '<br>' + row.aduana + '*' + row.regimen + '<br>' + 'S/Tipo carga');
                    }

                }
            },
            {
                targets: [6],
                class: 'text-center',
                render: function (data, type, row) {
                    return (row.nave + '<br>' + row.fch_eta);
                }
            }
        ],
        initComplete: function (settings, json) {

        }
    });
});