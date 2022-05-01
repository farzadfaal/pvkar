from django.contrib import admin

from .models import (
    MaterialAACService,
    MaterialBeamService,
    MaterialClayService,
    MaterialConcreteBlockService,
    MaterialConcreteService,
    MaterialFrameService,
    MaterialGrainsService,
    MaterialPolystyreneService,
    EngineeringService,
    InsuranceEmployeesLiabilityService,
    InsuranceQualityService,
    InsuranceThirdPartyLiabilityService,
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
)

# Emgineering Services
admin.site.register(EngineeringService)

# Material Services
admin.site.register(MaterialAACService)
admin.site.register(MaterialBeamService)
admin.site.register(MaterialClayService)
admin.site.register(MaterialConcreteBlockService)
admin.site.register(MaterialConcreteService)
admin.site.register(MaterialFrameService)
admin.site.register(MaterialGrainsService)
admin.site.register(MaterialPolystyreneService)

# Insurance Services
admin.site.register(InsuranceEmployeesLiabilityService)
admin.site.register(InsuranceQualityService)
admin.site.register(InsuranceThirdPartyLiabilityService)

# Contracting Services
admin.site.register(ContractingConcreteService)
admin.site.register(ContractingExcavationService)
admin.site.register(ContractingFacingService)
admin.site.register(ContractingGasService)
admin.site.register(ContractingNailingService)
admin.site.register(ContractingPaintingService)
admin.site.register(ContractingPilingService)
admin.site.register(ContractingPlasteringService)
admin.site.register(ContractingPlumbingService)
admin.site.register(ContractingScaffoldingService)
admin.site.register(ContractingSteelService)
admin.site.register(ContractingTilingService)
admin.site.register(ContractingTrussService)
admin.site.register(ContractingWallService)
admin.site.register(ContractingWaterproofingService)
admin.site.register(ContractingWiringService)
