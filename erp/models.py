from django.db import models
from datetime import datetime
from django.forms import model_to_dict


from erp.choices import status_choices


class oaperturadas(models.Model):
    orden = models.CharField(max_length=50, verbose_name='orden', unique=True)
    aduana = models.CharField(max_length=10, verbose_name='aduana')
    regimen = models.CharField(max_length=10, verbose_name='regimen')
    tipo_despacho = models.CharField(max_length=10, verbose_name='tipo_despacho')
    cod_cliente = models.CharField(max_length=15, verbose_name='cod_cliente')
    nomb_cliente = models.CharField(max_length=800, verbose_name='nomb_cliente', null=True, blank=True)
    referencia = models.CharField(max_length=800, verbose_name='referencia', null=True, blank=True)
    mercaderia = models.CharField(max_length=500, verbose_name='mercaderia', null=True, blank=True)
    fch_apertura = models.DateField(default=datetime.now, verbose_name='fch_aperturada', null=True, blank=True)
    fch_eta = models.DateField(default=datetime.now, verbose_name='fch_eta', null=True, blank=True)
    nave = models.CharField(max_length=800, verbose_name='nave', null=True, blank=True)
    cod_alm = models.CharField(max_length=20, verbose_name='cod_alm', null=True, blank=True)
    vcto_alm = models.DateField(default=datetime.now, verbose_name='vcto_alm', null=True, blank=True)
    fch_sobrstadia = models.DateField(default=datetime.now, verbose_name='fch_sobrstadia', null=True, blank=True)
    dam = models.CharField(max_length=10, verbose_name='dam', null=True, blank=True)
    fch_dam = models.DateField(default=datetime.now, verbose_name='fch_dam', null=True, blank=True)
    fch_cancelacion = models.DateField(default=datetime.now, verbose_name='fch_cancelacion', null=True, blank=True)
    canal = models.CharField(max_length=5, verbose_name='canal', null=True, blank=True)
    cod_eac = models.CharField(max_length=10, verbose_name='cod_eac', null=True, blank=True)
    fch_retiro_eac = models.DateField(default=datetime.now, verbose_name='retiro_eac', null=True, blank=True)
    fch_entrega_eac = models.DateField(default=datetime.now, verbose_name='entrega_eac', null=True, blank=True)
    fch_retiro_opera = models.DateField(default=datetime.now, verbose_name='fch_retiro_opera', null=True, blank=True)
    fch_entrega_opera = models.DateField(default=datetime.now, verbose_name='fch_entrega_opera', null=True, blank=True)
    fch_culminado = models.DateField(default=datetime.now, verbose_name='fch_culminado', null=True, blank=True)
    fch_regularizado = models.DateField(default=datetime.now, verbose_name='fch_regularizado', null=True, blank=True)
    fch_facturado = models.DateField(default=datetime.now, verbose_name='fch_facturado', null=True, blank=True)
    cuadrilla = models.CharField(max_length=5, verbose_name='cuadrilla', null=True, blank=True)
    custodia = models.CharField(max_length=5, verbose_name='custodia', null=True, blank=True)
    tipo_carga = models.CharField(max_length=10, verbose_name='tipo_carga', null=True, blank=True)
    ctn20 = models.CharField(max_length=5, verbose_name='ctn20', null=True, blank=True)
    ctn40 = models.CharField(max_length=5, verbose_name='ctn40', null=True, blank=True)
    cant_bul = models.CharField(max_length=5, verbose_name='cant_bul', null=True, blank=True)
    kls_bruto = models.CharField(max_length=10, verbose_name='kls_bruto', null=True, blank=True)
    peligrosa = models.CharField(max_length=5, verbose_name='peligrosa', null=True, blank=True)
    cif = models.CharField(max_length=20, verbose_name='cif', null=True, blank=True)
    obs_prog_eac = models.CharField(max_length=800, verbose_name='obs_prog_eac', null=True, blank=True)
    permiso_opera = models.CharField(max_length=5, verbose_name='permiso_opera', null=True, blank=True)
    asume_pago = models.CharField(max_length=500, verbose_name='asume_pago', null=True, blank=True)
    alm_devol = models.CharField(max_length=10, verbose_name='alm_devol', null=True, blank=True)
    facturar_a = models.CharField(max_length=500, verbose_name='facturar_a', null=True, blank=True)
    fch_levante = models.DateField(default=datetime.now, verbose_name='fch_levante', null=True, blank=True)
    fch_solicitud_vb = models.DateField(default=datetime.now, verbose_name='solicitud_vb', null=True, blank=True)
    vb_concluido = models.DateField(default=datetime.now, verbose_name='vb_concluido', null=True, blank=True)
    n_volante = models.CharField(max_length=50, verbose_name='n_volante', null=True, blank=True)
    fch_volante = models.DateField(default=datetime.now, verbose_name='fch_volante', null=True, blank=True)
    fch_status = models.DateField(default=datetime.now, verbose_name='fch_status', null=True, blank=True)
    status_ultimo = models.CharField(max_length=500, verbose_name='status_ultimo', null=True, blank=True)
    estado = models.CharField(max_length=5, verbose_name='estado', null=True, blank=True)
    kpi = models.CharField(max_length=20, verbose_name='kpi', null=True, blank=True)
    doc_faltante = models.CharField(max_length=800, verbose_name='doc_faltante', null=True, blank=True)

    def __str__(self):
        return self.orden

    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        verbose_name = "OS_Aperturada"
        verbose_name_plural = "OS_Aperturadas"
        ordering = ['-id']


