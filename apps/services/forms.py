from django import forms

from .models import (
    ContractingConcreteService,
    ContractingExcavationService,
    ContractingFacingService,
    ContractingGasService,
    ContractingNailingService,
    ContractingPaintingService,
    ContractingPilingService,
    ContractingPlasteringService,
    ContractingPlumbingService,
    ContractingScaffoldingService,
    ContractingSteelService,
    ContractingTilingService,
    ContractingTrussService,
    ContractingWallService,
    ContractingWaterproofingService,
    ContractingWiringService,
    EngineeringService,
    InsuranceEmployeesLiabilityService,
    InsuranceQualityService,
    InsuranceThirdPartyLiabilityService,
    MaterialAACService,
    MaterialBeamService,
    MaterialClayService,
    MaterialConcreteBlockService,
    MaterialConcreteService,
    MaterialFrameService,
    MaterialGrainsService,
    MaterialPolystyreneService,
)


class ServiceModelForm(forms.ModelForm):
    class Meta:
        exclude = (
            "project",
            "category",
        )


class MaterialAACServiceModelForm(ServiceModelForm):
    class Meta:
        model = MaterialAACService
        fields = [
            "required_quantity",
            "required_dimensions",
            "thickness",
            "height",
            "length",
            "custom_thickness",
            "custom_height",
            "custom_length",
            "transport",
            "palette",
            "glue",
            "extra_info",
        ]


class MaterialBeamServiceModelForm(ServiceModelForm):
    class Meta:
        model = MaterialBeamService
        fields = [
            "type",
            "implementation_area",
            "required_length",
            "required_quantity",
            "transport",
            "plan",
            "extra_info",
        ]


class MaterialClayServiceModelForm(ServiceModelForm):
    class Meta:
        model = MaterialClayService
        fields = [
            "required_quantity",
            "type",
            "simple_dimensions",
            "simple_thickness",
            "simple_height",
            "simple_length",
            "simple_custom_thickness",
            "simple_custom_height",
            "simple_custom_length",
            "foam_dimensions",
            "foam_thickness",
            "foam_height",
            "foam_length",
            "foam_custom_thickness",
            "foam_custom_height",
            "foam_custom_length",
            "transport",
            "extra_info",
        ]


class MaterialConcreteServiceModelForm(ServiceModelForm):
    class Meta:
        model = MaterialConcreteService
        fields = [
            "required_amount",
            "concreting_area",
            "story",
            "pump_type",
            "resistance",
            "required_slump",
            "extra_info",
        ]


class MaterialConcreteBlockServiceModelForm(ServiceModelForm):
    class Meta:
        model = MaterialConcreteBlockService
        fields = [
            "required_amount",
            "type",
            "concrete_dimensions",
            "concrete_thickness",
            "concrete_height",
            "concrete_length",
            "concrete_custom_thickness",
            "concrete_custom_height",
            "concrete_custom_length",
            "tuff_dimensions",
            "tuff_thickness",
            "tuff_height",
            "tuff_length",
            "tuff_custom_thickness",
            "tuff_custom_height",
            "tuff_custom_length",
            "transport",
            "extra_info",
        ]


class MaterialFrameServiceModelForm(ServiceModelForm):
    class Meta:
        model = MaterialFrameService
        fields = [
            "required_area",
            "required_length",
            "glass_type",
            "profile_type",
            "fitting_type",
            "plan",
            "extra_info",
        ]


class MaterialGrainsServiceModelForm(ServiceModelForm):
    class Meta:
        model = MaterialGrainsService
        fields = [
            "required_amount",
            "material_type",
            "sand_type",
            "gravel_type",
            "gravel_size",
            "extra_info",
        ]


class MaterialPolystyreneServiceModelForm(ServiceModelForm):
    class Meta:
        model = MaterialPolystyreneService
        fields = [
            "required_amount",
            "type",
            "required_dimensions",
            "thickness",
            "height",
            "length",
            "custom_thickness",
            "custom_height",
            "custom_length",
            "weight",
            "sheet_type",
            "particles_type",
            "transport",
            "extra_info",
        ]


class EngineeringServiceModelForm(ServiceModelForm):
    class Meta:
        model = EngineeringService
        fields = [
            "engineering_type",
            "total_stories",
            "building_type",
            "constructable_area",
            "infrastructure_area",
            "total_basements",
            "extra_info",
        ]


class ContractingConcreteServiceModelForm(ServiceModelForm):
    class Meta:
        model = ContractingConcreteService
        fields = [
            "foundation_type",
            "infrastructure_area",
            "ceiling_area",
            "ceiling_type",
            "total_ceilings",
            "total_basements",
            "columns_concreting",
            "plan",
            "start",
            "start",
            "extra_info",
        ]


class ContractingExcavationServiceModelForm(ServiceModelForm):
    class Meta:
        model = ContractingExcavationService
        fields = [
            "excavation_volume",
            "excavation_depth",
            "area_image",
            "start",
            "extra_info",
        ]


class ContractingFacingServiceModelForm(ServiceModelForm):
    class Meta:
        model = ContractingFacingService
        fields = [
            "type",
            "total_area",
            "opening_area",
            "facing_type",
            "custom_facing",
            "plan",
            "start",
            "extra_info",
        ]


class ContractingGasServiceModelForm(ServiceModelForm):
    class Meta:
        model = ContractingGasService
        fields = [
            "usecase",
            "total_suites",
            "average_area",
            "total_stories",
            "total_parkings",
            "plan",
            "start",
            "extra_info",
        ]


