from django.urls import path

from .views import (
    contracting_concrete_new,
    contracting_concrete_delete,
    contracting_excavation_new,
    contracting_excavation_delete,
    contracting_facing_new,
    contracting_facing_delete,
    contracting_gas_new,
    contracting_gas_delete,
    contracting_nailing_new,
    contracting_nailing_delete,
    contracting_painting_new,
    contracting_painting_delete,
    contracting_piling_new,
    contracting_piling_delete,
    contracting_plastering_new,
    contracting_plastering_delete,
    contracting_plumbing_new,
    contracting_plumbing_delete,
    contracting_scaffolding_new,
    contracting_scaffolding_delete,
    contracting_steel_new,
    contracting_steel_delete,
    contracting_tiling_new,
    contracting_tiling_delete,
    contracting_truss_new,
    contracting_truss_delete,
    contracting_wall_new,
    contracting_wall_delete,
    contracting_waterproofing_new,
    contracting_waterproofing_delete,
    contracting_wiring_new,
    contracting_wiring_delete,
    engineering_new,
    engineering_delete,
    insurance_employee_new,
    insurance_employee_delete,
    insurance_quality_new,
    insurance_quality_delete,
    insurance_third_party_new,
    insurance_third_party_delete,
    material_aac_new,
    material_aac_delete,
    material_beam_new,
    material_beam_delete,
    material_clay_new,
    material_clay_delete,
    material_concrete_block_new,
    material_concrete_block_delete,
    material_concrete_new,
    material_concrete_delete,
    material_frame_new,
    material_frame_delete,
    material_grains_new,
    material_grains_delete,
    material_polystyrene_new,
    material_polystyrene_delete,
)

app_name = "services"

# Material Services urlpatterns
urlpatterns = [
    path("material/aac/new/", material_aac_new, name="material_aac_new"),
    path("material/aac/<pk>/delete/", material_aac_delete, name="material_aac_delete"),
    path("material/beam/new/", material_beam_new, name="material_beam_new"),
    path("material/beam/<pk>/delete/", material_beam_delete, name="material_beam_delete"),
    path("material/clay/new/", material_clay_new, name="material_clay_new"),
    path("material/clay/<pk>/delete/", material_clay_delete, name="material_clay_delete"),
    path("material/concrete/new/", material_concrete_new, name="material_concrete_new"),
    path("material/concrete/<pk>/delete/", material_concrete_delete, name="material_concrete_delete"),
    path(
        "material/concrete-block/new/",
        material_concrete_block_new,
        name="material_concrete_block_new",
    ),
    path("material/concrete-block/<pk>/delete/", material_concrete_block_delete, name="material_concrete_block_delete"),
    path("material/frame/new/", material_frame_new, name="material_frame_new"),
    path("material/frame/<pk>/delete/", material_frame_delete, name="material_frame_delete"),
    path("material/grains/new/", material_grains_new, name="material_grains_new"),
    path("material/grains/<pk>/delete/", material_grains_delete, name="material_grains_delete"),
    path(
        "material/polystyrene/new/",
        material_polystyrene_new,
        name="material_polystyrene_new",
    ),
    path("material/polystyrene/<pk>/delete/", material_polystyrene_delete, name="material_polystyrene_delete"),
]