class depositos(models.Model):
    cod_deposito = models.CharField(max_length=10, verbose_name='cod_deposito', unique=True)
    nomb_deposito = models.CharField(max_length=500, verbose_name='nomb_deposito')
    alias_deposito = models.CharField(max_length=500, verbose_name='alias_deposito', null=True, blank=True)
    idestado = models.CharField(max_length=11, choices=status_choices, default='active', verbose_name='idestado')

    def __str__(self):
        return self.cod_deposito

    def toJSON(self):
        item = model_to_dict(self)
        # en gender retorno el valor del display de mi choices.py
        item['idestado'] = {'id': self.idestado, 'name': self.get_idestado_display()}
        return item

    class Meta:
        verbose_name = 'Deposito'
        verbose_name_plural = 'Depositos'
        ordering = ['id']


class history_alm(models.Model):
    orden = models.CharField(max_length=50, verbose_name='orden')
    cod_alm = models.CharField(max_length=50, verbose_name='cod_alm')
    section = models.CharField(max_length=10, null=True, blank=True, verbose_name='section')
    user_reg = models.CharField(max_length=50, null=True, blank=True, verbose_name='user_reg')
    user_ip = models.CharField(max_length=100, null=True, blank=True, verbose_name='user_ip')
    mac_user = models.CharField(max_length=200, null=True, blank=True, verbose_name='mac_user')
    fecha = models.DateField(default=datetime.now, verbose_name='fecha')

    def __str__(self):
        return self.cod_alm

    def toJSON(self):
        item = model_to_dict(self)
        item['fecha'] = self.fecha.strftime('%Y-%m-%d')
        return item

    class Meta:
        verbose_name = 'Historial de Almacen'
        verbose_name_plural = 'Historial de Almacenes'
        ordering = ['id']


class history_eta(models.Model):
    orden = models.CharField(max_length=50, verbose_name='orden')
    fecha_eta = models.DateField(default=datetime.now, verbose_name='fecha_eta')
    planning = models.CharField(max_length=50, null=True, blank=True, verbose_name='planning')
    section = models.CharField(max_length=10, null=True, blank=True, verbose_name='section')
    user_reg = models.CharField(max_length=50, null=True, blank=True, verbose_name='user_reg')
    user_ip = models.CharField(max_length=100, null=True, blank=True, verbose_name='user_ip')
    mac_user = models.CharField(max_length=200, null=True, blank=True, verbose_name='mac_user')
    fecha = models.DateField(default=datetime.now, verbose_name='fecha')

    def __str__(self):
        return self.fecha_eta

    def toJSON(self):
        item = model_to_dict(self)
        item['fecha_eta'] = self.fecha_eta.strftime('%Y-%m-%d')
        item['fecha'] = self.fecha.strftime('%Y-%m-%d')
        return item

    class Meta:
        verbose_name = 'Historial ETA'
        verbose_name_plural = 'Historial ETA'
        ordering = ['id']


class history_nave(models.Model):
    orden = models.CharField(max_length=50, verbose_name='orden')
    nave = models.CharField(max_length=800, verbose_name='nave')
    section = models.CharField(max_length=10, null=True, blank=True, verbose_name='section')
    user_reg = models.CharField(max_length=50, null=True, blank=True, verbose_name='user_reg')
    user_ip = models.CharField(max_length=100, null=True, blank=True, verbose_name='user_ip')
    mac_user = models.CharField(max_length=200, null=True, blank=True, verbose_name='mac_user')
    fecha = models.DateField(default=datetime.now, verbose_name='fecha')

    def __str__(self):
        return self.nave

    def toJSON(self):
        item = model_to_dict(self)
        item['fecha'] = self.fecha.strftime('%Y-%m-%d')
        return item

    class Meta:
        verbose_name = 'Historial Nave'
        verbose_name_plural = 'Historial de Naves'
        ordering = ['id']


class history_sobrstadia(models.Model):
    orden = models.CharField(max_length=50, verbose_name='orden')
    fecha_sbrstadia = models.DateField(default=datetime.now, verbose_name='fecha_sbrstadia')
    planning = models.CharField(max_length=50, null=True, blank=True, verbose_name='planning')
    section = models.CharField(max_length=10, null=True, blank=True, verbose_name='section')
    user_reg = models.CharField(max_length=50, null=True, blank=True, verbose_name='user_reg')
    user_ip = models.CharField(max_length=100, null=True, blank=True, verbose_name='user_ip')
    mac_user = models.CharField(max_length=200, null=True, blank=True, verbose_name='mac_user')
    fecha = models.DateField(default=datetime.now, verbose_name='fecha')

    def __str__(self):
        return self.name

    def toJSON(self):
        item = model_to_dict(self)
        item['fecha_sbrstadia'] = self.fecha_sbrstadia.strftime('%Y-%m-%d')
        item['fecha'] = self.fecha.strftime('%Y-%m-%d')
        return item

    class Meta:
        verbose_name = 'Historial Sobreestadia'
        verbose_name_plural = 'Historial de Sobreestadias'
        ordering = ['id']