class ContractingNailingServiceModelForm(ServiceModelForm):
    class Meta:
        model = ContractingNailingService
        fields = [
            "total_area",
            "depth",
            "horizontal_distance",
            "vertical_distance",
            "shotcret",
            "highest_length",
            "lowest_length",
            "water_level",
            "soil_type",
            "area_image",
            "log",
            "plan",
            "start",
            "extra_info",
        ]


class ContractingPaintingServiceModelForm(ServiceModelForm):
    class Meta:
        model = ContractingPaintingService
        fields = [
            "color_type",
            "total_area",
            "start",
            "extra_info",
        ]


class ContractingPilingServiceModelForm(ServiceModelForm):
    class Meta:
        model = ContractingPilingService
        fields = [
            "total_piles",
            "pile_diameter",
            "pile_depth",
            "bell_diameter",
            "water_level",
            "material_type",
            "log",
            "area_image",
            "plan",
            "start",
            "extra_info",
        ]


class ContractingPlasteringServiceModelForm(ServiceModelForm):
    class Meta:
        model = ContractingPlasteringService
        fields = [
            "plastering_type",
            "total_area",
            "start",
            "extra_info",
        ]


class ContractingPlumbingServiceModelForm(ServiceModelForm):
    class Meta:
        model = ContractingPlumbingService
        fields = [
            "facility_type",
            "pipe_type",
            "usecase",
            "total_suites",
            "total_stories",
            "total_parkings",
            "suite_area",
            "total_wc",
            "total_baths",
            "plan",
            "start",
            "extra_info",
        ]


class ContractingScaffoldingServiceModelForm(ServiceModelForm):
    class Meta:
        model = ContractingScaffoldingService
        fields = [
            "usecase",
            "required_duration",
            "required_area",
            "required_volume",
            "required_height",
            "start",
            "extra_info",
        ]


class ContractingSteelServiceModelForm(ServiceModelForm):
    class Meta:
        model = ContractingSteelService
        fields = [
            "foundation_type",
            "infrastructure_area",
            "ceiling_area",
            "total_ceilings",
            "total_basements",
            "total_area",
            "plan",
            "contractor_responsibilities",
            "start",
            "extra_info",
        ]


class ContractingTilingServiceModelForm(ServiceModelForm):
    class Meta:
        model = ContractingTilingService
        fields = [
            "place",
            "type",
            "size",
            "total_area",
            "plan",
            "start",
            "extra_info",
        ]


class ContractingTrussServiceModelForm(ServiceModelForm):
    class Meta:
        model = ContractingTrussService
        fields = [
            "total_area",
            "depth",
            "total_truss",
            "profile_tonnage",
            "wall_type",
            "water_level",
            "area_image",
            "plan",
            "start",
            "extra_info",
        ]


class ContractingWallServiceModelForm(ServiceModelForm):
    class Meta:
        model = ContractingWallService
        fields = [
            "wall_area",
            "wall_thickness",
            "wall_type",
            "plan",
            "start",
            "extra_info",
        ]


class ContractingWaterproofingServiceModelForm(ServiceModelForm):
    class Meta:
        model = ContractingWaterproofingService
        fields = [
            "required_places",
            "total_area",
            "start",
            "extra_info",
        ]


class ContractingWiringServiceModelForm(ServiceModelForm):
    class Meta:
        model = ContractingWiringService
        fields = [
            "usecase",
            "total_suites",
            "average_area",
            "total_stories",
            "total_parkings",
            "total_halogens",
            "contractor_responsibilities",
            "plan",
            "start",
            "extra_info",
        ]


class InsuranceServiceGeneralFields:
    fields = [
        "usecase",
        "infrastructure_area",
        "skeleton_type",
        "total_stories",
        "total_basements",
        "current_status",
        "requested_insurance_duration",
        "construction_area",
        "structural_system",
    ]


class InsuranceEmployeesLiabilityServiceModelForm(ServiceModelForm):
    class Meta:
        model = InsuranceEmployeesLiabilityService
        fields = InsuranceServiceGeneralFields.fields + [
            "singular_medical_expenses",
            "total_medical_expenses",
            "maximum_employees",
            "total_defected",
            "maximum_expenses_normal",
            "maximum_expenses_haram",
            "liability_3rd_parties",
            "diyats",
            "tamin_ejtemaei_numbers",
            "tamin_ejtemaei_demands",
            "increase_wergild",
            "extra_info",
        ]


class InsuranceThirdPartyLiabilityServiceModelForm(ServiceModelForm):
    class Meta:
        model = InsuranceThirdPartyLiabilityService
        fields = InsuranceServiceGeneralFields.fields + [
            "width",
            "depth",
            "soil_type",
            "excavation_method",
            "has_water_level",
            "water_level",
            "traffic",
            "raining_season",
            "drainage",
            "verified_plan",
            "has_fence",
            "financial_commitment",
            "medical_expenses_per_person",
            "medical_expenses_per_period",
            "north_neighbours",
            "east_neighbours",
            "south_neighbours",
            "west_neighbours",
            "extra_info",
        ]


class InsuranceQualityServiceModelForm(ServiceModelForm):
    class Meta:
        model = InsuranceQualityService
        fields = InsuranceServiceGeneralFields.fields + [
            "total_suites",
            "soil_type",
            "foundation_type",
            "excavation_depth",
            "building_type",
            "ceiling_height",
            "ceiling_type",
            "wall_material_type",
            "facing_type",
            "roofing",
            "construction_place",
            "humidity",
            "leak_possibility",
            "special_conditions",
            "experiments",
            "other_experiments",
            "excavation_time",
            "skeleton_time",
            "finish_time",
            "construction_value",
            "walling_value",
            "facilities_value",
            "facing_value",
            "other_value",
            "area_value",
            "required_annual_inflation",
            "extra_info",
        ]