# Contracting Services urlpatterns
urlpatterns += [
    path(
        "contracting/concrete/new/",
        contracting_concrete_new,
        name="contracting_concrete_new",
    ),
    path(
        "contracting/concrete/<pk>/delete/", contracting_concrete_delete, name="contracting_concrete_delete"
    ),
    path(
        "contracting/excavation/new/",
        contracting_excavation_new,
        name="contracting_excavation_new",
    ),
    path(
        "contracting/excavation/<pk>/delete/", contracting_excavation_delete, name="contracting_excavation_delete"
    ),
    path(
        "contracting/facing/new/",
        contracting_facing_new,
        name="contracting_facing_new",
    ),
    path(
        "contracting/facing/<pk>/delete/", contracting_facing_delete, name="contracting_facing_delete"
    ),
    path(
        "contracting/gas/new/",
        contracting_gas_new,
        name="contracting_gas_new",
    ),
    path(
        "contracting/gas/<pk>/delete/", contracting_gas_delete, name="contracting_gas_delete"
    ),
    path(
        "contracting/nailing/new/",
        contracting_nailing_new,
        name="contracting_nailing_new",
    ),
    path(
        "contracting/nailing/<pk>/delete/", contracting_nailing_delete, name="contracting_nailing_delete",
    ),
    path(
        "contracting/painting/new/",
        contracting_painting_new,
        name="contracting_painting_new",
    ),
    path(
        "contracting/painting/<pk>/delete/", contracting_painting_delete, name="contracting_painting_delete"
    ),
    path(
        "contracting/piling/new/",
        contracting_piling_new,
        name="contracting_piling_new",
    ),
    path(
        "contracting/piling/<pk>/delete/", contracting_piling_delete, name="contracting_piling_delete"
    ),
    path(
        "contracting/plastering/new/",
        contracting_plastering_new,
        name="contracting_plastering_new",
    ),
    path(
        "contracting/plastering/<pk>/delete/", contracting_plastering_delete, name="contracting_plastering_delete"
    ),
    path(
        "contracting/plumbing/new/",
        contracting_plumbing_new,
        name="contracting_plumbing_new",
    ),
    path(
        "contracting/plumbing/<pk>/delete/", contracting_plumbing_delete, name="contracting_plumbing_delete"
    ),
    path(
        "contracting/scaffolding/new/",
        contracting_scaffolding_new,
        name="contracting_scaffolding_new",
    ),
    path(
        "contracting/scaffolding/<pk>/delete/", contracting_scaffolding_delete, name="contracting_scaffolding_delete",
    ),
    path(
        "contracting/steel/new/",
        contracting_steel_new,
        name="contracting_steel_new",
    ),
    path(
        "contracting/steel/<pk>/delete/", contracting_steel_delete, name="contracting_steel_delete"
    ),
    path(
        "contracting/tiling/new/",
        contracting_tiling_new,
        name="contracting_tiling_new",
    ),
    path(
        "contracting/tiling/<pk>/delete/", contracting_tiling_delete, name="contracting_tiling_delete"
    ),
    path(
        "contracting/truss/new/",
        contracting_truss_new,
        name="contracting_truss_new",
    ),
    path(
        "contracting/truss/<pk>/delete/", contracting_truss_delete, name="contracting_truss_delete"
    ),
    path(
        "contracting/wall/new/",
        contracting_wall_new,
        name="contracting_wall_new",
    ),
    path(
        "contracting/wall/<pk>/delete/", contracting_wall_delete, name="contracting_wall_delete"
    ),
    path(
        "contracting/waterproofing/new/",
        contracting_waterproofing_new,
        name="contracting_waterproofing_new",
    ),
    path(
        "contracting/waterproofing/<pk>/delete/",
        contracting_waterproofing_delete,
        name="contracting_waterproofing_delete",
    ),
    path(
        "contracting/wiring/new/",
        contracting_wiring_new,
        name="contracting_wiring_new",
    ),
    path(
        "contracting/wiring/<pk>/delete/", contracting_wiring_delete, name="contracting_wiring_delete"
    ),
]

# Engineering Services urlpatterns
urlpatterns += [
    path("engineering/new/", engineering_new, name="engineering_new"),
    path("engineering/<pk>/delete/", engineering_delete, name="engineering_delete"),
]

# Insurance Services urlpatterns
urlpatterns += [
    path("insurance/quality/new/", insurance_quality_new, name="insurance_quality_new"),
    path(
        "insurance/quality/<pk>/delete/",
        insurance_quality_delete,
        name="insurance_quality_delete",
    ),
    path(
        "insurance/employee/new/", insurance_employee_new, name="insurance_employee_new"
    ),
    path(
        "insurance/employee/<pk>/delete/",
        insurance_employee_delete,
        name="insurance_employee_delete",
    ),
    path(
        "insurance/third-party/new/",
        insurance_third_party_new,
        name="insurance_third_party_new",
    ),
    path(
        "insurance/third-party/<pk>/delete/",
        insurance_third_party_delete,
        name="insurance_third_party_delete",
    ),
]
