# -*- coding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _
from mezzanine.conf import register_setting

register_setting(
    name="YANDEX_METRICA_ID",
    label=_("Yandex.Metrica ID"),
    editable=True,
    description=_("Yandex.Metrica ID (http://metrica.yandex.com/)"),
    default="",
)

register_setting(
    name="YANDEX_METRICA__WEBVISOR",
    label=_("WebVisor"),
    editable=True,
    description=_("Recording and analysis of site user behavior."),
    default=False,
)

register_setting(
    name="YANDEX_METRICA__CLICKMAP",
    label=_("Click map"),
    editable=True,
    description=_("Statistics used to create the \"Click map\" report."),
    default=True,
)

register_setting(
    name="YANDEX_METRICA__TRACK_LINKS",
    label=_("External links, file downloads and \"Share\" button report"),
    editable=True,
    description=_("Statistics for links to external resources, file downloads and \"Share\" buttons."),
    default=True,
)

register_setting(
    name="YANDEX_METRICA__ACCURATE_TRACK_BOUNCE",
    label=_("Accurate bounce rate"),
    editable=True,
    description=_("Any visit where a user only views one page and spends less than 15 seconds on it will be counted as a bounce."),
    default=True,
)

register_setting(
    name="YANDEX_METRICA__UT",
    label=_("Stop automatic page indexing"),
    editable=True,
    default=False,
)

register_setting(
    name="YANDEX_METRICA__ASYNC",
    label=_("Asynchronous code"),
    editable=True,
    description=_("Asynchronous code does not block or influence the loading speed of your site."),
    default=True,
)

register_setting(
    name="YANDEX_METRICA__TRACK_HASH",
    label=_("Hash tracking in the browser address window"),
    editable=True,
    description=_("Option applied to AJAX sites."),
    default=False,
)


register_setting(
    name="YANDEX_METRICA__XML_SITE",
    label=_("For XML sites"),
    editable=True,
    #description=_("The nonscript element should not be used in XML documents (Content‑Type:application/xhtml+xml)."),
    default=False,
)

register_setting(
    name="YANDEX_METRICA__INFORMER_ALLOWED",
    label=_("Informer"),
    editable=True,
    default=False,
    )

register_setting(
    name="YANDEX_METRICA__INFORMER_SIZE",
    label=_("Informer size"),
    editable=True,
    default='88x31',
    choices=[[x, x] for x in ['88x31', '80x31', '80x15',]]
)

register_setting(
    name="YANDEX_METRICA__INFORMER_DATA_TYPE",
    label=_("Informer data type"),
    editable=True,
    default='pageviews',
    choices=(
        ('pageviews', _('Page views')),
        ('visits', _('Visits')),
        ('uniques', _('Visitors')),
    )
)

register_setting(
    name="YANDEX_METRICA__INFORMER_DATA_TYPE",
    label=_("Informer data type"),
    editable=True,
    default='pageviews',
    choices=(
        ('pageviews', _('Page views')),
        ('visits', _('Visits')),
        ('uniques', _('Visitors')),
    )
)

register_setting(
    name="YANDEX_METRICA__INFORMER_COLOR",
    label=_("Informer color"),
    editable=True,
    default='EFEFEF',
)

register_setting(
    name="YANDEX_METRICA__INFORMER_GRADIENT",
    label=_("Informer background gradient"),
    editable=True,
    default=True,
)

register_setting(
    name="YANDEX_METRICA__INFORMER_FONT_COLOR",
    label=_("Informer font color"),
    editable=True,
    default=0,
    choices=(
        (0, _('Black')),
        (1, _('White')),
    )
)

register_setting(
    name="YANDEX_METRICA__INFORMER_ARROW_COLOR",
    label=_("Informer arrow color"),
    editable=True,
    default=1,
    choices=(
        (1, _('Color')),
        (0, _('Monochrome')),
    )
)

register_setting(
    name="YANDEX_METRICA__INFORMER_TYPE",
    label=_("Informer type"),
    editable=True,
    default=1,
    choices=(
        (0, _('Simple')),
        (1, _('Advanced')),
    )
)

register_setting(
    name="TEMPLATE_ACCESSIBLE_SETTINGS",
    default=(
        "YANDEX_METRICA_ID",
        "YANDEX_METRICA__WEBVISOR",
        "YANDEX_METRICA__CLICKMAP",
        "YANDEX_METRICA__TRACK_LINKS",
        "YANDEX_METRICA__ACCURATE_TRACK_BOUNCE",
        "YANDEX_METRICA__UT",
        "YANDEX_METRICA__ASYNC",
        "YANDEX_METRICA__TRACK_HASH",
        "YANDEX_METRICA__XML_SITE",
        "YANDEX_METRICA__INFORMER_ALLOWED",
        "YANDEX_METRICA__INFORMER_SIZE",
        "YANDEX_METRICA__INFORMER_DATA_TYPE",
        "YANDEX_METRICA__INFORMER_COLOR",
        "YANDEX_METRICA__INFORMER_GRADIENT",
        "YANDEX_METRICA__INFORMER_FONT_COLOR",
        "YANDEX_METRICA__INFORMER_ARROW_COLOR",
        "YANDEX_METRICA__INFORMER_TYPE",
    ),
    append=True
)